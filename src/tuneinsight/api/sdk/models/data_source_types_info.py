from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.database_type import DatabaseType
from ..types import UNSET, Unset

T = TypeVar("T", bound="DataSourceTypesInfo")


@attr.s(auto_attribs=True)
class DataSourceTypesInfo:
    """information about the available datasources

    Attributes:
        database_types (Union[Unset, List[DatabaseType]]): list of supported database types
        local_formats (Union[Unset, List[str]]): list of supported format for local datasources
        data_source_types (Union[Unset, List[str]]): list of available datasource types
    """

    database_types: Union[Unset, List[DatabaseType]] = UNSET
    local_formats: Union[Unset, List[str]] = UNSET
    data_source_types: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        database_types: Union[Unset, List[str]] = UNSET
        if not isinstance(self.database_types, Unset):
            database_types = []
            for database_types_item_data in self.database_types:
                database_types_item = database_types_item_data.value

                database_types.append(database_types_item)

        local_formats: Union[Unset, List[str]] = UNSET
        if not isinstance(self.local_formats, Unset):
            local_formats = self.local_formats

        data_source_types: Union[Unset, List[str]] = UNSET
        if not isinstance(self.data_source_types, Unset):
            data_source_types = self.data_source_types

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if database_types is not UNSET:
            field_dict["databaseTypes"] = database_types
        if local_formats is not UNSET:
            field_dict["localFormats"] = local_formats
        if data_source_types is not UNSET:
            field_dict["dataSourceTypes"] = data_source_types

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        database_types = []
        _database_types = d.pop("databaseTypes", UNSET)
        for database_types_item_data in _database_types or []:
            database_types_item = DatabaseType(database_types_item_data)

            database_types.append(database_types_item)

        local_formats = cast(List[str], d.pop("localFormats", UNSET))

        data_source_types = cast(List[str], d.pop("dataSourceTypes", UNSET))

        data_source_types_info = cls(
            database_types=database_types,
            local_formats=local_formats,
            data_source_types=data_source_types,
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
