from enum import Enum


class SetIntersectionOutputFormat(str, Enum):
    DATASET = "dataset"
    COHORT = "cohort"

    def __str__(self) -> str:
        return str(self.value)
