from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.duration import Duration


T = TypeVar("T", bound="InputTransformation")


@attr.s(auto_attribs=True)
class InputTransformation:
    """Transformation applied to a value extracted from the data as part of a TIQL query, before
    it is used in a filter.

        Attributes:
            time_offset (Union[Unset, Duration]): definition of a date-independent time interval
    """

    time_offset: Union[Unset, "Duration"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        time_offset: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.time_offset, Unset):
            time_offset = self.time_offset.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if time_offset is not UNSET:
            field_dict["timeOffset"] = time_offset

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.duration import Duration

        d = src_dict.copy()
        _time_offset = d.pop("timeOffset", UNSET)
        time_offset: Union[Unset, Duration]
        if isinstance(_time_offset, Unset):
            time_offset = UNSET
        else:
            time_offset = Duration.from_dict(_time_offset)

        input_transformation = cls(
            time_offset=time_offset,
        )

        input_transformation.additional_properties = d
        return input_transformation

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
