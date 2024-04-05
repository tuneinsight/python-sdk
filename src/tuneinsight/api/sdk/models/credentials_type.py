from enum import Enum


class CredentialsType(str, Enum):
    LOCAL = "local"
    AZUREKEYVAULT = "azureKeyVault"

    def __str__(self) -> str:
        return str(self.value)
