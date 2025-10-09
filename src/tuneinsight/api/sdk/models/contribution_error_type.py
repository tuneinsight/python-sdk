from enum import Enum


class ContributionErrorType(str, Enum):
    INSUFFICIENTRECORDS = "insufficientRecords"
    QUERYTIMEOUT = "queryTimeout"
    QUERYERROR = "queryError"
    UNRESPONSIVEINSTANCE = "unresponsiveInstance"

    def __str__(self) -> str:
        return str(self.value)
