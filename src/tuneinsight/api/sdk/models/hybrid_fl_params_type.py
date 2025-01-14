from enum import Enum


class HybridFLParamsType(str, Enum):
    HYBRIDFLSPECBASEPARAMS = "hybridFLSpecBaseParams"
    HYBRIDFLMACHINELEARNINGPARAMS = "hybridFLMachineLearningParams"
    HYBRIDFLCOMMUNITYDETECTIONPARAMS = "hybridFLCommunityDetectionParams"

    def __str__(self) -> str:
        return str(self.value)
