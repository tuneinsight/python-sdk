from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.privacy_warning_severity import PrivacyWarningSeverity
from ..types import UNSET, Unset

T = TypeVar("T", bound="PrivacyWarning")


@attr.s(auto_attribs=True)
class PrivacyWarning:
    """description of a potential privacy risk in the configuration of a project.

    Attributes:
        description (Union[Unset, str]): What is the privacy risk.
        severity (Union[Unset, PrivacyWarningSeverity]): How severe is the privacy risk.
    """

    description: Union[Unset, str] = UNSET
    severity: Union[Unset, PrivacyWarningSeverity] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        severity: Union[Unset, str] = UNSET
        if not isinstance(self.severity, Unset):
            severity = self.severity.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if severity is not UNSET:
            field_dict["severity"] = severity

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description", UNSET)

        _severity = d.pop("severity", UNSET)
        severity: Union[Unset, PrivacyWarningSeverity]
        if isinstance(_severity, Unset):
            severity = UNSET
        else:
            severity = PrivacyWarningSeverity(_severity)

        privacy_warning = cls(
            description=description,
            severity=severity,
        )

        privacy_warning.additional_properties = d
        return privacy_warning

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
