from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResultMetadata")


@attr.s(auto_attribs=True)
class ResultMetadata:
    """various metadata field along with the result to provide additional context

    Attributes:
        noise_bound (Union[Unset, float]): numerical bound on the amount of noise added to the result, on a 95%
            confidence interval.
    """

    noise_bound: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        noise_bound = self.noise_bound

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if noise_bound is not UNSET:
            field_dict["noiseBound"] = noise_bound

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        noise_bound = d.pop("noiseBound", UNSET)

        result_metadata = cls(
            noise_bound=noise_bound,
        )

        result_metadata.additional_properties = d
        return result_metadata

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
