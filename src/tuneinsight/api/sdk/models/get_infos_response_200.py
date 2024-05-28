from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetInfosResponse200")


@attr.s(auto_attribs=True)
class GetInfosResponse200:
    """
    Attributes:
        portal_status (Union[Unset, str]): Portal connectivity status
        version (Union[Unset, str]): Tune Insight instance version
        api_checksum (Union[Unset, str]): Checksum of the current version of the API.
        auth_status (Union[Unset, str]): Authentication provider connectivity status
    """

    portal_status: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    api_checksum: Union[Unset, str] = UNSET
    auth_status: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        portal_status = self.portal_status
        version = self.version
        api_checksum = self.api_checksum
        auth_status = self.auth_status

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if portal_status is not UNSET:
            field_dict["portalStatus"] = portal_status
        if version is not UNSET:
            field_dict["version"] = version
        if api_checksum is not UNSET:
            field_dict["APIChecksum"] = api_checksum
        if auth_status is not UNSET:
            field_dict["authStatus"] = auth_status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        portal_status = d.pop("portalStatus", UNSET)

        version = d.pop("version", UNSET)

        api_checksum = d.pop("APIChecksum", UNSET)

        auth_status = d.pop("authStatus", UNSET)

        get_infos_response_200 = cls(
            portal_status=portal_status,
            version=version,
            api_checksum=api_checksum,
            auth_status=auth_status,
        )

        get_infos_response_200.additional_properties = d
        return get_infos_response_200

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
