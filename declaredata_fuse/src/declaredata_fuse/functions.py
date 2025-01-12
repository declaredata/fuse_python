from typing import Any
from declaredata_fuse.column import (
    BasicColumn,
    Column,
    Condition,
    SortDirection,
    SortedColumn,
)
from declaredata_fuse.column_coalesce import CoalesceColumn
from declaredata_fuse.column_functional import FunctionalColumn
from declaredata_fuse.column_literal import LiteralColumn
from declaredata_fuse.column_or_name import ColumnOrName, col_or_name_to_basic
from declaredata_fuse.column_when import WhenColumn, ValOrCol
from declaredata_fuse.proto import sds_pb2


def asc(col: ColumnOrName) -> SortedColumn:
    """Return a SortedColumn to sort the given column in ascending"""
    return SortedColumn(col=col_or_name_to_basic(col), dir=SortDirection.ASC)


def desc(col: ColumnOrName) -> SortedColumn:
    """Return a SortedColumn to sort the given column in descending"""
    return SortedColumn(col=col_or_name_to_basic(col), dir=SortDirection.DESC)


def col(col_name: str) -> BasicColumn:
    """Return a reference to a pre-existing column"""
    return col_or_name_to_basic(col_name)


def column(col_name: str) -> BasicColumn:
    """Alias of `col(col_name)`"""
    return col(col_name)


def lit(val: Any) -> Column:
    """
    Return a new column with `val` in all rows
    """
    return LiteralColumn(_name=f"lit_{val}", lit_val=val)


def coalesce(*cols: ColumnOrName) -> Column:
    """
    Create a new column where each row contains the first non-`null` value
    in the given `cols` list.

    In other words, given a row, this function looks through the values
    in each of the given columns and copies the first non-`null` value into
    the new column.

    If all values in `cols` are null, the new column will also contain
    `null`.
    """
    cols_reified: list[Column] = [col_or_name_to_basic(col) for col in cols]
    names = [col.cur_name() for col in cols_reified]
    new_col_name = f"coalesce({', '.join(names)})"
    return CoalesceColumn(_name=new_col_name, cols=cols_reified)


def sum(col: ColumnOrName) -> Column:
    """
    Return a new column 
    Create a function to sum the values of a column"""
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


def when(cond: Condition, value: ValOrCol) -> WhenColumn:
    """
    Evaluate the condition described in `cond` and return a new `WhenColumn`
    that has `value` in the row when the condition is met. `value` can be
    a reference to a different `Column` or a constant.

    If the condition in `col` did not have `otherwise` called on it, and the
    condition is not met, `None` is put in the row. If `otherwise` was called
    on `col`, then the value passed to `otherwise` is put in the row.

    PySpark documentation:

    https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.functions.when.html
    """
    col_name = cond.description()
    return WhenColumn.from_cond(name=col_name, cond=cond, val=value)


def max(col: BasicColumn) -> Column:
    """
    Create a new `Column` that contains the maximum value in a given existing
    `Column`, `col`, across all rows in a window or group.

    Must only be used in windowing or aggregation (i.e. `DataFrame.groupBy`)
    scenarios.
    """
    col_name = col_or_name_to_basic(col).cur_name()
    return FunctionalColumn(
        _name=FunctionalColumn.col_name("max", col_name),
        args=[col_name],
        function=sds_pb2.Function.MAX,
    )


def first(col: ColumnOrName) -> Column:
    """
    Create a new `Column` that extracts the first value in `col` across all the
    rows in a window or group of rows.

    Must only be used in windowing or aggregation (i.e. `DataFrame.groupBy`)
    scenarios
    """
    col_name = col_or_name_to_basic(col).cur_name()
    return FunctionalColumn(
        _name=FunctionalColumn.col_name("first", col_name),
        args=[col_name],
        function=sds_pb2.Function.FIRST,
    )


def last(col: ColumnOrName) -> Column:
    """
    This function creates a new `Column` that extracts the last value in a
    given existing `Column` from a window or group of rows.

    Must only be used in windowing or aggregation (i.e. `DataFrame.groupBy`)
    scenarios
    """
    col_name = col_or_name_to_basic(col).cur_name()
    return FunctionalColumn(
        _name=FunctionalColumn.col_name("last", col_name),
        args=[col_name],
        function=sds_pb2.Function.LAST,
    )


def mean(col: ColumnOrName) -> Column:
    """
    This function creates a new `Column` that calculates the average value
    of the values in a given existing column across a set of rows in either
    a window or group.

    Must only be used in windowing or aggregation (i.e. `DataFrame.groupBy`)
    scenarios
    """
    col_name = col_or_name_to_basic(col).cur_name()
    return FunctionalColumn(
        _name=FunctionalColumn.col_name("mean", col_name),
        args=[col_name],
        function=sds_pb2.Function.MEAN,
    )


def mode(col: ColumnOrName) -> Column:
    """
    This function creates a new `Column` that gets the mode (most commonly
    found value) in a given existing `Column` across a set of rows in a 
    window or group.

    Must only be used in windowing or aggregation (i.e. `DataFrame.groupBy`)
    scenarios
    """
    col_name = col_or_name_to_basic(col).cur_name()
    return FunctionalColumn(
        _name=FunctionalColumn.col_name("mode", col_name),
        args=[col_name],
        function=sds_pb2.Function.MODE,
    )


def row_number() -> Column:
    """
    This function creates a new `Column` that contains a sequential number, 
    starting at 1, representing the current row within a window partition.

    Must only be used in windowing scenarios.
    """
    col_name = "row_number()"
    return FunctionalColumn(
        _name=FunctionalColumn.col_name("row_number", col_name),
        args=[],
        function=sds_pb2.Function.ROW_NUMBER,
    )
