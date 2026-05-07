from enum import Enum


class GetOntologySearchSortBy(str, Enum):
    RELEVANCE = "relevance"
    LEVEL = "level"
    OCCURRENCE = "occurrence"

    def __str__(self) -> str:
        return str(self.value)
