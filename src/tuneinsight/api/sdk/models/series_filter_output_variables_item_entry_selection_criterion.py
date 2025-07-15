from enum import Enum


class SeriesFilterOutputVariablesItemEntrySelectionCriterion(str, Enum):
    FIRST = "first"

    def __str__(self) -> str:
        return str(self.value)
