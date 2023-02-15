from enum import Enum


class DatabaseType(str, Enum):
    POSTGRES = "postgres"
    MYSQL = "mysql"

    def __str__(self) -> str:
        return str(self.value)
