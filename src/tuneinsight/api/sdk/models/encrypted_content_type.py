from enum import Enum


class EncryptedContentType(str, Enum):
    FLOATMATRIX = "floatMatrix"
    STATISTICS = "statistics"
    DATAOBJECT = "dataObject"
    PREDICTION = "prediction"

    def __str__(self) -> str:
        return str(self.value)
