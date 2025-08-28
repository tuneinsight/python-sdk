from enum import Enum


class DatabaseType(str, Enum):
    POSTGRES = "postgres"
    MYSQL = "mysql"
    ORACLE = "oracle"

    def __str__(self) -> str:
        return str(self.value)
