from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.relation import Relation
    from ..models.schema_field import SchemaField


T = TypeVar("T", bound="SchemaTable")


@attr.s(auto_attribs=True)
class SchemaTable:
    """Definition of a table or view within a data schema, including fields and local relations. This is a resource in
    FHIR.

        Attributes:
            description (Union[Unset, str]): optional description for the table
            fields (Union[Unset, List['SchemaField']]): List of fields available in this table.
            hidden (Union[Unset, bool]): whether this table should be hidden from the user in the frontend.
            identifier (Union[Unset, str]): The primary key column of this table (e.g., "id").
            is_hierarchy_table (Union[Unset, bool]): whether this table contains hierarchical data for its concept, which
                can be used in the catalog hierarchy and to compute ancestor counts.
            is_main (Union[Unset, bool]): Marks this table as the main entry point for queries. Only one table
                in the template should be marked `true`. This table provides the
                `mainTable` and `identifier` used in SQLMetadata.
            linked_template (Union[Unset, bool]): Indicates whether this table is linked to other templates.
            name (Union[Unset, str]): The actual table name in the database (e.g., "patients").
            relations (Union[Unset, List['Relation']]): List of foreign key relations from this table to others.
            timestamp_column (Union[Unset, str]): The column in this table that contains the timestamp for the encoded
                event.
            title (Union[Unset, str]): Human-readable label for the table (e.g., "Patient").
    """

    description: Union[Unset, str] = UNSET
    fields: Union[Unset, List["SchemaField"]] = UNSET
    hidden: Union[Unset, bool] = UNSET
    identifier: Union[Unset, str] = UNSET
    is_hierarchy_table: Union[Unset, bool] = UNSET
    is_main: Union[Unset, bool] = UNSET
    linked_template: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    relations: Union[Unset, List["Relation"]] = UNSET
    timestamp_column: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        fields: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.fields, Unset):
            fields = []
            for fields_item_data in self.fields:
                fields_item = fields_item_data.to_dict()

                fields.append(fields_item)

        hidden = self.hidden
        identifier = self.identifier
        is_hierarchy_table = self.is_hierarchy_table
        is_main = self.is_main
        linked_template = self.linked_template
        name = self.name
        relations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.relations, Unset):
            relations = []
            for relations_item_data in self.relations:
                relations_item = relations_item_data.to_dict()

                relations.append(relations_item)

        timestamp_column = self.timestamp_column
        title = self.title

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if fields is not UNSET:
            field_dict["fields"] = fields
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if is_hierarchy_table is not UNSET:
            field_dict["isHierarchyTable"] = is_hierarchy_table
        if is_main is not UNSET:
            field_dict["isMain"] = is_main
        if linked_template is not UNSET:
            field_dict["linkedTemplate"] = linked_template
        if name is not UNSET:
            field_dict["name"] = name
        if relations is not UNSET:
            field_dict["relations"] = relations
        if timestamp_column is not UNSET:
            field_dict["timestampColumn"] = timestamp_column
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.relation import Relation
        from ..models.schema_field import SchemaField

        d = src_dict.copy()
        description = d.pop("description", UNSET)

        fields = []
        _fields = d.pop("fields", UNSET)
        for fields_item_data in _fields or []:
            fields_item = SchemaField.from_dict(fields_item_data)

            fields.append(fields_item)

        hidden = d.pop("hidden", UNSET)

        identifier = d.pop("identifier", UNSET)

        is_hierarchy_table = d.pop("isHierarchyTable", UNSET)

        is_main = d.pop("isMain", UNSET)

        linked_template = d.pop("linkedTemplate", UNSET)

        name = d.pop("name", UNSET)

        relations = []
        _relations = d.pop("relations", UNSET)
        for relations_item_data in _relations or []:
            relations_item = Relation.from_dict(relations_item_data)

            relations.append(relations_item)

        timestamp_column = d.pop("timestampColumn", UNSET)

        title = d.pop("title", UNSET)

        schema_table = cls(
            description=description,
            fields=fields,
            hidden=hidden,
            identifier=identifier,
            is_hierarchy_table=is_hierarchy_table,
            is_main=is_main,
            linked_template=linked_template,
            name=name,
            relations=relations,
            timestamp_column=timestamp_column,
            title=title,
        )

        schema_table.additional_properties = d
        return schema_table

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
