from enum import Enum


class FillNAMethod(str, Enum):
    VALUE = "value"
    LOCAL_MEAN = "local-mean"
    LOCAL_MEDIAN = "local-median"
    LOCAL_MODE = "local-mode"
    FFILL = "ffill"
    BFILL = "bfill"
    INTERPOLATE = "interpolate"

    def __str__(self) -> str:
        return str(self.value)
