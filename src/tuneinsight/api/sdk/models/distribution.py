from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.distribution_availability_status import DistributionAvailabilityStatus
from ..models.distribution_type import DistributionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.distribution_bin import DistributionBin
    from ..models.terminology_field import TerminologyField


T = TypeVar("T", bound="Distribution")


@attr.s(auto_attribs=True)
class Distribution:
    """
    Attributes:
        availability_status (Union[Unset, DistributionAvailabilityStatus]): indicates whether distribution data is
            available or not.
        bins (Union[Unset, List['DistributionBin']]):
        description (Union[Unset, str]): Description of the distribution that will be displayed in the frontend.
        terminology (Union[Unset, TerminologyField]): Parameters that must be provided to schema fields when the field's
            values are terminology references.
        title (Union[Unset, str]): Title of the distribution that will be displayed in the frontend.
        type (Union[Unset, DistributionType]):
        unavailable_reason (Union[Unset, str]): reason for which distribution data is unavailable.
        x_unit (Union[Unset, str]): Displayed name of the unit of the x-axis when the distribution is shown on a chart.
        y_unit (Union[Unset, str]): Displayed name of the unit of the y-axis when the distribution is shown on a chart.
    """

    availability_status: Union[Unset, DistributionAvailabilityStatus] = UNSET
    bins: Union[Unset, List["DistributionBin"]] = UNSET
    description: Union[Unset, str] = UNSET
    terminology: Union[Unset, "TerminologyField"] = UNSET
    title: Union[Unset, str] = UNSET
    type: Union[Unset, DistributionType] = UNSET
    unavailable_reason: Union[Unset, str] = UNSET
    x_unit: Union[Unset, str] = UNSET
    y_unit: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        availability_status: Union[Unset, str] = UNSET
        if not isinstance(self.availability_status, Unset):
            availability_status = self.availability_status.value

        bins: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.bins, Unset):
            bins = []
            for bins_item_data in self.bins:
                bins_item = bins_item_data.to_dict()

                bins.append(bins_item)

        description = self.description
        terminology: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.terminology, Unset):
            terminology = self.terminology.to_dict()

        title = self.title
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        unavailable_reason = self.unavailable_reason
        x_unit = self.x_unit
        y_unit = self.y_unit

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if availability_status is not UNSET:
            field_dict["availabilityStatus"] = availability_status
        if bins is not UNSET:
            field_dict["bins"] = bins
        if description is not UNSET:
            field_dict["description"] = description
        if terminology is not UNSET:
            field_dict["terminology"] = terminology
        if title is not UNSET:
            field_dict["title"] = title
        if type is not UNSET:
            field_dict["type"] = type
        if unavailable_reason is not UNSET:
            field_dict["unavailableReason"] = unavailable_reason
        if x_unit is not UNSET:
            field_dict["xUnit"] = x_unit
        if y_unit is not UNSET:
            field_dict["yUnit"] = y_unit

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.distribution_bin import DistributionBin
        from ..models.terminology_field import TerminologyField

        d = src_dict.copy()
        _availability_status = d.pop("availabilityStatus", UNSET)
        availability_status: Union[Unset, DistributionAvailabilityStatus]
        if isinstance(_availability_status, Unset):
            availability_status = UNSET
        else:
            availability_status = DistributionAvailabilityStatus(_availability_status)

        bins = []
        _bins = d.pop("bins", UNSET)
        for bins_item_data in _bins or []:
            bins_item = DistributionBin.from_dict(bins_item_data)

            bins.append(bins_item)

        description = d.pop("description", UNSET)

        _terminology = d.pop("terminology", UNSET)
        terminology: Union[Unset, TerminologyField]
        if isinstance(_terminology, Unset):
            terminology = UNSET
        else:
            terminology = TerminologyField.from_dict(_terminology)

        title = d.pop("title", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, DistributionType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = DistributionType(_type)

        unavailable_reason = d.pop("unavailableReason", UNSET)

        x_unit = d.pop("xUnit", UNSET)

        y_unit = d.pop("yUnit", UNSET)

        distribution = cls(
            availability_status=availability_status,
            bins=bins,
            description=description,
            terminology=terminology,
            title=title,
            type=type,
            unavailable_reason=unavailable_reason,
            x_unit=x_unit,
            y_unit=y_unit,
        )

        distribution.additional_properties = d
        return distribution

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
