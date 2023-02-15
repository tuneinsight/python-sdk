from enum import Enum


class StorageOperation(str, Enum):
    ENCRYPT = "encrypt"
    DECRYPT = "decrypt"
    ROTATE = "rotate"
    BACKUP = "backup"
    RESTORE = "restore"

    def __str__(self) -> str:
        return str(self.value)
