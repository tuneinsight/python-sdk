from enum import Enum


class StatisticalQuantity(str, Enum):
    QUANTILES = "quantiles"
    MEAN = "mean"
    VARIANCE = "variance"

    def __str__(self) -> str:
        return str(self.value)
