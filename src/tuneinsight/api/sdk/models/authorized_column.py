from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.threshold import Threshold


T = TypeVar("T", bound="AuthorizedColumn")


@attr.s(auto_attribs=True)
class AuthorizedColumn:
    """identifier for a column with some disclosure-prevention constraints.

    Attributes:
        categorical (Union[Unset, bool]): whether the column is categorical.
        max_categories (Union[Unset, Threshold]): represents a threshold, which can be made relative of the dataset size
        name (Union[Unset, str]): name of the column.
        table_name (Union[Unset, str]): name of the table storing the column (not validated at the moment)
    """

    categorical: Union[Unset, bool] = UNSET
    max_categories: Union[Unset, "Threshold"] = UNSET
    name: Union[Unset, str] = UNSET
    table_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        categorical = self.categorical
        max_categories: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.max_categories, Unset):
            max_categories = self.max_categories.to_dict()

        name = self.name
        table_name = self.table_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if categorical is not UNSET:
            field_dict["categorical"] = categorical
        if max_categories is not UNSET:
            field_dict["maxCategories"] = max_categories
        if name is not UNSET:
            field_dict["name"] = name
        if table_name is not UNSET:
            field_dict["tableName"] = table_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.threshold import Threshold

        d = src_dict.copy()
        categorical = d.pop("categorical", UNSET)

        _max_categories = d.pop("maxCategories", UNSET)
        max_categories: Union[Unset, Threshold]
        if isinstance(_max_categories, Unset):
            max_categories = UNSET
        else:
            max_categories = Threshold.from_dict(_max_categories)

        name = d.pop("name", UNSET)

        table_name = d.pop("tableName", UNSET)

        authorized_column = cls(
            categorical=categorical,
            max_categories=max_categories,
            name=name,
            table_name=table_name,
        )

        authorized_column.additional_properties = d
        return authorized_column

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
