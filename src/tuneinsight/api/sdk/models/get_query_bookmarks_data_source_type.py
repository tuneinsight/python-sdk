from enum import Enum


class GetQueryBookmarksDataSourceType(str, Enum):
    LOCAL = "local"
    DATABASE = "database"
    API = "api"

    def __str__(self) -> str:
        return str(self.value)
