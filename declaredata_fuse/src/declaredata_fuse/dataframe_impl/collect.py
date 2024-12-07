from typing import Any
from declaredata_fuse.proto import sds_pb2, sds_pb2_grpc
from declaredata_fuse.row import Row


def collect_impl(*, df_uid: str, stub: sds_pb2_grpc.sdsStub) -> list[Row]:
    req = sds_pb2.DataFrameUID(dataframe_uid=df_uid)
    resp = stub.Collect(req)
    ret: list[Row] = []

    for elt in resp.rows:
        row_lookup: dict[str, Any] = {}
        for k, v in elt.data.items():
            row_lookup[k] = v
        ret.append(Row(lookup=row_lookup))

    return ret
