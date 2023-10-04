from enum import Enum


class ComputationErrorType(str, Enum):
    QUERY = "query"
    PREPROCESSING = "preprocessing"
    DISCLOSUREPREVENTION = "disclosurePrevention"
    VALIDATION = "validation"
    INTERNAL = "internal"

    def __str__(self) -> str:
        return str(self.value)
