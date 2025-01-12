from typing import Callable

from declaredata_fuse.column.base import Column
from declaredata_fuse.proto import sds_pb2

FilterFunction = Callable[[Column], bool] | Callable[[Column, int], bool]


class FilterColumn(Column):
    """
    A `Column` created by fetching all the rows from another column, then passing
    each row's value to a function to determine whether it should be kept or
    filtered out. If it should be filtered out, the value of the new column at
    that row will be null. If not, it will be identical to the value of the
    original column at that row.

    ## Efficiency Note

    Filtering operations will be done on the client rather than the server, so
    especially for large datasets, these columns can be inefficient. If you can,
    try to use other kinds of `Column`s, because they operate on the server and
    are generally more efficient.
    """

    def __init__(self, col_name: str, func: FilterFunction):
        """
        Create a new `FilteredColumn` using `col_name` as the original column
        whose values should be filtered, and `func` as the filtering function.
        """
        self._orig_col_name = col_name
        self._func = func

    def cur_name(self) -> str:
        return f"{self._orig_col_name}-filter"

    def alias(self, new_name: str) -> Column:
        return AliasedFilterColumn(
            orig_col_name=self._orig_col_name,
            new_col_name=new_name,
            func=self._func,
        )

    def to_pb(self) -> sds_pb2.Column:
        raise NotImplementedError("not implemented")


class AliasedFilterColumn(Column):
    """
    A `FilterColumn` that is identical to another one, but with a new name.

    The same efficiency properties apply to `AliasedFilterColumn`s as to
    `FilteredColumn`s.
    """

    def __init__(self, orig_col_name: str, new_col_name: str, func: FilterFunction):
        """Create a new `AliasedFilterColumn`"""
        self._orig_col_name = orig_col_name
        self._new_col_name = new_col_name
        self._func = func

    def cur_name(self) -> str:
        return self._new_col_name

    def alias(self, new_name: str) -> Column:
        return AliasedFilterColumn(
            orig_col_name=self._orig_col_name,
            new_col_name=new_name,
            func=self._func,
        )

    def to_pb(self) -> sds_pb2.Column:
        raise NotImplementedError("not implemented")
