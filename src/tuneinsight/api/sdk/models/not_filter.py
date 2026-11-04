from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.advanced_filter_type import AdvancedFilterType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advanced_filter import AdvancedFilter


T = TypeVar("T", bound="NotFilter")


@attr.s(auto_attribs=True)
class NotFilter:
    """A TIQL++ filter that computes the negation of its nested filter (true if the filter is false and vice versa).
    This should be used for exclusion criteria.
    The TIQL transpiler unwraps this filter and computes the logical negation of its nested filter.

        Attributes:
            type (AdvancedFilterType): A type of filter for cross-standard queries.
            filter_ (Union[Unset, AdvancedFilter]): Abstract subclass of a filter for cross-standard queries.
    """

    type: AdvancedFilterType
    filter_: Union[Unset, "AdvancedFilter"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        filter_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if filter_ is not UNSET:
            field_dict["filter"] = filter_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.advanced_filter import AdvancedFilter

        d = src_dict.copy()
        type = AdvancedFilterType(d.pop("type"))

        _filter_ = d.pop("filter", UNSET)
        filter_: Union[Unset, AdvancedFilter]
        if isinstance(_filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = AdvancedFilter.from_dict(_filter_)

        not_filter = cls(
            type=type,
            filter_=filter_,
        )

        not_filter.additional_properties = d
        return not_filter

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
