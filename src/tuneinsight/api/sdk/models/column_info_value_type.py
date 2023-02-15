from enum import Enum


class ColumnInfoValueType(str, Enum):
    ROWCOUNT = "rowCount"
    VALUESUM = "valueSum"

    def __str__(self) -> str:
        return str(self.value)
