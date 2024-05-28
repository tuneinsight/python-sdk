from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.credentials_type import CredentialsType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Credentials")


@attr.s(auto_attribs=True)
class Credentials:
    """The credentials needed to access the data source.

    Attributes:
        connection_string (Union[Unset, str]): connection string for a database
        credentials_id (Union[Unset, str]): the id of the credentials stored in the key vault
        password (Union[Unset, str]): generic password field.
        type (Union[Unset, CredentialsType]):
        username (Union[Unset, str]): generic username field.
        api_token (Union[Unset, str]): Token to connect to the API
    """

    connection_string: Union[Unset, str] = UNSET
    credentials_id: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    type: Union[Unset, CredentialsType] = UNSET
    username: Union[Unset, str] = UNSET
    api_token: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        connection_string = self.connection_string
        credentials_id = self.credentials_id
        password = self.password
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        username = self.username
        api_token = self.api_token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if connection_string is not UNSET:
            field_dict["connectionString"] = connection_string
        if credentials_id is not UNSET:
            field_dict["credentialsId"] = credentials_id
        if password is not UNSET:
            field_dict["password"] = password
        if type is not UNSET:
            field_dict["type"] = type
        if username is not UNSET:
            field_dict["username"] = username
        if api_token is not UNSET:
            field_dict["api-token"] = api_token

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        connection_string = d.pop("connectionString", UNSET)

        credentials_id = d.pop("credentialsId", UNSET)

        password = d.pop("password", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, CredentialsType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = CredentialsType(_type)

        username = d.pop("username", UNSET)

        api_token = d.pop("api-token", UNSET)

        credentials = cls(
            connection_string=connection_string,
            credentials_id=credentials_id,
            password=password,
            type=type,
            username=username,
            api_token=api_token,
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
