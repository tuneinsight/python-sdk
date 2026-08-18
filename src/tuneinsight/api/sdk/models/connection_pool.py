from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConnectionPool")


@attr.s(auto_attribs=True)
class ConnectionPool:
    """represents a database connection current status.

    Attributes:
        id (Union[Unset, str]): unique name of the connection pool or data source.
        idle_connections (Union[Unset, int]): number of idle connections.
        in_use_connections (Union[Unset, int]): number of in-use connections.
        max_connections (Union[Unset, int]): maximum number of connections configured on the pool.
        open_connections (Union[Unset, int]): number of open connections.
        used_at (Union[Unset, str]): last time the connection pool was used for querying.
        wait_count (Union[Unset, int]): number of processes waiting for a connection.
    """

    id: Union[Unset, str] = UNSET
    idle_connections: Union[Unset, int] = UNSET
    in_use_connections: Union[Unset, int] = UNSET
    max_connections: Union[Unset, int] = UNSET
    open_connections: Union[Unset, int] = UNSET
    used_at: Union[Unset, str] = UNSET
    wait_count: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        idle_connections = self.idle_connections
        in_use_connections = self.in_use_connections
        max_connections = self.max_connections
        open_connections = self.open_connections
        used_at = self.used_at
        wait_count = self.wait_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if idle_connections is not UNSET:
            field_dict["idleConnections"] = idle_connections
        if in_use_connections is not UNSET:
            field_dict["inUseConnections"] = in_use_connections
        if max_connections is not UNSET:
            field_dict["maxConnections"] = max_connections
        if open_connections is not UNSET:
            field_dict["openConnections"] = open_connections
        if used_at is not UNSET:
            field_dict["usedAt"] = used_at
        if wait_count is not UNSET:
            field_dict["waitCount"] = wait_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        idle_connections = d.pop("idleConnections", UNSET)

        in_use_connections = d.pop("inUseConnections", UNSET)

        max_connections = d.pop("maxConnections", UNSET)

        open_connections = d.pop("openConnections", UNSET)

        used_at = d.pop("usedAt", UNSET)

        wait_count = d.pop("waitCount", UNSET)

        connection_pool = cls(
            id=id,
            idle_connections=idle_connections,
            in_use_connections=in_use_connections,
            max_connections=max_connections,
            open_connections=open_connections,
            used_at=used_at,
            wait_count=wait_count,
        )

        connection_pool.additional_properties = d
        return connection_pool

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
