from enum import Enum


class OntologyType(str, Enum):
    ICD10 = "ICD10"
    ATC = "ATC"
    LOINC = "LOINC"
    CHOP = "CHOP"
    SNOMED = "SNOMED"

    def __str__(self) -> str:
        return str(self.value)
