from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Relation")


@attr.s(auto_attribs=True)
class Relation:
    """A foreign key relation between two schema tables.

    Attributes:
        foreign_key (Union[Unset, str]): The foreign key column in the current table.
        target_table (Union[Unset, str]): Name of the target table in the relation.
    """

    foreign_key: Union[Unset, str] = UNSET
    target_table: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        foreign_key = self.foreign_key
        target_table = self.target_table

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if foreign_key is not UNSET:
            field_dict["foreignKey"] = foreign_key
        if target_table is not UNSET:
            field_dict["targetTable"] = target_table

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        foreign_key = d.pop("foreignKey", UNSET)

        target_table = d.pop("targetTable", UNSET)

        relation = cls(
            foreign_key=foreign_key,
            target_table=target_table,
        )

        relation.additional_properties = d
        return relation

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
