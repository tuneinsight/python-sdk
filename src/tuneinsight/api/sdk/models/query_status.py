from enum import Enum


class QueryStatus(str, Enum):
    REQUESTED = "requested"
    RUNNING = "running"
    SUCCESS = "success"
    ERROR = "error"

    def __str__(self) -> str:
        return str(self.value)
