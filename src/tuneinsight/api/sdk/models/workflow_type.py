from enum import Enum


class WorkflowType(str, Enum):
    CUSTOM = "custom"
    MAAS = "maas"
    IBAN_SEARCH = "iban_search"
    FEASIBILITY = "feasibility"
    SURVEY = "survey"

    def __str__(self) -> str:
        return str(self.value)
