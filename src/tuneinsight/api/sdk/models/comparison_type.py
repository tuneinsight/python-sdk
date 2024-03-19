from enum import Enum


class ComparisonType(str, Enum):
    EQUAL = "equal"
    NEQUAL = "nEqual"
    GREATER = "greater"
    GREATEREQ = "greaterEq"
    LESS = "less"
    LESSEQ = "lessEq"
    IN = "in"
    ISIN = "isin"

    def __str__(self) -> str:
        return str(self.value)
