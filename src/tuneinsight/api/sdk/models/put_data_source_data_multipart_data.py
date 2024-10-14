from io import BytesIO
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, File, FileJsonType, Unset

T = TypeVar("T", bound="PutDataSourceDataMultipartData")


@attr.s(auto_attribs=True)
class PutDataSourceDataMultipartData:
    """
    Attributes:
        data_source_request_data (Union[Unset, File]): Data source data file. Supported format: CSV.
        data_source_request_data_raw (Union[Unset, str]): Data source data provided as raw string csv
        table_name (Union[Unset, str]): optional table name to upload data to.
        delimiter (Union[Unset, str]): optional delimiter setting for csv loading
    """

    data_source_request_data: Union[Unset, File] = UNSET
    data_source_request_data_raw: Union[Unset, str] = UNSET
    table_name: Union[Unset, str] = UNSET
    delimiter: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data_source_request_data: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.data_source_request_data, Unset):
            data_source_request_data = self.data_source_request_data.to_tuple()

        data_source_request_data_raw = self.data_source_request_data_raw
        table_name = self.table_name
        delimiter = self.delimiter

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data_source_request_data is not UNSET:
            field_dict["dataSourceRequestData"] = data_source_request_data
        if data_source_request_data_raw is not UNSET:
            field_dict["dataSourceRequestDataRaw"] = data_source_request_data_raw
        if table_name is not UNSET:
            field_dict["tableName"] = table_name
        if delimiter is not UNSET:
            field_dict["delimiter"] = delimiter

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        data_source_request_data: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.data_source_request_data, Unset):
            data_source_request_data = self.data_source_request_data.to_tuple()

        data_source_request_data_raw = (
            self.data_source_request_data_raw
            if isinstance(self.data_source_request_data_raw, Unset)
            else (None, str(self.data_source_request_data_raw).encode(), "text/plain")
        )
        table_name = (
            self.table_name
            if isinstance(self.table_name, Unset)
            else (None, str(self.table_name).encode(), "text/plain")
        )
        delimiter = (
            self.delimiter if isinstance(self.delimiter, Unset) else (None, str(self.delimiter).encode(), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update({})
        if data_source_request_data is not UNSET:
            field_dict["dataSourceRequestData"] = data_source_request_data
        if data_source_request_data_raw is not UNSET:
            field_dict["dataSourceRequestDataRaw"] = data_source_request_data_raw
        if table_name is not UNSET:
            field_dict["tableName"] = table_name
        if delimiter is not UNSET:
            field_dict["delimiter"] = delimiter

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _data_source_request_data = d.pop("dataSourceRequestData", UNSET)
        data_source_request_data: Union[Unset, File]
        if isinstance(_data_source_request_data, Unset):
            data_source_request_data = UNSET
        else:
            data_source_request_data = File(payload=BytesIO(_data_source_request_data))

        data_source_request_data_raw = d.pop("dataSourceRequestDataRaw", UNSET)

        table_name = d.pop("tableName", UNSET)

        delimiter = d.pop("delimiter", UNSET)

        put_data_source_data_multipart_data = cls(
            data_source_request_data=data_source_request_data,
            data_source_request_data_raw=data_source_request_data_raw,
            table_name=table_name,
            delimiter=delimiter,
        )

        put_data_source_data_multipart_data.additional_properties = d
        return put_data_source_data_multipart_data

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
