from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.death_config import DeathConfig
    from ..models.individual_notification_config import IndividualNotificationConfig
    from ..models.last_planned_stay_config import LastPlannedStayConfig
    from ..models.opposition_config import OppositionConfig


T = TypeVar("T", bound="PatientNotificationFields")


@attr.s(auto_attribs=True)
class PatientNotificationFields:
    """Groups the table configurations used to select patients eligible for individual notification.

    Attributes:
        death (Union[Unset, DeathConfig]): Identifies the table recording patient deaths. Deceased patients are excluded
            from individual notification.
        individual_notification (Union[Unset, IndividualNotificationConfig]): Identifies the table recording individual
            patient notification.
        last_planned_stay (Union[Unset, LastPlannedStayConfig]): Identifies the table last planned stay of patients at
            care sites.
        opposition (Union[Unset, OppositionConfig]): Identifies the table recording patient oppositions to data
            processing.
    """

    death: Union[Unset, "DeathConfig"] = UNSET
    individual_notification: Union[Unset, "IndividualNotificationConfig"] = UNSET
    last_planned_stay: Union[Unset, "LastPlannedStayConfig"] = UNSET
    opposition: Union[Unset, "OppositionConfig"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        death: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.death, Unset):
            death = self.death.to_dict()

        individual_notification: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.individual_notification, Unset):
            individual_notification = self.individual_notification.to_dict()

        last_planned_stay: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.last_planned_stay, Unset):
            last_planned_stay = self.last_planned_stay.to_dict()

        opposition: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.opposition, Unset):
            opposition = self.opposition.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if death is not UNSET:
            field_dict["death"] = death
        if individual_notification is not UNSET:
            field_dict["individualNotification"] = individual_notification
        if last_planned_stay is not UNSET:
            field_dict["lastPlannedStay"] = last_planned_stay
        if opposition is not UNSET:
            field_dict["opposition"] = opposition

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.death_config import DeathConfig
        from ..models.individual_notification_config import IndividualNotificationConfig
        from ..models.last_planned_stay_config import LastPlannedStayConfig
        from ..models.opposition_config import OppositionConfig

        d = src_dict.copy()
        _death = d.pop("death", UNSET)
        death: Union[Unset, DeathConfig]
        if isinstance(_death, Unset):
            death = UNSET
        else:
            death = DeathConfig.from_dict(_death)

        _individual_notification = d.pop("individualNotification", UNSET)
        individual_notification: Union[Unset, IndividualNotificationConfig]
        if isinstance(_individual_notification, Unset):
            individual_notification = UNSET
        else:
            individual_notification = IndividualNotificationConfig.from_dict(_individual_notification)

        _last_planned_stay = d.pop("lastPlannedStay", UNSET)
        last_planned_stay: Union[Unset, LastPlannedStayConfig]
        if isinstance(_last_planned_stay, Unset):
            last_planned_stay = UNSET
        else:
            last_planned_stay = LastPlannedStayConfig.from_dict(_last_planned_stay)

        _opposition = d.pop("opposition", UNSET)
        opposition: Union[Unset, OppositionConfig]
        if isinstance(_opposition, Unset):
            opposition = UNSET
        else:
            opposition = OppositionConfig.from_dict(_opposition)

        patient_notification_fields = cls(
            death=death,
            individual_notification=individual_notification,
            last_planned_stay=last_planned_stay,
            opposition=opposition,
        )

        patient_notification_fields.additional_properties = d
        return patient_notification_fields

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
