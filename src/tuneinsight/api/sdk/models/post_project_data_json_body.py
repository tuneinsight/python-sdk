from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostProjectDataJsonBody")


@attr.s(auto_attribs=True)
class PostProjectDataJsonBody:
    """
    Attributes:
        broadcast (Union[Unset, bool]):
    """

    broadcast: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        broadcast = self.broadcast

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if broadcast is not UNSET:
            field_dict["broadcast"] = broadcast

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        broadcast = d.pop("broadcast", UNSET)

        post_project_data_json_body = cls(
            broadcast=broadcast,
        )

        post_project_data_json_body.additional_properties = d
        return post_project_data_json_body

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
