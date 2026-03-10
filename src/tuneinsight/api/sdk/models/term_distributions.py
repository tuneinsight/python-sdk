from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.distribution import Distribution


T = TypeVar("T", bound="TermDistributions")


@attr.s(auto_attribs=True)
class TermDistributions:
    """
    Attributes:
        age (Union[Unset, Distribution]):
        gender (Union[Unset, Distribution]):
        vital_status (Union[Unset, Distribution]):
        year (Union[Unset, Distribution]):
    """

    age: Union[Unset, "Distribution"] = UNSET
    gender: Union[Unset, "Distribution"] = UNSET
    vital_status: Union[Unset, "Distribution"] = UNSET
    year: Union[Unset, "Distribution"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        age: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.age, Unset):
            age = self.age.to_dict()

        gender: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.gender, Unset):
            gender = self.gender.to_dict()

        vital_status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.vital_status, Unset):
            vital_status = self.vital_status.to_dict()

        year: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.year, Unset):
            year = self.year.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if age is not UNSET:
            field_dict["age"] = age
        if gender is not UNSET:
            field_dict["gender"] = gender
        if vital_status is not UNSET:
            field_dict["vitalStatus"] = vital_status
        if year is not UNSET:
            field_dict["year"] = year

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.distribution import Distribution

        d = src_dict.copy()
        _age = d.pop("age", UNSET)
        age: Union[Unset, Distribution]
        if isinstance(_age, Unset):
            age = UNSET
        else:
            age = Distribution.from_dict(_age)

        _gender = d.pop("gender", UNSET)
        gender: Union[Unset, Distribution]
        if isinstance(_gender, Unset):
            gender = UNSET
        else:
            gender = Distribution.from_dict(_gender)

        _vital_status = d.pop("vitalStatus", UNSET)
        vital_status: Union[Unset, Distribution]
        if isinstance(_vital_status, Unset):
            vital_status = UNSET
        else:
            vital_status = Distribution.from_dict(_vital_status)

        _year = d.pop("year", UNSET)
        year: Union[Unset, Distribution]
        if isinstance(_year, Unset):
            year = UNSET
        else:
            year = Distribution.from_dict(_year)

        term_distributions = cls(
            age=age,
            gender=gender,
            vital_status=vital_status,
            year=year,
        )

        term_distributions.additional_properties = d
        return term_distributions

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
