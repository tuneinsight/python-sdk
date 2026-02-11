from enum import Enum


class AgentType(str, Enum):
    QUERYBUILDER = "queryBuilder"
    PREPROCESSING = "preprocessing"

    def __str__(self) -> str:
        return str(self.value)
