import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.notification_type import NotificationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Notification")


@attr.s(auto_attribs=True)
class Notification:
    """represents a user notification.

    Attributes:
        archived (Union[Unset, bool]): whether the notification has been archived.
        content (Union[Unset, str]): content of the notification.
        created_at (Union[Unset, datetime.datetime]): time at which the notification was issued.
        id (Union[Unset, str]): id of the notification.
        link_title (Union[Unset, str]): name of the button used to access the navigation link.
        nav_link (Union[Unset, str]): optional UI navigation link to access the relevant page from the notification
        project_id (Union[Unset, str]): Unique identifier of a project.
        read (Union[Unset, bool]): whether the notification has been read.
        title (Union[Unset, str]): title of the notification.
        type (Union[Unset, NotificationType]):
    """

    archived: Union[Unset, bool] = UNSET
    content: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    id: Union[Unset, str] = UNSET
    link_title: Union[Unset, str] = UNSET
    nav_link: Union[Unset, str] = UNSET
    project_id: Union[Unset, str] = UNSET
    read: Union[Unset, bool] = UNSET
    title: Union[Unset, str] = UNSET
    type: Union[Unset, NotificationType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        archived = self.archived
        content = self.content
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        id = self.id
        link_title = self.link_title
        nav_link = self.nav_link
        project_id = self.project_id
        read = self.read
        title = self.title
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if archived is not UNSET:
            field_dict["archived"] = archived
        if content is not UNSET:
            field_dict["content"] = content
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if id is not UNSET:
            field_dict["id"] = id
        if link_title is not UNSET:
            field_dict["linkTitle"] = link_title
        if nav_link is not UNSET:
            field_dict["navLink"] = nav_link
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if read is not UNSET:
            field_dict["read"] = read
        if title is not UNSET:
            field_dict["title"] = title
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        archived = d.pop("archived", UNSET)

        content = d.pop("content", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        id = d.pop("id", UNSET)

        link_title = d.pop("linkTitle", UNSET)

        nav_link = d.pop("navLink", UNSET)

        project_id = d.pop("projectId", UNSET)

        read = d.pop("read", UNSET)

        title = d.pop("title", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, NotificationType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = NotificationType(_type)

        notification = cls(
            archived=archived,
            content=content,
            created_at=created_at,
            id=id,
            link_title=link_title,
            nav_link=nav_link,
            project_id=project_id,
            read=read,
            title=title,
            type=type,
        )

        notification.additional_properties = d
        return notification

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
