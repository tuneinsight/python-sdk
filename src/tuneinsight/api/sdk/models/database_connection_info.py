from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.database_type import DatabaseType
from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseConnectionInfo")


@attr.s(auto_attribs=True)
class DatabaseConnectionInfo:
    """common connection information for various databases

    Attributes:
        database (str): Name of the database
        host (str): Hostname of the database
        port (str): Port number of the database
        password (Union[Unset, str]): Password to connect to db
        type (Union[Unset, DatabaseType]): Type of the database
        user (Union[Unset, str]): User name
    """

    database: str
    host: str
    port: str
    password: Union[Unset, str] = UNSET
    type: Union[Unset, DatabaseType] = UNSET
    user: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        database = self.database
        host = self.host
        port = self.port
        password = self.password
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        user = self.user

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "database": database,
                "host": host,
                "port": port,
            }
        )
        if password is not UNSET:
            field_dict["password"] = password
        if type is not UNSET:
            field_dict["type"] = type
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        database = d.pop("database")

        host = d.pop("host")

        port = d.pop("port")

        password = d.pop("password", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, DatabaseType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = DatabaseType(_type)

        user = d.pop("user", UNSET)

        database_connection_info = cls(
            database=database,
            host=host,
            port=port,
            password=password,
            type=type,
            user=user,
        )

        database_connection_info.additional_properties = d
        return database_connection_info

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
