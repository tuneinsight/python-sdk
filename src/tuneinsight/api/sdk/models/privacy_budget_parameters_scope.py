from enum import Enum


class PrivacyBudgetParametersScope(str, Enum):
    USER = "user"
    PROJECT = "project"

    def __str__(self) -> str:
        return str(self.value)
