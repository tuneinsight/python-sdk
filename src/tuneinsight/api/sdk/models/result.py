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
        shared (Union[Unset, None, bool]): if set to true, the result is shared with users from the same project
        tags (Union[Unset, List[str]]):
        title (Union[Unset, str]): title given to the result
        is_large (Union[Unset, None, bool]): format to display the result
        metadata (Union[Unset, ResultMetadata]): various metadata field along with the result to provide additional
            context
        owner (Union[Unset, str]):
        updated_at (Union[Unset, str]):
        computation_id (Union[Unset, str]): Identifier of a computation, unique across all computing nodes.
        computation_type (Union[Unset, ComputationType]): Type of the computation.
        created_at (Union[Unset, str]):
        data_object_id (Union[Unset, str]): Unique identifier of a data object.
        id (Union[Unset, str]): Unique identifier of a result.
    """

    shared: Union[Unset, None, bool] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    title: Union[Unset, str] = UNSET
    is_large: Union[Unset, None, bool] = UNSET
    metadata: Union[Unset, "ResultMetadata"] = UNSET
    owner: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    computation_id: Union[Unset, str] = UNSET
    computation_type: Union[Unset, ComputationType] = UNSET
    created_at: Union[Unset, str] = UNSET
    data_object_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        shared = self.shared
        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        title = self.title
        is_large = self.is_large
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        owner = self.owner
        updated_at = self.updated_at
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
        if shared is not UNSET:
            field_dict["shared"] = shared
        if tags is not UNSET:
            field_dict["tags"] = tags
        if title is not UNSET:
            field_dict["title"] = title
        if is_large is not UNSET:
            field_dict["isLarge"] = is_large
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if owner is not UNSET:
            field_dict["owner"] = owner
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
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
        shared = d.pop("shared", UNSET)

        tags = cast(List[str], d.pop("tags", UNSET))

        title = d.pop("title", UNSET)

        is_large = d.pop("isLarge", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, ResultMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ResultMetadata.from_dict(_metadata)

        owner = d.pop("owner", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

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
            shared=shared,
            tags=tags,
            title=title,
            is_large=is_large,
            metadata=metadata,
            owner=owner,
            updated_at=updated_at,
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
