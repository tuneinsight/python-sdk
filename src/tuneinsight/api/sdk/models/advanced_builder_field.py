from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="AdvancedBuilderField")


@attr.s(auto_attribs=True)
class AdvancedBuilderField:
    """Configuration for an advanced builder parameter field.

    Attributes:
        column (str): The column name in the table.
        table (str): The table/concept name in the database schema.
    """

    column: str
    table: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        column = self.column
        table = self.table

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "column": column,
                "table": table,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        column = d.pop("column")

        table = d.pop("table")

        advanced_builder_field = cls(
            column=column,
            table=table,
        )

        advanced_builder_field.additional_properties = d
        return advanced_builder_field

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
