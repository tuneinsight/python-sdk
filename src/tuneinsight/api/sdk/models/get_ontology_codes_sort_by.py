from enum import Enum


class GetOntologyCodesSortBy(str, Enum):
    RELEVANCE = "relevance"
    LEVEL = "level"
    OCCURRENCE = "occurrence"

    def __str__(self) -> str:
        return str(self.value)
