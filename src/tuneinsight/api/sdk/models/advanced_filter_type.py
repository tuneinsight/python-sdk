from enum import Enum


class AdvancedFilterType(str, Enum):
    LOGICALOPERATORFILTER = "logicalOperatorFilter"
    ATOMICFILTER = "atomicFilter"
    SERIESFILTER = "seriesFilter"

    def __str__(self) -> str:
        return str(self.value)
