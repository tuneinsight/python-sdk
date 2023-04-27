from enum import Enum


class ThresholdType(str, Enum):
    FIXED = "fixed"
    RELATIVE = "relative"

    def __str__(self) -> str:
        return str(self.value)
