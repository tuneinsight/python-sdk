from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.screening_column import ScreeningColumn


T = TypeVar("T", bound="ScreeningMetadata")


@attr.s(auto_attribs=True)
class ScreeningMetadata:
    """metadata of the dataset used in the screening process.

    Attributes:
        columns (Union[Unset, List['ScreeningColumn']]):
        count (Union[Unset, int]): number of rows in the original dataset.
        screened_count (Union[Unset, int]): number of screened rows.
    """

    columns: Union[Unset, List["ScreeningColumn"]] = UNSET
    count: Union[Unset, int] = UNSET
    screened_count: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        columns: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.columns, Unset):
            columns = []
            for columns_item_data in self.columns:
                columns_item = columns_item_data.to_dict()

                columns.append(columns_item)

        count = self.count
        screened_count = self.screened_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if columns is not UNSET:
            field_dict["columns"] = columns
        if count is not UNSET:
            field_dict["count"] = count
        if screened_count is not UNSET:
            field_dict["screenedCount"] = screened_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.screening_column import ScreeningColumn

        d = src_dict.copy()
        columns = []
        _columns = d.pop("columns", UNSET)
        for columns_item_data in _columns or []:
            columns_item = ScreeningColumn.from_dict(columns_item_data)

            columns.append(columns_item)

        count = d.pop("count", UNSET)

        screened_count = d.pop("screenedCount", UNSET)

        screening_metadata = cls(
            columns=columns,
            count=count,
            screened_count=screened_count,
        )

        screening_metadata.additional_properties = d
        return screening_metadata

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
