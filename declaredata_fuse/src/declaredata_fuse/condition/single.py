from dataclasses import dataclass

from typing import TYPE_CHECKING, Any

from declaredata_fuse.proto import sds_pb2

if TYPE_CHECKING:
    from declaredata_fuse.column_abc import Column


@dataclass(frozen=True)
class SingleCondition:
    left: "Column"
    operator: str
    right: Any

    def to_pb(self) -> sds_pb2.SingleCondition:
        right = str(self.right)
        return sds_pb2.SingleCondition(
            left=self.left.cur_name(), operator=self.operator, right=right
        )
