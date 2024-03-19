from enum import Enum


class RunMode(str, Enum):
    LOCAL = "local"
    COLLECTIVE = "collective"
    COMBINED = "combined"

    def __str__(self) -> str:
        return str(self.value)
