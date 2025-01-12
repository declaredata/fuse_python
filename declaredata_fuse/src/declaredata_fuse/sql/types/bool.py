from declaredata_fuse.sql.types.data_type_base import DataType


class BooleanType(DataType):
    def typeName(self) -> str:
        return "boolean"
