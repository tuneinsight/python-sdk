from enum import Enum


class BooleanAggregator(str, Enum):
    ALL = "ALL"
    ANY = "ANY"
    COUNT = "COUNT"

    def __str__(self) -> str:
        return str(self.value)
