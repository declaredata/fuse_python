"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import proto.sds_pb2
import typing

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(
    collections.abc.AsyncIterator[_T],
    collections.abc.Iterator[_T],
    metaclass=abc.ABCMeta,
): ...
class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class sdsStub:
    """//////////////////////////////////////
    session/dataframe initialization methods
    //////////////////////////////////////
    """

    def __init__(
        self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]
    ) -> None: ...
    ExecuteSql: grpc.UnaryUnaryMultiCallable[
        proto.sds_pb2.ExecuteSqlRequest,
        proto.sds_pb2.DataFrameUID,
    ]
    """execute SQL against a session and return a new DataFrame representing
    the result
    """

    CreateSession: grpc.UnaryUnaryMultiCallable[
        proto.sds_pb2.Empty,
        proto.sds_pb2.SessionUID,
    ]
    """create a new session with no DataFrames therein, then return its UID"""

    LoadCSV: grpc.UnaryUnaryMultiCallable[
        proto.sds_pb2.LoadFileRequest,
        proto.sds_pb2.DataFrameUID,
    ]
    """Load a CSV into a DataFrame, then return its UID"""

    LoadParquet: grpc.UnaryUnaryMultiCallable[
        proto.sds_pb2.LoadFileRequest,
        proto.sds_pb2.DataFrameUID,
    ]
    """Load a Parquet file into a DataFrame, then return its UID"""

    LoadJSON: grpc.UnaryUnaryMultiCallable[
        proto.sds_pb2.LoadFileRequest,
        proto.sds_pb2.DataFrameUID,
    ]
    """Load a JSON file into a DataFrame, then return its UID"""

    CloseSession: grpc.UnaryUnaryMultiCallable[
        proto.sds_pb2.SessionUID,
        proto.sds_pb2.Empty,
    ]
    """//////////////////////////////////////
    session destruction methods
    //////////////////////////////////////

    Close a session and free all associated dataframes.

    This is a highly destructive method, because all dataframes
    created directly or indirectly as part of this session
    will be instantly deleted.
    """

    SaveDataFrameAsTable: grpc.UnaryUnaryMultiCallable[
        proto.sds_pb2.SaveDataFrameAsTableRequest,
        proto.sds_pb2.Empty,
    ]
    """//////////////////////////////////////
    dataframe instance methods
    //////////////////////////////////////

    save a dataframe as a table, so that you can execute SQL queries 
    against it
    """

    PrettyPrintDataframe: grpc.UnaryUnaryMultiCallable[
        proto.sds_pb2.DataFrameUID,
        proto.sds_pb2.PrettyPrintDataframeResponse,
    ]
    """pretty-print a given dataframe.

    TODO: throw an error if the dataframe is too big to pretty-print
    """

    LimitDataFrame: grpc.UnaryUnaryMultiCallable[
        proto.sds_pb2.LimitDataFrameRequest,
        proto.sds_pb2.DataFrameUID,
    ]
    """filter an existing DataFrame, and return a new DataFrame"""

    SortDataFrame: grpc.UnaryUnaryMultiCallable[
        proto.sds_pb2.SortDataFrameRequest,
        proto.sds_pb2.DataFrameUID,
    ]
    """sort a dataframe by 1 or more column(s)"""

    FilterDataFrame: grpc.UnaryUnaryMultiCallable[
        proto.sds_pb2.FilterDataFrameRequest,
        proto.sds_pb2.DataFrameUID,
    ]
    """filter a dataframe according to 1 or more filter conditions"""

    Aggregate: grpc.UnaryUnaryMultiCallable[
        proto.sds_pb2.AggregateRequest,
        proto.sds_pb2.DataFrameUID,
    ]
    """Group rows in a DataFrame, then compute an aggregate across all the
    rows in each group
    """

    WithColumn: grpc.UnaryUnaryMultiCallable[
        proto.sds_pb2.WithColumnRequest,
        proto.sds_pb2.DataFrameUID,
    ]
    """add a new column -- optionally by doing some calculation -- to a 
    given dataframe
    """

    Select: grpc.UnaryUnaryMultiCallable[
        proto.sds_pb2.SelectRequest,
        proto.sds_pb2.DataFrameUID,
    ]
    """project a DataFrame onto a new one, optionally by calculating new
    values
    """

    Collect: grpc.UnaryUnaryMultiCallable[
        proto.sds_pb2.DataFrameUID,
        proto.sds_pb2.DataFrameContents,
    ]
    """eagerly evaluate the dataframe, then return its contents"""

    Join: grpc.UnaryUnaryMultiCallable[
        proto.sds_pb2.JoinRequest,
        proto.sds_pb2.DataFrameUID,
    ]
    """Join 2 dataframes together into one"""

    Distinct: grpc.UnaryUnaryMultiCallable[
        proto.sds_pb2.DataFrameUID,
        proto.sds_pb2.DataFrameUID,
    ]
    """Return a new DataFrame whose contents are the same as the given
    DataFrame, except with duplicate rows removed
    """

    Union: grpc.UnaryUnaryMultiCallable[
        proto.sds_pb2.UnionRequest,
        proto.sds_pb2.DataFrameUID,
    ]
    """Combine two DataFrames together to calculate the union of the two.

    Both DataFrames must have the same schema. If they do not, return
    an error. If they do, preserve duplicate rows in the final result.
    """

    Drop: grpc.UnaryUnaryMultiCallable[
        proto.sds_pb2.DropRequest,
        proto.sds_pb2.DataFrameUID,
    ]
    """return a new DataFrame with the given columns missing.

    if you pass a column that does not exist, this entire operation
    will be a no-op and you'll get the same UUID back
    """

    ExportCSV: grpc.UnaryUnaryMultiCallable[
        proto.sds_pb2.DataFrameUID,
        proto.sds_pb2.CSVOutput,
    ]
    """export a CSV file and return it in the response"""

