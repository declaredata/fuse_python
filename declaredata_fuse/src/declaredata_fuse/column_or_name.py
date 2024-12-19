from declaredata_fuse.column import BasicColumn
from declaredata_fuse.column_abc import Column

ColumnOrName = Column | str


def col_or_name_to_basic(cn: ColumnOrName) -> BasicColumn:
    return BasicColumn(
        _name=cn if isinstance(cn, str) else cn.cur_name(),
    )
