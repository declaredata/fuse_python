from dataclasses import dataclass
from typing import TYPE_CHECKING

from declaredata_fuse.functions import Function
from declaredata_fuse.proto import sds_pb2
from declaredata_fuse.proto.sds_pb2 import Agg
from declaredata_fuse.proto.sds_pb2_grpc import sdsStub

if TYPE_CHECKING:
    from declaredata_fuse.dataframe import DataFrame


@dataclass(frozen=True)
class Grouped:
    group_cols: list[str]
    """The columns to group by in the aggregation"""
    df_uid: str
    stub: sdsStub

    def agg(self, *funcs: Function) -> "DataFrame":
        aggs: list[Agg] = []
        for func in funcs:
            aggs.append(func.to_pb())

        req = sds_pb2.AggregateRequest(
            dataframe_uid=self.df_uid,
            group_by=self.group_cols,
            aggs=aggs,
        )
        resp = self.stub.Aggregate(req)
        from declaredata_fuse.dataframe import DataFrame
        return DataFrame(
            df_uid=resp.dataframe_uid,
            stub=self.stub
        )

