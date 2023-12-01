from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.column_schema import ColumnSchema


T = TypeVar("T", bound="DatasetSchemaColumns")


@attr.s(auto_attribs=True)
class DatasetSchemaColumns:
    """mapping from column names to a set of constraints
    that the values present in the column should comply to.

    """

    additional_properties: Dict[str, "ColumnSchema"] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pass

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.column_schema import ColumnSchema

        d = src_dict.copy()
        dataset_schema_columns = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = ColumnSchema.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        dataset_schema_columns.additional_properties = additional_properties
        return dataset_schema_columns

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "ColumnSchema":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "ColumnSchema") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
