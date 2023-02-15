from enum import Enum


class ProjectStatus(str, Enum):
    DRAFT = "draft"
    PENDING = "pending"
    READY = "ready"
    ARCHIVED = "archived"

    def __str__(self) -> str:
        return str(self.value)
