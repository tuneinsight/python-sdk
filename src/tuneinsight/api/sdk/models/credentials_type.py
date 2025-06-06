from enum import Enum


class CredentialsType(str, Enum):
    LOCAL = "local"
    AZUREKEYVAULT = "azureKeyVault"
    OPENBAO = "openbao"

    def __str__(self) -> str:
        return str(self.value)
