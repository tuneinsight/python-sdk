from enum import Enum


class DataSourceConsentType(str, Enum):
    NONE = "none"
    BROAD = "broad"
    SPECIFIC = "specific"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
