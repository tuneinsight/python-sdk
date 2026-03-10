from enum import Enum


class DistributionType(str, Enum):
    NUMERIC = "numeric"
    CATEGORICAL = "categorical"

    def __str__(self) -> str:
        return str(self.value)
