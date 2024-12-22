from typing import Any
from declaredata_fuse.column import Column, SortDirection, SortedColumn
from declaredata_fuse.column_coalesce import CoalesceColumn
from declaredata_fuse.column_functional import FunctionalColumn
from declaredata_fuse.column_literal import LiteralColumn
from declaredata_fuse.column_or_name import ColumnOrName, col_or_name_to_basic
from declaredata_fuse.proto import sds_pb2


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


def sum(col: ColumnOrName) -> Column:
    """Create a function to sum the values of a column"""
    col_name = col_or_name_to_basic(col).cur_name()
    return FunctionalColumn(
        _name=FunctionalColumn.col_name("sum", col_name),
        args=[col_name],
        function=sds_pb2.Function.SUM,
    )


def count(col: ColumnOrName) -> Column:
    """Create a function to count the number of values in a column"""
    col_name = col_or_name_to_basic(col).cur_name()
    return FunctionalColumn(
        _name=FunctionalColumn.col_name("count", col_name),
        args=[col_name],
        function=sds_pb2.Function.COUNT,
    )


def min(col: ColumnOrName) -> Column:
    """Create a function to find the minimum value"""
    col_name = col_or_name_to_basic(col).cur_name()
    return FunctionalColumn(
        _name=FunctionalColumn.col_name("min", col_name),
        args=[col_name],
        function=sds_pb2.Function.MIN,
    )


def max(col: ColumnOrName) -> Column:
    """Create a function to find the maximum value"""
    col_name = col_or_name_to_basic(col).cur_name()
    return FunctionalColumn(
        _name=FunctionalColumn.col_name("max", col_name),
        args=[col_name],
        function=sds_pb2.Function.MAX,
    )


def first(col: ColumnOrName) -> Column:
    """Create a function to find the first value"""
    col_name = col_or_name_to_basic(col).cur_name()
    return FunctionalColumn(
        _name=FunctionalColumn.col_name("first", col_name),
        args=[col_name],
        function=sds_pb2.Function.FIRST,
    )


def last(col: ColumnOrName) -> Column:
    """Create a function to find the last value"""
    col_name = col_or_name_to_basic(col).cur_name()
    return FunctionalColumn(
        _name=FunctionalColumn.col_name("last", col_name),
        args=[col_name],
        function=sds_pb2.Function.LAST,
    )
