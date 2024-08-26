from enum import Enum


class ParticipationStatus(str, Enum):
    PARTICIPATING = "participating"
    PENDING = "pending"
    UNAVAILABLE = "unavailable"
    LEFT = "left"
    REMOVED = "removed"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
