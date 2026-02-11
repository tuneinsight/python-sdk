from enum import Enum


class QueryBuilderType(str, Enum):
    LOCALTIQL = "localTIQL"
    TIQL = "TIQL"
    SQL = "SQL"
    OMOP = "OMOP"
    SPARQL = "SPARQL"
    API = "API"
    S3 = "S3"

    def __str__(self) -> str:
        return str(self.value)
