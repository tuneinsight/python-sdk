from enum import Enum


class PostprocessingOperation(str, Enum):
    DP_STATISTICS = "dp-statistics"
    AVERAGE = "average"

    def __str__(self) -> str:
        return str(self.value)
