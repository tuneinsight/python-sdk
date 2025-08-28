from enum import Enum


class UsageType(str, Enum):
    HEALTH = "health"
    GENERIC = "generic"

    def __str__(self) -> str:
        return str(self.value)
