from enum import Enum


class Client(str, Enum):
    SECOIA = "secoia"
    DIAPASON_PY = "diapason-py"
    CLI = "cli"
    CONFIGURATION = "configuration"

    def __str__(self) -> str:
        return str(self.value)
