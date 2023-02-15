from enum import Enum


class GetQueryListSortBy(str, Enum):
    CREATEDAT = "createdAt"

    def __str__(self) -> str:
        return str(self.value)
