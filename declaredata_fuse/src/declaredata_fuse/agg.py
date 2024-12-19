from dataclasses import dataclass
from typing import Callable

from declaredata_fuse.functions import Function
from declaredata_fuse.proto import sds_pb2_grpc, sds_pb2
from declaredata_fuse.proto.sds_pb2 import Agg


@dataclass(frozen=True)
class AggBuilder[T]:
    df_uid: str
    stub: sds_pb2_grpc.sdsStub
    group_cols: list[str]
    """The columns to group by in the aggregation"""
    new_t: Callable[[str], T]
    """The lambda that can convert a dataframe_uid back to a DataFrame"""

    def agg(self, *funcs: Function) -> T:
        aggs: list[Agg] = []
        for func in funcs:
            aggs.append(func.to_pb())

        req = sds_pb2.AggregateRequest(
            dataframe_uid=self.df_uid,
            group_by=self.group_cols,
            aggs=aggs,
        )
        resp = self.stub.Aggregate(req)  # type: ignore
        return self.new_t(resp.dataframe_uid)  # type: ignore

    def run(self) -> T:
        raise NotImplementedError("can't run aggregations/group-by yet")
