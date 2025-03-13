from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="DummySimulatedStagesItem")


@attr.s(auto_attribs=True)
class DummySimulatedStagesItem:
    """
    Attributes:
        name (Union[Unset, str]): name of the stage
        steps (Union[Unset, int]): number of steps in the stage.
        time_milliseconds (Union[Unset, int]): simulated sleep time in milliseconds (for the whole stage or per step if
            steps > 1)
    """

    name: Union[Unset, str] = UNSET
    steps: Union[Unset, int] = UNSET
    time_milliseconds: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        steps = self.steps
        time_milliseconds = self.time_milliseconds

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if steps is not UNSET:
            field_dict["steps"] = steps
        if time_milliseconds is not UNSET:
            field_dict["timeMilliseconds"] = time_milliseconds

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        steps = d.pop("steps", UNSET)

        time_milliseconds = d.pop("timeMilliseconds", UNSET)

        dummy_simulated_stages_item = cls(
            name=name,
            steps=steps,
            time_milliseconds=time_milliseconds,
        )

        dummy_simulated_stages_item.additional_properties = d
        return dummy_simulated_stages_item

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
