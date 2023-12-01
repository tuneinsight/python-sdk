from enum import Enum


class NetworkVisibilityType(str, Enum):
    GLOBAL = "global"
    RESTRICTED = "restricted"

    def __str__(self) -> str:
        return str(self.value)
