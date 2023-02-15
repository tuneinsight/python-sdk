from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.noise_parameters import NoiseParameters


T = TypeVar("T", bound="DifferentialPrivacyParameters")


@attr.s(auto_attribs=True)
class DifferentialPrivacyParameters:
    """parameters for adding differential privacy noise to the computation's encrypted output

    Attributes:
        minimum_global_input_size (Union[Unset, int]): minimum size on the collective dataset, computed securely before
            the computation
        minimum_local_input_size (Union[Unset, int]): minimum size of the dataset used as local input
        noise_parameters (Union[Unset, NoiseParameters]): parameters for adding differential privacy noise to the
            computation's encrypted output
    """

    minimum_global_input_size: Union[Unset, int] = UNSET
    minimum_local_input_size: Union[Unset, int] = UNSET
    noise_parameters: Union[Unset, "NoiseParameters"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        minimum_global_input_size = self.minimum_global_input_size
        minimum_local_input_size = self.minimum_local_input_size
        noise_parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.noise_parameters, Unset):
            noise_parameters = self.noise_parameters.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if minimum_global_input_size is not UNSET:
            field_dict["minimumGlobalInputSize"] = minimum_global_input_size
        if minimum_local_input_size is not UNSET:
            field_dict["minimumLocalInputSize"] = minimum_local_input_size
        if noise_parameters is not UNSET:
            field_dict["noiseParameters"] = noise_parameters

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.noise_parameters import NoiseParameters

        d = src_dict.copy()
        minimum_global_input_size = d.pop("minimumGlobalInputSize", UNSET)

        minimum_local_input_size = d.pop("minimumLocalInputSize", UNSET)

        _noise_parameters = d.pop("noiseParameters", UNSET)
        noise_parameters: Union[Unset, NoiseParameters]
        if isinstance(_noise_parameters, Unset):
            noise_parameters = UNSET
        else:
            noise_parameters = NoiseParameters.from_dict(_noise_parameters)

        differential_privacy_parameters = cls(
            minimum_global_input_size=minimum_global_input_size,
            minimum_local_input_size=minimum_local_input_size,
            noise_parameters=noise_parameters,
        )

        differential_privacy_parameters.additional_properties = d
        return differential_privacy_parameters

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
