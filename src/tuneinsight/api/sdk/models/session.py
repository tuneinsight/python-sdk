from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Session")


@attr.s(auto_attribs=True)
class Session:
    """basic information about a session returned from POST/GET

    Attributes:
        collective_key (Union[Unset, str]): Unique identifier of a data object.
        id (Union[Unset, str]): Unique identifier of a session
        network_id (Union[Unset, str]): network of the session
        params (Union[Unset, str]): b64 encoded marshaled parameters
        scheme (Union[Unset, str]): cryptographic scheme used, comes from the cryptolib
    """

    collective_key: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    network_id: Union[Unset, str] = UNSET
    params: Union[Unset, str] = UNSET
    scheme: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        collective_key = self.collective_key
        id = self.id
        network_id = self.network_id
        params = self.params
        scheme = self.scheme

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if collective_key is not UNSET:
            field_dict["collectiveKey"] = collective_key
        if id is not UNSET:
            field_dict["id"] = id
        if network_id is not UNSET:
            field_dict["networkId"] = network_id
        if params is not UNSET:
            field_dict["params"] = params
        if scheme is not UNSET:
            field_dict["scheme"] = scheme

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        collective_key = d.pop("collectiveKey", UNSET)

        id = d.pop("id", UNSET)

        network_id = d.pop("networkId", UNSET)

        params = d.pop("params", UNSET)

        scheme = d.pop("scheme", UNSET)

        session = cls(
            collective_key=collective_key,
            id=id,
            network_id=network_id,
            params=params,
            scheme=scheme,
        )

        session.additional_properties = d
        return session

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
