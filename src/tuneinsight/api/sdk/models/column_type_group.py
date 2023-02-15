from enum import Enum


class ColumnTypeGroup(str, Enum):
    NUMERICAL = "numerical"
    TEXT = "text"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
