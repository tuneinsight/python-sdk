from enum import Enum


class ParticipationStatus(str, Enum):
    PARTICIPATING = "participating"
    PENDING = "pending"
    UNAVAILABLE = "unavailable"

    def __str__(self) -> str:
        return str(self.value)
