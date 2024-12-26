from dataclasses import dataclass
from declaredata_fuse.column_abc import Column
from declaredata_fuse.proto import sds_pb2


@dataclass(frozen=True)
class AliasedColumn(Column):
    orig_column: Column
    """The original name of the column"""
    new_name: str
    """The name of the new column"""

    def alias(self, new_name: str) -> "Column":
        """
        Create a new column with the same data as this one, but with a
        new name.
        """
        return AliasedColumn(orig_column=self.orig_column, new_name=new_name)

    def cur_name(self) -> str:
        """Get the current name of this `AliasedColumn`"""
        return self.new_name

    def to_pb(self) -> sds_pb2.Column:
        """Not intended for public use."""
        return sds_pb2.Column(col_name=self.new_name)
