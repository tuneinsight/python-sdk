from enum import Enum


class APIConnectionInfoType(str, Enum):
    ELASTIC = "elastic"
    MISP = "misp"
    GENERIC = "generic"

    def __str__(self) -> str:
        return str(self.value)
