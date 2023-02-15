from enum import Enum


class PostDataObjectJsonBodyMethod(str, Enum):
    DATASOURCE = "datasource"
    CREATE = "create"
    ENCRYPT = "encrypt"
    DECRYPT = "decrypt"

    def __str__(self) -> str:
        return str(self.value)
