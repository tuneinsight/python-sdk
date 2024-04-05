from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.computation_type import ComputationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.result_metadata import ResultMetadata


T = TypeVar("T", bound="Result")


@attr.s(auto_attribs=True)
class Result:
    """
    Attributes:
        is_large (Union[Unset, None, bool]): format to display the result
        shared (Union[Unset, None, bool]): if set to true, the result is shared with users from the same project
        tags (Union[Unset, List[str]]):
        title (Union[Unset, str]): title given to the result
        updated_at (Union[Unset, str]):
        collective_encrypted (Union[Unset, None, bool]):
        end_to_end_encrypted (Union[Unset, bool]):
        metadata (Union[Unset, ResultMetadata]): various metadata field along with the result to provide additional
            context
        switching_key_id (Union[Unset, str]): Unique identifier of a data object.
        switching_params (Union[Unset, str]):
        original_ciphertext_id (Union[Unset, str]): Unique identifier of a data object.
        owner (Union[Unset, str]):
        computation_id (Union[Unset, str]): Identifier of a computation, unique across all computing nodes.
        computation_type (Union[Unset, ComputationType]): Type of the computation.
        created_at (Union[Unset, str]):
        data_object_id (Union[Unset, str]): Unique identifier of a data object.
        id (Union[Unset, str]): Unique identifier of a result.
    """

    is_large: Union[Unset, None, bool] = UNSET
    shared: Union[Unset, None, bool] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    title: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    collective_encrypted: Union[Unset, None, bool] = UNSET
    end_to_end_encrypted: Union[Unset, bool] = UNSET
    metadata: Union[Unset, "ResultMetadata"] = UNSET
    switching_key_id: Union[Unset, str] = UNSET
    switching_params: Union[Unset, str] = UNSET
    original_ciphertext_id: Union[Unset, str] = UNSET
    owner: Union[Unset, str] = UNSET
    computation_id: Union[Unset, str] = UNSET
    computation_type: Union[Unset, ComputationType] = UNSET
    created_at: Union[Unset, str] = UNSET
    data_object_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        is_large = self.is_large
        shared = self.shared
        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        title = self.title
        updated_at = self.updated_at
        collective_encrypted = self.collective_encrypted
        end_to_end_encrypted = self.end_to_end_encrypted
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        switching_key_id = self.switching_key_id
        switching_params = self.switching_params
        original_ciphertext_id = self.original_ciphertext_id
        owner = self.owner
        computation_id = self.computation_id
        computation_type: Union[Unset, str] = UNSET
        if not isinstance(self.computation_type, Unset):
            computation_type = self.computation_type.value

        created_at = self.created_at
        data_object_id = self.data_object_id
        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_large is not UNSET:
            field_dict["isLarge"] = is_large
        if shared is not UNSET:
            field_dict["shared"] = shared
        if tags is not UNSET:
            field_dict["tags"] = tags
        if title is not UNSET:
            field_dict["title"] = title
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if collective_encrypted is not UNSET:
            field_dict["collectiveEncrypted"] = collective_encrypted
        if end_to_end_encrypted is not UNSET:
            field_dict["endToEndEncrypted"] = end_to_end_encrypted
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if switching_key_id is not UNSET:
            field_dict["switchingKeyId"] = switching_key_id
        if switching_params is not UNSET:
            field_dict["switchingParams"] = switching_params
        if original_ciphertext_id is not UNSET:
            field_dict["originalCiphertextID"] = original_ciphertext_id
        if owner is not UNSET:
            field_dict["owner"] = owner
        if computation_id is not UNSET:
            field_dict["computationId"] = computation_id
        if computation_type is not UNSET:
            field_dict["computationType"] = computation_type
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if data_object_id is not UNSET:
            field_dict["dataObjectId"] = data_object_id
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.result_metadata import ResultMetadata

        d = src_dict.copy()
        is_large = d.pop("isLarge", UNSET)

        shared = d.pop("shared", UNSET)

        tags = cast(List[str], d.pop("tags", UNSET))

        title = d.pop("title", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        collective_encrypted = d.pop("collectiveEncrypted", UNSET)

        end_to_end_encrypted = d.pop("endToEndEncrypted", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, ResultMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ResultMetadata.from_dict(_metadata)

        switching_key_id = d.pop("switchingKeyId", UNSET)

        switching_params = d.pop("switchingParams", UNSET)

        original_ciphertext_id = d.pop("originalCiphertextID", UNSET)

        owner = d.pop("owner", UNSET)

        computation_id = d.pop("computationId", UNSET)

        _computation_type = d.pop("computationType", UNSET)
        computation_type: Union[Unset, ComputationType]
        if isinstance(_computation_type, Unset):
            computation_type = UNSET
        else:
            computation_type = ComputationType(_computation_type)

        created_at = d.pop("createdAt", UNSET)

        data_object_id = d.pop("dataObjectId", UNSET)

        id = d.pop("id", UNSET)

        result = cls(
            is_large=is_large,
            shared=shared,
            tags=tags,
            title=title,
            updated_at=updated_at,
            collective_encrypted=collective_encrypted,
            end_to_end_encrypted=end_to_end_encrypted,
            metadata=metadata,
            switching_key_id=switching_key_id,
            switching_params=switching_params,
            original_ciphertext_id=original_ciphertext_id,
            owner=owner,
            computation_id=computation_id,
            computation_type=computation_type,
            created_at=created_at,
            data_object_id=data_object_id,
            id=id,
        )

        result.additional_properties = d
        return result

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
