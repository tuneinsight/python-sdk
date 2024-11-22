from typing import Any, Dict, List, Type, TypeVar, cast

import attr

from ..models.preprocessing_operation_type import PreprocessingOperationType

T = TypeVar("T", bound="Drop")


@attr.s(auto_attribs=True)
class Drop:
    """
    Attributes:
        type (PreprocessingOperationType): type of preprocessing operation
        columns (List[str]): list of columns to drop
    """

    type: PreprocessingOperationType
    columns: List[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        columns = self.columns

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "columns": columns,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = PreprocessingOperationType(d.pop("type"))

        columns = cast(List[str], d.pop("columns"))

        drop = cls(
            type=type,
            columns=columns,
        )

        drop.additional_properties = d
        return drop

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
