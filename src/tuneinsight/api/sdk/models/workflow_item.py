from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workflow_item_data import WorkflowItemData
    from ..models.workflow_item_position import WorkflowItemPosition


T = TypeVar("T", bound="WorkflowItem")


@attr.s(auto_attribs=True)
class WorkflowItem:
    """
    Attributes:
        data (Union[Unset, WorkflowItemData]):
        id (Union[Unset, str]):
        position (Union[Unset, WorkflowItemPosition]):
        progress (Union[Unset, int]):
        source (Union[Unset, str]): not used - UI specific
        source_handle (Union[Unset, str]): not used - UI specific
        target (Union[Unset, str]): not used - UI specific
        target_handle (Union[Unset, str]): not used - UI specific
        type (Union[Unset, str]):
    """

    data: Union[Unset, "WorkflowItemData"] = UNSET
    id: Union[Unset, str] = UNSET
    position: Union[Unset, "WorkflowItemPosition"] = UNSET
    progress: Union[Unset, int] = UNSET
    source: Union[Unset, str] = UNSET
    source_handle: Union[Unset, str] = UNSET
    target: Union[Unset, str] = UNSET
    target_handle: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        id = self.id
        position: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.position, Unset):
            position = self.position.to_dict()

        progress = self.progress
        source = self.source
        source_handle = self.source_handle
        target = self.target
        target_handle = self.target_handle
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if id is not UNSET:
            field_dict["id"] = id
        if position is not UNSET:
            field_dict["position"] = position
        if progress is not UNSET:
            field_dict["progress"] = progress
        if source is not UNSET:
            field_dict["source"] = source
        if source_handle is not UNSET:
            field_dict["sourceHandle"] = source_handle
        if target is not UNSET:
            field_dict["target"] = target
        if target_handle is not UNSET:
            field_dict["targetHandle"] = target_handle
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.workflow_item_data import WorkflowItemData
        from ..models.workflow_item_position import WorkflowItemPosition

        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, WorkflowItemData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = WorkflowItemData.from_dict(_data)

        id = d.pop("id", UNSET)

        _position = d.pop("position", UNSET)
        position: Union[Unset, WorkflowItemPosition]
        if isinstance(_position, Unset):
            position = UNSET
        else:
            position = WorkflowItemPosition.from_dict(_position)

        progress = d.pop("progress", UNSET)

        source = d.pop("source", UNSET)

        source_handle = d.pop("sourceHandle", UNSET)

        target = d.pop("target", UNSET)

        target_handle = d.pop("targetHandle", UNSET)

        type = d.pop("type", UNSET)

        workflow_item = cls(
            data=data,
            id=id,
            position=position,
            progress=progress,
            source=source,
            source_handle=source_handle,
            target=target,
            target_handle=target_handle,
            type=type,
        )

        workflow_item.additional_properties = d
        return workflow_item

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
