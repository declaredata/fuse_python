from collections.abc import Callable
from dataclasses import dataclass

from declaredata_fuse.column import Column

FilterFunctionDef = Callable[[Column], Column] | Callable[[Column, int], Column]


@dataclass(frozen=True)
class FilterFunction:
    col_name: str
    filter_func: FilterFunctionDef

    def alias(self, new_name: str) -> "AliasedFilterFunction":
        return AliasedFilterFunction(
            orig_col_name=self.col_name,
            new_col_name=new_name,
            filter_func=self.filter_func,
        )

    # def to_pb(self) ->


@dataclass(frozen=True)
class AliasedFilterFunction:
    orig_col_name: str
    new_col_name: str
    filter_func: FilterFunctionDef

    # def to_pb(self) ->
