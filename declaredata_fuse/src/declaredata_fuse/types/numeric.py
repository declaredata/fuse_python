from declaredata_fuse.types import DataType


class DecimalType(DataType):
    def __init__(self, one: int, two: int) -> None:
        self._one = one
        self._two = two


class DoubleType(DataType):
    pass


class IntegerType(DataType):
    pass


class LongType(DataType):
    pass
