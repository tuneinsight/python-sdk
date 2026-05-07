from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.term_occurrence import TermOccurrence


T = TypeVar("T", bound="CareSite")


@attr.s(auto_attribs=True)
class CareSite:
    """Metadata/address about a care site or medical center.

    Attributes:
        address (Union[Unset, str]): address line containing the street name and number etc.
        city (Union[Unset, str]): City or urban area in which the care site is physically located. Often overlaps with
            `locality`.
        country (Union[Unset, str]): Country in which the care site is located (ISO 3166-1 alpha-2 recommended, e.g.,
            FR, CH, US).
        data_source_id (Union[Unset, str]): data source id this care site was retrieved from.
        district (Union[Unset, str]): Represents the second-level administrative division within a country.
            Examples by country:
            - FR: Département
            - CH: District
            - US: County
            - UK: County or Unitary Authority
            - DE: Landkreis / Kreis
        global_catalog (Union[Unset, TermOccurrence]): Represents a number of occurrences of a term in a data source.
            More specifically, given a specific term from an ontology, this object
            stores the number of patients that have at least one record referencing this term in the data source.
            Moreover, this object also stores other useful metadata and statistics about the term.
        latitude (Union[Unset, float]): latitude of the care site.
        locality (Union[Unset, str]): Represents the third-level administrative division within a country.
            Examples by country:
            - FR: Commune
            - CH: Municipality
            - US: City/town
            - UK: Town / Borough
            - DE: Municipality
        longitude (Union[Unset, float]): longitude of the care site.
        name (Union[Unset, str]): Name of the care site and primary identifier used in the catalog.
        postal_code (Union[Unset, str]): Postal or ZIP code of the care site. Often used for validation and quick
            geographic filtering.
        refreshed_at (Union[Unset, str]): the time at which this care site was updated/retrieved from the data source on
            the instance that built the catalog.
        region (Union[Unset, str]): Represents the first-level administrative division within a country.
            Examples by country:
            - FR, UK, DE: Region
            - CH: Canton
            - US: State
        remote_instance (Union[Unset, str]): remote instance this care site was retrieved from.
        type (Union[Unset, str]): Optional type given to the care site (e.g., hospital, clinic, laboratory).
    """

    address: Union[Unset, str] = UNSET
    city: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    data_source_id: Union[Unset, str] = UNSET
    district: Union[Unset, str] = UNSET
    global_catalog: Union[Unset, "TermOccurrence"] = UNSET
    latitude: Union[Unset, float] = UNSET
    locality: Union[Unset, str] = UNSET
    longitude: Union[Unset, float] = UNSET
    name: Union[Unset, str] = UNSET
    postal_code: Union[Unset, str] = UNSET
    refreshed_at: Union[Unset, str] = UNSET
    region: Union[Unset, str] = UNSET
    remote_instance: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        address = self.address
        city = self.city
        country = self.country
        data_source_id = self.data_source_id
        district = self.district
        global_catalog: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.global_catalog, Unset):
            global_catalog = self.global_catalog.to_dict()

        latitude = self.latitude
        locality = self.locality
        longitude = self.longitude
        name = self.name
        postal_code = self.postal_code
        refreshed_at = self.refreshed_at
        region = self.region
        remote_instance = self.remote_instance
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if city is not UNSET:
            field_dict["city"] = city
        if country is not UNSET:
            field_dict["country"] = country
        if data_source_id is not UNSET:
            field_dict["dataSourceId"] = data_source_id
        if district is not UNSET:
            field_dict["district"] = district
        if global_catalog is not UNSET:
            field_dict["globalCatalog"] = global_catalog
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if locality is not UNSET:
            field_dict["locality"] = locality
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if name is not UNSET:
            field_dict["name"] = name
        if postal_code is not UNSET:
            field_dict["postalCode"] = postal_code
        if refreshed_at is not UNSET:
            field_dict["refreshedAt"] = refreshed_at
        if region is not UNSET:
            field_dict["region"] = region
        if remote_instance is not UNSET:
            field_dict["remoteInstance"] = remote_instance
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.term_occurrence import TermOccurrence

        d = src_dict.copy()
        address = d.pop("address", UNSET)

        city = d.pop("city", UNSET)

        country = d.pop("country", UNSET)

        data_source_id = d.pop("dataSourceId", UNSET)

        district = d.pop("district", UNSET)

        _global_catalog = d.pop("globalCatalog", UNSET)
        global_catalog: Union[Unset, TermOccurrence]
        if isinstance(_global_catalog, Unset):
            global_catalog = UNSET
        else:
            global_catalog = TermOccurrence.from_dict(_global_catalog)

        latitude = d.pop("latitude", UNSET)

        locality = d.pop("locality", UNSET)

        longitude = d.pop("longitude", UNSET)

        name = d.pop("name", UNSET)

        postal_code = d.pop("postalCode", UNSET)

        refreshed_at = d.pop("refreshedAt", UNSET)

        region = d.pop("region", UNSET)

        remote_instance = d.pop("remoteInstance", UNSET)

        type = d.pop("type", UNSET)

        care_site = cls(
            address=address,
            city=city,
            country=country,
            data_source_id=data_source_id,
            district=district,
            global_catalog=global_catalog,
            latitude=latitude,
            locality=locality,
            longitude=longitude,
            name=name,
            postal_code=postal_code,
            refreshed_at=refreshed_at,
            region=region,
            remote_instance=remote_instance,
            type=type,
        )

        care_site.additional_properties = d
        return care_site

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
