from dataclasses import dataclass
from declaredata_fuse.column_abc import Column
from declaredata_fuse.proto import sds_pb2


@dataclass
class AliasedColumn(Column):
    orig_column: Column
    new_name: str

    def alias(self, new_name: str) -> "Column":
        return AliasedColumn(orig_column=self.orig_column, new_name=new_name)

    def cur_name(self) -> str:
        return self.new_name

    def to_pb(self) -> sds_pb2.Column:
        return sds_pb2.Column(col_name=self.new_name)
