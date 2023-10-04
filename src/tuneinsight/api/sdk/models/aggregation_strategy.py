from enum import Enum


class AggregationStrategy(str, Enum):
    CONSTANT = "constant"
    LINEAR = "linear"
    LOG = "log"

    def __str__(self) -> str:
        return str(self.value)
