from declaredata_fuse.column.base import Column
from declaredata_fuse.column.derived import NamedDerivedColumn
from declaredata_fuse.proto import sds_pb2


SelectColumn = str | Column | NamedDerivedColumn

def select_column_to_pb(src: SelectColumn) -> sds_pb2.Column:
    match src:
        case str():
            return sds_pb2.Column(col_name=src)
        case Column():
            return src.to_pb()
        case NamedDerivedColumn():
            return sds_pb2.Column(col_derived=src.to_pb())
