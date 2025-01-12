from dataclasses import dataclass
from typing import Any

from declaredata_fuse.column import Condition
from declaredata_fuse.column_abc import Column
from declaredata_fuse.proto import sds_pb2

ValOrCol = Any | Column


@dataclass(frozen=True)
class WhenClause:
    condition: Condition
    """The condition to match"""

    if_match: ValOrCol
    """The value that should be in a row if `WhenColumn.condition` is met"""

    if_no_match: ValOrCol | None = None
    """
    The value that should be in a row if `WhenColumn.condition` is not met
    """


@dataclass(frozen=True)
class WhenColumn(Column):
    _name: str
    """The current name of this column"""

    """
    A `Column` implementation that is returned from functions.when. 
    It represents an arbitrarily complex if/else-if/.../else statament
    """

    _clauses: list[WhenClause]
    """
    The clauses to match. The first one in this list that matches will be used,
    and no further clauses will be checked.
    """

    _otherwise: ValOrCol | None = None
    """
    The value that will be used if no clause in `WhenColumn.clauses` matched
    """

    @staticmethod
    def from_cond(name: str, cond: Condition, val: ValOrCol) -> "WhenColumn":
        return WhenColumn(
            _name=name,
            _clauses=[WhenClause(condition=cond, if_match=val)],
            _otherwise=None,
        )

    def when(self, condition: Condition, value: Any | Column) -> "WhenColumn":
        """
        Add another condition to `self`. This condition will be checked only
        if all previously-added conditions do not match.
        """
        new_clause = WhenClause(condition=condition, if_match=value)
        return WhenColumn(
            _name=self._name,
            _clauses=self._clauses + [new_clause],
            _otherwise=self._otherwise,
        )

    def otherwise(self, otherwise: ValOrCol) -> "WhenColumn":
        return WhenColumn(
            _name=self._name,
            _clauses=self._clauses,
            _otherwise=otherwise,
        )

    def cur_name(self) -> str:
        return self._name

    def alias(self, new_name: str) -> "Column":
        return WhenColumn(
            _name=new_name,
            _clauses=self._clauses,
            _otherwise=self._otherwise,
        )

    def to_pb(self) -> sds_pb2.Column:
        raise NotImplementedError("can't turn a WhenColumn into protobuf yet")
