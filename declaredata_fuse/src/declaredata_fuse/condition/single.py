from dataclasses import dataclass

from typing import TYPE_CHECKING, Any

from declaredata_fuse.column_or_name import col_or_name_to_basic
from declaredata_fuse.condition.base import BaseCondition
from declaredata_fuse.proto import sds_pb2

if TYPE_CHECKING:
    from declaredata_fuse.column_abc import Column


@dataclass(frozen=True)
class SingleCondition(BaseCondition):
    left: "Column"
    operator: str
    right: Any

    def description(self) -> str:
        left_name = col_or_name_to_basic(self.left)
        return f"{left_name}{self.operator}{self.right}"

    def to_pb(self) -> sds_pb2.SingleCondition:
        """
        Turn `self` into a Fuse-compatible gRPC/protobuf payload.

        For internal use only
        """
        right = str(self.right)
        return sds_pb2.SingleCondition(
            left=self.left.cur_name(), operator=self.operator, right=right
        )
