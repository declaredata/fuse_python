from dataclasses import dataclass
from typing import Any, TYPE_CHECKING

from declaredata_fuse.condition.and_condition import AndCondition
from declaredata_fuse.condition.base import BaseCondition
from declaredata_fuse.condition.or_condition import OrCondition
from declaredata_fuse.condition.single import SingleCondition

if TYPE_CHECKING:
    from declaredata_fuse.column_abc import Column

from declaredata_fuse.proto import sds_pb2


@dataclass(frozen=True)
class Condition(BaseCondition):
    single: SingleCondition | None
    conj: AndCondition | None
    disj: OrCondition | None

    @staticmethod
    def new_single(left: "Column", operator: str, right: Any) -> "Condition":
        return Condition(
            single=SingleCondition(left=left, operator=operator, right=right),
            conj=None,
            disj=None,
        )

    def description(self) -> str:
        if self.single is not None:
            return self.single.description()
        elif self.conj is not None:
            return self.conj.description()
        else:
            assert self.disj is not None
            return self.disj.description()

    def to_pb(self) -> sds_pb2.FilterCondition:
        """
        Turn `self` into a Fuse-compatible protobuf payload.

        For internal use only.
        """
        if self.single:
            return sds_pb2.FilterCondition(single=self.single.to_pb())
        elif self.conj:
            return sds_pb2.FilterCondition(conjunction=self.conj.to_pb())
        elif self.disj:
            return sds_pb2.FilterCondition(disjunction=self.disj.to_pb())
        else:
            raise ValueError(
                "exactly one of [single, conjunction, disjunction] condition must be set"
            )

    def __and__(self, other: "Condition") -> "Condition":
        """
        Return a new `Condition` that is the conjunction (e.g. `&&`) of
        `self` and `other`
        """
        return Condition(
            single=None,
            conj=AndCondition(cond1=self, cond2=other),
            disj=None,
        )

    def __or__(self, other: "Condition") -> "Condition":
        """
        Return a new `Condition` that is the disjunction (e.g. `||`) of
        `self` and `other`
        """
        return Condition(
            single=None,
            conj=None,
            disj=OrCondition(self, other),
        )
