from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.distribution_type import DistributionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.distribution_bin import DistributionBin


T = TypeVar("T", bound="Distribution")


@attr.s(auto_attribs=True)
class Distribution:
    """
    Attributes:
        bins (Union[Unset, List['DistributionBin']]):
        type (Union[Unset, DistributionType]):
    """

    bins: Union[Unset, List["DistributionBin"]] = UNSET
    type: Union[Unset, DistributionType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        bins: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.bins, Unset):
            bins = []
            for bins_item_data in self.bins:
                bins_item = bins_item_data.to_dict()

                bins.append(bins_item)

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bins is not UNSET:
            field_dict["bins"] = bins
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.distribution_bin import DistributionBin

        d = src_dict.copy()
        bins = []
        _bins = d.pop("bins", UNSET)
        for bins_item_data in _bins or []:
            bins_item = DistributionBin.from_dict(bins_item_data)

            bins.append(bins_item)

        _type = d.pop("type", UNSET)
        type: Union[Unset, DistributionType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = DistributionType(_type)

        distribution = cls(
            bins=bins,
            type=type,
        )

        distribution.additional_properties = d
        return distribution

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
