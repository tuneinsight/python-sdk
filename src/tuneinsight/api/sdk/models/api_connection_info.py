from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_connection_info_type import APIConnectionInfoType
from ..types import UNSET, Unset

T = TypeVar("T", bound="APIConnectionInfo")


@attr.s(auto_attribs=True)
class APIConnectionInfo:
    """Connection information for a API data sources

    Attributes:
        api_token (Union[Unset, str]): Token to connect to the API
        api_url (Union[Unset, str]): URL of the API
        type (Union[Unset, APIConnectionInfoType]): Type of API
    """

    api_token: Union[Unset, str] = UNSET
    api_url: Union[Unset, str] = UNSET
    type: Union[Unset, APIConnectionInfoType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        api_token = self.api_token
        api_url = self.api_url
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if api_token is not UNSET:
            field_dict["api-token"] = api_token
        if api_url is not UNSET:
            field_dict["api-url"] = api_url
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        api_token = d.pop("api-token", UNSET)

        api_url = d.pop("api-url", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, APIConnectionInfoType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = APIConnectionInfoType(_type)

        api_connection_info = cls(
            api_token=api_token,
            api_url=api_url,
            type=type,
        )

        api_connection_info.additional_properties = d
        return api_connection_info

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
