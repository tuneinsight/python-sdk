from enum import Enum


class ComputationStatus(str, Enum):
    REQUESTED = "requested"
    RUNNING = "running"
    SUCCESS = "success"
    ERROR = "error"
    UNMONITORED = "unmonitored"

    def __str__(self) -> str:
        return str(self.value)
