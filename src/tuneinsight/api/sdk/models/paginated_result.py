from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PaginatedResult")


@attr.s(auto_attribs=True)
class PaginatedResult:
    """
    Attributes:
        total (Union[Unset, int]):
        items (Union[Unset, List[Any]]):
    """

    total: Union[Unset, int] = UNSET
    items: Union[Unset, List[Any]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total = self.total
        items: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.items, Unset):
            items = self.items

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total is not UNSET:
            field_dict["total"] = total
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        total = d.pop("total", UNSET)

        items = cast(List[Any], d.pop("items", UNSET))

        paginated_result = cls(
            total=total,
            items=items,
        )

        paginated_result.additional_properties = d
        return paginated_result

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
