from enum import Enum


class ComparisonType(str, Enum):
    EQUAL = "equal"
    NEQUAL = "nEqual"
    GREATER = "greater"
    GREATEREQ = "greaterEq"
    LESS = "less"
    LESSEQ = "lessEq"
    IN = "in"
    NOTIN = "notIn"
    ISIN = "isin"
    CONTAINS = "contains"
    NOTCONTAINS = "notContains"
    BEGINSWITH = "beginsWith"
    NOTBEGINSWITH = "notBeginsWith"
    ENDSWITH = "endsWith"
    NOTENDSWITH = "notEndsWith"
    ISNULL = "isNull"
    ISNOTNULL = "isNotNull"
    BETWEEN = "between"
    NOTBETWEEN = "notBetween"

    def __str__(self) -> str:
        return str(self.value)
