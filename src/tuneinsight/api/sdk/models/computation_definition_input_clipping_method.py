from enum import Enum


class ComputationDefinitionInputClippingMethod(str, Enum):
    NONE = "none"
    SILENT = "silent"
    WARNING = "warning"
    ERROR = "error"

    def __str__(self) -> str:
        return str(self.value)
