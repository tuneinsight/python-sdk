from enum import Enum


class LocalDataSourceType(str, Enum):
    CSV = "CSV"
    JSON = "JSON"

    def __str__(self) -> str:
        return str(self.value)
