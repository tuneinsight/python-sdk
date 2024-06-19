from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserListQuery")


@attr.s(auto_attribs=True)
class UserListQuery:
    """
    Attributes:
        first_name (Union[Unset, str]):
        last_name (Union[Unset, str]):
        search (Union[Unset, str]):
        max_ (Union[Unset, int]):
        brief_representation (Union[Unset, bool]):
        email (Union[Unset, str]):
        idp_user_id (Union[Unset, str]):
        enabled (Union[Unset, bool]):
        idp_alias (Union[Unset, str]):
        q (Union[Unset, str]):
        username (Union[Unset, str]):
        email_verified (Union[Unset, bool]):
        exact (Union[Unset, bool]):
        first (Union[Unset, int]):
    """

    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    search: Union[Unset, str] = UNSET
    max_: Union[Unset, int] = UNSET
    brief_representation: Union[Unset, bool] = UNSET
    email: Union[Unset, str] = UNSET
    idp_user_id: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    idp_alias: Union[Unset, str] = UNSET
    q: Union[Unset, str] = UNSET
    username: Union[Unset, str] = UNSET
    email_verified: Union[Unset, bool] = UNSET
    exact: Union[Unset, bool] = UNSET
    first: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        first_name = self.first_name
        last_name = self.last_name
        search = self.search
        max_ = self.max_
        brief_representation = self.brief_representation
        email = self.email
        idp_user_id = self.idp_user_id
        enabled = self.enabled
        idp_alias = self.idp_alias
        q = self.q
        username = self.username
        email_verified = self.email_verified
        exact = self.exact
        first = self.first

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if search is not UNSET:
            field_dict["search"] = search
        if max_ is not UNSET:
            field_dict["max"] = max_
        if brief_representation is not UNSET:
            field_dict["briefRepresentation"] = brief_representation
        if email is not UNSET:
            field_dict["email"] = email
        if idp_user_id is not UNSET:
            field_dict["idpUserId"] = idp_user_id
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if idp_alias is not UNSET:
            field_dict["idpAlias"] = idp_alias
        if q is not UNSET:
            field_dict["q"] = q
        if username is not UNSET:
            field_dict["username"] = username
        if email_verified is not UNSET:
            field_dict["emailVerified"] = email_verified
        if exact is not UNSET:
            field_dict["exact"] = exact
        if first is not UNSET:
            field_dict["first"] = first

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        search = d.pop("search", UNSET)

        max_ = d.pop("max", UNSET)

        brief_representation = d.pop("briefRepresentation", UNSET)

        email = d.pop("email", UNSET)

        idp_user_id = d.pop("idpUserId", UNSET)

        enabled = d.pop("enabled", UNSET)

        idp_alias = d.pop("idpAlias", UNSET)

        q = d.pop("q", UNSET)

        username = d.pop("username", UNSET)

        email_verified = d.pop("emailVerified", UNSET)

        exact = d.pop("exact", UNSET)

        first = d.pop("first", UNSET)

        user_list_query = cls(
            first_name=first_name,
            last_name=last_name,
            search=search,
            max_=max_,
            brief_representation=brief_representation,
            email=email,
            idp_user_id=idp_user_id,
            enabled=enabled,
            idp_alias=idp_alias,
            q=q,
            username=username,
            email_verified=email_verified,
            exact=exact,
            first=first,
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
