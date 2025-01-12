from declaredata_fuse.sql.types.data_type_base import DataType


class StringType(DataType):
    def typeName(self) -> str:
        return "string"
