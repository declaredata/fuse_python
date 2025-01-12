from declaredata_fuse.sql.types.data_type_base import DataType


class DecimalType(DataType):
    def typeName(self) -> str:
        return "decimal"

class DoubleType(DataType):
    def typeName(self) -> str:
        return "double"

class IntegerType(DataType):
    def typeName(self) -> str:
        return "integer"

class LongType(DataType):
    def typeName(self) -> str:
        return "long"
