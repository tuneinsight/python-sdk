from enum import Enum


class GetJobsOrder(str, Enum):
    DESC = "desc"
    ASC = "asc"

    def __str__(self) -> str:
        return str(self.value)
