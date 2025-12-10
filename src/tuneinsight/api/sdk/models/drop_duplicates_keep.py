from enum import Enum


class DropDuplicatesKeep(str, Enum):
    FIRST = "first"
    LAST = "last"
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
