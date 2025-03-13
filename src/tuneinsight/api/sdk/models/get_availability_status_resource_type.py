from enum import Enum


class GetAvailabilityStatusResourceType(str, Enum):
    DATASOURCE = "dataSource"
    PROJECT = "project"

    def __str__(self) -> str:
        return str(self.value)
