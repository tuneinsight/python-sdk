from enum import Enum


class ExportScreenedDataMethod(str, Enum):
    VIEW = "view"
    SNAPSHOT = "snapshot"

    def __str__(self) -> str:
        return str(self.value)
