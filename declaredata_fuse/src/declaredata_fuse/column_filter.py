from typing import Callable

from declaredata_fuse.column_abc import Column

FilterFunction = Callable[[Column], bool] | Callable[[Column, int], bool]


class FilterColumn(Column):
    def __init__(self, col_name: str, func: FilterFunction):
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


class AliasedFilterColumn:
    def __init__(self, orig_col_name: str, new_col_name: str, func: FilterFunction):
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
