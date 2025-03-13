from enum import Enum


class DataSourceType(str, Enum):
    LOCAL = "local"
    DATABASE = "database"
    API = "api"
    S3 = "s3"

    def __str__(self) -> str:
        return str(self.value)
