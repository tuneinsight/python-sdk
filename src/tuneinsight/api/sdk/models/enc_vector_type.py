from enum import Enum


class EncVectorType(str, Enum):
    INT = "int"
    FLOAT = "float"

    def __str__(self) -> str:
        return str(self.value)
