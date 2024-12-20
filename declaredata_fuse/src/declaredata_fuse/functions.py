from dataclasses import dataclass
from typing import Any
from declaredata_fuse.column import Column, SortDirection, SortedColumn
from declaredata_fuse.column_coalesce import CoalesceColumn
from declaredata_fuse.column_literal import LiteralColumn
from declaredata_fuse.column_or_name import ColumnOrName, col_or_name_to_basic
from declaredata_fuse.proto.sds_pb2 import (
    AggOperation,
    Agg,
)


def asc(col: ColumnOrName) -> SortedColumn:
    """Return a SortedColumn to sort the given column in ascending"""
    return SortedColumn(col=col_or_name_to_basic(col), dir=SortDirection.ASC)


def desc(col: ColumnOrName) -> SortedColumn:
    """Return a SortedColumn to sort the given column in descending"""
    return SortedColumn(col=col_or_name_to_basic(col), dir=SortDirection.DESC)


def col(col_name: str) -> Column:
    return col_or_name_to_basic(col_name)


def column(col_name: str) -> Column:
    return col(col_name)


def lit(val: Any) -> Column:
    return LiteralColumn(_name=f"lit_{val}", lit_val=val)


def coalesce(*cols: ColumnOrName) -> Column:
    cols_reified: list[Column] = [col_or_name_to_basic(col) for col in cols]
    names = [col.cur_name() for col in cols_reified]
    new_col_name = f"coalesce({', '.join(names)})"
    return CoalesceColumn(_name=new_col_name, cols=cols_reified)


def sum(col_name: str) -> "Function":
    """Create a function to sum the values of a column"""
    # TODO: return type should be Column here
    return Function(col_name=col_name, op=AggOperation.SUM)


def count(col_name: str) -> "Function":
    """Create a function to count the number of values in a column"""
    # TODO: return type should be Column here
    return Function(col_name=col_name, op=AggOperation.COUNT)


def min(col_name: str) -> "Function":
    """Create a function to find the minimum value"""
    # TODO: return type should be Column here
    return Function(col_name=col_name, op=AggOperation.MIN)


def max(col_name: str) -> "Function":
    """Create a function to find the maximum value"""
    # TODO: return type should be Column here
    return Function(col_name=col_name, op=AggOperation.MAX)


def first(col_name: str) -> "Function":
    """Create a function to find the first value"""
    # TODO: return type should be Column here
    return Function(col_name=col_name, op=AggOperation.FIRST)


def last(col_name: str) -> "Function":
    """Create a function to find the last value"""
    # TODO: return type should be Column here
    return Function(col_name=col_name, op=AggOperation.LAST)


@dataclass(frozen=True)
class Function:
    """
    A function that will be executed over the values of 1 or more columns
    over a series of rows.

    If you don't already have an instance of Function, the best way to create
    a new one is with one of the free-standing functions like sum() or count()

    If you do already have an instance of Function, you can create new,
    derivative Functions from that one using methods like alias() and over()
    """

    col_name: str
    op: AggOperation.ValueType
    alias_col_name: str | None = None

    def alias(self, new_col_name: str) -> "Function":
        """
        Create a new function that will put the return value of the existing
        function into a new column with the specified name
        """
        return Function(
            col_name=self.col_name,
            alias_col_name=new_col_name,
            op=self.op,
        )

    def to_pb(self) -> Agg:
        """
        Convert this function into a protobuf-compatible structure.
        Not for public use.
        """
        return Agg(
            col_name=self.col_name,
            op=self.op,
            alias=self.alias_col_name,
        )
