from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.data_object_type import DataObjectType
from ..models.data_object_visibility_status import DataObjectVisibilityStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="DataObject")


@attr.s(auto_attribs=True)
class DataObject:
    """A data object definition.

    Attributes:
        byte_size (Union[Unset, int]): Total byteSize of the object uploaded through PUT method by chunks. This value is
            updated at each data chunk upload.
        encrypted (Union[Unset, bool]):
        has_data (Union[Unset, bool]): whether the dataobject's data has been set
        session_id (Union[Unset, str]): Unique identifier of a session
        shared (Union[Unset, bool]): whether the dataobject reference exists for other participants in the project.
        shared_id (Union[Unset, str]): Shared identifier of a data object.
        type (Union[Unset, DataObjectType]): type of the dataobject
        unique_id (Union[Unset, str]): Unique identifier of a data object.
        visibility_status (Union[Unset, DataObjectVisibilityStatus]): type of visibility set to the dataobject
    """

    byte_size: Union[Unset, int] = UNSET
    encrypted: Union[Unset, bool] = UNSET
    has_data: Union[Unset, bool] = UNSET
    session_id: Union[Unset, str] = UNSET
    shared: Union[Unset, bool] = UNSET
    shared_id: Union[Unset, str] = UNSET
    type: Union[Unset, DataObjectType] = UNSET
    unique_id: Union[Unset, str] = UNSET
    visibility_status: Union[Unset, DataObjectVisibilityStatus] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        byte_size = self.byte_size
        encrypted = self.encrypted
        has_data = self.has_data
        session_id = self.session_id
        shared = self.shared
        shared_id = self.shared_id
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        unique_id = self.unique_id
        visibility_status: Union[Unset, str] = UNSET
        if not isinstance(self.visibility_status, Unset):
            visibility_status = self.visibility_status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if byte_size is not UNSET:
            field_dict["byteSize"] = byte_size
        if encrypted is not UNSET:
            field_dict["encrypted"] = encrypted
        if has_data is not UNSET:
            field_dict["hasData"] = has_data
        if session_id is not UNSET:
            field_dict["sessionId"] = session_id
        if shared is not UNSET:
            field_dict["shared"] = shared
        if shared_id is not UNSET:
            field_dict["sharedId"] = shared_id
        if type is not UNSET:
            field_dict["type"] = type
        if unique_id is not UNSET:
            field_dict["uniqueId"] = unique_id
        if visibility_status is not UNSET:
            field_dict["visibilityStatus"] = visibility_status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        byte_size = d.pop("byteSize", UNSET)

        encrypted = d.pop("encrypted", UNSET)

        has_data = d.pop("hasData", UNSET)

        session_id = d.pop("sessionId", UNSET)

        shared = d.pop("shared", UNSET)

        shared_id = d.pop("sharedId", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, DataObjectType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = DataObjectType(_type)

        unique_id = d.pop("uniqueId", UNSET)

        _visibility_status = d.pop("visibilityStatus", UNSET)
        visibility_status: Union[Unset, DataObjectVisibilityStatus]
        if isinstance(_visibility_status, Unset):
            visibility_status = UNSET
        else:
            visibility_status = DataObjectVisibilityStatus(_visibility_status)

        data_object = cls(
            byte_size=byte_size,
            encrypted=encrypted,
            has_data=has_data,
            session_id=session_id,
            shared=shared,
            shared_id=shared_id,
            type=type,
            unique_id=unique_id,
            visibility_status=visibility_status,
        )

        data_object.additional_properties = d
        return data_object

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
