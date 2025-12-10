from enum import Enum


class TerminologyReferenceType(str, Enum):
    NAME = "name"
    CODE = "code"
    URI = "uri"

    def __str__(self) -> str:
        return str(self.value)
