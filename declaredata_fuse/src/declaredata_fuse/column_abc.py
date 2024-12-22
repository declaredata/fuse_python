from abc import ABC, abstractmethod

from declaredata_fuse.proto import sds_pb2
from declaredata_fuse.window import WindowSpec


class Column(ABC):
    """A basic representation of a column in a DataFrame"""

    @abstractmethod
    def alias(self, new_name: str) -> "Column": ...

    """
    Create a new column with the same values as this one,
    but with a new name
    """

    def name(self, new_name: str) -> "Column":
        """Same as self.alias(new_name)"""
        return self.alias(new_name=new_name)

    @abstractmethod
    def cur_name(self) -> str: ...

    """Get the name of this column"""

    @abstractmethod
    def to_pb(self) -> sds_pb2.Column: ...

    """
    Get the protobuf-encoded representation of this column. Not intended
    for public use.
    """

    def over(self, window: WindowSpec) -> "Column":
        """
        Apply a window frame to this column. Only some columns implement
        this, while the rest will raise a not-implemented exception.
        """
        raise NotImplementedError("column doesn't support windowing")
