from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.network_type import NetworkType
from ..models.network_visibility_type import NetworkVisibilityType
from ..models.topology import Topology
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.node import Node


T = TypeVar("T", bound="Network")


@attr.s(auto_attribs=True)
class Network:
    """Network that represents a set of nodes

    Attributes:
        name (Union[Unset, str]):
        network_type (Union[Unset, NetworkType]): Network Type. 'default' or 'sse'. In a NAT network, leaf node use SSE
            to connect to the root.
        nodes (Union[Unset, List['Node']]):
        restricted (Union[Unset, None, bool]): if set, then the network can only be viewed by the users in the network.
            (does not apply to projects)
        topology (Union[Unset, Topology]): Network Topologies. 'star' or 'tree'. In star topology all nodes are
            connected to a central node. In tree topology all nodes are connected and aware of each other.
        users (Union[Unset, List[str]]): list of users in the network
        visibility_type (Union[Unset, NetworkVisibilityType]): represents the type of visibility leaf nodes have in a
            network
    """

    name: Union[Unset, str] = UNSET
    network_type: Union[Unset, NetworkType] = UNSET
    nodes: Union[Unset, List["Node"]] = UNSET
    restricted: Union[Unset, None, bool] = UNSET
    topology: Union[Unset, Topology] = UNSET
    users: Union[Unset, List[str]] = UNSET
    visibility_type: Union[Unset, NetworkVisibilityType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        network_type: Union[Unset, str] = UNSET
        if not isinstance(self.network_type, Unset):
            network_type = self.network_type.value

        nodes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.nodes, Unset):
            nodes = []
            for nodes_item_data in self.nodes:
                nodes_item = nodes_item_data.to_dict()

                nodes.append(nodes_item)

        restricted = self.restricted
        topology: Union[Unset, str] = UNSET
        if not isinstance(self.topology, Unset):
            topology = self.topology.value

        users: Union[Unset, List[str]] = UNSET
        if not isinstance(self.users, Unset):
            users = self.users

        visibility_type: Union[Unset, str] = UNSET
        if not isinstance(self.visibility_type, Unset):
            visibility_type = self.visibility_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if network_type is not UNSET:
            field_dict["networkType"] = network_type
        if nodes is not UNSET:
            field_dict["nodes"] = nodes
        if restricted is not UNSET:
            field_dict["restricted"] = restricted
        if topology is not UNSET:
            field_dict["topology"] = topology
        if users is not UNSET:
            field_dict["users"] = users
        if visibility_type is not UNSET:
            field_dict["visibilityType"] = visibility_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.node import Node

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        _network_type = d.pop("networkType", UNSET)
        network_type: Union[Unset, NetworkType]
        if isinstance(_network_type, Unset):
            network_type = UNSET
        else:
            network_type = NetworkType(_network_type)

        nodes = []
        _nodes = d.pop("nodes", UNSET)
        for nodes_item_data in _nodes or []:
            nodes_item = Node.from_dict(nodes_item_data)

            nodes.append(nodes_item)

        restricted = d.pop("restricted", UNSET)

        _topology = d.pop("topology", UNSET)
        topology: Union[Unset, Topology]
        if isinstance(_topology, Unset):
            topology = UNSET
        else:
            topology = Topology(_topology)

        users = cast(List[str], d.pop("users", UNSET))

        _visibility_type = d.pop("visibilityType", UNSET)
        visibility_type: Union[Unset, NetworkVisibilityType]
        if isinstance(_visibility_type, Unset):
            visibility_type = UNSET
        else:
            visibility_type = NetworkVisibilityType(_visibility_type)

        network = cls(
            name=name,
            network_type=network_type,
            nodes=nodes,
            restricted=restricted,
            topology=topology,
            users=users,
            visibility_type=visibility_type,
        )

        network.additional_properties = d
        return network

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
