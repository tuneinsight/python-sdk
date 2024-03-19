from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

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
        nodes (Union[Unset, List['Node']]):
        topology (Union[Unset, Topology]): Network Topologies. 'star' or 'tree'. In star topology all nodes are
            connected to a central node. In tree topology all nodes are connected and aware of each other.
        visibility_type (Union[Unset, NetworkVisibilityType]): represents the type of visibility leaf nodes have in a
            network
    """

    name: Union[Unset, str] = UNSET
    nodes: Union[Unset, List["Node"]] = UNSET
    topology: Union[Unset, Topology] = UNSET
    visibility_type: Union[Unset, NetworkVisibilityType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        nodes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.nodes, Unset):
            nodes = []
            for nodes_item_data in self.nodes:
                nodes_item = nodes_item_data.to_dict()

                nodes.append(nodes_item)

        topology: Union[Unset, str] = UNSET
        if not isinstance(self.topology, Unset):
            topology = self.topology.value

        visibility_type: Union[Unset, str] = UNSET
        if not isinstance(self.visibility_type, Unset):
            visibility_type = self.visibility_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if nodes is not UNSET:
            field_dict["nodes"] = nodes
        if topology is not UNSET:
            field_dict["topology"] = topology
        if visibility_type is not UNSET:
            field_dict["visibilityType"] = visibility_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.node import Node

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        nodes = []
        _nodes = d.pop("nodes", UNSET)
        for nodes_item_data in _nodes or []:
            nodes_item = Node.from_dict(nodes_item_data)

            nodes.append(nodes_item)

        _topology = d.pop("topology", UNSET)
        topology: Union[Unset, Topology]
        if isinstance(_topology, Unset):
            topology = UNSET
        else:
            topology = Topology(_topology)

        _visibility_type = d.pop("visibilityType", UNSET)
        visibility_type: Union[Unset, NetworkVisibilityType]
        if isinstance(_visibility_type, Unset):
            visibility_type = UNSET
        else:
            visibility_type = NetworkVisibilityType(_visibility_type)

        network = cls(
            name=name,
            nodes=nodes,
            topology=topology,
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
