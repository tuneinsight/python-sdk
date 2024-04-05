from enum import Enum


class DataSourceType(str, Enum):
    LOCAL = "local"
    DATABASE = "database"
    API = "api"

    def __str__(self) -> str:
        return str(self.value)
