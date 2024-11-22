from enum import Enum


class PostMockDatasetAccessScope(str, Enum):
    PRIVATE = "private"
    RESTRICTED = "restricted"
    ORGANIZATION = "organization"
    NETWORK = "network"

    def __str__(self) -> str:
        return str(self.value)
