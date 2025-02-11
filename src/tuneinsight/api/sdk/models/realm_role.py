from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RealmRole")


@attr.s(auto_attribs=True)
class RealmRole:
    """
    Attributes:
        client_role (Union[Unset, bool]):
        composite (Union[Unset, bool]):
        container_id (Union[Unset, str]):
        description (Union[Unset, str]):
        id (Union[Unset, str]):
        name (Union[Unset, str]):
    """

    client_role: Union[Unset, bool] = UNSET
    composite: Union[Unset, bool] = UNSET
    container_id: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        client_role = self.client_role
        composite = self.composite
        container_id = self.container_id
        description = self.description
        id = self.id
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if client_role is not UNSET:
            field_dict["clientRole"] = client_role
        if composite is not UNSET:
            field_dict["composite"] = composite
        if container_id is not UNSET:
            field_dict["containerId"] = container_id
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        client_role = d.pop("clientRole", UNSET)

        composite = d.pop("composite", UNSET)

        container_id = d.pop("containerId", UNSET)

        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        realm_role = cls(
            client_role=client_role,
            composite=composite,
            container_id=container_id,
            description=description,
            id=id,
            name=name,
        )

        realm_role.additional_properties = d
        return realm_role

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
