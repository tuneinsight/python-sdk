from enum import Enum


class DataSourceCommandType(str, Enum):
    GENERICCOMMAND = "genericCommand"
    GETMETADATACOMMAND = "getMetadataCommand"
    GETCONCEPTFIELDVALUESCOMMAND = "getConceptFieldValuesCommand"
    GETTRANSLATEDQUERYCOMMAND = "getTranslatedQueryCommand"

    def __str__(self) -> str:
        return str(self.value)
