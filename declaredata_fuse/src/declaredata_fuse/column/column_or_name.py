from declaredata_fuse.column.basic import BasicColumn
from declaredata_fuse.column.base import Column

ColumnOrName = Column | str


def col_or_name_to_basic(cn: ColumnOrName) -> BasicColumn:
    return BasicColumn(
        _name=cn if isinstance(cn, str) else cn.cur_name(),
    )
