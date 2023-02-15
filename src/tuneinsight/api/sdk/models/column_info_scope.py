from enum import Enum


class ColumnInfoScope(str, Enum):
    ALL = "all"
    SUBGROUP = "subgroup"

    def __str__(self) -> str:
        return str(self.value)
