from dataclasses import dataclass
from declaredata_fuse.column import Column, SortDirection, SortedColumn
from declaredata_fuse.column_filter import FilterColumn, FilterFunction
from declaredata_fuse.column_or_name import ColumnOrName, col_or_name_to_basic
from declaredata_fuse.proto.sds_pb2 import (
    AggOperation,
    Agg,
    WindowSpec as ProtoWindowSpec,
)
from declaredata_fuse.window import WindowSpec


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


def sum(col_name: str) -> "Function":
    """Create a function to sum the values of a column"""
    return Function(col_name=col_name, op=AggOperation.SUM)


def count(col_name: str) -> "Function":
    """Create a function to count the number of values in a column"""
    return Function(col_name=col_name, op=AggOperation.COUNT)


def min(col_name: str) -> "Function":
    """Create a function to find the minimum value"""
    return Function(col_name=col_name, op=AggOperation.MIN)


def max(col_name: str) -> "Function":
    """Create a function to find the maximum value"""
    return Function(col_name=col_name, op=AggOperation.MAX)


def first(col_name: str) -> "Function":
    """Create a function to find the first value"""
    return Function(col_name=col_name, op=AggOperation.FIRST)


def last(col_name: str) -> "Function":
    """Create a function to find the last value"""
    return Function(col_name=col_name, op=AggOperation.LAST)


def filter(col: Column | str, func: FilterFunction) -> Column:
    col_reified = col.cur_name() if isinstance(col, Column) else col
    return FilterColumn(col_name=col_reified, func=func)

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
    window_spec: WindowSpec | None = None

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

    def over(self, window: WindowSpec) -> "Function":
        """
        Create a new function that will execute the existing function over the
        given window
        """
        return Function(
            col_name=self.col_name,
            op=self.op,
            alias_col_name=self.alias_col_name,
            window_spec=window,
        )

    def to_pb(self) -> Agg:
        """
        Convert this function into a protobuf-compatible structure.

        This is not for public use.
        """
        window_spec: ProtoWindowSpec | None = None
        if self.window_spec is not None:
            left = self.window_spec.left if type(self.window_spec.left) is int else 0
            right = self.window_spec.right if type(self.window_spec.right) is int else 0
            window_spec = ProtoWindowSpec(
                partition_by=self.window_spec.partition_col or "",
                order_by=self.window_spec.order_col or "",
                left_boundary=left,
                right_boundary=right,
            )

        return Agg(
            col_name=self.col_name,
            op=self.op,
            alias=self.alias_col_name,
            window=window_spec,
        )
