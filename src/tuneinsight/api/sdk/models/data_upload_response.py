from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_source import DataSource
    from ..models.data_source_query_preview import DataSourceQueryPreview


T = TypeVar("T", bound="DataUploadResponse")


@attr.s(auto_attribs=True)
class DataUploadResponse:
    """response when uploading data to a data source.

    Attributes:
        data_source (Union[Unset, DataSource]):
        preview (Union[Unset, DataSourceQueryPreview]): preview of a datasource query
    """

    data_source: Union[Unset, "DataSource"] = UNSET
    preview: Union[Unset, "DataSourceQueryPreview"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data_source: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data_source, Unset):
            data_source = self.data_source.to_dict()

        preview: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.preview, Unset):
            preview = self.preview.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data_source is not UNSET:
            field_dict["dataSource"] = data_source
        if preview is not UNSET:
            field_dict["preview"] = preview

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.data_source import DataSource
        from ..models.data_source_query_preview import DataSourceQueryPreview

        d = src_dict.copy()
        _data_source = d.pop("dataSource", UNSET)
        data_source: Union[Unset, DataSource]
        if isinstance(_data_source, Unset):
            data_source = UNSET
        else:
            data_source = DataSource.from_dict(_data_source)

        _preview = d.pop("preview", UNSET)
        preview: Union[Unset, DataSourceQueryPreview]
        if isinstance(_preview, Unset):
            preview = UNSET
        else:
            preview = DataSourceQueryPreview.from_dict(_preview)

        data_upload_response = cls(
            data_source=data_source,
            preview=preview,
        )

        data_upload_response.additional_properties = d
        return data_upload_response

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
