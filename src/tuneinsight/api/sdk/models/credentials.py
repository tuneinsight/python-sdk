from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Credentials")


@attr.s(auto_attribs=True)
class Credentials:
    """The credentials needed to access the data source.

    Attributes:
        username (Union[Unset, str]):
        connection_string (Union[Unset, str]):
        id (Union[Unset, str]):
        password (Union[Unset, str]):
    """

    username: Union[Unset, str] = UNSET
    connection_string: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        username = self.username
        connection_string = self.connection_string
        id = self.id
        password = self.password

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if username is not UNSET:
            field_dict["username"] = username
        if connection_string is not UNSET:
            field_dict["connectionString"] = connection_string
        if id is not UNSET:
            field_dict["id"] = id
        if password is not UNSET:
            field_dict["password"] = password

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        username = d.pop("username", UNSET)

        connection_string = d.pop("connectionString", UNSET)

        id = d.pop("id", UNSET)

        password = d.pop("password", UNSET)

        credentials = cls(
            username=username,
            connection_string=connection_string,
            id=id,
            password=password,
        )

        credentials.additional_properties = d
        return credentials

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
