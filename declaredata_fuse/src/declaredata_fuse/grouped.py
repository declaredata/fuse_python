from dataclasses import dataclass
from typing import TYPE_CHECKING

from declaredata_fuse.functions import Function
from declaredata_fuse.proto import sds_pb2
from declaredata_fuse.proto.sds_pb2 import Agg

if TYPE_CHECKING:
    from declaredata_fuse.dataframe import DataFrame


@dataclass(frozen=True)
class Grouped:
    group_cols: list[str]
    """The columns to group by in the aggregation"""
    orig_df: DataFrame

    def agg(self, *funcs: Function) -> DataFrame:
        aggs: list[Agg] = []
        for func in funcs:
            aggs.append(func.to_pb())

        req = sds_pb2.AggregateRequest(
            dataframe_uid=self.orig_df.df_uid,
            group_by=self.group_cols,
            aggs=aggs,
        )
        resp = self.orig_df.stub.Aggregate(req)  # type: ignore
        return DataFrame(
            df_uid=resp.dataframe_uid,
            stub=self.orig_df.stub
        )

