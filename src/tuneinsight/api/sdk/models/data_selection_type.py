from enum import Enum


class DataSelectionType(str, Enum):
    BOOKMARK = "bookmark"
    TEMPLATE = "template"
    PREVIEW = "preview"

    def __str__(self) -> str:
        return str(self.value)
