from enum import Enum


class RenameAxis(str, Enum):
    INDEX = "index"
    COLUMNS = "columns"

    def __str__(self) -> str:
        return str(self.value)
