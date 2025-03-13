from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dataset_schema_columns import DatasetSchemaColumns


T = TypeVar("T", bound="DatasetSchema")


@attr.s(auto_attribs=True)
class DatasetSchema:
    """dataset schema definition used to validate input datasets.

    Attributes:
        columns (Union[Unset, DatasetSchemaColumns]): mapping from column names to a set of constraints
            that the values present in the column should comply to.
        drop_invalid_rows (Union[Unset, bool]): whether invalid rows are automatically dropped instead of raising an
            error
        name (Union[Unset, str]): a name that describes this data schema.
    """

    columns: Union[Unset, "DatasetSchemaColumns"] = UNSET
    drop_invalid_rows: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        columns: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.columns, Unset):
            columns = self.columns.to_dict()

        drop_invalid_rows = self.drop_invalid_rows
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if columns is not UNSET:
            field_dict["columns"] = columns
        if drop_invalid_rows is not UNSET:
            field_dict["drop_invalid_rows"] = drop_invalid_rows
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dataset_schema_columns import DatasetSchemaColumns

        d = src_dict.copy()
        _columns = d.pop("columns", UNSET)
        columns: Union[Unset, DatasetSchemaColumns]
        if isinstance(_columns, Unset):
            columns = UNSET
        else:
            columns = DatasetSchemaColumns.from_dict(_columns)

        drop_invalid_rows = d.pop("drop_invalid_rows", UNSET)

        name = d.pop("name", UNSET)

        dataset_schema = cls(
            columns=columns,
            drop_invalid_rows=drop_invalid_rows,
            name=name,
        )

        dataset_schema.additional_properties = d
        return dataset_schema

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
