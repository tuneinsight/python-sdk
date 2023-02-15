from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.content_type import ContentType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.result_contextual_info import ResultContextualInfo


T = TypeVar("T", bound="FloatMatrix")


@attr.s(auto_attribs=True)
class FloatMatrix:
    """
    Attributes:
        type (ContentType): Type of the content
        columns (List[str]): Name of the columns of the matrix
        data (List[List[float]]): 2d array of float values
        contextual_info (Union[Unset, ResultContextualInfo]): contextual information about the content retrieved
        column_count (Union[Unset, int]):
        row_count (Union[Unset, int]):
    """

    type: ContentType
    columns: List[str]
    data: List[List[float]]
    contextual_info: Union[Unset, "ResultContextualInfo"] = UNSET
    column_count: Union[Unset, int] = UNSET
    row_count: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        columns = self.columns

        data = []
        for data_item_data in self.data:
            data_item = data_item_data

            data.append(data_item)

        contextual_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.contextual_info, Unset):
            contextual_info = self.contextual_info.to_dict()

        column_count = self.column_count
        row_count = self.row_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "columns": columns,
                "data": data,
            }
        )
        if contextual_info is not UNSET:
            field_dict["contextualInfo"] = contextual_info
        if column_count is not UNSET:
            field_dict["columnCount"] = column_count
        if row_count is not UNSET:
            field_dict["rowCount"] = row_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.result_contextual_info import ResultContextualInfo

        d = src_dict.copy()
        type = ContentType(d.pop("type"))

        columns = cast(List[str], d.pop("columns"))

        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = cast(List[float], data_item_data)

            data.append(data_item)

        _contextual_info = d.pop("contextualInfo", UNSET)
        contextual_info: Union[Unset, ResultContextualInfo]
        if isinstance(_contextual_info, Unset):
            contextual_info = UNSET
        else:
            contextual_info = ResultContextualInfo.from_dict(_contextual_info)

        column_count = d.pop("columnCount", UNSET)

        row_count = d.pop("rowCount", UNSET)

        float_matrix = cls(
            type=type,
            columns=columns,
            data=data,
            contextual_info=contextual_info,
            column_count=column_count,
            row_count=row_count,
        )

        float_matrix.additional_properties = d
        return float_matrix

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