class sdsAsyncStub:
    """//////////////////////////////////////
    session/dataframe initialization methods
    //////////////////////////////////////
    """

    ExecuteSql: grpc.aio.UnaryUnaryMultiCallable[
        proto.sds_pb2.ExecuteSqlRequest,
        proto.sds_pb2.DataFrameUID,
    ]
    """execute SQL against a session and return a new DataFrame representing
    the result
    """

    CreateSession: grpc.aio.UnaryUnaryMultiCallable[
        proto.sds_pb2.Empty,
        proto.sds_pb2.SessionUID,
    ]
    """create a new session with no DataFrames therein, then return its UID"""

    LoadCSV: grpc.aio.UnaryUnaryMultiCallable[
        proto.sds_pb2.LoadFileRequest,
        proto.sds_pb2.DataFrameUID,
    ]
    """Load a CSV into a DataFrame, then return its UID"""

    LoadParquet: grpc.aio.UnaryUnaryMultiCallable[
        proto.sds_pb2.LoadFileRequest,
        proto.sds_pb2.DataFrameUID,
    ]
    """Load a Parquet file into a DataFrame, then return its UID"""

    LoadJSON: grpc.aio.UnaryUnaryMultiCallable[
        proto.sds_pb2.LoadFileRequest,
        proto.sds_pb2.DataFrameUID,
    ]
    """Load a JSON file into a DataFrame, then return its UID"""

    CloseSession: grpc.aio.UnaryUnaryMultiCallable[
        proto.sds_pb2.SessionUID,
        proto.sds_pb2.Empty,
    ]
    """//////////////////////////////////////
    session destruction methods
    //////////////////////////////////////

    Close a session and free all associated dataframes.

    This is a highly destructive method, because all dataframes
    created directly or indirectly as part of this session
    will be instantly deleted.
    """

    SaveDataFrameAsTable: grpc.aio.UnaryUnaryMultiCallable[
        proto.sds_pb2.SaveDataFrameAsTableRequest,
        proto.sds_pb2.Empty,
    ]
    """//////////////////////////////////////
    dataframe instance methods
    //////////////////////////////////////

    save a dataframe as a table, so that you can execute SQL queries 
    against it
    """

    PrettyPrintDataframe: grpc.aio.UnaryUnaryMultiCallable[
        proto.sds_pb2.DataFrameUID,
        proto.sds_pb2.PrettyPrintDataframeResponse,
    ]
    """pretty-print a given dataframe.

    TODO: throw an error if the dataframe is too big to pretty-print
    """

    LimitDataFrame: grpc.aio.UnaryUnaryMultiCallable[
        proto.sds_pb2.LimitDataFrameRequest,
        proto.sds_pb2.DataFrameUID,
    ]
    """filter an existing DataFrame, and return a new DataFrame"""

    SortDataFrame: grpc.aio.UnaryUnaryMultiCallable[
        proto.sds_pb2.SortDataFrameRequest,
        proto.sds_pb2.DataFrameUID,
    ]
    """sort a dataframe by 1 or more column(s)"""

    FilterDataFrame: grpc.aio.UnaryUnaryMultiCallable[
        proto.sds_pb2.FilterDataFrameRequest,
        proto.sds_pb2.DataFrameUID,
    ]
    """filter a dataframe according to 1 or more filter conditions"""

    Aggregate: grpc.aio.UnaryUnaryMultiCallable[
        proto.sds_pb2.AggregateRequest,
        proto.sds_pb2.DataFrameUID,
    ]
    """Group rows in a DataFrame, then compute an aggregate across all the
    rows in each group
    """

    WithColumn: grpc.aio.UnaryUnaryMultiCallable[
        proto.sds_pb2.WithColumnRequest,
        proto.sds_pb2.DataFrameUID,
    ]
    """add a new column -- optionally by doing some calculation -- to a 
    given dataframe
    """

    Select: grpc.aio.UnaryUnaryMultiCallable[
        proto.sds_pb2.SelectRequest,
        proto.sds_pb2.DataFrameUID,
    ]
    """project a DataFrame onto a new one, optionally by calculating new
    values
    """

    Collect: grpc.aio.UnaryUnaryMultiCallable[
        proto.sds_pb2.DataFrameUID,
        proto.sds_pb2.DataFrameContents,
    ]
    """eagerly evaluate the dataframe, then return its contents"""

    Join: grpc.aio.UnaryUnaryMultiCallable[
        proto.sds_pb2.JoinRequest,
        proto.sds_pb2.DataFrameUID,
    ]
    """Join 2 dataframes together into one"""

    Distinct: grpc.aio.UnaryUnaryMultiCallable[
        proto.sds_pb2.DataFrameUID,
        proto.sds_pb2.DataFrameUID,
    ]
    """Return a new DataFrame whose contents are the same as the given
    DataFrame, except with duplicate rows removed
    """

    Union: grpc.aio.UnaryUnaryMultiCallable[
        proto.sds_pb2.UnionRequest,
        proto.sds_pb2.DataFrameUID,
    ]
    """Combine two DataFrames together to calculate the union of the two.

    Both DataFrames must have the same schema. If they do not, return
    an error. If they do, preserve duplicate rows in the final result.
    """

    Drop: grpc.aio.UnaryUnaryMultiCallable[
        proto.sds_pb2.DropRequest,
        proto.sds_pb2.DataFrameUID,
    ]
    """return a new DataFrame with the given columns missing.

    if you pass a column that does not exist, this entire operation
    will be a no-op and you'll get the same UUID back
    """

    ExportCSV: grpc.aio.UnaryUnaryMultiCallable[
        proto.sds_pb2.DataFrameUID,
        proto.sds_pb2.CSVOutput,
    ]
    """export a CSV file and return it in the response"""

