from enum import Enum


class GetAIBuilderPromptsDataSourceType(str, Enum):
    LOCAL = "local"
    DATABASE = "database"
    API = "api"
    S3 = "s3"
    DATAVIEW = "dataView"

    def __str__(self) -> str:
        return str(self.value)
