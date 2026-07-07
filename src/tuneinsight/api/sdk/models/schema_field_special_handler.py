from enum import Enum


class SchemaFieldSpecialHandler(str, Enum):
    CONTEXTUALAGE = "contextualAge"
    VITALSTATUS = "vitalStatus"

    def __str__(self) -> str:
        return str(self.value)
