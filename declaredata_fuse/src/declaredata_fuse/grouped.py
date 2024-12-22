from dataclasses import dataclass
from typing import TYPE_CHECKING


from declaredata_fuse.column_abc import Column
from declaredata_fuse.proto import sds_pb2
from declaredata_fuse.proto.sds_pb2_grpc import sdsStub

if TYPE_CHECKING:
    from declaredata_fuse.dataframe import DataFrame


@dataclass(frozen=True)
class Grouped:
    group_cols: list[str]
    """The columns to group by in the aggregation"""
    df_uid: str
    stub: sdsStub

    def agg(self, *cols: Column) -> "DataFrame":
        cols_pb = [col.to_pb() for col in cols]

        req = sds_pb2.AggregateRequest(
            dataframe_uid=self.df_uid,
            group_by=self.group_cols,
            cols=cols_pb,
        )
        resp = self.stub.Aggregate(req)  # type: ignore
        from declaredata_fuse.dataframe import DataFrame

        return DataFrame(
            df_uid=resp.dataframe_uid,  # type: ignore
            stub=self.stub,
        )
