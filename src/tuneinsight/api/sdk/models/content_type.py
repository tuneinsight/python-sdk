from enum import Enum


class ContentType(str, Enum):
    FLOATMATRIX = "floatMatrix"
    STRINGMATRIX = "stringMatrix"
    CIPHERTABLE = "ciphertable"
    PREDICTION = "prediction"
    STATISTICS = "statistics"

    def __str__(self) -> str:
        return str(self.value)
