from enum import Enum


class BuildCatalogAction(str, Enum):
    START = "start"
    STOP = "stop"
    PAUSE = "pause"
    RESUME = "resume"
    RESET = "reset"

    def __str__(self) -> str:
        return str(self.value)
