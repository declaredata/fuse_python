from declaredata_fuse.column.base import Column
from declaredata_fuse.proto.sds_pb2 import INNER, JoinType, LEFT, RIGHT, FULL


def str_to_join_type(raw: str) -> JoinType.ValueType:
    if raw == "inner":
        return INNER
    elif raw == "left":
        return LEFT
    elif raw == "right":
        return RIGHT
    elif raw == "full":
        return FULL
    raise ValueError(f"unsupported join type: {raw}")


def reify_join_cols(on: list[str] | str | Column | None) -> list[str]:
    if isinstance(on, list):
        return on
    elif isinstance(on, str):
        return [on]
    elif isinstance(on, Column):
        return [on.cur_name()]
    else:
        return []
