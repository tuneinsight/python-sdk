from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="HybridFLSpecBaseParams")


@attr.s(auto_attribs=True)
class HybridFLSpecBaseParams:
    """Specific parameters for the Hybrid Federated Learning (base pattern), required for handling project fetching from
    geco

        Attributes:
            params_type (Union[Unset, str]): Type of the protocol to use
            test (Union[Unset, str]): Test parameter
    """

    params_type: Union[Unset, str] = UNSET
    test: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        params_type = self.params_type
        test = self.test

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if params_type is not UNSET:
            field_dict["paramsType"] = params_type
        if test is not UNSET:
            field_dict["test"] = test

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        params_type = d.pop("paramsType", UNSET)

        test = d.pop("test", UNSET)

        hybrid_fl_spec_base_params = cls(
            params_type=params_type,
            test=test,
        )

        hybrid_fl_spec_base_params.additional_properties = d
        return hybrid_fl_spec_base_params

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
