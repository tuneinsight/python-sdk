from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_source_table import DataSourceTable


T = TypeVar("T", bound="DataSourceQueryPreview")


@attr.s(auto_attribs=True)
class DataSourceQueryPreview:
    """preview of a datasource query

    Attributes:
        columns (Union[Unset, List[str]]): columns of the queried table
        rows (Union[Unset, List[List[str]]]): previewed records
        table_metadata (Union[Unset, DataSourceTable]): schema information for a table from a datasource
    """

    columns: Union[Unset, List[str]] = UNSET
    rows: Union[Unset, List[List[str]]] = UNSET
    table_metadata: Union[Unset, "DataSourceTable"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        columns: Union[Unset, List[str]] = UNSET
        if not isinstance(self.columns, Unset):
            columns = self.columns

        rows: Union[Unset, List[List[str]]] = UNSET
        if not isinstance(self.rows, Unset):
            rows = []
            for rows_item_data in self.rows:
                rows_item = rows_item_data

                rows.append(rows_item)

        table_metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.table_metadata, Unset):
            table_metadata = self.table_metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if columns is not UNSET:
            field_dict["columns"] = columns
        if rows is not UNSET:
            field_dict["rows"] = rows
        if table_metadata is not UNSET:
            field_dict["tableMetadata"] = table_metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.data_source_table import DataSourceTable

        d = src_dict.copy()
        columns = cast(List[str], d.pop("columns", UNSET))

        rows = []
        _rows = d.pop("rows", UNSET)
        for rows_item_data in _rows or []:
            rows_item = cast(List[str], rows_item_data)

            rows.append(rows_item)

        _table_metadata = d.pop("tableMetadata", UNSET)
        table_metadata: Union[Unset, DataSourceTable]
        if isinstance(_table_metadata, Unset):
            table_metadata = UNSET
        else:
            table_metadata = DataSourceTable.from_dict(_table_metadata)

        data_source_query_preview = cls(
            columns=columns,
            rows=rows,
            table_metadata=table_metadata,
        )

        data_source_query_preview.additional_properties = d
        return data_source_query_preview

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
