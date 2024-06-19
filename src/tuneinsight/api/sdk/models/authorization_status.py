from enum import Enum


class AuthorizationStatus(str, Enum):
    UNAUTHORIZED = "unauthorized"
    AUTHORIZED = "authorized"
    DENIED = "denied"
    DISABLED = "disabled"

    def __str__(self) -> str:
        return str(self.value)
