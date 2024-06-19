from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="LocusRange")


@attr.s(auto_attribs=True)
class LocusRange:
    """range specification for locus genomic positions

    Attributes:
        min_chromosome (Union[Unset, str]):
        min_position (Union[Unset, int]):
        max_chromosome (Union[Unset, str]):
        max_position (Union[Unset, int]):
    """

    min_chromosome: Union[Unset, str] = UNSET
    min_position: Union[Unset, int] = UNSET
    max_chromosome: Union[Unset, str] = UNSET
    max_position: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        min_chromosome = self.min_chromosome
        min_position = self.min_position
        max_chromosome = self.max_chromosome
        max_position = self.max_position

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if min_chromosome is not UNSET:
            field_dict["minChromosome"] = min_chromosome
        if min_position is not UNSET:
            field_dict["minPosition"] = min_position
        if max_chromosome is not UNSET:
            field_dict["maxChromosome"] = max_chromosome
        if max_position is not UNSET:
            field_dict["maxPosition"] = max_position

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        min_chromosome = d.pop("minChromosome", UNSET)

        min_position = d.pop("minPosition", UNSET)

        max_chromosome = d.pop("maxChromosome", UNSET)

        max_position = d.pop("maxPosition", UNSET)

        locus_range = cls(
            min_chromosome=min_chromosome,
            min_position=min_position,
            max_chromosome=max_chromosome,
            max_position=max_position,
        )

        locus_range.additional_properties = d
        return locus_range

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
