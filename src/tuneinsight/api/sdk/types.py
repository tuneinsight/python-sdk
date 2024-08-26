""" Contains some shared types for properties """

from http import HTTPStatus
from typing import Any, BinaryIO, Generic, Literal, MutableMapping, Optional, Tuple, TypeVar

from attrs import define


class Unset:
    def __bool__(self) -> Literal[False]:
        return False


UNSET: Unset = Unset()


def is_unset(v: Any) -> bool:
    """Returns whether a value in an API model is unset."""
    return isinstance(v, Unset)


def is_set(v: Any) -> bool:
    """Returns whether a value in an API model has been set (is not UNSET)."""
    return not is_unset(v)


def is_empty(v: Any) -> bool:
    """Returns whether an API model is either Unset or its to_dict is equal to {}."""
    return is_unset(v) or len(v.to_dict()) == 0


def value_if_unset(v: Any, default: Any) -> Any:
    """If v is Unset, returns the default value. Otherwise returns v unchanged."""
    if is_set(v):
        return v
    return default


def none_if_unset(v: Any) -> Any:
    """If v is Unset, returns None. Otherwise, returns v unchanged."""
    return value_if_unset(v, None)


def false_if_unset(v: Any) -> Any:
    """if v is Unset, returns False. Otherwise, returns v unchanged."""
    return value_if_unset(v, False)


FileJsonType = Tuple[Optional[str], BinaryIO, Optional[str]]


@define
class File:
    """Contains information for file uploads."""

    payload: BinaryIO
    file_name: Optional[str] = None
    mime_type: Optional[str] = None

    def to_tuple(self) -> FileJsonType:
        """Returns a tuple representation that httpx will accept for multipart/form-data."""
        return self.file_name, self.payload, self.mime_type


T = TypeVar("T")


@define
class Response(Generic[T]):
    """A response from an endpoint."""

    status_code: HTTPStatus
    content: bytes
    headers: MutableMapping[str, str]
    parsed: Optional[T]


__all__ = ["File", "Response", "FileJsonType", "Unset", "UNSET"]
