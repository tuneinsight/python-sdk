from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="HybridFLDpParams")


@attr.s(auto_attribs=True)
class HybridFLDpParams:
    """Parameters for Differential Privacy in the Hybrid Federated Learning

    Attributes:
        delta (Union[Unset, float]): Delta parameter of the differential privacy in HybridFL
        gradient_clipping (Union[Unset, float]): Gradient clipping to apply for the training and the noise computation
        use_clipping_factor (Union[Unset, bool]): If set to true, gradient clipping is adjusted specifically at each
            layer Default: True.
    """

    delta: Union[Unset, float] = UNSET
    gradient_clipping: Union[Unset, float] = UNSET
    use_clipping_factor: Union[Unset, bool] = True
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        delta = self.delta
        gradient_clipping = self.gradient_clipping
        use_clipping_factor = self.use_clipping_factor

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if delta is not UNSET:
            field_dict["delta"] = delta
        if gradient_clipping is not UNSET:
            field_dict["gradientClipping"] = gradient_clipping
        if use_clipping_factor is not UNSET:
            field_dict["useClippingFactor"] = use_clipping_factor

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        delta = d.pop("delta", UNSET)

        gradient_clipping = d.pop("gradientClipping", UNSET)

        use_clipping_factor = d.pop("useClippingFactor", UNSET)

        hybrid_fl_dp_params = cls(
            delta=delta,
            gradient_clipping=gradient_clipping,
            use_clipping_factor=use_clipping_factor,
        )

        hybrid_fl_dp_params.additional_properties = d
        return hybrid_fl_dp_params

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
