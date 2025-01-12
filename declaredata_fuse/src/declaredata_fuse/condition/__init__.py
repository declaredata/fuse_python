from dataclasses import dataclass
from typing import Any
from declaredata_fuse.column.base import Column
from declaredata_fuse.proto import sds_pb2


@dataclass
class Condition:
    left: "Column"
    operator: str
    right: Any

    def to_pb(self) -> sds_pb2.FilterCondition:
        right = str(self.right)
        return sds_pb2.FilterCondition(
            left=self.left.cur_name(), operator=self.operator, right=right
        )
