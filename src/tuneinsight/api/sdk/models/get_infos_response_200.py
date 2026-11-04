from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.get_infos_response_200_andor_status import GetInfosResponse200AndorStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_infos_response_200_catalog_status import GetInfosResponse200CatalogStatus


T = TypeVar("T", bound="GetInfosResponse200")


@attr.s(auto_attribs=True)
class GetInfosResponse200:
    """
    Attributes:
        api_checksum (Union[Unset, str]): Checksum of the current version of the API.
        accepted_groups (Union[Unset, List[str]]): List of user groups that this instance accepts (users are treated as
            local)
        andor_status (Union[Unset, GetInfosResponse200AndorStatus]): ANDOR reachability status (ok or nok). Only present
            when an ANDOR URL is configured. Connection failures and HTTP 5xx responses report nok; other HTTP responses
            report ok without verifying authentication.
        auth_status (Union[Unset, str]): Authentication provider connectivity status
        build_version (Union[Unset, str]): Tune Insight build version
        catalog_status (Union[Unset, GetInfosResponse200CatalogStatus]): Status of the node's catalog
        maintenance_mode (Union[Unset, bool]): whether the instance is in maintenance mode (only GET and admin endpoints
            enabled).
        portal_status (Union[Unset, str]): Portal connectivity status
        push_catalog_enabled (Union[Unset, bool]): whether the instance has enabled the option to push the catalog to
            the portal.
        service_account (Union[Unset, str]): name of the service account used by this instance when sending requests to
            other instances.
        startup_status (Union[Unset, str]): Reports the startup process status.
        terminology_version (Union[Unset, str]): Instance version when the ontologies were last updated.
        version (Union[Unset, str]): Tune Insight instance version
    """

    api_checksum: Union[Unset, str] = UNSET
    accepted_groups: Union[Unset, List[str]] = UNSET
    andor_status: Union[Unset, GetInfosResponse200AndorStatus] = UNSET
    auth_status: Union[Unset, str] = UNSET
    build_version: Union[Unset, str] = UNSET
    catalog_status: Union[Unset, "GetInfosResponse200CatalogStatus"] = UNSET
    maintenance_mode: Union[Unset, bool] = UNSET
    portal_status: Union[Unset, str] = UNSET
    push_catalog_enabled: Union[Unset, bool] = UNSET
    service_account: Union[Unset, str] = UNSET
    startup_status: Union[Unset, str] = UNSET
    terminology_version: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        api_checksum = self.api_checksum
        accepted_groups: Union[Unset, List[str]] = UNSET
        if not isinstance(self.accepted_groups, Unset):
            accepted_groups = self.accepted_groups

        andor_status: Union[Unset, str] = UNSET
        if not isinstance(self.andor_status, Unset):
            andor_status = self.andor_status.value

        auth_status = self.auth_status
        build_version = self.build_version
        catalog_status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.catalog_status, Unset):
            catalog_status = self.catalog_status.to_dict()

        maintenance_mode = self.maintenance_mode
        portal_status = self.portal_status
        push_catalog_enabled = self.push_catalog_enabled
        service_account = self.service_account
        startup_status = self.startup_status
        terminology_version = self.terminology_version
        version = self.version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if api_checksum is not UNSET:
            field_dict["APIChecksum"] = api_checksum
        if accepted_groups is not UNSET:
            field_dict["acceptedGroups"] = accepted_groups
        if andor_status is not UNSET:
            field_dict["andorStatus"] = andor_status
        if auth_status is not UNSET:
            field_dict["authStatus"] = auth_status
        if build_version is not UNSET:
            field_dict["buildVersion"] = build_version
        if catalog_status is not UNSET:
            field_dict["catalogStatus"] = catalog_status
        if maintenance_mode is not UNSET:
            field_dict["maintenanceMode"] = maintenance_mode
        if portal_status is not UNSET:
            field_dict["portalStatus"] = portal_status
        if push_catalog_enabled is not UNSET:
            field_dict["pushCatalogEnabled"] = push_catalog_enabled
        if service_account is not UNSET:
            field_dict["serviceAccount"] = service_account
        if startup_status is not UNSET:
            field_dict["startupStatus"] = startup_status
        if terminology_version is not UNSET:
            field_dict["terminologyVersion"] = terminology_version
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_infos_response_200_catalog_status import GetInfosResponse200CatalogStatus

        d = src_dict.copy()
        api_checksum = d.pop("APIChecksum", UNSET)

        accepted_groups = cast(List[str], d.pop("acceptedGroups", UNSET))

        _andor_status = d.pop("andorStatus", UNSET)
        andor_status: Union[Unset, GetInfosResponse200AndorStatus]
        if isinstance(_andor_status, Unset):
            andor_status = UNSET
        else:
            andor_status = GetInfosResponse200AndorStatus(_andor_status)

        auth_status = d.pop("authStatus", UNSET)

        build_version = d.pop("buildVersion", UNSET)

        _catalog_status = d.pop("catalogStatus", UNSET)
        catalog_status: Union[Unset, GetInfosResponse200CatalogStatus]
        if isinstance(_catalog_status, Unset):
            catalog_status = UNSET
        else:
            catalog_status = GetInfosResponse200CatalogStatus.from_dict(_catalog_status)

        maintenance_mode = d.pop("maintenanceMode", UNSET)

        portal_status = d.pop("portalStatus", UNSET)

        push_catalog_enabled = d.pop("pushCatalogEnabled", UNSET)

        service_account = d.pop("serviceAccount", UNSET)

        startup_status = d.pop("startupStatus", UNSET)

        terminology_version = d.pop("terminologyVersion", UNSET)

        version = d.pop("version", UNSET)

        get_infos_response_200 = cls(
            api_checksum=api_checksum,
            accepted_groups=accepted_groups,
            andor_status=andor_status,
            auth_status=auth_status,
            build_version=build_version,
            catalog_status=catalog_status,
            maintenance_mode=maintenance_mode,
            portal_status=portal_status,
            push_catalog_enabled=push_catalog_enabled,
            service_account=service_account,
            startup_status=startup_status,
            terminology_version=terminology_version,
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
