from enum import Enum


class SphnOntologiesSearchOntologiesItem(str, Enum):
    ICD10 = "ICD10"
    ATC = "ATC"
    LOINC = "LOINC"
    CHOP = "CHOP"

    def __str__(self) -> str:
        return str(self.value)
