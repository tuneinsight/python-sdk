from enum import Enum


class OntologyType(str, Enum):
    ICD10 = "ICD10"
    ATC = "ATC"
    LOINC = "LOINC"
    CHOP = "CHOP"
    SNOMED = "SNOMED"
    CCAM = "CCAM"
    RXNORM = "RxNorm"
    UCUM = "UCUM"
    CMS_PLACE_OF_SERVICE = "CMS Place of Service"
    OMOPGENERATED = "OMOPGenerated"

    def __str__(self) -> str:
        return str(self.value)
