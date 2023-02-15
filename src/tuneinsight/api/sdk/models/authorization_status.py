from enum import Enum


class AuthorizationStatus(str, Enum):
    UNAUTHORIZED = "unauthorized"
    AUTHORIZED = "authorized"
    DISABLED = "disabled"

    def __str__(self) -> str:
        return str(self.value)
