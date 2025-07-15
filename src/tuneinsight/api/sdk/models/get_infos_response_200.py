from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetInfosResponse200")


@attr.s(auto_attribs=True)
class GetInfosResponse200:
    """
    Attributes:
        api_checksum (Union[Unset, str]): Checksum of the current version of the API.
        accepted_groups (Union[Unset, List[str]]): List of user groups that this instance accepts (users are treated as
            local)
        auth_status (Union[Unset, str]): Authentication provider connectivity status
        build_version (Union[Unset, str]): Tune Insight build version
        portal_status (Union[Unset, str]): Portal connectivity status
        service_account (Union[Unset, str]): name of the service account used by this instance when sending requests to
            other instances.
        startup_status (Union[Unset, str]): Reports the startup process status.
        version (Union[Unset, str]): Tune Insight instance version
    """

    api_checksum: Union[Unset, str] = UNSET
    accepted_groups: Union[Unset, List[str]] = UNSET
    auth_status: Union[Unset, str] = UNSET
    build_version: Union[Unset, str] = UNSET
    portal_status: Union[Unset, str] = UNSET
    service_account: Union[Unset, str] = UNSET
    startup_status: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        api_checksum = self.api_checksum
        accepted_groups: Union[Unset, List[str]] = UNSET
        if not isinstance(self.accepted_groups, Unset):
            accepted_groups = self.accepted_groups

        auth_status = self.auth_status
        build_version = self.build_version
        portal_status = self.portal_status
        service_account = self.service_account
        startup_status = self.startup_status
        version = self.version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if api_checksum is not UNSET:
            field_dict["APIChecksum"] = api_checksum
        if accepted_groups is not UNSET:
            field_dict["acceptedGroups"] = accepted_groups
        if auth_status is not UNSET:
            field_dict["authStatus"] = auth_status
        if build_version is not UNSET:
            field_dict["buildVersion"] = build_version
        if portal_status is not UNSET:
            field_dict["portalStatus"] = portal_status
        if service_account is not UNSET:
            field_dict["serviceAccount"] = service_account
        if startup_status is not UNSET:
            field_dict["startupStatus"] = startup_status
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        api_checksum = d.pop("APIChecksum", UNSET)

        accepted_groups = cast(List[str], d.pop("acceptedGroups", UNSET))

        auth_status = d.pop("authStatus", UNSET)

        build_version = d.pop("buildVersion", UNSET)

        portal_status = d.pop("portalStatus", UNSET)

        service_account = d.pop("serviceAccount", UNSET)

        startup_status = d.pop("startupStatus", UNSET)

        version = d.pop("version", UNSET)

        get_infos_response_200 = cls(
            api_checksum=api_checksum,
            accepted_groups=accepted_groups,
            auth_status=auth_status,
            build_version=build_version,
            portal_status=portal_status,
            service_account=service_account,
            startup_status=startup_status,
            version=version,
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
