from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectStepItem")


@attr.s(auto_attribs=True)
class ProjectStepItem:
    """Representation of a step of the project mapped from the workflow UI

    Attributes:
        box_id (Union[Unset, str]): ID of the workflow Item in the frontend
        error (Union[Unset, str]):
        id (Union[Unset, str]):
        progress (Union[Unset, int]):
        type (Union[Unset, str]):
    """

    box_id: Union[Unset, str] = UNSET
    error: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    progress: Union[Unset, int] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        box_id = self.box_id
        error = self.error
        id = self.id
        progress = self.progress
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if box_id is not UNSET:
            field_dict["boxID"] = box_id
        if error is not UNSET:
            field_dict["error"] = error
        if id is not UNSET:
            field_dict["id"] = id
        if progress is not UNSET:
            field_dict["progress"] = progress
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        box_id = d.pop("boxID", UNSET)

        error = d.pop("error", UNSET)

        id = d.pop("id", UNSET)

        progress = d.pop("progress", UNSET)

        type = d.pop("type", UNSET)

        project_step_item = cls(
            box_id=box_id,
            error=error,
            id=id,
            progress=progress,
            type=type,
        )

        project_step_item.additional_properties = d
        return project_step_item

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
