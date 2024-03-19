from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserListQuery")


@attr.s(auto_attribs=True)
class UserListQuery:
    """
    Attributes:
        last_name (Union[Unset, str]):
        q (Union[Unset, str]):
        username (Union[Unset, str]):
        first (Union[Unset, int]):
        first_name (Union[Unset, str]):
        max_ (Union[Unset, int]):
        email (Union[Unset, str]):
        enabled (Union[Unset, bool]):
        exact (Union[Unset, bool]):
        idp_user_id (Union[Unset, str]):
        search (Union[Unset, str]):
        brief_representation (Union[Unset, bool]):
        email_verified (Union[Unset, bool]):
        idp_alias (Union[Unset, str]):
    """

    last_name: Union[Unset, str] = UNSET
    q: Union[Unset, str] = UNSET
    username: Union[Unset, str] = UNSET
    first: Union[Unset, int] = UNSET
    first_name: Union[Unset, str] = UNSET
    max_: Union[Unset, int] = UNSET
    email: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    exact: Union[Unset, bool] = UNSET
    idp_user_id: Union[Unset, str] = UNSET
    search: Union[Unset, str] = UNSET
    brief_representation: Union[Unset, bool] = UNSET
    email_verified: Union[Unset, bool] = UNSET
    idp_alias: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        last_name = self.last_name
        q = self.q
        username = self.username
        first = self.first
        first_name = self.first_name
        max_ = self.max_
        email = self.email
        enabled = self.enabled
        exact = self.exact
        idp_user_id = self.idp_user_id
        search = self.search
        brief_representation = self.brief_representation
        email_verified = self.email_verified
        idp_alias = self.idp_alias

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if q is not UNSET:
            field_dict["q"] = q
        if username is not UNSET:
            field_dict["username"] = username
        if first is not UNSET:
            field_dict["first"] = first
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if max_ is not UNSET:
            field_dict["max"] = max_
        if email is not UNSET:
            field_dict["email"] = email
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if exact is not UNSET:
            field_dict["exact"] = exact
        if idp_user_id is not UNSET:
            field_dict["idpUserId"] = idp_user_id
        if search is not UNSET:
            field_dict["search"] = search
        if brief_representation is not UNSET:
            field_dict["briefRepresentation"] = brief_representation
        if email_verified is not UNSET:
            field_dict["emailVerified"] = email_verified
        if idp_alias is not UNSET:
            field_dict["idpAlias"] = idp_alias

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        last_name = d.pop("lastName", UNSET)

        q = d.pop("q", UNSET)

        username = d.pop("username", UNSET)

        first = d.pop("first", UNSET)

        first_name = d.pop("firstName", UNSET)

        max_ = d.pop("max", UNSET)

        email = d.pop("email", UNSET)

        enabled = d.pop("enabled", UNSET)

        exact = d.pop("exact", UNSET)

        idp_user_id = d.pop("idpUserId", UNSET)

        search = d.pop("search", UNSET)

        brief_representation = d.pop("briefRepresentation", UNSET)

        email_verified = d.pop("emailVerified", UNSET)

        idp_alias = d.pop("idpAlias", UNSET)

        user_list_query = cls(
            last_name=last_name,
            q=q,
            username=username,
            first=first,
            first_name=first_name,
            max_=max_,
            email=email,
            enabled=enabled,
            exact=exact,
            idp_user_id=idp_user_id,
            search=search,
            brief_representation=brief_representation,
            email_verified=email_verified,
            idp_alias=idp_alias,
        )

        user_list_query.additional_properties = d
        return user_list_query

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
