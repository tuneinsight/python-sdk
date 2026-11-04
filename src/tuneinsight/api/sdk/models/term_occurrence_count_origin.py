from enum import Enum


class TermOccurrenceCountOrigin(str, Enum):
    DIRECT = "direct"
    MAPPED = "mapped"
    COMBINED = "combined"

    def __str__(self) -> str:
        return str(self.value)
