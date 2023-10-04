from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="NoiseParameters")


@attr.s(auto_attribs=True)
class NoiseParameters:
    """parameters for adding differential privacy noise to the computation's encrypted output

    Attributes:
        sensitivity (Union[Unset, float]): sensitivity of the function applied Default: 1.0.
        delta (Union[Unset, float]): probability of privacy leakage Default: 0.0001.
        discrete (Union[Unset, bool]): whether to sample discrete noise or not Default: True.
        epsilon (Union[Unset, float]): the privacy budget Default: 0.2.
    """

    sensitivity: Union[Unset, float] = 1.0
    delta: Union[Unset, float] = 0.0001
    discrete: Union[Unset, bool] = True
    epsilon: Union[Unset, float] = 0.2
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sensitivity = self.sensitivity
        delta = self.delta
        discrete = self.discrete
        epsilon = self.epsilon

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sensitivity is not UNSET:
            field_dict["sensitivity"] = sensitivity
        if delta is not UNSET:
            field_dict["delta"] = delta
        if discrete is not UNSET:
            field_dict["discrete"] = discrete
        if epsilon is not UNSET:
            field_dict["epsilon"] = epsilon

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        sensitivity = d.pop("sensitivity", UNSET)

        delta = d.pop("delta", UNSET)

        discrete = d.pop("discrete", UNSET)

        epsilon = d.pop("epsilon", UNSET)

        noise_parameters = cls(
            sensitivity=sensitivity,
            delta=delta,
            discrete=discrete,
            epsilon=epsilon,
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
