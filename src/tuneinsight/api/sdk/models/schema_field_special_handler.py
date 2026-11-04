from enum import Enum


class SchemaFieldSpecialHandler(str, Enum):
    CONTEXTUALAGE = "contextualAge"
    VITALSTATUS = "vitalStatus"
    OCCURRENCEFILTER = "occurrenceFilter"

    def __str__(self) -> str:
        return str(self.value)
