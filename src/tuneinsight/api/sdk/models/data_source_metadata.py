from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_source_table import DataSourceTable


T = TypeVar("T", bound="DataSourceMetadata")


@attr.s(auto_attribs=True)
class DataSourceMetadata:
    """metadata about a datasource

    Attributes:
        errors (Union[Unset, List[str]]): list of errors triggered when creating the metadata.
        metadata_available (Union[Unset, bool]): whether or not the datasource supports returning metadata
        stores_templates (Union[Unset, bool]): whether the data source stores template tables.
        tables (Union[Unset, List['DataSourceTable']]):
        total_tables (Union[Unset, int]): total number of tables available with this data source. Not all tables may
            appear in this metadata as they can still be loading.
        warnings (Union[Unset, List[str]]): list of warnings triggered when creating the metadata.
    """

    errors: Union[Unset, List[str]] = UNSET
    metadata_available: Union[Unset, bool] = UNSET
    stores_templates: Union[Unset, bool] = UNSET
    tables: Union[Unset, List["DataSourceTable"]] = UNSET
    total_tables: Union[Unset, int] = UNSET
    warnings: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        errors: Union[Unset, List[str]] = UNSET
        if not isinstance(self.errors, Unset):
            errors = self.errors

        metadata_available = self.metadata_available
        stores_templates = self.stores_templates
        tables: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tables, Unset):
            tables = []
            for tables_item_data in self.tables:
                tables_item = tables_item_data.to_dict()

                tables.append(tables_item)

        total_tables = self.total_tables
        warnings: Union[Unset, List[str]] = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = self.warnings

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if errors is not UNSET:
            field_dict["errors"] = errors
        if metadata_available is not UNSET:
            field_dict["metadataAvailable"] = metadata_available
        if stores_templates is not UNSET:
            field_dict["storesTemplates"] = stores_templates
        if tables is not UNSET:
            field_dict["tables"] = tables
        if total_tables is not UNSET:
            field_dict["totalTables"] = total_tables
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.data_source_table import DataSourceTable

        d = src_dict.copy()
        errors = cast(List[str], d.pop("errors", UNSET))

        metadata_available = d.pop("metadataAvailable", UNSET)

        stores_templates = d.pop("storesTemplates", UNSET)

        tables = []
        _tables = d.pop("tables", UNSET)
        for tables_item_data in _tables or []:
            tables_item = DataSourceTable.from_dict(tables_item_data)

            tables.append(tables_item)

        total_tables = d.pop("totalTables", UNSET)

        warnings = cast(List[str], d.pop("warnings", UNSET))

        data_source_metadata = cls(
            errors=errors,
            metadata_available=metadata_available,
            stores_templates=stores_templates,
            tables=tables,
            total_tables=total_tables,
            warnings=warnings,
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
