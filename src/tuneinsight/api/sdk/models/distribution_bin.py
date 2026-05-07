from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.confidence_interval import ConfidenceInterval


T = TypeVar("T", bound="DistributionBin")


@attr.s(auto_attribs=True)
class DistributionBin:
    """Single bin with count

    Attributes:
        confidence_interval (Union[Unset, ConfidenceInterval]): a confidence interval on a noisy or otherwise
            uncertainty value.
        count (Union[Unset, None, int]): Number of patients
        label (Union[Unset, str]): Field label
        max_ (Union[Unset, None, float]): Maximum value
        min_ (Union[Unset, None, float]): Minimum value
        value (Union[Unset, None, str]):
    """

    confidence_interval: Union[Unset, "ConfidenceInterval"] = UNSET
    count: Union[Unset, None, int] = UNSET
    label: Union[Unset, str] = UNSET
    max_: Union[Unset, None, float] = UNSET
    min_: Union[Unset, None, float] = UNSET
    value: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        confidence_interval: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.confidence_interval, Unset):
            confidence_interval = self.confidence_interval.to_dict()

        count = self.count
        label = self.label
        max_ = self.max_
        min_ = self.min_
        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if confidence_interval is not UNSET:
            field_dict["confidenceInterval"] = confidence_interval
        if count is not UNSET:
            field_dict["count"] = count
        if label is not UNSET:
            field_dict["label"] = label
        if max_ is not UNSET:
            field_dict["max"] = max_
        if min_ is not UNSET:
            field_dict["min"] = min_
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.confidence_interval import ConfidenceInterval

        d = src_dict.copy()
        _confidence_interval = d.pop("confidenceInterval", UNSET)
        confidence_interval: Union[Unset, ConfidenceInterval]
        if isinstance(_confidence_interval, Unset):
            confidence_interval = UNSET
        else:
            confidence_interval = ConfidenceInterval.from_dict(_confidence_interval)

        count = d.pop("count", UNSET)

        label = d.pop("label", UNSET)

        max_ = d.pop("max", UNSET)

        min_ = d.pop("min", UNSET)

        value = d.pop("value", UNSET)

        distribution_bin = cls(
            confidence_interval=confidence_interval,
            count=count,
            label=label,
            max_=max_,
            min_=min_,
            value=value,
        )

        distribution_bin.additional_properties = d
        return distribution_bin

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
