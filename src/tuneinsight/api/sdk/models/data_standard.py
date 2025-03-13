from enum import Enum


class DataStandard(str, Enum):
    OMOP = "OMOP"
    FHIR = "FHIR"
    SPHN = "SPHN"

    def __str__(self) -> str:
        return str(self.value)
