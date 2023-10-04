from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_network_metadata_response_200_nodes_item import GetNetworkMetadataResponse200NodesItem


T = TypeVar("T", bound="GetNetworkMetadataResponse200")


@attr.s(auto_attribs=True)
class GetNetworkMetadataResponse200:
    """
    Attributes:
        nodes (List['GetNetworkMetadataResponse200NodesItem']):
        public_key (str): Aggregated public key of the collective authority.
        default_topology (Union[Unset, str]): Indicates the default topology of the network used when creating a
            project. Values can be "star" or "tree".
        dpo_authorization_enabled (Union[Unset, bool]):
        initiated (Union[Unset, bool]): Indicates if the session has been initiated. Meaning that the collective public
            key and relinearization key have been generated and shared across all nodes.
    """

    nodes: List["GetNetworkMetadataResponse200NodesItem"]
    public_key: str
    default_topology: Union[Unset, str] = UNSET
    dpo_authorization_enabled: Union[Unset, bool] = UNSET
    initiated: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        nodes = []
        for nodes_item_data in self.nodes:
            nodes_item = nodes_item_data.to_dict()

            nodes.append(nodes_item)

        public_key = self.public_key
        default_topology = self.default_topology
        dpo_authorization_enabled = self.dpo_authorization_enabled
        initiated = self.initiated

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "nodes": nodes,
                "public-key": public_key,
            }
        )
        if default_topology is not UNSET:
            field_dict["default-topology"] = default_topology
        if dpo_authorization_enabled is not UNSET:
            field_dict["dpoAuthorizationEnabled"] = dpo_authorization_enabled
        if initiated is not UNSET:
            field_dict["initiated"] = initiated

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_network_metadata_response_200_nodes_item import GetNetworkMetadataResponse200NodesItem

        d = src_dict.copy()
        nodes = []
        _nodes = d.pop("nodes")
        for nodes_item_data in _nodes:
            nodes_item = GetNetworkMetadataResponse200NodesItem.from_dict(nodes_item_data)

            nodes.append(nodes_item)

        public_key = d.pop("public-key")

        default_topology = d.pop("default-topology", UNSET)

        dpo_authorization_enabled = d.pop("dpoAuthorizationEnabled", UNSET)

        initiated = d.pop("initiated", UNSET)

        get_network_metadata_response_200 = cls(
            nodes=nodes,
            public_key=public_key,
            default_topology=default_topology,
            dpo_authorization_enabled=dpo_authorization_enabled,
            initiated=initiated,
        )

        get_network_metadata_response_200.additional_properties = d
        return get_network_metadata_response_200

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
