from enum import Enum


class ExecutionQuotaParametersScope(str, Enum):
    USER = "user"
    PROJECT = "project"

    def __str__(self) -> str:
        return str(self.value)
