from enum import Enum


class PrivacyWarningType(str, Enum):
    COMBINELOCALRESULTS = "combineLocalResults"
    LENIENTAUTHORIZATIONCONTRACT = "lenientAuthorizationContract"
    NODATAPROTECTION = "noDataProtection"
    NOE2EE = "noE2EE"
    MINCONTRIBUTORSTOOSMALL = "minContributorsTooSmall"
    NOQUERYLIMIT = "noQueryLimit"
    NOQUERYLIMITDP = "noQueryLimitDP"
    PERINSTANCEBREAKDOWN = "perInstanceBreakdown"
    RECORDLINKAGE = "recordLinkage"
    UNLOCKEDCOMPUTATIONTYPE = "unlockedComputationType"
    UNLOCKEDCUSTOMPREPROCESSING = "unlockedCustomPreprocessing"

    def __str__(self) -> str:
        return str(self.value)
