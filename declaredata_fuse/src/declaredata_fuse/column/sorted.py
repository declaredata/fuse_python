from enum import Enum
from dataclasses import dataclass
from declaredata_fuse.column.base import Column
from declaredata_fuse.proto import sds_pb2


class SortDirection(Enum):
    """The direction by which to sort"""

    ASC = 0
    """Sort by ascending - lowest values first"""
    DESC = 1
    """Sort by descending - highest values first"""


@dataclass
class SortedColumn:
    """A sorting specification"""

    col: "Column"
    """The column whose values should be used to sort rows"""
    dir: SortDirection
    """The direction by which to sort"""

    def to_pb(self) -> sds_pb2.SortColumn:
        """
        Convert this SortedColumn specification to protobuf.

        Not intended for public use.
        """
        dir = (
            sds_pb2.SortDirection.ASC
            if self.dir == SortDirection.ASC
            else sds_pb2.SortDirection.DESC
        )
        return sds_pb2.SortColumn(
            col_name=self.col.cur_name(),
            direction=dir,
        )
