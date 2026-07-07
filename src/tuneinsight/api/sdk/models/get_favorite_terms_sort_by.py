from enum import Enum


class GetFavoriteTermsSortBy(str, Enum):
    CREATEDAT = "createdAt"
    UPDATEDAT = "updatedAt"

    def __str__(self) -> str:
        return str(self.value)
