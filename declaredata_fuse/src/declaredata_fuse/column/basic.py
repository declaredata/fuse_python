from typing import Any
from declaredata_fuse.column.aliased import AliasedColumn
from declaredata_fuse.column.base import Column
from declaredata_fuse.column.sorted import SortDirection, SortedColumn
from declaredata_fuse.column.derived import DerivedColumn
from declaredata_fuse.column.operations import BinaryOp
from declaredata_fuse.condition import Condition
from dataclasses import dataclass

from declaredata_fuse.proto import sds_pb2


@dataclass(frozen=True)
class BasicColumn(Column):
    """The representation of a column in a DataFrame"""

    _name: str

    def __gt__(self, other: Any) -> "Condition":
        return Condition(self, ">", other)

    def __ge__(self, other: Any) -> "Condition":
        return Condition(self, ">=", other)

    def __lt__(self, other: Any) -> "Condition":
        return Condition(self, "<", other)

    def __le__(self, other: Any) -> "Condition":
        return Condition(self, "<=", other)

    def __eq__(self, other: Any) -> "Condition":  # type: ignore
        return Condition(self, "==", other)

    def __ne__(self, other: Any) -> "Condition":  # type: ignore
        return Condition(self, "!=", other)

    def __add__(self, other: Any) -> DerivedColumn:
        return DerivedColumn(src_col=self._name, op=BinaryOp.ADD, const=other)

    def __sub__(self, other: Any) -> DerivedColumn:
        return DerivedColumn(src_col=self._name, op=BinaryOp.SUB, const=other)

    def __mul__(self, other: Any) -> DerivedColumn:
        return DerivedColumn(src_col=self._name, op=BinaryOp.MUL, const=other)

    def __truediv__(self, other: Any) -> DerivedColumn:
        return DerivedColumn(src_col=self._name, op=BinaryOp.DIV, const=other)

    def desc(self) -> "SortedColumn":
        return SortedColumn(col=self, dir=SortDirection.DESC)

    def asc(self) -> "SortedColumn":
        return SortedColumn(col=self, dir=SortDirection.ASC)

    def alias(self, new_name: str) -> "Column":
        return AliasedColumn(orig_column=self, new_name=new_name)

    def cur_name(self) -> str:
        return self._name

    def to_pb(self) -> sds_pb2.Column:
        return sds_pb2.Column(col_name=self._name)
