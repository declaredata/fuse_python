from fuse_python.proto import sds_pb2, sds_pb2_grpc
from fuse_python.column import SelectColumn, select_column_to_pb


def select_impl(
    *, df_uid: str, stub: sds_pb2_grpc.sdsStub, cols: list[SelectColumn]
) -> str:
    derived_columns = [select_column_to_pb(col) for col in cols]
    req = sds_pb2.SelectRequest(df_uid=df_uid, columns=derived_columns)
    resp = stub.Select(req)
    return resp.dataframe_uid
