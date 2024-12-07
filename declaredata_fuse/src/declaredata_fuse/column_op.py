from enum import Enum
from dataclasses import dataclass

from declaredata_fuse.proto import sds_pb2


class BinaryOp(Enum):
    ADD = 0
    SUB = 1
    MUL = 2
    DIV = 3

    def __str__(self) -> str:
        match self:
            case BinaryOp.ADD:
                return "+"
            case BinaryOp.SUB:
                return "-"
            case BinaryOp.MUL:
                return "*"
            case BinaryOp.DIV:
                return "/"


@dataclass
class DerivedColumn:
    """
    A placeholder for a new column that is derived by calculating its
    values from an existing column.

    This new column does not yet have a name
    """

    src_col: str
    op: BinaryOp
    const: int | str

    def alias(self, new_name: str) -> "NamedDerivedColumn":
        return NamedDerivedColumn(derivation=self, new_col_name=new_name)


@dataclass
class NamedDerivedColumn:
    """
    A new named column that is derived by calculating its values from at least
    one existing column.
    """

    derivation: DerivedColumn
    new_col_name: str

    def to_pb(self) -> sds_pb2.NamedDerivedColumn:
        match self.derivation.const:
            case int():
                return sds_pb2.NamedDerivedColumn(
                    src_col=self.derivation.src_col,
                    new_col=self.new_col_name,
                    operator=str(self.derivation.op),
                    i64_val=self.derivation.const,
                )
            case str():
                return sds_pb2.NamedDerivedColumn(
                    src_col=self.derivation.src_col,
                    new_col=self.new_col_name,
                    operator=str(self.derivation.op),
                    str_val=self.derivation.const,
                )
