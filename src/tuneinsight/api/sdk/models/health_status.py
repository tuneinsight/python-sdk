from enum import Enum


class HealthStatus(str, Enum):
    OK = "ok"
    NOK = "nok"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
