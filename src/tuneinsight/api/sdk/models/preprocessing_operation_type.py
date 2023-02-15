from enum import Enum


class PreprocessingOperationType(str, Enum):
    ONEHOTENCODING = "oneHotEncoding"
    PHONETICENCODING = "phoneticEncoding"
    SELECT = "select"
    DROP = "drop"
    FILTER = "filter"
    COUNTS = "counts"
    SURVIVAL = "survival"
    TRANSPOSE = "transpose"
    SETINDEX = "setIndex"
    ASTYPE = "asType"
    RESETINDEX = "resetIndex"
    RENAME = "rename"
    EXTRACTDICTFIELD = "extractDictField"
    APPLYREGEX = "applyRegEx"

    def __str__(self) -> str:
        return str(self.value)
