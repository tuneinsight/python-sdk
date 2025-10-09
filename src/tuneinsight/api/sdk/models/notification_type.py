from enum import Enum


class NotificationType(str, Enum):
    PROJECTSHARE = "projectShare"
    AUTHREQUEST = "authRequest"
    COMPUTATIONEND = "computationEnd"
    DATASOURCENOK = "dataSourceNok"

    def __str__(self) -> str:
        return str(self.value)
