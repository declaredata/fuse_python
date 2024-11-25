from enum import Enum
from dataclasses import dataclass


class RowBoundary(Enum):
    """Non-numeric row boundaries"""

    UnboundedPreceding = 1
    """
    Indicates that the left boundary of a window should be the begininng of
    the partition
    """


class Window:
    """Builders for WindowSpecs"""

    unboundedPreceding: RowBoundary = RowBoundary.UnboundedPreceding
    """See the RowBoundary.UnboundedPreceding for details"""

    @staticmethod
    def orderBy(col_name: str) -> "WindowSpec":
        """
        Create a new WindowSpec representing a window that is ordered by
        the values in the given col name
        """
        return WindowSpec(order_col=col_name)

    @staticmethod
    def partitionBy(col_name: str) -> "WindowSpec":
        """
        Create a new WindowSpec with partitions created from the values in the
        given column name
        """
        return WindowSpec(partition_col=col_name)


@dataclass
class WindowSpec:
    """The specification for a window query"""

    left: RowBoundary | int = RowBoundary.UnboundedPreceding
    """The specification for the left side of the window"""
    right: RowBoundary | int = 0
    """The specification for the right side of the window"""
    order_col: str | None = None
    """
    The column whose values should be used to order the rows in 
    the window.
    
    If this is None, an arbitrary ordering, that is not guaranteed
    and may change over time, will be chosen.
    """
    partition_col: str | None = None
    """
    The column whose values should be used to choose partitions prior to 
    constructing windows.
    
    If this is None, partitions will be chosen in an unspecified way that
    may change over time.
    """

    def partitionBy(self, col_name: str) -> "WindowSpec":
        """
        Modify this window spec to partition on the values of the given
        column name
        """
        self.partition_col = col_name
        return self

    def orderBy(self, col_name: str) -> "WindowSpec":
        """
        Modify this window spec to order rows based on the values in the given
        column name
        """
        self.order_col = col_name
        return self

    def rowsBetween(
        self, left: RowBoundary | int, right: RowBoundary | int
    ) -> "WindowSpec":
        """
        Modify this window spec to alter the "window frame". In other words,
        specify the left and right boundaries of each window inside an
        arbitrary partition.
        """
        self.left = left
        self.right = right
        return self
