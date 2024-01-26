from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrganizationCoordinates")


@attr.s(auto_attribs=True)
class OrganizationCoordinates:
    """Coordinates of the organization. (Decimal degrees, WGS84)

    Attributes:
        longitude (Union[Unset, float]):
        latitude (Union[Unset, float]):
    """

    longitude: Union[Unset, float] = UNSET
    latitude: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        longitude = self.longitude
        latitude = self.latitude

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if latitude is not UNSET:
            field_dict["latitude"] = latitude

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        longitude = d.pop("longitude", UNSET)

        latitude = d.pop("latitude", UNSET)

        organization_coordinates = cls(
            longitude=longitude,
            latitude=latitude,
        )

        organization_coordinates.additional_properties = d
        return organization_coordinates

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
