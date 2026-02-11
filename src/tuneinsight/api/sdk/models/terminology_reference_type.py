from enum import Enum


class TerminologyReferenceType(str, Enum):
    NAME = "name"
    CODE = "code"
    URI = "uri"
    OMOPCONCEPTID = "OMOPConceptId"

    def __str__(self) -> str:
        return str(self.value)
