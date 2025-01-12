from declaredata_fuse.sql.types.data_type_base import DataType


class MapType(DataType):
    def typeName(self) -> str:
        return "map"
