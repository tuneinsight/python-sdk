from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.matching_column import MatchingColumn


T = TypeVar("T", bound="MatchingParams")


@attr.s(auto_attribs=True)
class MatchingParams:
    """parameters relevant for matching

    Attributes:
        matching_columns (Union[Unset, List['MatchingColumn']]):
    """

    matching_columns: Union[Unset, List["MatchingColumn"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        matching_columns: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.matching_columns, Unset):
            matching_columns = []
            for matching_columns_item_data in self.matching_columns:
                matching_columns_item = matching_columns_item_data.to_dict()

                matching_columns.append(matching_columns_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if matching_columns is not UNSET:
            field_dict["matchingColumns"] = matching_columns

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.matching_column import MatchingColumn

        d = src_dict.copy()
        matching_columns = []
        _matching_columns = d.pop("matchingColumns", UNSET)
        for matching_columns_item_data in _matching_columns or []:
            matching_columns_item = MatchingColumn.from_dict(matching_columns_item_data)

            matching_columns.append(matching_columns_item)

        matching_params = cls(
            matching_columns=matching_columns,
        )

        matching_params.additional_properties = d
        return matching_params

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
