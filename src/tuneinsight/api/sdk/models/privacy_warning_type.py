from enum import Enum


class PrivacyWarningType(str, Enum):
    CANSINGLEOUTPARTICIPANTCONTRIBUTION = "canSingleOutParticipantContribution"
    COMBINELOCALRESULTS = "combineLocalResults"
    LENIENTAUTHORIZATIONCONTRACT = "lenientAuthorizationContract"
    MINCONTRIBUTORSTOOSMALL = "minContributorsTooSmall"
    MINDATASETSIZETOOSMALL = "minDatasetSizeTooSmall"
    NODATAPROTECTION = "noDataProtection"
    NOE2EE = "noE2EE"
    NOQUERYLIMIT = "noQueryLimit"
    NOQUERYLIMITDP = "noQueryLimitDP"
    PERINSTANCEBREAKDOWN = "perInstanceBreakdown"
    RECORDLINKAGE = "recordLinkage"
    UNLOCKEDCOMPUTATIONTYPE = "unlockedComputationType"
    UNLOCKEDCUSTOMPREPROCESSING = "unlockedCustomPreprocessing"

    def __str__(self) -> str:
        return str(self.value)
