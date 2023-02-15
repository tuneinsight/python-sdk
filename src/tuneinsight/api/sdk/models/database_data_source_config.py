from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.data_source_config_type import DataSourceConfigType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.database_connection_info import DatabaseConnectionInfo


T = TypeVar("T", bound="DatabaseDataSourceConfig")


@attr.s(auto_attribs=True)
class DatabaseDataSourceConfig:
    """
    Attributes:
        type (DataSourceConfigType):
        connection_info (Union[Unset, DatabaseConnectionInfo]): common connection information for various databases
    """

    type: DataSourceConfigType
    connection_info: Union[Unset, "DatabaseConnectionInfo"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        connection_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.connection_info, Unset):
            connection_info = self.connection_info.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if connection_info is not UNSET:
            field_dict["connectionInfo"] = connection_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.database_connection_info import DatabaseConnectionInfo

        d = src_dict.copy()
        type = DataSourceConfigType(d.pop("type"))

        _connection_info = d.pop("connectionInfo", UNSET)
        connection_info: Union[Unset, DatabaseConnectionInfo]
        if isinstance(_connection_info, Unset):
            connection_info = UNSET
        else:
            connection_info = DatabaseConnectionInfo.from_dict(_connection_info)

        database_data_source_config = cls(
            type=type,
            connection_info=connection_info,
        )

        database_data_source_config.additional_properties = d
        return database_data_source_config

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
