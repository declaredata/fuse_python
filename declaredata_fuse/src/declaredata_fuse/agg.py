from dataclasses import dataclass
from typing import Callable

from declaredata_fuse.column_abc import Column
from declaredata_fuse.proto import sds_pb2_grpc, sds_pb2


@dataclass(frozen=True)
class AggBuilder[T]:
    df_uid: str
    stub: sds_pb2_grpc.sdsStub
    group_cols: list[str]
    """The columns to group by in the aggregation"""
    new_t: Callable[[str], T]
    """The lambda that can convert a dataframe_uid back to a DataFrame"""

    def agg(self, *cols: Column) -> T:
        cols_pb = [col.to_pb() for col in cols]

        req = sds_pb2.AggregateRequest(
            dataframe_uid=self.df_uid,
            group_by=self.group_cols,
            cols=cols_pb,
        )
        resp = self.stub.Aggregate(req)  # type: ignore
        return self.new_t(resp.dataframe_uid)  # type: ignore

    def run(self) -> T:
        raise NotImplementedError("can't run aggregations/group-by yet")
