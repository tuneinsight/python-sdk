from enum import Enum


class GetNetworkMetadataResponse200NetworkType(str, Enum):
    DEFAULT = "default"
    SSE = "sse"

    def __str__(self) -> str:
        return str(self.value)
