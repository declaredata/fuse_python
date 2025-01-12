from enum import Enum

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
