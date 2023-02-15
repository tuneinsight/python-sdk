from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="FuzzyMatchingParameters")


@attr.s(auto_attribs=True)
class FuzzyMatchingParameters:
    """
    Attributes:
        phonetic_columns (Union[Unset, List[str]]): Columns which should be matched according to phonetic value
    """

    phonetic_columns: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        phonetic_columns: Union[Unset, List[str]] = UNSET
        if not isinstance(self.phonetic_columns, Unset):
            phonetic_columns = self.phonetic_columns

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if phonetic_columns is not UNSET:
            field_dict["phoneticColumns"] = phonetic_columns

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        phonetic_columns = cast(List[str], d.pop("phoneticColumns", UNSET))

        fuzzy_matching_parameters = cls(
            phonetic_columns=phonetic_columns,
        )

        fuzzy_matching_parameters.additional_properties = d
        return fuzzy_matching_parameters

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
