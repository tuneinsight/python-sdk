from enum import Enum


class DataSourceCommandResultType(str, Enum):
    GENERICCOMMANDRESULT = "genericCommandResult"
    GETMETADATACOMMANDRESULT = "getMetadataCommandResult"
    GETCONCEPTMETADATACOMMANDRESULT = "getConceptMetadataCommandResult"
    GETCONCEPTFIELDVALUESCOMMANDRESULT = "getConceptFieldValuesCommandResult"

    def __str__(self) -> str:
        return str(self.value)
