from declaredata_fuse.column import Column, DropColumn
from declaredata_fuse.proto import sds_pb2, sds_pb2_grpc


def drop_impl(df_uid: str, stub: sds_pb2_grpc.sdsStub, cols: list[DropColumn]) -> str:
    col_names = [_drop_col_to_str(col) for col in cols]
    req = sds_pb2.DropRequest(df_uid=df_uid, col_names=col_names)
    resp = stub.Drop(req)
    return resp.dataframe_uid


def _drop_col_to_str(d: DropColumn) -> str:
    match d:
        case Column():
            return d.cur_name()
        case str():
            return d
