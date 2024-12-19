from dataclasses import dataclass
from typing import Any
from declaredata_fuse.column import BasicColumn
from declaredata_fuse.column_abc import Column
from declaredata_fuse.proto import sds_pb2


@dataclass(frozen=True)
class TypedAny:
    val: str | int

    def to_pb(self) -> sds_pb2.TypedAny:
        if isinstance(self.val, str):
            return sds_pb2.TypedAny(str_val=self.val)
        else:
            return sds_pb2.TypedAny(i64_val=str(self.val))


@dataclass(frozen=True)
class LiteralColumn(BasicColumn):
    lit_val: Any

    def alias(self, new_name: str) -> Column:
        return LiteralColumn(_name=new_name, lit_val=self.lit_val)

    def to_pb(self) -> sds_pb2.Column:
        typed_any = sds_pb2.TypedAny(str_val=self.lit_val)
        return sds_pb2.Column(
            col_lit=sds_pb2.LiteralColumn(name=self.cur_name(), val=[typed_any])
        )
