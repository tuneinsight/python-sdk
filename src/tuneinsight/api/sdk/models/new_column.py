from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.preprocessing_operation_type import PreprocessingOperationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.new_column_random import NewColumnRandom


T = TypeVar("T", bound="NewColumn")


@attr.s(auto_attribs=True)
class NewColumn:
    """
    Attributes:
        type (PreprocessingOperationType): type of preprocessing operation
        name (str): the name of the column to create or overwrite.
        random (Union[Unset, NewColumnRandom]): if specified, the column is filled with random normal values.
        value (Union[Unset, str]): the constant value to assign to the column.
    """

    type: PreprocessingOperationType
    name: str
    random: Union[Unset, "NewColumnRandom"] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        name = self.name
        random: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.random, Unset):
            random = self.random.to_dict()

        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "name": name,
            }
        )
        if random is not UNSET:
            field_dict["random"] = random
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.new_column_random import NewColumnRandom

        d = src_dict.copy()
        type = PreprocessingOperationType(d.pop("type"))

        name = d.pop("name")

        _random = d.pop("random", UNSET)
        random: Union[Unset, NewColumnRandom]
        if isinstance(_random, Unset):
            random = UNSET
        else:
            random = NewColumnRandom.from_dict(_random)

        value = d.pop("value", UNSET)

        new_column = cls(
            type=type,
            name=name,
            random=random,
            value=value,
        )

        new_column.additional_properties = d
        return new_column

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
