from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.authorization_status import AuthorizationStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.organization_coordinates import OrganizationCoordinates


T = TypeVar("T", bound="Organization")


@attr.s(auto_attribs=True)
class Organization:
    """Organization taking part in a project

    Attributes:
        authorization_status (Union[Unset, AuthorizationStatus]): Authorization status of the project
        coordinates (Union[Unset, OrganizationCoordinates]): Coordinates of the organization. (Decimal degrees, WGS84)
        country (Union[Unset, str]): Country code of the organization. (Lower case two-letter ISO 3166-1 alpha-2)
        data_officer (Union[Unset, str]): Name of the data officer in charge in the organization
        group (Union[Unset, str]): Name of the corresponding keycloak group
        name (Union[Unset, str]): Name of the organization
    """

    authorization_status: Union[Unset, AuthorizationStatus] = UNSET
    coordinates: Union[Unset, "OrganizationCoordinates"] = UNSET
    country: Union[Unset, str] = UNSET
    data_officer: Union[Unset, str] = UNSET
    group: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        authorization_status: Union[Unset, str] = UNSET
        if not isinstance(self.authorization_status, Unset):
            authorization_status = self.authorization_status.value

        coordinates: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.coordinates, Unset):
            coordinates = self.coordinates.to_dict()

        country = self.country
        data_officer = self.data_officer
        group = self.group
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if authorization_status is not UNSET:
            field_dict["authorizationStatus"] = authorization_status
        if coordinates is not UNSET:
            field_dict["coordinates"] = coordinates
        if country is not UNSET:
            field_dict["country"] = country
        if data_officer is not UNSET:
            field_dict["dataOfficer"] = data_officer
        if group is not UNSET:
            field_dict["group"] = group
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.organization_coordinates import OrganizationCoordinates

        d = src_dict.copy()
        _authorization_status = d.pop("authorizationStatus", UNSET)
        authorization_status: Union[Unset, AuthorizationStatus]
        if isinstance(_authorization_status, Unset):
            authorization_status = UNSET
        else:
            authorization_status = AuthorizationStatus(_authorization_status)

        _coordinates = d.pop("coordinates", UNSET)
        coordinates: Union[Unset, OrganizationCoordinates]
        if isinstance(_coordinates, Unset):
            coordinates = UNSET
        else:
            coordinates = OrganizationCoordinates.from_dict(_coordinates)

        country = d.pop("country", UNSET)

        data_officer = d.pop("dataOfficer", UNSET)

        group = d.pop("group", UNSET)

        name = d.pop("name", UNSET)

        organization = cls(
            authorization_status=authorization_status,
            coordinates=coordinates,
            country=country,
            data_officer=data_officer,
            group=group,
            name=name,
        )

        organization.additional_properties = d
        return organization

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
