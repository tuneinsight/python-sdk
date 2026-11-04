from enum import Enum


class GetInfosResponse200AndorStatus(str, Enum):
    OK = "ok"
    NOK = "nok"

    def __str__(self) -> str:
        return str(self.value)
