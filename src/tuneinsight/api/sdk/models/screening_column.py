from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.column_type_group import ColumnTypeGroup
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.date_format import DateFormat


T = TypeVar("T", bound="ScreeningColumn")


@attr.s(auto_attribs=True)
class ScreeningColumn:
    """
    Attributes:
        name (Union[Unset, str]):
        type (Union[Unset, str]):
        type_group (Union[Unset, ColumnTypeGroup]): represents a type group indicating the way the data may actually be
            processed
        mean (Union[Unset, float]): mean of the column (when numeric) on the unscreened data.
        numeric_count (Union[Unset, int]): number of rows that contain valid numeric values for this column.
        possible_date_formats (Union[Unset, List['DateFormat']]): list of possible date formats sorted in descending
            likelihood order.
        std (Union[Unset, float]): standard deviation of the column (when numeric) on the unscreened data.
    """

    name: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    type_group: Union[Unset, ColumnTypeGroup] = UNSET
    mean: Union[Unset, float] = UNSET
    numeric_count: Union[Unset, int] = UNSET
    possible_date_formats: Union[Unset, List["DateFormat"]] = UNSET
    std: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        type = self.type
        type_group: Union[Unset, str] = UNSET
        if not isinstance(self.type_group, Unset):
            type_group = self.type_group.value

        mean = self.mean
        numeric_count = self.numeric_count
        possible_date_formats: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.possible_date_formats, Unset):
            possible_date_formats = []
            for possible_date_formats_item_data in self.possible_date_formats:
                possible_date_formats_item = possible_date_formats_item_data.to_dict()

                possible_date_formats.append(possible_date_formats_item)

        std = self.std

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if type is not UNSET:
            field_dict["type"] = type
        if type_group is not UNSET:
            field_dict["typeGroup"] = type_group
        if mean is not UNSET:
            field_dict["mean"] = mean
        if numeric_count is not UNSET:
            field_dict["numericCount"] = numeric_count
        if possible_date_formats is not UNSET:
            field_dict["possibleDateFormats"] = possible_date_formats
        if std is not UNSET:
            field_dict["std"] = std

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.date_format import DateFormat

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        type = d.pop("type", UNSET)

        _type_group = d.pop("typeGroup", UNSET)
        type_group: Union[Unset, ColumnTypeGroup]
        if isinstance(_type_group, Unset):
            type_group = UNSET
        else:
            type_group = ColumnTypeGroup(_type_group)

        mean = d.pop("mean", UNSET)

        numeric_count = d.pop("numericCount", UNSET)

        possible_date_formats = []
        _possible_date_formats = d.pop("possibleDateFormats", UNSET)
        for possible_date_formats_item_data in _possible_date_formats or []:
            possible_date_formats_item = DateFormat.from_dict(possible_date_formats_item_data)

            possible_date_formats.append(possible_date_formats_item)

        std = d.pop("std", UNSET)

        screening_column = cls(
            name=name,
            type=type,
            type_group=type_group,
            mean=mean,
            numeric_count=numeric_count,
            possible_date_formats=possible_date_formats,
            std=std,
        )

        screening_column.additional_properties = d
        return screening_column

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
