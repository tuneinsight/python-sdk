from enum import Enum


class NoiseDistributions(str, Enum):
    LAPLACE = "laplace"
    GAUSSIAN = "gaussian"
    LAPLACESUM = "laplaceSum"

    def __str__(self) -> str:
        return str(self.value)
