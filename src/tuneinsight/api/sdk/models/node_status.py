from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="NodeStatus")


@attr.s(auto_attribs=True)
class NodeStatus:
    """Network Status of a node

    Attributes:
        accepted_groups (Union[Unset, List[str]]): list of user groups that are accepted by this instance. This is used
            to authorize node-to-node requests.
        node (Union[Unset, str]): URL of the node
        rtt (Union[Unset, int]): Round-trip time to this node in milliseconds
        service_account (Union[Unset, str]): name of the service account used by this instance to authenticate when
            sending requests to other instances.
        status (Union[Unset, str]): Status (ok/nok)
        version (Union[Unset, str]): Version of the node
    """

    accepted_groups: Union[Unset, List[str]] = UNSET
    node: Union[Unset, str] = UNSET
    rtt: Union[Unset, int] = UNSET
    service_account: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        accepted_groups: Union[Unset, List[str]] = UNSET
        if not isinstance(self.accepted_groups, Unset):
            accepted_groups = self.accepted_groups

        node = self.node
        rtt = self.rtt
        service_account = self.service_account
        status = self.status
        version = self.version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if accepted_groups is not UNSET:
            field_dict["acceptedGroups"] = accepted_groups
        if node is not UNSET:
            field_dict["node"] = node
        if rtt is not UNSET:
            field_dict["rtt"] = rtt
        if service_account is not UNSET:
            field_dict["serviceAccount"] = service_account
        if status is not UNSET:
            field_dict["status"] = status
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        accepted_groups = cast(List[str], d.pop("acceptedGroups", UNSET))

        node = d.pop("node", UNSET)

        rtt = d.pop("rtt", UNSET)

        service_account = d.pop("serviceAccount", UNSET)

        status = d.pop("status", UNSET)

        version = d.pop("version", UNSET)

        node_status = cls(
            accepted_groups=accepted_groups,
            node=node,
            rtt=rtt,
            service_account=service_account,
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
