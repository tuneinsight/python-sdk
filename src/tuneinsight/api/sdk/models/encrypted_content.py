from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.content_type import ContentType
from ..models.encrypted_content_type import EncryptedContentType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.result_contextual_info import ResultContextualInfo


T = TypeVar("T", bound="EncryptedContent")


@attr.s(auto_attribs=True)
class EncryptedContent:
    """
    Attributes:
        type (ContentType): Type of the content
        value (str): serialized encrypted content in base64
        contextual_info (Union[Unset, ResultContextualInfo]): contextual information about the content retrieved
        columns (Union[Unset, List[str]]): optional metadata giving the name of the columns of the encrypted matrix
        encrypted_type (Union[Unset, EncryptedContentType]): Type of the plaintext content stored in an
            encryptedContent.
        required_post_processing (Union[Unset, str]): if specified, a post-processing operation that needs to be applied
            once the content of this object is decrypted.
    """

    type: ContentType
    value: str
    contextual_info: Union[Unset, "ResultContextualInfo"] = UNSET
    columns: Union[Unset, List[str]] = UNSET
    encrypted_type: Union[Unset, EncryptedContentType] = UNSET
    required_post_processing: Union[Unset, str] = UNSET
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

        encrypted_type: Union[Unset, str] = UNSET
        if not isinstance(self.encrypted_type, Unset):
            encrypted_type = self.encrypted_type.value

        required_post_processing = self.required_post_processing

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
        if encrypted_type is not UNSET:
            field_dict["encryptedType"] = encrypted_type
        if required_post_processing is not UNSET:
            field_dict["requiredPostProcessing"] = required_post_processing

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.result_contextual_info import ResultContextualInfo

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

        _encrypted_type = d.pop("encryptedType", UNSET)
        encrypted_type: Union[Unset, EncryptedContentType]
        if isinstance(_encrypted_type, Unset):
            encrypted_type = UNSET
        else:
            encrypted_type = EncryptedContentType(_encrypted_type)

        required_post_processing = d.pop("requiredPostProcessing", UNSET)

        encrypted_content = cls(
            type=type,
            value=value,
            contextual_info=contextual_info,
            columns=columns,
            encrypted_type=encrypted_type,
            required_post_processing=required_post_processing,
        )

        encrypted_content.additional_properties = d
        return encrypted_content

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
