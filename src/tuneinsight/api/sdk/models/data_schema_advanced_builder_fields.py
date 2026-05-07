from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advanced_builder_field import AdvancedBuilderField


T = TypeVar("T", bound="DataSchemaAdvancedBuilderFields")


@attr.s(auto_attribs=True)
class DataSchemaAdvancedBuilderFields:
    """Predefined fields for advanced query builder parameters.

    Attributes:
        age (Union[Unset, AdvancedBuilderField]): Configuration for an advanced builder parameter field.
        birth_date (Union[Unset, AdvancedBuilderField]): Configuration for an advanced builder parameter field.
        care_site (Union[Unset, AdvancedBuilderField]): Configuration for an advanced builder parameter field.
        gender (Union[Unset, AdvancedBuilderField]): Configuration for an advanced builder parameter field.
        visit_date (Union[Unset, AdvancedBuilderField]): Configuration for an advanced builder parameter field.
        vital_status (Union[Unset, AdvancedBuilderField]): Configuration for an advanced builder parameter field.
    """

    age: Union[Unset, "AdvancedBuilderField"] = UNSET
    birth_date: Union[Unset, "AdvancedBuilderField"] = UNSET
    care_site: Union[Unset, "AdvancedBuilderField"] = UNSET
    gender: Union[Unset, "AdvancedBuilderField"] = UNSET
    visit_date: Union[Unset, "AdvancedBuilderField"] = UNSET
    vital_status: Union[Unset, "AdvancedBuilderField"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        age: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.age, Unset):
            age = self.age.to_dict()

        birth_date: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.birth_date, Unset):
            birth_date = self.birth_date.to_dict()

        care_site: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.care_site, Unset):
            care_site = self.care_site.to_dict()

        gender: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.gender, Unset):
            gender = self.gender.to_dict()

        visit_date: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.visit_date, Unset):
            visit_date = self.visit_date.to_dict()

        vital_status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.vital_status, Unset):
            vital_status = self.vital_status.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if age is not UNSET:
            field_dict["age"] = age
        if birth_date is not UNSET:
            field_dict["birthDate"] = birth_date
        if care_site is not UNSET:
            field_dict["careSite"] = care_site
        if gender is not UNSET:
            field_dict["gender"] = gender
        if visit_date is not UNSET:
            field_dict["visitDate"] = visit_date
        if vital_status is not UNSET:
            field_dict["vitalStatus"] = vital_status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.advanced_builder_field import AdvancedBuilderField

        d = src_dict.copy()
        _age = d.pop("age", UNSET)
        age: Union[Unset, AdvancedBuilderField]
        if isinstance(_age, Unset):
            age = UNSET
        else:
            age = AdvancedBuilderField.from_dict(_age)

        _birth_date = d.pop("birthDate", UNSET)
        birth_date: Union[Unset, AdvancedBuilderField]
        if isinstance(_birth_date, Unset):
            birth_date = UNSET
        else:
            birth_date = AdvancedBuilderField.from_dict(_birth_date)

        _care_site = d.pop("careSite", UNSET)
        care_site: Union[Unset, AdvancedBuilderField]
        if isinstance(_care_site, Unset):
            care_site = UNSET
        else:
            care_site = AdvancedBuilderField.from_dict(_care_site)

        _gender = d.pop("gender", UNSET)
        gender: Union[Unset, AdvancedBuilderField]
        if isinstance(_gender, Unset):
            gender = UNSET
        else:
            gender = AdvancedBuilderField.from_dict(_gender)

        _visit_date = d.pop("visitDate", UNSET)
        visit_date: Union[Unset, AdvancedBuilderField]
        if isinstance(_visit_date, Unset):
            visit_date = UNSET
        else:
            visit_date = AdvancedBuilderField.from_dict(_visit_date)

        _vital_status = d.pop("vitalStatus", UNSET)
        vital_status: Union[Unset, AdvancedBuilderField]
        if isinstance(_vital_status, Unset):
            vital_status = UNSET
        else:
            vital_status = AdvancedBuilderField.from_dict(_vital_status)

        data_schema_advanced_builder_fields = cls(
            age=age,
            birth_date=birth_date,
            care_site=care_site,
            gender=gender,
            visit_date=visit_date,
            vital_status=vital_status,
        )

        data_schema_advanced_builder_fields.additional_properties = d
        return data_schema_advanced_builder_fields

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
