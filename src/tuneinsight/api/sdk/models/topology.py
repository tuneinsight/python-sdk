from enum import Enum


class Topology(str, Enum):
    STAR = "star"
    TREE = "tree"

    def __str__(self) -> str:
        return str(self.value)
