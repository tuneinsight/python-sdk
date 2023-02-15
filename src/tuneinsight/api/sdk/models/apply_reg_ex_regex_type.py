from enum import Enum


class ApplyRegExRegexType(str, Enum):
    MATCH = "match"
    POSITION = "position"
    FINDALL = "findall"

    def __str__(self) -> str:
        return str(self.value)
