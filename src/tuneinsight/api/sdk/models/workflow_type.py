from enum import Enum


class WorkflowType(str, Enum):
    CUSTOM = "custom"
    MAAS = "maas"
    IBAN_SEARCH = "iban_search"
    FEASIBILITY = "feasibility"
    CREATOR_ONLY = "creator_only"

    def __str__(self) -> str:
        return str(self.value)
