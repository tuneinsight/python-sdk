from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.node import Node


T = TypeVar("T", bound="UserGroup")


@attr.s(auto_attribs=True)
class UserGroup:
    """information about a user group.

    Attributes:
        name (Union[Unset, str]): string-value of the group
        origin_node (Union[Unset, Node]): Node or agent of the network
    """

    name: Union[Unset, str] = UNSET
    origin_node: Union[Unset, "Node"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        origin_node: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.origin_node, Unset):
            origin_node = self.origin_node.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if origin_node is not UNSET:
            field_dict["originNode"] = origin_node

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.node import Node

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        _origin_node = d.pop("originNode", UNSET)
        origin_node: Union[Unset, Node]
        if isinstance(_origin_node, Unset):
            origin_node = UNSET
        else:
            origin_node = Node.from_dict(_origin_node)

        user_group = cls(
            name=name,
            origin_node=origin_node,
        )

        user_group.additional_properties = d
        return user_group

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
