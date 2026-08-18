from enum import Enum


class DataStandard(str, Enum):
    FHIR = "FHIR"
    SPHN = "SPHN"

    def __str__(self) -> str:
        return str(self.value)
