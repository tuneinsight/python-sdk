from enum import Enum


class RegressionType(str, Enum):
    LINEAR = "linear"
    LOGISTIC = "logistic"
    POISSON = "poisson"

    def __str__(self) -> str:
        return str(self.value)
