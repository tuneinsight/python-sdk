from enum import Enum


class ContentType(str, Enum):
    FLOATMATRIX = "floatMatrix"
    STRINGMATRIX = "stringMatrix"
    ENCRYPTEDCONTENT = "encryptedContent"
    ENCRYPTEDMASKSHARES = "encryptedMaskShares"
    PREDICTION = "prediction"
    EXTERNALMLRESULT = "externalMlResult"
    STATISTICS = "statistics"

    def __str__(self) -> str:
        return str(self.value)