class sdsServicer(metaclass=abc.ABCMeta):
    """//////////////////////////////////////
    session/dataframe initialization methods
    //////////////////////////////////////
    """

    @abc.abstractmethod
    def ExecuteSql(
        self,
        request: proto.sds_pb2.ExecuteSqlRequest,
        context: _ServicerContext,
    ) -> typing.Union[
        proto.sds_pb2.DataFrameUID,
        collections.abc.Awaitable[proto.sds_pb2.DataFrameUID],
    ]:
        """execute SQL against a session and return a new DataFrame representing
        the result
        """

    @abc.abstractmethod
    def CreateSession(
        self,
        request: proto.sds_pb2.Empty,
        context: _ServicerContext,
    ) -> typing.Union[
        proto.sds_pb2.SessionUID, collections.abc.Awaitable[proto.sds_pb2.SessionUID]
    ]:
        """create a new session with no DataFrames therein, then return its UID"""

    @abc.abstractmethod
    def LoadCSV(
        self,
        request: proto.sds_pb2.LoadFileRequest,
        context: _ServicerContext,
    ) -> typing.Union[
        proto.sds_pb2.DataFrameUID,
        collections.abc.Awaitable[proto.sds_pb2.DataFrameUID],
    ]:
        """Load a CSV into a DataFrame, then return its UID"""

    @abc.abstractmethod
    def LoadParquet(
        self,
        request: proto.sds_pb2.LoadFileRequest,
        context: _ServicerContext,
    ) -> typing.Union[
        proto.sds_pb2.DataFrameUID,
        collections.abc.Awaitable[proto.sds_pb2.DataFrameUID],
    ]:
        """Load a Parquet file into a DataFrame, then return its UID"""

    @abc.abstractmethod
    def LoadJSON(
        self,
        request: proto.sds_pb2.LoadFileRequest,
        context: _ServicerContext,
    ) -> typing.Union[
        proto.sds_pb2.DataFrameUID,
        collections.abc.Awaitable[proto.sds_pb2.DataFrameUID],
    ]:
        """Load a JSON file into a DataFrame, then return its UID"""

    @abc.abstractmethod
    def CloseSession(
        self,
        request: proto.sds_pb2.SessionUID,
        context: _ServicerContext,
    ) -> typing.Union[
        proto.sds_pb2.Empty, collections.abc.Awaitable[proto.sds_pb2.Empty]
    ]:
        """//////////////////////////////////////
        session destruction methods
        //////////////////////////////////////

        Close a session and free all associated dataframes.

        This is a highly destructive method, because all dataframes
        created directly or indirectly as part of this session
        will be instantly deleted.
        """

    @abc.abstractmethod
    def SaveDataFrameAsTable(
        self,
        request: proto.sds_pb2.SaveDataFrameAsTableRequest,
        context: _ServicerContext,
    ) -> typing.Union[
        proto.sds_pb2.Empty, collections.abc.Awaitable[proto.sds_pb2.Empty]
    ]:
        """//////////////////////////////////////
        dataframe instance methods
        //////////////////////////////////////

        save a dataframe as a table, so that you can execute SQL queries
        against it
        """

    @abc.abstractmethod
    def PrettyPrintDataframe(
        self,
        request: proto.sds_pb2.DataFrameUID,
        context: _ServicerContext,
    ) -> typing.Union[
        proto.sds_pb2.PrettyPrintDataframeResponse,
        collections.abc.Awaitable[proto.sds_pb2.PrettyPrintDataframeResponse],
    ]:
        """pretty-print a given dataframe.

        TODO: throw an error if the dataframe is too big to pretty-print
        """

    @abc.abstractmethod
    def LimitDataFrame(
        self,
        request: proto.sds_pb2.LimitDataFrameRequest,
        context: _ServicerContext,
    ) -> typing.Union[
        proto.sds_pb2.DataFrameUID,
        collections.abc.Awaitable[proto.sds_pb2.DataFrameUID],
    ]:
        """filter an existing DataFrame, and return a new DataFrame"""

    @abc.abstractmethod
    def SortDataFrame(
        self,
        request: proto.sds_pb2.SortDataFrameRequest,
        context: _ServicerContext,
    ) -> typing.Union[
        proto.sds_pb2.DataFrameUID,
        collections.abc.Awaitable[proto.sds_pb2.DataFrameUID],
    ]:
        """sort a dataframe by 1 or more column(s)"""

    @abc.abstractmethod
    def FilterDataFrame(
        self,
        request: proto.sds_pb2.FilterDataFrameRequest,
        context: _ServicerContext,
    ) -> typing.Union[
        proto.sds_pb2.DataFrameUID,
        collections.abc.Awaitable[proto.sds_pb2.DataFrameUID],
    ]:
        """filter a dataframe according to 1 or more filter conditions"""

    @abc.abstractmethod
    def Aggregate(
        self,
        request: proto.sds_pb2.AggregateRequest,
        context: _ServicerContext,
    ) -> typing.Union[
        proto.sds_pb2.DataFrameUID,
        collections.abc.Awaitable[proto.sds_pb2.DataFrameUID],
    ]:
        """Group rows in a DataFrame, then compute an aggregate across all the
        rows in each group
        """

    @abc.abstractmethod
    def WithColumn(
        self,
        request: proto.sds_pb2.WithColumnRequest,
        context: _ServicerContext,
    ) -> typing.Union[
        proto.sds_pb2.DataFrameUID,
        collections.abc.Awaitable[proto.sds_pb2.DataFrameUID],
    ]:
        """add a new column -- optionally by doing some calculation -- to a
        given dataframe
        """

    @abc.abstractmethod
    def Select(
        self,
        request: proto.sds_pb2.SelectRequest,
        context: _ServicerContext,
    ) -> typing.Union[
        proto.sds_pb2.DataFrameUID,
        collections.abc.Awaitable[proto.sds_pb2.DataFrameUID],
    ]:
        """project a DataFrame onto a new one, optionally by calculating new
        values
        """

    @abc.abstractmethod
    def Collect(
        self,
        request: proto.sds_pb2.DataFrameUID,
        context: _ServicerContext,
    ) -> typing.Union[
        proto.sds_pb2.DataFrameContents,
        collections.abc.Awaitable[proto.sds_pb2.DataFrameContents],
    ]:
        """eagerly evaluate the dataframe, then return its contents"""

    @abc.abstractmethod
    def Join(
        self,
        request: proto.sds_pb2.JoinRequest,
        context: _ServicerContext,
    ) -> typing.Union[
        proto.sds_pb2.DataFrameUID,
        collections.abc.Awaitable[proto.sds_pb2.DataFrameUID],
    ]:
        """Join 2 dataframes together into one"""

    @abc.abstractmethod
    def Distinct(
        self,
        request: proto.sds_pb2.DataFrameUID,
        context: _ServicerContext,
    ) -> typing.Union[
        proto.sds_pb2.DataFrameUID,
        collections.abc.Awaitable[proto.sds_pb2.DataFrameUID],
    ]:
        """Return a new DataFrame whose contents are the same as the given
        DataFrame, except with duplicate rows removed
        """

    @abc.abstractmethod
    def Union(
        self,
        request: proto.sds_pb2.UnionRequest,
        context: _ServicerContext,
    ) -> typing.Union[
        proto.sds_pb2.DataFrameUID,
        collections.abc.Awaitable[proto.sds_pb2.DataFrameUID],
    ]:
        """Combine two DataFrames together to calculate the union of the two.

        Both DataFrames must have the same schema. If they do not, return
        an error. If they do, preserve duplicate rows in the final result.
        """

    @abc.abstractmethod
    def Drop(
        self,
        request: proto.sds_pb2.DropRequest,
        context: _ServicerContext,
    ) -> typing.Union[
        proto.sds_pb2.DataFrameUID,
        collections.abc.Awaitable[proto.sds_pb2.DataFrameUID],
    ]:
        """return a new DataFrame with the given columns missing.

        if you pass a column that does not exist, this entire operation
        will be a no-op and you'll get the same UUID back
        """

    @abc.abstractmethod
    def ExportCSV(
        self,
        request: proto.sds_pb2.DataFrameUID,
        context: _ServicerContext,
    ) -> typing.Union[
        proto.sds_pb2.CSVOutput, collections.abc.Awaitable[proto.sds_pb2.CSVOutput]
    ]:
        """export a CSV file and return it in the response"""

def add_sdsServicer_to_server(
    servicer: sdsServicer, server: typing.Union[grpc.Server, grpc.aio.Server]
) -> None: ...
