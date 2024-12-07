from itertools import chain
from typing import Any
from declaredata_fuse.column import Column, SortedColumn, asc, desc


_KWARGS_ASC_KEY = "ascending"


def _asc_from_kwargs(**kwargs: Any) -> bool | None:
    if _KWARGS_ASC_KEY in kwargs:
        return (
            kwargs[_KWARGS_ASC_KEY]
            if isinstance(kwargs[_KWARGS_ASC_KEY], bool)
            else None
        )
    return None


def _convert_col(
    *, col: str | Column | list[str | Column], is_asc: bool
) -> list[SortedColumn]:
    sort_fn = asc if is_asc else desc
    match col:
        case str():
            return [sort_fn(col)]
        case Column():
            return [sort_fn(col.name)]
        case _:
            list_of_lists = [_convert_col(col=c, is_asc=is_asc) for c in col]
            ch = chain.from_iterable(list_of_lists)
            return list(ch)


def to_sorted_col_list(
    *cols: str | Column | list[str | Column],
    **kwargs: Any,
) -> list[SortedColumn]:
    global_asc = _asc_from_kwargs(**kwargs)
    # if ascending=False was passed, then do descending. otherwise use
    # asc if it was ascending=True or if it was missing (i.e. the default)
    is_asc = False if global_asc is not None and not global_asc else True
    list_of_lists = [_convert_col(col=c, is_asc=is_asc) for c in cols]
    return list(chain.from_iterable(list_of_lists))
