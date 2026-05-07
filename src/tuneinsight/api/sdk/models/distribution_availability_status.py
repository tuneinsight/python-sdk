from enum import Enum


class DistributionAvailabilityStatus(str, Enum):
    AVAILABLE = "available"
    SUPPRESSED = "suppressed"
    UNAVAILABLE = "unavailable"

    def __str__(self) -> str:
        return str(self.value)
