from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dp_noise_metadata import DpNoiseMetadata


T = TypeVar("T", bound="ResultMetadata")


@attr.s(auto_attribs=True)
class ResultMetadata:
    """various metadata field along with the result to provide additional context

    Attributes:
        dp_noise (Union[Unset, List['DpNoiseMetadata']]): when using differential privacy, the metadata on the noise
            added to results.
    """

    dp_noise: Union[Unset, List["DpNoiseMetadata"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dp_noise: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.dp_noise, Unset):
            dp_noise = []
            for dp_noise_item_data in self.dp_noise:
                dp_noise_item = dp_noise_item_data.to_dict()

                dp_noise.append(dp_noise_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dp_noise is not UNSET:
            field_dict["dpNoise"] = dp_noise

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dp_noise_metadata import DpNoiseMetadata

        d = src_dict.copy()
        dp_noise = []
        _dp_noise = d.pop("dpNoise", UNSET)
        for dp_noise_item_data in _dp_noise or []:
            dp_noise_item = DpNoiseMetadata.from_dict(dp_noise_item_data)

            dp_noise.append(dp_noise_item)

        result_metadata = cls(
            dp_noise=dp_noise,
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
