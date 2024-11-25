from typing import Any, TypeVar


T = TypeVar("T", bound="Row")


class Row:
    _lookup: dict[str, Any]

    def __init__(self, lookup: dict[str, Any]):
        self._lookup = lookup

    def __getattr__(self, name: str) -> Any:
        if name not in self._lookup:
            raise NameError(f"{name} is not found in this row")
        return self._lookup[name]

    def __getitem__(self, name: str) -> Any:
        return self.__getattr__(name)

    def asDict(self, recursive: bool = False) -> dict[str, Any]:
        return self._lookup
