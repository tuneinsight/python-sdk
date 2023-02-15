from enum import Enum


class BackupType(str, Enum):
    LOCAL = "local"
    REMOTE = "remote"

    def __str__(self) -> str:
        return str(self.value)
