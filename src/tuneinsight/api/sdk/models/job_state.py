from enum import Enum


class JobState(str, Enum):
    AVAILABLE = "available"
    CANCELLED = "cancelled"
    COMPLETED = "completed"
    DISCARDED = "discarded"
    PENDING = "pending"
    RETRYABLE = "retryable"
    RUNNING = "running"
    SCHEDULED = "scheduled"

    def __str__(self) -> str:
        return str(self.value)
