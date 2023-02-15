from enum import Enum


class DataSourceConfigType(str, Enum):
    LOCALDATASOURCECONFIG = "localDataSourceConfig"
    DATABASEDATASOURCECONFIG = "databaseDataSourceConfig"
    APIDATASOURCECONFIG = "apiDataSourceConfig"

    def __str__(self) -> str:
        return str(self.value)
