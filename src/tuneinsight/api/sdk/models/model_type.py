from enum import Enum


class ModelType(str, Enum):
    LOCAL = "local"
    COLLECTIVE = "collective"

    def __str__(self) -> str:
        return str(self.value)
