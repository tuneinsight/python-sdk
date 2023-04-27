from enum import Enum


class GetCompBookmarkListSortBy(str, Enum):
    CREATEDAT = "createdAt"

    def __str__(self) -> str:
        return str(self.value)
