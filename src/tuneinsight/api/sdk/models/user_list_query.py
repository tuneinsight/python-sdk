from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserListQuery")


@attr.s(auto_attribs=True)
class UserListQuery:
    """
    Attributes:
        email (Union[Unset, str]):
        last_name (Union[Unset, str]):
        username (Union[Unset, str]):
        exact (Union[Unset, bool]):
        search (Union[Unset, str]):
        enabled (Union[Unset, bool]):
        idp_user_id (Union[Unset, str]):
        idp_alias (Union[Unset, str]):
        max_ (Union[Unset, int]):
        q (Union[Unset, str]):
        brief_representation (Union[Unset, bool]):
        email_verified (Union[Unset, bool]):
        first (Union[Unset, int]):
        first_name (Union[Unset, str]):
    """

    email: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    username: Union[Unset, str] = UNSET
    exact: Union[Unset, bool] = UNSET
    search: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    idp_user_id: Union[Unset, str] = UNSET
    idp_alias: Union[Unset, str] = UNSET
    max_: Union[Unset, int] = UNSET
    q: Union[Unset, str] = UNSET
    brief_representation: Union[Unset, bool] = UNSET
    email_verified: Union[Unset, bool] = UNSET
    first: Union[Unset, int] = UNSET
    first_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        email = self.email
        last_name = self.last_name
        username = self.username
        exact = self.exact
        search = self.search
        enabled = self.enabled
        idp_user_id = self.idp_user_id
        idp_alias = self.idp_alias
        max_ = self.max_
        q = self.q
        brief_representation = self.brief_representation
        email_verified = self.email_verified
        first = self.first
        first_name = self.first_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if username is not UNSET:
            field_dict["username"] = username
        if exact is not UNSET:
            field_dict["exact"] = exact
        if search is not UNSET:
            field_dict["search"] = search
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if idp_user_id is not UNSET:
            field_dict["idpUserId"] = idp_user_id
        if idp_alias is not UNSET:
            field_dict["idpAlias"] = idp_alias
        if max_ is not UNSET:
            field_dict["max"] = max_
        if q is not UNSET:
            field_dict["q"] = q
        if brief_representation is not UNSET:
            field_dict["briefRepresentation"] = brief_representation
        if email_verified is not UNSET:
            field_dict["emailVerified"] = email_verified
        if first is not UNSET:
            field_dict["first"] = first
        if first_name is not UNSET:
            field_dict["firstName"] = first_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        email = d.pop("email", UNSET)

        last_name = d.pop("lastName", UNSET)

        username = d.pop("username", UNSET)

        exact = d.pop("exact", UNSET)

        search = d.pop("search", UNSET)

        enabled = d.pop("enabled", UNSET)

        idp_user_id = d.pop("idpUserId", UNSET)

        idp_alias = d.pop("idpAlias", UNSET)

        max_ = d.pop("max", UNSET)

        q = d.pop("q", UNSET)

        brief_representation = d.pop("briefRepresentation", UNSET)

        email_verified = d.pop("emailVerified", UNSET)

        first = d.pop("first", UNSET)

        first_name = d.pop("firstName", UNSET)

        user_list_query = cls(
            email=email,
            last_name=last_name,
            username=username,
            exact=exact,
            search=search,
            enabled=enabled,
            idp_user_id=idp_user_id,
            idp_alias=idp_alias,
            max_=max_,
            q=q,
            brief_representation=brief_representation,
            email_verified=email_verified,
            first=first,
            first_name=first_name,
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
