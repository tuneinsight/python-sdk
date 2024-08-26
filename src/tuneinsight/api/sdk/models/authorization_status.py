from enum import Enum


class AuthorizationStatus(str, Enum):
    DRAFT = "draft"
    PENDING = "pending"
    AUTHORIZED = "authorized"
    DENIED = "denied"

    def __str__(self) -> str:
        return str(self.value)
