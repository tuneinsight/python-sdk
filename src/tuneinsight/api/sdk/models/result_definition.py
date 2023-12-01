from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResultDefinition")


@attr.s(auto_attribs=True)
class ResultDefinition:
    """user-defined computation result fields

    Attributes:
        shared (Union[Unset, None, bool]): if set to true, the result is shared with users from the same project
        tags (Union[Unset, List[str]]):
        title (Union[Unset, str]): title given to the result
        is_large (Union[Unset, None, bool]): format to display the result
    """

    shared: Union[Unset, None, bool] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    title: Union[Unset, str] = UNSET
    is_large: Union[Unset, None, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        shared = self.shared
        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        title = self.title
        is_large = self.is_large

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if shared is not UNSET:
            field_dict["shared"] = shared
        if tags is not UNSET:
            field_dict["tags"] = tags
        if title is not UNSET:
            field_dict["title"] = title
        if is_large is not UNSET:
            field_dict["isLarge"] = is_large

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        shared = d.pop("shared", UNSET)

        tags = cast(List[str], d.pop("tags", UNSET))

        title = d.pop("title", UNSET)

        is_large = d.pop("isLarge", UNSET)

        result_definition = cls(
            shared=shared,
            tags=tags,
            title=title,
            is_large=is_large,
        )

        result_definition.additional_properties = d
        return result_definition

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
