from io import BytesIO
from typing import Any, Dict, List, Type, TypeVar

import attr

from ..types import File, Unset

T = TypeVar("T", bound="PostProtocolMessageMultipartData")


@attr.s(auto_attribs=True)
class PostProtocolMessageMultipartData:
    """
    Attributes:
        request_data (File): Binary stream
        protocol_base (str): JSON of the protocol base request encoded in b64
        computation_id (str): Identifier of a computation, unique across all computing nodes.
        name (str): name of the message channel
        id (str): id of the message used for chunking
        byte_length (int): total length of the message for chunking
        end (bool): whether this is the end of the message or not
        index (int): current message index for chunking
    """

    request_data: File
    protocol_base: str
    computation_id: str
    name: str
    id: str
    byte_length: int
    end: bool
    index: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        request_data = self.request_data.to_tuple()

        protocol_base = self.protocol_base
        computation_id = self.computation_id
        name = self.name
        id = self.id
        byte_length = self.byte_length
        end = self.end
        index = self.index

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "requestData": request_data,
                "protocolBase": protocol_base,
                "computationId": computation_id,
                "name": name,
                "id": id,
                "byteLength": byte_length,
                "end": end,
                "index": index,
            }
        )

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        request_data = self.request_data.to_tuple()

        protocol_base = (
            self.protocol_base
            if isinstance(self.protocol_base, Unset)
            else (None, str(self.protocol_base).encode(), "text/plain")
        )
        computation_id = (
            self.computation_id
            if isinstance(self.computation_id, Unset)
            else (None, str(self.computation_id).encode(), "text/plain")
        )
        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")
        id = self.id if isinstance(self.id, Unset) else (None, str(self.id).encode(), "text/plain")
        byte_length = (
            self.byte_length
            if isinstance(self.byte_length, Unset)
            else (None, str(self.byte_length).encode(), "text/plain")
        )
        end = self.end if isinstance(self.end, Unset) else (None, str(self.end).encode(), "text/plain")
        index = self.index if isinstance(self.index, Unset) else (None, str(self.index).encode(), "text/plain")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "requestData": request_data,
                "protocolBase": protocol_base,
                "computationId": computation_id,
                "name": name,
                "id": id,
                "byteLength": byte_length,
                "end": end,
                "index": index,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        request_data = File(payload=BytesIO(d.pop("requestData")))

        protocol_base = d.pop("protocolBase")

        computation_id = d.pop("computationId")

        name = d.pop("name")

        id = d.pop("id")

        byte_length = d.pop("byteLength")

        end = d.pop("end")

        index = d.pop("index")

        post_protocol_message_multipart_data = cls(
            request_data=request_data,
            protocol_base=protocol_base,
            computation_id=computation_id,
            name=name,
            id=id,
            byte_length=byte_length,
            end=end,
            index=index,
        )

        post_protocol_message_multipart_data.additional_properties = d
        return post_protocol_message_multipart_data

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
