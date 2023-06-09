from enum import Enum


class ProjectBaseWorkflowType(str, Enum):
    CUSTOM = "custom"
    MAAS = "maas"
    IBAN_SEARCH = "iban_search"

    def __str__(self) -> str:
        return str(self.value)
