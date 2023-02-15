from enum import Enum


class TrainingAlgorithm(str, Enum):
    LINEAR_REGRESSION = "linear-regression"
    LOGISTIC_REGRESSION = "logistic-regression"
    POISSON_REGRESSION = "poisson-regression"

    def __str__(self) -> str:
        return str(self.value)
