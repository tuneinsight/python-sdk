from enum import Enum


class ExecutionQuotaParametersScope(str, Enum):
    PROJECT = "project"
    DATASOURCE = "datasource"

    def __str__(self) -> str:
        return str(self.value)
