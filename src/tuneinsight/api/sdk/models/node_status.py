from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="NodeStatus")


@attr.s(auto_attribs=True)
class NodeStatus:
    """Network Status of a node

    Attributes:
        node (Union[Unset, str]): URL of the node
        status (Union[Unset, str]): Status (ok/nok)
        version (Union[Unset, str]): Version of the node
    """

    node: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        node = self.node
        status = self.status
        version = self.version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if node is not UNSET:
            field_dict["node"] = node
        if status is not UNSET:
            field_dict["status"] = status
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        node = d.pop("node", UNSET)

        status = d.pop("status", UNSET)

        version = d.pop("version", UNSET)

        node_status = cls(
            node=node,
            status=status,
            version=version,
        )

        node_status.additional_properties = d
        return node_status

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
