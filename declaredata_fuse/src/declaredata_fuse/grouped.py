from dataclasses import dataclass
from typing import TYPE_CHECKING

<<<<<<< HEAD:declaredata_fuse/src/declaredata_fuse/grouped.py
from declaredata_fuse.functions import Function
from declaredata_fuse.proto import sds_pb2
from declaredata_fuse.proto.sds_pb2 import Agg
from declaredata_fuse.proto.sds_pb2_grpc import sdsStub

if TYPE_CHECKING:
    from declaredata_fuse.dataframe import DataFrame
=======
from declaredata_fuse.column_abc import Column
from declaredata_fuse.proto import sds_pb2_grpc, sds_pb2
>>>>>>> origin/main:declaredata_fuse/src/declaredata_fuse/agg.py


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
        resp = self.stub.Aggregate(req)
        from declaredata_fuse.dataframe import DataFrame
        return DataFrame(
            df_uid=resp.dataframe_uid,
            stub=self.stub
        )

