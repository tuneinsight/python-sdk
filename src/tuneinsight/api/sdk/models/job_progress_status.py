from enum import Enum


class JobProgressStatus(str, Enum):
    STOP = "stop"
    PROGRESS = "progress"
    PAUSE = "pause"
    CANCELLED = "cancelled"
    DONE = "done"

    def __str__(self) -> str:
        return str(self.value)
