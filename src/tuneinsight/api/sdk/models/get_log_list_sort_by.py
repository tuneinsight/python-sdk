from enum import Enum


class GetLogListSortBy(str, Enum):
    CREATEDAT = "createdAt"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
