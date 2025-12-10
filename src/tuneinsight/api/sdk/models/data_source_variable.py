from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.column_type_group import ColumnTypeGroup
from ..types import UNSET, Unset

T = TypeVar("T", bound="DataSourceVariable")


@attr.s(auto_attribs=True)
class DataSourceVariable:
    """Description of a variable available for a computation after pre-processing.
    This is similar to dataSourceColumn, except it contains information about the location of this
    variable in the data, i.e. the concept and field where the value is found. These values must be
    accurate, so that the corresponding value can be retrieved in the data. If left empty, this
    indicates that the variable is not directly extracted from the data but otherwise produced, e.g.,
    by a preprocessing operation.
    The variable name is not obligated to match the name of the field, and can be a user-defined name,
    for instance one that is more human readable.

        Attributes:
            name (Union[Unset, str]):
            type (Union[Unset, str]):
            type_group (Union[Unset, ColumnTypeGroup]): represents a type group indicating the way the data may actually be
                processed
            concept (Union[Unset, str]): Concept in the data where this variable is found.
            field (Union[Unset, str]): Field in the data concept that contains the data for this variable.
    """

    name: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    type_group: Union[Unset, ColumnTypeGroup] = UNSET
    concept: Union[Unset, str] = UNSET
    field: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        type = self.type
        type_group: Union[Unset, str] = UNSET
        if not isinstance(self.type_group, Unset):
            type_group = self.type_group.value

        concept = self.concept
        field = self.field

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if type is not UNSET:
            field_dict["type"] = type
        if type_group is not UNSET:
            field_dict["typeGroup"] = type_group
        if concept is not UNSET:
            field_dict["concept"] = concept
        if field is not UNSET:
            field_dict["field"] = field

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        type = d.pop("type", UNSET)

        _type_group = d.pop("typeGroup", UNSET)
        type_group: Union[Unset, ColumnTypeGroup]
        if isinstance(_type_group, Unset):
            type_group = UNSET
        else:
            type_group = ColumnTypeGroup(_type_group)

        concept = d.pop("concept", UNSET)

        field = d.pop("field", UNSET)

        data_source_variable = cls(
            name=name,
            type=type,
            type_group=type_group,
            concept=concept,
            field=field,
        )

        data_source_variable.additional_properties = d
        return data_source_variable

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
