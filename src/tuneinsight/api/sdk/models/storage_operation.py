from enum import Enum


class StorageOperation(str, Enum):
    ENCRYPT = "encrypt"
    ROTATE = "rotate"
    DELETEDANGLING = "deleteDangling"

    def __str__(self) -> str:
        return str(self.value)
