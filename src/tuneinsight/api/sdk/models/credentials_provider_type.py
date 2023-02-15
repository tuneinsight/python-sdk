from enum import Enum


class CredentialsProviderType(str, Enum):
    LOCALCREDENTIALSPROVIDER = "localCredentialsProvider"
    AZUREKEYVAULTCREDENTIALSPROVIDER = "azureKeyVaultCredentialsProvider"

    def __str__(self) -> str:
        return str(self.value)
