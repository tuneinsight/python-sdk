from enum import Enum


class APIType(str, Enum):
    ELASTIC = "elastic"
    MISP = "misp"
    HUBSPOT = "hubspot"
    VIRTUOSO = "virtuoso"
    EINSTEIN = "einstein"
    GENERIC = "generic"

    def __str__(self) -> str:
        return str(self.value)
