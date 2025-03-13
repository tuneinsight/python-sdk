from enum import Enum


class GetScreeningSessionsOrder(str, Enum):
    DESC = "desc"
    ASC = "asc"

    def __str__(self) -> str:
        return str(self.value)
