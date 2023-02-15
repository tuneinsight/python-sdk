from enum import Enum


class GetComputationListSortBy(str, Enum):
    CREATEDAT = "createdAt"
    UPDATEDAT = "updatedAt"

    def __str__(self) -> str:
        return str(self.value)
