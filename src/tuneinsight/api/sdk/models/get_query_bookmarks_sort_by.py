from enum import Enum


class GetQueryBookmarksSortBy(str, Enum):
    CREATEDAT = "createdAt"
    UPDATEDAT = "updatedAt"

    def __str__(self) -> str:
        return str(self.value)
