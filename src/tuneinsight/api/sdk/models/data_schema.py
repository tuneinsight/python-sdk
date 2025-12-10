from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_schema_advanced_builder_fields import DataSchemaAdvancedBuilderFields
    from ..models.schema_table import SchemaTable


T = TypeVar("T", bound="DataSchema")


@attr.s(auto_attribs=True)
class DataSchema:
    """aims to provide a flexible definition of a data schema, which includes the tables and their relationships.

    Attributes:
        advanced_builder_fields (Union[Unset, DataSchemaAdvancedBuilderFields]): Predefined fields for advanced query
            builder parameters.
        name (Union[Unset, str]): optional name for the schema.
        tables (Union[Unset, List['SchemaTable']]):
    """

    advanced_builder_fields: Union[Unset, "DataSchemaAdvancedBuilderFields"] = UNSET
    name: Union[Unset, str] = UNSET
    tables: Union[Unset, List["SchemaTable"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        advanced_builder_fields: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.advanced_builder_fields, Unset):
            advanced_builder_fields = self.advanced_builder_fields.to_dict()

        name = self.name
        tables: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tables, Unset):
            tables = []
            for tables_item_data in self.tables:
                tables_item = tables_item_data.to_dict()

                tables.append(tables_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if advanced_builder_fields is not UNSET:
            field_dict["advancedBuilderFields"] = advanced_builder_fields
        if name is not UNSET:
            field_dict["name"] = name
        if tables is not UNSET:
            field_dict["tables"] = tables

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.data_schema_advanced_builder_fields import DataSchemaAdvancedBuilderFields
        from ..models.schema_table import SchemaTable

        d = src_dict.copy()
        _advanced_builder_fields = d.pop("advancedBuilderFields", UNSET)
        advanced_builder_fields: Union[Unset, DataSchemaAdvancedBuilderFields]
        if isinstance(_advanced_builder_fields, Unset):
            advanced_builder_fields = UNSET
        else:
            advanced_builder_fields = DataSchemaAdvancedBuilderFields.from_dict(_advanced_builder_fields)

        name = d.pop("name", UNSET)

        tables = []
        _tables = d.pop("tables", UNSET)
        for tables_item_data in _tables or []:
            tables_item = SchemaTable.from_dict(tables_item_data)

            tables.append(tables_item)

        data_schema = cls(
            advanced_builder_fields=advanced_builder_fields,
            name=name,
            tables=tables,
        )

        data_schema.additional_properties = d
        return data_schema

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
