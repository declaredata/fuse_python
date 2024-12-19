from enum import Enum
from dataclasses import dataclass
from declaredata_fuse.column_abc import Column
from declaredata_fuse.column_alias import AliasedColumn
from declaredata_fuse.column_op import BinaryOp, DerivedColumn, NamedDerivedColumn
from declaredata_fuse.proto import sds_pb2
from typing import Any


@dataclass
class Condition:
    left: "Column"
    operator: str
    right: Any

    def to_pb(self) -> sds_pb2.FilterCondition:
        right = str(self.right)
        return sds_pb2.FilterCondition(
            left=self.left.cur_name(), operator=self.operator, right=right
        )


class SortDirection(Enum):
    """The direction by which to sort"""

    ASC = 0
    """Sort by ascending - lowest values first"""
    DESC = 1
    """Sort by descending - highest values first"""


@dataclass
class SortedColumn:
    """A sorting specification"""

    col: "Column"
    """The column whose values should be used to sort rows"""
    dir: SortDirection
    """The direction by which to sort"""

    def to_pb(self) -> sds_pb2.SortColumn:
        """
        Convert this SortedColumn specification to protobuf.

        Not intended for public use.
        """
        dir = (
            sds_pb2.SortDirection.ASC
            if self.dir == SortDirection.ASC
            else sds_pb2.SortDirection.DESC
        )
        return sds_pb2.SortColumn(
            col_name=self.col.cur_name(),
            direction=dir,
        )


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


SelectColumn = str | Column | NamedDerivedColumn
DropColumn = str | Column


def select_column_to_pb(src: SelectColumn) -> sds_pb2.Column:
    match src:
        case str():
            return sds_pb2.Column(col_name=src)
        case Column():
            return src.to_pb()
        case NamedDerivedColumn():
            return sds_pb2.Column(col_derived=src.to_pb())
