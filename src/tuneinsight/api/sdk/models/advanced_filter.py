from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.advanced_filter_type import AdvancedFilterType

T = TypeVar("T", bound="AdvancedFilter")


@attr.s(auto_attribs=True)
class AdvancedFilter:
    """Abstract subclass of a filter for cross-standard queries.

    Attributes:
        type (AdvancedFilterType): A type of filter for cross-standard queries.
    """

    type: AdvancedFilterType
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = AdvancedFilterType(d.pop("type"))

        advanced_filter = cls(
            type=type,
        )

        advanced_filter.additional_properties = d
        return advanced_filter

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
