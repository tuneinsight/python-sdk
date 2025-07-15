from enum import Enum


class NotificationType(str, Enum):
    PROJECTSHARE = "projectShare"
    AUTHREQUEST = "authRequest"
    COMPUTATIONEND = "computationEnd"

    def __str__(self) -> str:
        return str(self.value)
