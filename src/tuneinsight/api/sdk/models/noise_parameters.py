from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="NoiseParameters")


@attr.s(auto_attribs=True)
class NoiseParameters:
    """parameters for adding differential privacy noise to the computation's encrypted output

    Attributes:
        epsilon (Union[Unset, float]): the privacy budget Default: 0.2.
        sensitivity (Union[Unset, float]): sensitivity of the function applied Default: 1.0.
    """

    epsilon: Union[Unset, float] = 0.2
    sensitivity: Union[Unset, float] = 1.0
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        epsilon = self.epsilon
        sensitivity = self.sensitivity

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if epsilon is not UNSET:
            field_dict["epsilon"] = epsilon
        if sensitivity is not UNSET:
            field_dict["sensitivity"] = sensitivity

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        epsilon = d.pop("epsilon", UNSET)

        sensitivity = d.pop("sensitivity", UNSET)

        noise_parameters = cls(
            epsilon=epsilon,
            sensitivity=sensitivity,
        )

        noise_parameters.additional_properties = d
        return noise_parameters

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
