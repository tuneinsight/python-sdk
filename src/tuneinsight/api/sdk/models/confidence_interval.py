from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConfidenceInterval")


@attr.s(auto_attribs=True)
class ConfidenceInterval:
    """a confidence interval on a noisy or otherwise uncertainty value.

    Attributes:
        center (Union[Unset, None, float]): The center of the confidence interval in the probability sense (the median,
            not the geometric center).
            This is typically the value for which the confidence interval is computed.
        confidence (Union[Unset, float]): the confidence level of the interval, between 0 and 1.
        high (Union[Unset, float]): the upper bound of the interval.
        low (Union[Unset, float]): the lower bound of the interval.
    """

    center: Union[Unset, None, float] = UNSET
    confidence: Union[Unset, float] = UNSET
    high: Union[Unset, float] = UNSET
    low: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        center = self.center
        confidence = self.confidence
        high = self.high
        low = self.low

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if center is not UNSET:
            field_dict["center"] = center
        if confidence is not UNSET:
            field_dict["confidence"] = confidence
        if high is not UNSET:
            field_dict["high"] = high
        if low is not UNSET:
            field_dict["low"] = low

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        center = d.pop("center", UNSET)

        confidence = d.pop("confidence", UNSET)

        high = d.pop("high", UNSET)

        low = d.pop("low", UNSET)

        confidence_interval = cls(
            center=center,
            confidence=confidence,
            high=high,
            low=low,
        )

        confidence_interval.additional_properties = d
        return confidence_interval

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
