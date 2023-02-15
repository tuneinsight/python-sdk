from enum import Enum


class GroupByType(str, Enum):
    CATEGORY = "category"
    RANGE = "range"

    def __str__(self) -> str:
        return str(self.value)
