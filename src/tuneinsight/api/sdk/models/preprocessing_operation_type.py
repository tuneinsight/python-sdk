from enum import Enum


class PreprocessingOperationType(str, Enum):
    ONEHOTENCODING = "oneHotEncoding"
    PHONETICENCODING = "phoneticEncoding"
    SELECT = "select"
    DROP = "drop"
    FILTER = "filter"
    SURVIVAL = "survival"
    TRANSPOSE = "transpose"
    SETINDEX = "setIndex"
    ASTYPE = "asType"
    RESETINDEX = "resetIndex"
    RENAME = "rename"
    EXTRACTDICTFIELD = "extractDictField"
    APPLYREGEX = "applyRegEx"
    QUANTILES = "quantiles"
    TIMEDIFF = "timeDiff"
    DROPNA = "dropna"
    APPLYMAPPING = "applyMapping"
    CUT = "cut"
    DEVIATIONSQUARES = "deviationSquares"
    ADDCOLUMNS = "addColumns"
    DATASETVALIDATION = "datasetValidation"
    SCALE = "scale"
    MULTIPLYCOLUMNS = "multiplyColumns"
    NEWCOLUMN = "newColumn"
    CUSTOM = "custom"

    def __str__(self) -> str:
        return str(self.value)
