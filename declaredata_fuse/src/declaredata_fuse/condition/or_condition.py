from dataclasses import dataclass

from typing import TYPE_CHECKING

from declaredata_fuse.condition.base import BaseCondition
from declaredata_fuse.proto import sds_pb2

if TYPE_CHECKING:
    from declaredata_fuse.condition import Condition


@dataclass(frozen=True)
class OrCondition(BaseCondition):
    cond1: "Condition"
    cond2: "Condition"

    def description(self) -> str:
        return f"{self.cond1.description()} | {self.cond2.description()}"

    def to_pb(self) -> sds_pb2.OrCondition:
        """
        Turn `self` into a Fuse-compatible protobuf payload.

        For internal use only.
        """
        return sds_pb2.OrCondition(
            cond1=self.cond1.to_pb(),
            cond2=self.cond2.to_pb(),
        )
