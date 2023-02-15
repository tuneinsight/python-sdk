from enum import Enum


class PostProjectDataSourceQueryJsonBodyAggregationType(str, Enum):
    PER_NODE = "per_node"
    AGGREGATED = "aggregated"
    OBFUSCATED = "obfuscated"

    def __str__(self) -> str:
        return str(self.value)
