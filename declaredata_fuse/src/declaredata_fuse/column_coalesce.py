from dataclasses import dataclass

from declaredata_fuse.column import BasicColumn
from declaredata_fuse.column_abc import Column
from declaredata_fuse.proto import sds_pb2


@dataclass(frozen=True)
class CoalesceColumn(BasicColumn):
    """
    A column that is created by selecting the first non-null value from a list
    of other columns in the same row.
    """

    cols: list[Column]
    """The columns from which to look for non-null values."""

    def alias(self, new_name: str) -> Column:
        """
        Create a new `CoalesceColumn` identical to this one,
        but with a new name
        """
        return CoalesceColumn(_name=new_name, cols=self.cols)

    def to_pb(self) -> sds_pb2.Column:
        """Not intended for public use."""
        col_names = [col.cur_name() for col in self.cols]
        return sds_pb2.Column(
            col_coalesce=sds_pb2.CoalesceColumn(
                name=self._name,
                cols=col_names,
            )
        )
