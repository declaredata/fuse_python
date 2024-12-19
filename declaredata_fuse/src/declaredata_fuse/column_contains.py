from declaredata_fuse.column_abc import Column
from declaredata_fuse.proto import sds_pb2


class ContainsColumn(Column):
    def __init__(self, left: Column, right: Column) -> None:
        self._name = f"contains({left.cur_name()}, {right.cur_name()})"

    def alias(self, new_name: str) -> Column:
        self._name = new_name
        return self

    def cur_name(self) -> str:
        return self._name

    def to_pb(self) -> sds_pb2.Column:
        raise NotImplementedError("not yet implemented")
