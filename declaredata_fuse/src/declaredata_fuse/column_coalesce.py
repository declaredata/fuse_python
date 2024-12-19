from dataclasses import dataclass

from declaredata_fuse.column import BasicColumn
from declaredata_fuse.column_abc import Column
from declaredata_fuse.proto import sds_pb2


@dataclass(frozen=True)
class CoalesceColumn(BasicColumn):
    cols: list[Column]

    def alias(self, new_name: str) -> Column:
        return CoalesceColumn(_name=new_name, cols=self.cols)
    
    def to_pb(self) -> sds_pb2.Column:
        col_names = [col.cur_name() for col in self.cols]
        return sds_pb2.Column(
            col_coalesce=sds_pb2.CoalesceColumn(
                name=self._name,
                cols=col_names,
            )
        )
