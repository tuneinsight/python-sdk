from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_source_table import DataSourceTable


T = TypeVar("T", bound="DataSourceMetadata")


@attr.s(auto_attribs=True)
class DataSourceMetadata:
    """metadata about a datasource

    Attributes:
        metadata_available (Union[Unset, bool]): whether or not the datasource supports returning metadata
        stores_templates (Union[Unset, bool]): whether the data source stores template tables.
        tables (Union[Unset, List['DataSourceTable']]):
    """

    metadata_available: Union[Unset, bool] = UNSET
    stores_templates: Union[Unset, bool] = UNSET
    tables: Union[Unset, List["DataSourceTable"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        metadata_available = self.metadata_available
        stores_templates = self.stores_templates
        tables: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tables, Unset):
            tables = []
            for tables_item_data in self.tables:
                tables_item = tables_item_data.to_dict()

                tables.append(tables_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if metadata_available is not UNSET:
            field_dict["metadataAvailable"] = metadata_available
        if stores_templates is not UNSET:
            field_dict["storesTemplates"] = stores_templates
        if tables is not UNSET:
            field_dict["tables"] = tables

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.data_source_table import DataSourceTable

        d = src_dict.copy()
        metadata_available = d.pop("metadataAvailable", UNSET)

        stores_templates = d.pop("storesTemplates", UNSET)

        tables = []
        _tables = d.pop("tables", UNSET)
        for tables_item_data in _tables or []:
            tables_item = DataSourceTable.from_dict(tables_item_data)

            tables.append(tables_item)

        data_source_metadata = cls(
            metadata_available=metadata_available,
            stores_templates=stores_templates,
            tables=tables,
        )

        data_source_metadata.additional_properties = d
        return data_source_metadata

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
