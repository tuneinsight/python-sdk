from enum import Enum


class TiqlSelectionCriterion(str, Enum):
    FIRST = "first"

    def __str__(self) -> str:
        return str(self.value)
