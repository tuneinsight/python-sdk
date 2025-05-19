from enum import Enum


class GetUserPreferenceKey(str, Enum):
    USEPOLICYSTATUS = "usePolicyStatus"

    def __str__(self) -> str:
        return str(self.value)
