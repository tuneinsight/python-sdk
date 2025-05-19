from enum import Enum


class UserPreferenceKey(str, Enum):
    USEPOLICYSTATUS = "usePolicyStatus"

    def __str__(self) -> str:
        return str(self.value)
