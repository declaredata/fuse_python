from dataclasses import dataclass

from typing import TYPE_CHECKING

from declaredata_fuse.proto import sds_pb2

if TYPE_CHECKING:
    from declaredata_fuse.condition import Condition


@dataclass(frozen=True)
class AndCondition:
    cond1: Condition
    cond2: Condition

    def to_pb(self) -> sds_pb2.AndCondition:
        return sds_pb2.AndCondition(
            cond1=self.cond1.to_pb(),
            cond2=self.cond2.to_pb(),
        )
