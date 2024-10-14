from io import BytesIO
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, File, Unset

T = TypeVar("T", bound="PutDataObjectDataMultipartData")


@attr.s(auto_attribs=True)
class PutDataObjectDataMultipartData:
    """
    Attributes:
        data_object_data (File): Data sent as bytes
        object_key (Union[Unset, str]): optional object key to store a specific part of the data. Can be empty and
            defined.
        append (Union[Unset, bool]): if set to true and an object key is specified, then the data is appended to the
            existing data object data at this key.
            WARNING: only use append mode when uploading data sequentially. For parallel uploads, use the chunk index
            parameter.
        chunk_index (Union[Unset, int]): if specified along with an object key, the data will be considered as a chunk
            and written at the specified index.
            This parameter enables safe concurrent upload of chunks.
            indices start at 0. Note that, the size of the data uploaded cannot exceed 4MB when uploading individual chunks.
    """

    data_object_data: File
    object_key: Union[Unset, str] = UNSET
    append: Union[Unset, bool] = UNSET
    chunk_index: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data_object_data = self.data_object_data.to_tuple()

        object_key = self.object_key
        append = self.append
        chunk_index = self.chunk_index

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dataObjectData": data_object_data,
            }
        )
        if object_key is not UNSET:
            field_dict["objectKey"] = object_key
        if append is not UNSET:
            field_dict["append"] = append
        if chunk_index is not UNSET:
            field_dict["chunkIndex"] = chunk_index

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        data_object_data = self.data_object_data.to_tuple()

        object_key = (
            self.object_key
            if isinstance(self.object_key, Unset)
            else (None, str(self.object_key).encode(), "text/plain")
        )
        append = self.append if isinstance(self.append, Unset) else (None, str(self.append).encode(), "text/plain")
        chunk_index = (
            self.chunk_index
            if isinstance(self.chunk_index, Unset)
            else (None, str(self.chunk_index).encode(), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "dataObjectData": data_object_data,
            }
        )
        if object_key is not UNSET:
            field_dict["objectKey"] = object_key
        if append is not UNSET:
            field_dict["append"] = append
        if chunk_index is not UNSET:
            field_dict["chunkIndex"] = chunk_index

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        data_object_data = File(payload=BytesIO(d.pop("dataObjectData")))

        object_key = d.pop("objectKey", UNSET)

        append = d.pop("append", UNSET)

        chunk_index = d.pop("chunkIndex", UNSET)

        put_data_object_data_multipart_data = cls(
            data_object_data=data_object_data,
            object_key=object_key,
            append=append,
            chunk_index=chunk_index,
        )

        put_data_object_data_multipart_data.additional_properties = d
        return put_data_object_data_multipart_data

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
