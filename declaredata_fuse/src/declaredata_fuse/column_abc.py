from abc import ABC, abstractmethod

from declaredata_fuse.proto import sds_pb2
from declaredata_fuse.window import WindowSpec


class Column(ABC):
    """
    A basic representation of a column in a DataFrame.

    This abstract class or its subclasses should almost never be used directly.
    Instead, prefer to use the functions in `declaredata_fuse.functions` to
    create new `Column` instances (or instances of subclasses). An example is
    below:

    ```python
    # assume that 'df' is a DataFrame you already have
    just_the_years_df = df.select(col("year"))
    ```
    """

    @abstractmethod
    def alias(self, new_name: str) -> "Column":
        """
        Create a new column with the same values as this one,
        but with a new name
        """
        ...

    def name(self, new_name: str) -> "Column":
        """Same as self.alias(new_name)"""
        return self.alias(new_name=new_name)

    @abstractmethod
    def cur_name(self) -> str:
        """
        Get the name of this column. Note that some `Column` subclasses have
        member variables that hold a full or partial name. Even in those cases,
        you should prefer to use `cur_name` to get column names. This method's
        return value will change if `name` or `alias` are called.
        """
        ...

    @abstractmethod
    def to_pb(self) -> sds_pb2.Column:
        """
        Get the protobuf-encoded representation of this column. Not intended
        for public use.
        """
        ...

    def over(self, window: WindowSpec) -> "Column":
        """
        Specify that the computation used to derive this column should be
        applied over a window of rows.

        Note that only some types of computations support windowing. If you
        call this method on a `Column` that is using an unsupported computation,
        this method will raise a `NotImplementedError`.
        """
        raise NotImplementedError("column doesn't support windowing")
