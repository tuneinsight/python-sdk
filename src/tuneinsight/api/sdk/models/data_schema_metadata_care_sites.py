from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advanced_builder_field import AdvancedBuilderField


T = TypeVar("T", bound="DataSchemaMetadataCareSites")


@attr.s(auto_attribs=True)
class DataSchemaMetadataCareSites:
    """information on fields related to care site metadata. Each field links to an optional care site attributes that can
    be retrieved from any table in the data source.

        Attributes:
            address (Union[Unset, AdvancedBuilderField]): Configuration for an advanced builder parameter field.
            city (Union[Unset, AdvancedBuilderField]): Configuration for an advanced builder parameter field.
            country (Union[Unset, AdvancedBuilderField]): Configuration for an advanced builder parameter field.
            district (Union[Unset, AdvancedBuilderField]): Configuration for an advanced builder parameter field.
            latitude (Union[Unset, AdvancedBuilderField]): Configuration for an advanced builder parameter field.
            locality (Union[Unset, AdvancedBuilderField]): Configuration for an advanced builder parameter field.
            longitude (Union[Unset, AdvancedBuilderField]): Configuration for an advanced builder parameter field.
            main_table (Union[Unset, str]): identifies the primary table in the schema which stores the care site
                information.
            name (Union[Unset, AdvancedBuilderField]): Configuration for an advanced builder parameter field.
            postal_code (Union[Unset, AdvancedBuilderField]): Configuration for an advanced builder parameter field.
            region (Union[Unset, AdvancedBuilderField]): Configuration for an advanced builder parameter field.
            type (Union[Unset, AdvancedBuilderField]): Configuration for an advanced builder parameter field.
    """

    address: Union[Unset, "AdvancedBuilderField"] = UNSET
    city: Union[Unset, "AdvancedBuilderField"] = UNSET
    country: Union[Unset, "AdvancedBuilderField"] = UNSET
    district: Union[Unset, "AdvancedBuilderField"] = UNSET
    latitude: Union[Unset, "AdvancedBuilderField"] = UNSET
    locality: Union[Unset, "AdvancedBuilderField"] = UNSET
    longitude: Union[Unset, "AdvancedBuilderField"] = UNSET
    main_table: Union[Unset, str] = UNSET
    name: Union[Unset, "AdvancedBuilderField"] = UNSET
    postal_code: Union[Unset, "AdvancedBuilderField"] = UNSET
    region: Union[Unset, "AdvancedBuilderField"] = UNSET
    type: Union[Unset, "AdvancedBuilderField"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        city: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.city, Unset):
            city = self.city.to_dict()

        country: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.country, Unset):
            country = self.country.to_dict()

        district: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.district, Unset):
            district = self.district.to_dict()

        latitude: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.latitude, Unset):
            latitude = self.latitude.to_dict()

        locality: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.locality, Unset):
            locality = self.locality.to_dict()

        longitude: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.longitude, Unset):
            longitude = self.longitude.to_dict()

        main_table = self.main_table
        name: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.to_dict()

        postal_code: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.postal_code, Unset):
            postal_code = self.postal_code.to_dict()

        region: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.region, Unset):
            region = self.region.to_dict()

        type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if city is not UNSET:
            field_dict["city"] = city
        if country is not UNSET:
            field_dict["country"] = country
        if district is not UNSET:
            field_dict["district"] = district
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if locality is not UNSET:
            field_dict["locality"] = locality
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if main_table is not UNSET:
            field_dict["mainTable"] = main_table
        if name is not UNSET:
            field_dict["name"] = name
        if postal_code is not UNSET:
            field_dict["postalCode"] = postal_code
        if region is not UNSET:
            field_dict["region"] = region
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.advanced_builder_field import AdvancedBuilderField

        d = src_dict.copy()
        _address = d.pop("address", UNSET)
        address: Union[Unset, AdvancedBuilderField]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = AdvancedBuilderField.from_dict(_address)

        _city = d.pop("city", UNSET)
        city: Union[Unset, AdvancedBuilderField]
        if isinstance(_city, Unset):
            city = UNSET
        else:
            city = AdvancedBuilderField.from_dict(_city)

        _country = d.pop("country", UNSET)
        country: Union[Unset, AdvancedBuilderField]
        if isinstance(_country, Unset):
            country = UNSET
        else:
            country = AdvancedBuilderField.from_dict(_country)

        _district = d.pop("district", UNSET)
        district: Union[Unset, AdvancedBuilderField]
        if isinstance(_district, Unset):
            district = UNSET
        else:
            district = AdvancedBuilderField.from_dict(_district)

        _latitude = d.pop("latitude", UNSET)
        latitude: Union[Unset, AdvancedBuilderField]
        if isinstance(_latitude, Unset):
            latitude = UNSET
        else:
            latitude = AdvancedBuilderField.from_dict(_latitude)

        _locality = d.pop("locality", UNSET)
        locality: Union[Unset, AdvancedBuilderField]
        if isinstance(_locality, Unset):
            locality = UNSET
        else:
            locality = AdvancedBuilderField.from_dict(_locality)

        _longitude = d.pop("longitude", UNSET)
        longitude: Union[Unset, AdvancedBuilderField]
        if isinstance(_longitude, Unset):
            longitude = UNSET
        else:
            longitude = AdvancedBuilderField.from_dict(_longitude)

        main_table = d.pop("mainTable", UNSET)

        _name = d.pop("name", UNSET)
        name: Union[Unset, AdvancedBuilderField]
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = AdvancedBuilderField.from_dict(_name)

        _postal_code = d.pop("postalCode", UNSET)
        postal_code: Union[Unset, AdvancedBuilderField]
        if isinstance(_postal_code, Unset):
            postal_code = UNSET
        else:
            postal_code = AdvancedBuilderField.from_dict(_postal_code)

        _region = d.pop("region", UNSET)
        region: Union[Unset, AdvancedBuilderField]
        if isinstance(_region, Unset):
            region = UNSET
        else:
            region = AdvancedBuilderField.from_dict(_region)

        _type = d.pop("type", UNSET)
        type: Union[Unset, AdvancedBuilderField]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = AdvancedBuilderField.from_dict(_type)

        data_schema_metadata_care_sites = cls(
            address=address,
            city=city,
            country=country,
            district=district,
            latitude=latitude,
            locality=locality,
            longitude=longitude,
            main_table=main_table,
            name=name,
            postal_code=postal_code,
            region=region,
            type=type,
        )

        data_schema_metadata_care_sites.additional_properties = d
        return data_schema_metadata_care_sites

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
