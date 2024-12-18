# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""

import grpc

from declaredata_fuse.proto import sds_pb2 as proto_dot_sds__pb2


class sdsStub(object):
    """//////////////////////////////////////
    session/dataframe initialization methods
    //////////////////////////////////////
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ExecuteSql = channel.unary_unary(
            "/sds.sds/ExecuteSql",
            request_serializer=proto_dot_sds__pb2.ExecuteSqlRequest.SerializeToString,
            response_deserializer=proto_dot_sds__pb2.DataFrameUID.FromString,
            _registered_method=True,
        )
        self.CreateSession = channel.unary_unary(
            "/sds.sds/CreateSession",
            request_serializer=proto_dot_sds__pb2.Empty.SerializeToString,
            response_deserializer=proto_dot_sds__pb2.SessionUID.FromString,
            _registered_method=True,
        )
        self.LoadCSV = channel.unary_unary(
            "/sds.sds/LoadCSV",
            request_serializer=proto_dot_sds__pb2.LoadFileRequest.SerializeToString,
            response_deserializer=proto_dot_sds__pb2.DataFrameUID.FromString,
            _registered_method=True,
        )
        self.LoadParquet = channel.unary_unary(
            "/sds.sds/LoadParquet",
            request_serializer=proto_dot_sds__pb2.LoadFileRequest.SerializeToString,
            response_deserializer=proto_dot_sds__pb2.DataFrameUID.FromString,
            _registered_method=True,
        )
        self.LoadJSON = channel.unary_unary(
            "/sds.sds/LoadJSON",
            request_serializer=proto_dot_sds__pb2.LoadFileRequest.SerializeToString,
            response_deserializer=proto_dot_sds__pb2.DataFrameUID.FromString,
            _registered_method=True,
        )
        self.CloseSession = channel.unary_unary(
            "/sds.sds/CloseSession",
            request_serializer=proto_dot_sds__pb2.SessionUID.SerializeToString,
            response_deserializer=proto_dot_sds__pb2.Empty.FromString,
            _registered_method=True,
        )
        self.SaveDataFrameAsTable = channel.unary_unary(
            "/sds.sds/SaveDataFrameAsTable",
            request_serializer=proto_dot_sds__pb2.SaveDataFrameAsTableRequest.SerializeToString,
            response_deserializer=proto_dot_sds__pb2.Empty.FromString,
            _registered_method=True,
        )
        self.PrettyPrintDataframe = channel.unary_unary(
            "/sds.sds/PrettyPrintDataframe",
            request_serializer=proto_dot_sds__pb2.DataFrameUID.SerializeToString,
            response_deserializer=proto_dot_sds__pb2.PrettyPrintDataframeResponse.FromString,
            _registered_method=True,
        )
        self.LimitDataFrame = channel.unary_unary(
            "/sds.sds/LimitDataFrame",
            request_serializer=proto_dot_sds__pb2.LimitDataFrameRequest.SerializeToString,
            response_deserializer=proto_dot_sds__pb2.DataFrameUID.FromString,
            _registered_method=True,
        )
        self.SortDataFrame = channel.unary_unary(
            "/sds.sds/SortDataFrame",
            request_serializer=proto_dot_sds__pb2.SortDataFrameRequest.SerializeToString,
            response_deserializer=proto_dot_sds__pb2.DataFrameUID.FromString,
            _registered_method=True,
        )
        self.FilterDataFrame = channel.unary_unary(
            "/sds.sds/FilterDataFrame",
            request_serializer=proto_dot_sds__pb2.FilterDataFrameRequest.SerializeToString,
            response_deserializer=proto_dot_sds__pb2.DataFrameUID.FromString,
            _registered_method=True,
        )
        self.Aggregate = channel.unary_unary(
            "/sds.sds/Aggregate",
            request_serializer=proto_dot_sds__pb2.AggregateRequest.SerializeToString,
            response_deserializer=proto_dot_sds__pb2.DataFrameUID.FromString,
            _registered_method=True,
        )
        self.WithColumn = channel.unary_unary(
            "/sds.sds/WithColumn",
            request_serializer=proto_dot_sds__pb2.WithColumnRequest.SerializeToString,
            response_deserializer=proto_dot_sds__pb2.DataFrameUID.FromString,
            _registered_method=True,
        )
        self.Select = channel.unary_unary(
            "/sds.sds/Select",
            request_serializer=proto_dot_sds__pb2.SelectRequest.SerializeToString,
            response_deserializer=proto_dot_sds__pb2.DataFrameUID.FromString,
            _registered_method=True,
        )
        self.Collect = channel.unary_unary(
            "/sds.sds/Collect",
            request_serializer=proto_dot_sds__pb2.DataFrameUID.SerializeToString,
            response_deserializer=proto_dot_sds__pb2.DataFrameContents.FromString,
            _registered_method=True,
        )
        self.Join = channel.unary_unary(
            "/sds.sds/Join",
            request_serializer=proto_dot_sds__pb2.JoinRequest.SerializeToString,
            response_deserializer=proto_dot_sds__pb2.DataFrameUID.FromString,
            _registered_method=True,
        )
        self.Drop = channel.unary_unary(
            "/sds.sds/Drop",
            request_serializer=proto_dot_sds__pb2.DropRequest.SerializeToString,
            response_deserializer=proto_dot_sds__pb2.DataFrameUID.FromString,
            _registered_method=True,
        )
        self.ExportCSV = channel.unary_unary(
            "/sds.sds/ExportCSV",
            request_serializer=proto_dot_sds__pb2.DataFrameUID.SerializeToString,
            response_deserializer=proto_dot_sds__pb2.CSVOutput.FromString,
            _registered_method=True,
        )


class sdsServicer(object):
    """//////////////////////////////////////
    session/dataframe initialization methods
    //////////////////////////////////////
    """

    def ExecuteSql(self, request, context):
        """execute SQL against a session and return a new DataFrame representing
        the result
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def CreateSession(self, request, context):
        """create a new session with no DataFrames therein, then return its UID"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def LoadCSV(self, request, context):
        """Load a CSV into a DataFrame, then return its UID"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def LoadParquet(self, request, context):
        """Load a Parquet file into a DataFrame, then return its UID"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def LoadJSON(self, request, context):
        """Load a JSON file into a DataFrame, then return its UID"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def CloseSession(self, request, context):
        """//////////////////////////////////////
        session destruction methods
        //////////////////////////////////////

        Close a session and free all associated dataframes.

        This is a highly destructive method, because all dataframes
        created directly or indirectly as part of this session
        will be instantly deleted.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def SaveDataFrameAsTable(self, request, context):
        """//////////////////////////////////////
        dataframe instance methods
        //////////////////////////////////////

        save a dataframe as a table, so that you can execute SQL queries
        against it
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def PrettyPrintDataframe(self, request, context):
        """pretty-print a given dataframe.

        TODO: throw an error if the dataframe is too big to pretty-print
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def LimitDataFrame(self, request, context):
        """filter an existing DataFrame, and return a new DataFrame"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def SortDataFrame(self, request, context):
        """sort a dataframe by 1 or more column(s)"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def FilterDataFrame(self, request, context):
        """filter a dataframe according to 1 or more filter conditions"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Aggregate(self, request, context):
        """group by, then aggregate a dataframe's data, the return a new dataframe"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def WithColumn(self, request, context):
        """add a new column -- optionally by doing some calculation -- to a
        given dataframe
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Select(self, request, context):
        """project a DataFrame onto a new one, optionally by calculating new
        values
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Collect(self, request, context):
        """eagerly evaluate the dataframe, then return its contents"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Join(self, request, context):
        """Join 2 dataframes together into one"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Drop(self, request, context):
        """return a new DataFrame with the given columns missing.

        if you pass a column that does not exist, this entire operation
        will be a no-op and you'll get the same UUID back
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ExportCSV(self, request, context):
        """export a CSV file and return it in the response"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_sdsServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "ExecuteSql": grpc.unary_unary_rpc_method_handler(
            servicer.ExecuteSql,
            request_deserializer=proto_dot_sds__pb2.ExecuteSqlRequest.FromString,
            response_serializer=proto_dot_sds__pb2.DataFrameUID.SerializeToString,
        ),
        "CreateSession": grpc.unary_unary_rpc_method_handler(
            servicer.CreateSession,
            request_deserializer=proto_dot_sds__pb2.Empty.FromString,
            response_serializer=proto_dot_sds__pb2.SessionUID.SerializeToString,
        ),
        "LoadCSV": grpc.unary_unary_rpc_method_handler(
            servicer.LoadCSV,
            request_deserializer=proto_dot_sds__pb2.LoadFileRequest.FromString,
            response_serializer=proto_dot_sds__pb2.DataFrameUID.SerializeToString,
        ),
        "LoadParquet": grpc.unary_unary_rpc_method_handler(
            servicer.LoadParquet,
            request_deserializer=proto_dot_sds__pb2.LoadFileRequest.FromString,
            response_serializer=proto_dot_sds__pb2.DataFrameUID.SerializeToString,
        ),
        "LoadJSON": grpc.unary_unary_rpc_method_handler(
            servicer.LoadJSON,
            request_deserializer=proto_dot_sds__pb2.LoadFileRequest.FromString,
            response_serializer=proto_dot_sds__pb2.DataFrameUID.SerializeToString,
        ),
        "CloseSession": grpc.unary_unary_rpc_method_handler(
            servicer.CloseSession,
            request_deserializer=proto_dot_sds__pb2.SessionUID.FromString,
            response_serializer=proto_dot_sds__pb2.Empty.SerializeToString,
        ),
        "SaveDataFrameAsTable": grpc.unary_unary_rpc_method_handler(
            servicer.SaveDataFrameAsTable,
            request_deserializer=proto_dot_sds__pb2.SaveDataFrameAsTableRequest.FromString,
            response_serializer=proto_dot_sds__pb2.Empty.SerializeToString,
        ),
        "PrettyPrintDataframe": grpc.unary_unary_rpc_method_handler(
            servicer.PrettyPrintDataframe,
            request_deserializer=proto_dot_sds__pb2.DataFrameUID.FromString,
            response_serializer=proto_dot_sds__pb2.PrettyPrintDataframeResponse.SerializeToString,
        ),
        "LimitDataFrame": grpc.unary_unary_rpc_method_handler(
            servicer.LimitDataFrame,
            request_deserializer=proto_dot_sds__pb2.LimitDataFrameRequest.FromString,
            response_serializer=proto_dot_sds__pb2.DataFrameUID.SerializeToString,
        ),
        "SortDataFrame": grpc.unary_unary_rpc_method_handler(
            servicer.SortDataFrame,
            request_deserializer=proto_dot_sds__pb2.SortDataFrameRequest.FromString,
            response_serializer=proto_dot_sds__pb2.DataFrameUID.SerializeToString,
        ),
        "FilterDataFrame": grpc.unary_unary_rpc_method_handler(
            servicer.FilterDataFrame,
            request_deserializer=proto_dot_sds__pb2.FilterDataFrameRequest.FromString,
            response_serializer=proto_dot_sds__pb2.DataFrameUID.SerializeToString,
        ),
        "Aggregate": grpc.unary_unary_rpc_method_handler(
            servicer.Aggregate,
            request_deserializer=proto_dot_sds__pb2.AggregateRequest.FromString,
            response_serializer=proto_dot_sds__pb2.DataFrameUID.SerializeToString,
        ),
        "WithColumn": grpc.unary_unary_rpc_method_handler(
            servicer.WithColumn,
            request_deserializer=proto_dot_sds__pb2.WithColumnRequest.FromString,
            response_serializer=proto_dot_sds__pb2.DataFrameUID.SerializeToString,
        ),
        "Select": grpc.unary_unary_rpc_method_handler(
            servicer.Select,
            request_deserializer=proto_dot_sds__pb2.SelectRequest.FromString,
            response_serializer=proto_dot_sds__pb2.DataFrameUID.SerializeToString,
        ),
        "Collect": grpc.unary_unary_rpc_method_handler(
            servicer.Collect,
            request_deserializer=proto_dot_sds__pb2.DataFrameUID.FromString,
            response_serializer=proto_dot_sds__pb2.DataFrameContents.SerializeToString,
        ),
        "Join": grpc.unary_unary_rpc_method_handler(
            servicer.Join,
            request_deserializer=proto_dot_sds__pb2.JoinRequest.FromString,
            response_serializer=proto_dot_sds__pb2.DataFrameUID.SerializeToString,
        ),
        "Drop": grpc.unary_unary_rpc_method_handler(
            servicer.Drop,
            request_deserializer=proto_dot_sds__pb2.DropRequest.FromString,
            response_serializer=proto_dot_sds__pb2.DataFrameUID.SerializeToString,
        ),
        "ExportCSV": grpc.unary_unary_rpc_method_handler(
            servicer.ExportCSV,
            request_deserializer=proto_dot_sds__pb2.DataFrameUID.FromString,
            response_serializer=proto_dot_sds__pb2.CSVOutput.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "sds.sds", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers("sds.sds", rpc_method_handlers)


# This class is part of an EXPERIMENTAL API.
class sds(object):
    """//////////////////////////////////////
    session/dataframe initialization methods
    //////////////////////////////////////
    """

    @staticmethod
    def ExecuteSql(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/sds.sds/ExecuteSql",
            proto_dot_sds__pb2.ExecuteSqlRequest.SerializeToString,
            proto_dot_sds__pb2.DataFrameUID.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def CreateSession(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/sds.sds/CreateSession",
            proto_dot_sds__pb2.Empty.SerializeToString,
            proto_dot_sds__pb2.SessionUID.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def LoadCSV(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/sds.sds/LoadCSV",
            proto_dot_sds__pb2.LoadFileRequest.SerializeToString,
            proto_dot_sds__pb2.DataFrameUID.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def LoadParquet(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/sds.sds/LoadParquet",
            proto_dot_sds__pb2.LoadFileRequest.SerializeToString,
            proto_dot_sds__pb2.DataFrameUID.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def LoadJSON(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/sds.sds/LoadJSON",
            proto_dot_sds__pb2.LoadFileRequest.SerializeToString,
            proto_dot_sds__pb2.DataFrameUID.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def CloseSession(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/sds.sds/CloseSession",
            proto_dot_sds__pb2.SessionUID.SerializeToString,
            proto_dot_sds__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def SaveDataFrameAsTable(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/sds.sds/SaveDataFrameAsTable",
            proto_dot_sds__pb2.SaveDataFrameAsTableRequest.SerializeToString,
            proto_dot_sds__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def PrettyPrintDataframe(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/sds.sds/PrettyPrintDataframe",
            proto_dot_sds__pb2.DataFrameUID.SerializeToString,
            proto_dot_sds__pb2.PrettyPrintDataframeResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def LimitDataFrame(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/sds.sds/LimitDataFrame",
            proto_dot_sds__pb2.LimitDataFrameRequest.SerializeToString,
            proto_dot_sds__pb2.DataFrameUID.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def SortDataFrame(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/sds.sds/SortDataFrame",
            proto_dot_sds__pb2.SortDataFrameRequest.SerializeToString,
            proto_dot_sds__pb2.DataFrameUID.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def FilterDataFrame(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/sds.sds/FilterDataFrame",
            proto_dot_sds__pb2.FilterDataFrameRequest.SerializeToString,
            proto_dot_sds__pb2.DataFrameUID.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def Aggregate(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/sds.sds/Aggregate",
            proto_dot_sds__pb2.AggregateRequest.SerializeToString,
            proto_dot_sds__pb2.DataFrameUID.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def WithColumn(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/sds.sds/WithColumn",
            proto_dot_sds__pb2.WithColumnRequest.SerializeToString,
            proto_dot_sds__pb2.DataFrameUID.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def Select(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/sds.sds/Select",
            proto_dot_sds__pb2.SelectRequest.SerializeToString,
            proto_dot_sds__pb2.DataFrameUID.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def Collect(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/sds.sds/Collect",
            proto_dot_sds__pb2.DataFrameUID.SerializeToString,
            proto_dot_sds__pb2.DataFrameContents.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def Join(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/sds.sds/Join",
            proto_dot_sds__pb2.JoinRequest.SerializeToString,
            proto_dot_sds__pb2.DataFrameUID.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def Drop(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/sds.sds/Drop",
            proto_dot_sds__pb2.DropRequest.SerializeToString,
            proto_dot_sds__pb2.DataFrameUID.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def ExportCSV(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/sds.sds/ExportCSV",
            proto_dot_sds__pb2.DataFrameUID.SerializeToString,
            proto_dot_sds__pb2.CSVOutput.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )
