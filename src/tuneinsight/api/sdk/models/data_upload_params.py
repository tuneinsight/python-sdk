from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="DataUploadParams")


@attr.s(auto_attribs=True)
class DataUploadParams:
    """parameters used when uploading data to a data source

    Attributes:
        data (Union[Unset, str]): string containing the csv data to upload
        delimiter (Union[Unset, str]): optional delimiter used in the csv to separate values.
        replace (Union[Unset, bool]): whether to replace the data or append the data.
        skip_invalid_rows (Union[Unset, bool]): whether invalid rows return an error or are simply skipped.
        table_name (Union[Unset, str]): optional table name to upload the data to (when data source is a database)
    """

    data: Union[Unset, str] = UNSET
    delimiter: Union[Unset, str] = UNSET
    replace: Union[Unset, bool] = UNSET
    skip_invalid_rows: Union[Unset, bool] = UNSET
    table_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data = self.data
        delimiter = self.delimiter
        replace = self.replace
        skip_invalid_rows = self.skip_invalid_rows
        table_name = self.table_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if delimiter is not UNSET:
            field_dict["delimiter"] = delimiter
        if replace is not UNSET:
            field_dict["replace"] = replace
        if skip_invalid_rows is not UNSET:
            field_dict["skipInvalidRows"] = skip_invalid_rows
        if table_name is not UNSET:
            field_dict["tableName"] = table_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        data = d.pop("data", UNSET)

        delimiter = d.pop("delimiter", UNSET)

        replace = d.pop("replace", UNSET)

        skip_invalid_rows = d.pop("skipInvalidRows", UNSET)

        table_name = d.pop("tableName", UNSET)

        data_upload_params = cls(
            data=data,
            delimiter=delimiter,
            replace=replace,
            skip_invalid_rows=skip_invalid_rows,
            table_name=table_name,
        )

        data_upload_params.additional_properties = d
        return data_upload_params

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
