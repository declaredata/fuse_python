from typing import Literal
from dataclasses import dataclass

from declaredata_fuse.proto import sds_pb2


@dataclass(frozen=True)
class RowBoundary:
    direction: Literal["preceding", "following"]


class Window:
    """Builders for WindowSpecs"""

    unboundedPreceding: RowBoundary = RowBoundary(direction="preceding")
    """
    Indicates that the left boundary of a window should be the begininng of
    the partition
    """

    unboundedFollowing: RowBoundary = RowBoundary(direction="following")
    """
    Indicates that the right boundary of a window should be at the end
    of the partition.
    """

    currentRow: int = 0
    """
    Indicates that one of the boundaries (left or right) should be the 
    current row. You can just pass the value 0 to indicate the current row,
    but it's recommended to use this constant instead.
    """

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

    left: int | None = None
    """
    The specification for the left side of the window.

    Passing None here indicates an unbounded left side of the window.
    """
    right: int | None = None
    """
    The specification for the right side of the window.

    Passing None here indicates an unbounded right side of the window.
    """
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

    is_range: bool = False
    """
    True if this spec defines a range of values, False if it defines 
    a range of rows
    """

    def partitionBy(self, col_name: str) -> "WindowSpec":
        """
        Modify this window spec to partition on the values of the given
        column name
        """
        return WindowSpec(
            left=self.left,
            right=self.right,
            order_col=self.order_col,
            partition_col=col_name,
            is_range=self.is_range,
        )

    def orderBy(self, col_name: str) -> "WindowSpec":
        """
        Modify this window spec to order rows based on the values in the given
        column name
        """
        return WindowSpec(
            left=self.left,
            right=self.right,
            order_col=col_name,
            partition_col=self.partition_col,
            is_range=self.is_range,
        )

    def rowsBetween(
        self, left: int | RowBoundary, right: int | RowBoundary
    ) -> "WindowSpec":
        """
        Specify the window frame to start at a given number of rows before
        the current one (left), and end a given number of rows after the
        current one (right).

        PySpark docs for reference:

        https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.Window.rowsBetween.html
        """
        return WindowSpec(
            left=left if isinstance(left, int) else None,
            right=right if isinstance(right, int) else None,
            order_col=self.order_col,
            partition_col=self.partition_col,
            is_range=False,
        )

    def rangeBetween(
        self,
        left: int | RowBoundary,
        right: int | RowBoundary,
    ) -> "WindowSpec":
        """
        Similar to self.rowsBetween(left, right), except left and right params
        express a range of _values_ rather than rows to include in the window
        frame.

        PySpark docs for reference:

        https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.Window.rangeBetween.html
        """
        return WindowSpec(
            left=left if isinstance(left, int) else None,
            right=right if isinstance(right, int) else None,
            order_col=self.order_col,
            partition_col=self.partition_col,
            is_range=True,
        )

    def to_pb2(self) -> sds_pb2.WindowSpec:
        return sds_pb2.WindowSpec(
            partition_by=self.partition_col,
            order_by=self.order_col,
            left_boundary=self.left,
            right_boundary=self.right,
        )
