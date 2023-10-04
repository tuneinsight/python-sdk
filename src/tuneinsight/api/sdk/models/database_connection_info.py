from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.database_type import DatabaseType
from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseConnectionInfo")


@attr.s(auto_attribs=True)
class DatabaseConnectionInfo:
    """common connection information for various databases

    Attributes:
        port (str): Port number of the database
        database (str): Name of the database
        host (str): Hostname of the database
        type (Union[Unset, DatabaseType]): Type of the database
        user (Union[Unset, str]): User name
        password (Union[Unset, str]): Password to connect to db
    """

    port: str
    database: str
    host: str
    type: Union[Unset, DatabaseType] = UNSET
    user: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        port = self.port
        database = self.database
        host = self.host
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        user = self.user
        password = self.password

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "port": port,
                "database": database,
                "host": host,
            }
        )
        if type is not UNSET:
            field_dict["type"] = type
        if user is not UNSET:
            field_dict["user"] = user
        if password is not UNSET:
            field_dict["password"] = password

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        port = d.pop("port")

        database = d.pop("database")

        host = d.pop("host")

        _type = d.pop("type", UNSET)
        type: Union[Unset, DatabaseType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = DatabaseType(_type)

        user = d.pop("user", UNSET)

        password = d.pop("password", UNSET)

        database_connection_info = cls(
            port=port,
            database=database,
            host=host,
            type=type,
            user=user,
            password=password,
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
