from enum import Enum


class WorkflowType(str, Enum):
    CUSTOM = "custom"
    MAAS = "maas"
    FEASIBILITY = "feasibility"
    SURVEY = "survey"

    def __str__(self) -> str:
        return str(self.value)
