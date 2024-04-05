from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.data_source_type import DataSourceType
from ..models.database_type import DatabaseType
from ..models.local_data_source_type import LocalDataSourceType
from ..types import UNSET, Unset

T = TypeVar("T", bound="DataSourceTypesInfo")


@attr.s(auto_attribs=True)
class DataSourceTypesInfo:
    """information about the available datasources

    Attributes:
        data_source_types (Union[Unset, List[DataSourceType]]): list of available datasource types
        database_types (Union[Unset, List[DatabaseType]]): list of supported database types
        local_formats (Union[Unset, List[LocalDataSourceType]]): list of supported format for local datasources
    """

    data_source_types: Union[Unset, List[DataSourceType]] = UNSET
    database_types: Union[Unset, List[DatabaseType]] = UNSET
    local_formats: Union[Unset, List[LocalDataSourceType]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data_source_types: Union[Unset, List[str]] = UNSET
        if not isinstance(self.data_source_types, Unset):
            data_source_types = []
            for data_source_types_item_data in self.data_source_types:
                data_source_types_item = data_source_types_item_data.value

                data_source_types.append(data_source_types_item)

        database_types: Union[Unset, List[str]] = UNSET
        if not isinstance(self.database_types, Unset):
            database_types = []
            for database_types_item_data in self.database_types:
                database_types_item = database_types_item_data.value

                database_types.append(database_types_item)

        local_formats: Union[Unset, List[str]] = UNSET
        if not isinstance(self.local_formats, Unset):
            local_formats = []
            for local_formats_item_data in self.local_formats:
                local_formats_item = local_formats_item_data.value

                local_formats.append(local_formats_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data_source_types is not UNSET:
            field_dict["dataSourceTypes"] = data_source_types
        if database_types is not UNSET:
            field_dict["databaseTypes"] = database_types
        if local_formats is not UNSET:
            field_dict["localFormats"] = local_formats

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        data_source_types = []
        _data_source_types = d.pop("dataSourceTypes", UNSET)
        for data_source_types_item_data in _data_source_types or []:
            data_source_types_item = DataSourceType(data_source_types_item_data)

            data_source_types.append(data_source_types_item)

        database_types = []
        _database_types = d.pop("databaseTypes", UNSET)
        for database_types_item_data in _database_types or []:
            database_types_item = DatabaseType(database_types_item_data)

            database_types.append(database_types_item)

        local_formats = []
        _local_formats = d.pop("localFormats", UNSET)
        for local_formats_item_data in _local_formats or []:
            local_formats_item = LocalDataSourceType(local_formats_item_data)

            local_formats.append(local_formats_item)

        data_source_types_info = cls(
            data_source_types=data_source_types,
            database_types=database_types,
            local_formats=local_formats,
        )

        data_source_types_info.additional_properties = d
        return data_source_types_info

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
