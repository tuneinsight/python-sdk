from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.content_type import ContentType
from ..models.result_contextual_info import ResultContextualInfo
from ..types import UNSET, Unset

T = TypeVar("T", bound="Ciphertable")


@attr.s(auto_attribs=True)
class Ciphertable:
    """
    Attributes:
        type (ContentType): Type of the content
        value (str): serialized ciphertable in base64
        contextual_info (Union[Unset, ResultContextualInfo]): contextual information about the content retrieved
        columns (Union[Unset, List[str]]): name of the columns of the encrypted matrix
    """

    type: ContentType
    value: str
    contextual_info: Union[Unset, ResultContextualInfo] = UNSET
    columns: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        value = self.value
        contextual_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.contextual_info, Unset):
            contextual_info = self.contextual_info.to_dict()

        columns: Union[Unset, List[str]] = UNSET
        if not isinstance(self.columns, Unset):
            columns = self.columns

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "value": value,
            }
        )
        if contextual_info is not UNSET:
            field_dict["contextualInfo"] = contextual_info
        if columns is not UNSET:
            field_dict["columns"] = columns

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = ContentType(d.pop("type"))

        value = d.pop("value")

        _contextual_info = d.pop("contextualInfo", UNSET)
        contextual_info: Union[Unset, ResultContextualInfo]
        if isinstance(_contextual_info, Unset):
            contextual_info = UNSET
        else:
            contextual_info = ResultContextualInfo.from_dict(_contextual_info)

        columns = cast(List[str], d.pop("columns", UNSET))

        ciphertable = cls(
            type=type,
            value=value,
            contextual_info=contextual_info,
            columns=columns,
        )

        ciphertable.additional_properties = d
        return ciphertable

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
