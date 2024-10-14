from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.get_network_metadata_response_200_network_type import GetNetworkMetadataResponse200NetworkType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.network import Network
    from ..models.node import Node


T = TypeVar("T", bound="GetNetworkMetadataResponse200")


@attr.s(auto_attribs=True)
class GetNetworkMetadataResponse200:
    """
    Attributes:
        compound_queries_enabled (Union[Unset, bool]): Indicates if compound queries are enabled. If true, the data
            source queries can be composed of multiple queries.
        default_topology (Union[Unset, str]): Indicates the default topology of the network used when creating a
            project. Values can be "star" or "tree".
        dpo_authorization_enabled (Union[Unset, bool]): Indicates if collective projects require authorization.
        e_2_ee_enforced (Union[Unset, bool]): Indicates if the instance is configured to only allow end-to-end encrypted
            computations.
            When this mode is activated, the e2e project setting cannot be toggled off anymore and only computations
            supporting e2e mode can be launched.
        network_type (Union[Unset, GetNetworkMetadataResponse200NetworkType]): Indicates the type of network. Values can
            be "default" or "sse".
        networks (Union[Unset, List['Network']]):
        nodes (Union[Unset, List['Node']]):
        warnings (Union[Unset, List[str]]):
    """

    compound_queries_enabled: Union[Unset, bool] = UNSET
    default_topology: Union[Unset, str] = UNSET
    dpo_authorization_enabled: Union[Unset, bool] = UNSET
    e_2_ee_enforced: Union[Unset, bool] = UNSET
    network_type: Union[Unset, GetNetworkMetadataResponse200NetworkType] = UNSET
    networks: Union[Unset, List["Network"]] = UNSET
    nodes: Union[Unset, List["Node"]] = UNSET
    warnings: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        compound_queries_enabled = self.compound_queries_enabled
        default_topology = self.default_topology
        dpo_authorization_enabled = self.dpo_authorization_enabled
        e_2_ee_enforced = self.e_2_ee_enforced
        network_type: Union[Unset, str] = UNSET
        if not isinstance(self.network_type, Unset):
            network_type = self.network_type.value

        networks: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.networks, Unset):
            networks = []
            for networks_item_data in self.networks:
                networks_item = networks_item_data.to_dict()

                networks.append(networks_item)

        nodes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.nodes, Unset):
            nodes = []
            for nodes_item_data in self.nodes:
                nodes_item = nodes_item_data.to_dict()

                nodes.append(nodes_item)

        warnings: Union[Unset, List[str]] = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = self.warnings

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if compound_queries_enabled is not UNSET:
            field_dict["compoundQueriesEnabled"] = compound_queries_enabled
        if default_topology is not UNSET:
            field_dict["defaultTopology"] = default_topology
        if dpo_authorization_enabled is not UNSET:
            field_dict["dpoAuthorizationEnabled"] = dpo_authorization_enabled
        if e_2_ee_enforced is not UNSET:
            field_dict["e2eeEnforced"] = e_2_ee_enforced
        if network_type is not UNSET:
            field_dict["networkType"] = network_type
        if networks is not UNSET:
            field_dict["networks"] = networks
        if nodes is not UNSET:
            field_dict["nodes"] = nodes
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.network import Network
        from ..models.node import Node

        d = src_dict.copy()
        compound_queries_enabled = d.pop("compoundQueriesEnabled", UNSET)

        default_topology = d.pop("defaultTopology", UNSET)

        dpo_authorization_enabled = d.pop("dpoAuthorizationEnabled", UNSET)

        e_2_ee_enforced = d.pop("e2eeEnforced", UNSET)

        _network_type = d.pop("networkType", UNSET)
        network_type: Union[Unset, GetNetworkMetadataResponse200NetworkType]
        if isinstance(_network_type, Unset):
            network_type = UNSET
        else:
            network_type = GetNetworkMetadataResponse200NetworkType(_network_type)

        networks = []
        _networks = d.pop("networks", UNSET)
        for networks_item_data in _networks or []:
            networks_item = Network.from_dict(networks_item_data)

            networks.append(networks_item)

        nodes = []
        _nodes = d.pop("nodes", UNSET)
        for nodes_item_data in _nodes or []:
            nodes_item = Node.from_dict(nodes_item_data)

            nodes.append(nodes_item)

        warnings = cast(List[str], d.pop("warnings", UNSET))

        get_network_metadata_response_200 = cls(
            compound_queries_enabled=compound_queries_enabled,
            default_topology=default_topology,
            dpo_authorization_enabled=dpo_authorization_enabled,
            e_2_ee_enforced=e_2_ee_enforced,
            network_type=network_type,
            networks=networks,
            nodes=nodes,
            warnings=warnings,
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
