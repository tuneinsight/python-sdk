from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.noise_distributions import NoiseDistributions
from ..types import UNSET, Unset

T = TypeVar("T", bound="DpNoiseMetadata")


@attr.s(auto_attribs=True)
class DpNoiseMetadata:
    """The metadata of the noise added to a part of a result.

    Attributes:
        name (Union[Unset, str]): name that describes which part of the result the noise applies to.
        noise_scale (Union[Unset, List[float]]): standard deviation of the noise added on each entry in the results
        noise_type (Union[Unset, NoiseDistributions]): the distribution of the noise added on each entry in the results
    """

    name: Union[Unset, str] = UNSET
    noise_scale: Union[Unset, List[float]] = UNSET
    noise_type: Union[Unset, NoiseDistributions] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        noise_scale: Union[Unset, List[float]] = UNSET
        if not isinstance(self.noise_scale, Unset):
            noise_scale = self.noise_scale

        noise_type: Union[Unset, str] = UNSET
        if not isinstance(self.noise_type, Unset):
            noise_type = self.noise_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if noise_scale is not UNSET:
            field_dict["noiseScale"] = noise_scale
        if noise_type is not UNSET:
            field_dict["noiseType"] = noise_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        noise_scale = cast(List[float], d.pop("noiseScale", UNSET))

        _noise_type = d.pop("noiseType", UNSET)
        noise_type: Union[Unset, NoiseDistributions]
        if isinstance(_noise_type, Unset):
            noise_type = UNSET
        else:
            noise_type = NoiseDistributions(_noise_type)

        dp_noise_metadata = cls(
            name=name,
            noise_scale=noise_scale,
            noise_type=noise_type,
        )

        dp_noise_metadata.additional_properties = d
        return dp_noise_metadata

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
