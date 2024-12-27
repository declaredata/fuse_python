from contextlib import contextmanager
from dataclasses import dataclass
from typing import Optional
from grpc import Channel, insecure_channel  # ignore: import-not-found
from declaredata_fuse.proto import sds_pb2_grpc, sds_pb2
from declaredata_fuse.dataframe import DataFrame
from uuid import uuid4

DEFAULT_HOST: str = "localhost"
DEFAULT_PORT: int = 8080


@dataclass
class FuseSessionBuilder:
    """
    A builder for FuseSessions. This is intended to be a singleton for
    production code, so don't create instances of FuseSessionBuilder directly.
    Instead, use FuseSession.builder and then call methods on that.
    """

    _app_name: Optional[str] = None
    _host: str = DEFAULT_HOST
    _port: int = DEFAULT_PORT

    def appName(self, name: str) -> "FuseSessionBuilder":
        """
        Set the name of the application that should be associated with
        the FuseSession that will be built, then return the same
        FuseSessionBuilder instance.
        """
        self._app_name = name
        return self

    def host(self, host: str) -> "FuseSessionBuilder":
        """
        Set the host to which the FuseSession will connect, after it's built,
        then return the same FuseSessionBuilder instance.
        """
        self._host = host
        return self

    def port(self, port: int) -> "FuseSessionBuilder":
        """
        Set the port to which the FuseSession will connect, after it's built,
        then return the same FuseSessionBuilder instance.
        """
        self._port = port
        return self

    def getOrCreate(self) -> "FuseSession":
        """Build the new FuseSession"""
        channel = insecure_channel(target=f"{self._host}:{self._port}")
        stub = sds_pb2_grpc.sdsStub(channel=channel)
        resp = stub.CreateSession(sds_pb2.Empty())  # type: ignore
        return FuseSession(
            session_uid=resp.session_uid,  # type: ignore
            _channel=channel,
            _stub=stub,
            _app_name=self._app_name,
        )


@dataclass(frozen=True)
class FuseDataSource:
    """
    A data source from which to read DataFrames. Do not create an instance
    of this class directly. Instead, create a new FuseSession (using the
    FuseSession.builder builder) and then use FuseSession.read
    """

    session_uid: str
    stub: sds_pb2_grpc.sdsStub

    def csv(self, file_name: str) -> DataFrame:
        """
        Load a CSV from the given filename into a new DataFrame on which
        you can start doing operations.

        Depending on how your Fuse server is configured, you may be able to
        specify different file prefixes like `s3://` and `https://`.

        Local filesystem filenames are always supported regardless of
        configuration.
        """
        load_req = self._load_file_req(file_name)
        resp = self.stub.LoadCSV(load_req)  # type: ignore
        return DataFrame(
            stub=self.stub,
            df_uid=resp.dataframe_uid,  # type: ignore
        )

    def json(self, file_name: str) -> DataFrame:
        """
        Same as `self.csv(file_name)`, except this function expects the file
        located at `file_name` to be a JSON file rather than a CSV
        """
        load_req = self._load_file_req(file_name)
        resp = self.stub.LoadJSON(load_req)  # type: ignore
        return DataFrame(
            stub=self.stub,
            df_uid=resp.dataframe_uid,  # type: ignore
        )

    def parquet(self, file_name: str) -> DataFrame:
        """
        Same as `self.csv(file_name)`, except this function expects the file
        located at `file_name` to be a Parquet file rather than a CSV
        """
        load_req = self._load_file_req(file_name)
        resp = self.stub.LoadParquet(load_req)  # type: ignore
        return DataFrame(
            stub=self.stub,
            df_uid=resp.dataframe_uid,  # type: ignore
        )

    def delta(self, file_name: str) -> DataFrame:
        load_req = self._load_file_req(file_name)
        resp = self.stub.LoadDeltaTable(load_req)  # type: ignore
        return DataFrame(
            stub=self.stub,
            df_uid=resp.dataframe_uid,  # type: ignore
        )

    def _load_file_req(self, file_name: str) -> sds_pb2.LoadFileRequest:
        return sds_pb2.LoadFileRequest(
            session_id=self.session_uid,
            source=file_name,
        )


@dataclass
class FuseSession:
    """
    A new session with the Fuse server, with which data can be read and
    procesed. The general way to create a new session is as follows:

    session = FuseSession.builder.appName("sampleapp").host("localhost").port(8080).getOrCreate()

    After you have a session, you can use the 'read' property to start
    reading data:

    csv_dataframe = session.read.csv("s3://somebucket/somefile.csv")

    See documentation in FuseDataSource for more information on session.read
    """

    session_uid: str
    _app_name: Optional[str]
    _stub: sds_pb2_grpc.sdsStub
    _channel: Channel

    builder = FuseSessionBuilder()

    @property
    def read(self) -> FuseDataSource:
        """
        The FuseDataSource singleton with which to read data.

        See documentation at the top of FuseSession for a usage example
        """
        return FuseDataSource(session_uid=self.session_uid, stub=self._stub)

    @staticmethod
    def get_builder(
        host: str, port: int = 8080, app_name: str | None = None
    ) -> FuseSessionBuilder:
        """
        Get a FuseSessionBuilder configured with the given app name,
        host and port.

        If app_name is unspecified or passed as None, uses a unique
        app name.
        """
        reified_app_name = app_name or str(uuid4())
        return FuseSessionBuilder(_app_name=reified_app_name, _host=host, _port=port)

    def sql(self, query: str) -> DataFrame:
        """
        Use the existing session to execute SQL and return a DataFrame
        with the results.
        """
        req = sds_pb2.ExecuteSqlRequest(
            session_uid=self.session_uid,
            query=query,
        )
        resp = self._stub.ExecuteSql(req)  # type: ignore
        return DataFrame(
            df_uid=resp.dataframe_uid,  # type: ignore
            stub=self._stub,
        )

    def stop(self):
        """
        Drop all DataFrames associated with this session and close
        the connection to the server.

        Important note:

        This may be a _very destructive_ action, especially if you have
        created a lot of dataframes (directly or indirectly) from this session.
        """
        self._channel.close()


@contextmanager
def session(host: str, port: int, app_name: str | None = None):
    """
    Context manager for configuring and creating a new session, executing an
    action, then shutting it down (even if the action raised an exception).

    Example usage:

    with session("localhost", 8080, "myapp") as fuse:
        csv_dataframe = fuse.read.csv("s3://somebucket/somefile.csv")
    """
    bld = (
        FuseSession.builder.appName(app_name if app_name is not None else str(uuid4()))
        .host(host)
        .port(port)
    )
    sess = bld.getOrCreate()
    yield sess
    sess.stop()
