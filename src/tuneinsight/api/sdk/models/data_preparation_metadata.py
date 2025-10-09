from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_preparation_column import DataPreparationColumn


T = TypeVar("T", bound="DataPreparationMetadata")


@attr.s(auto_attribs=True)
class DataPreparationMetadata:
    """metadata of the dataset used in the data preparation process.

    Attributes:
        count (Union[Unset, int]): number of rows in the dataset before screening operations are applied to it.
        preprocessing_columns (Union[Unset, List['DataPreparationColumn']]): list of columns that are available before
            the preprocessing has run.
        screened_count (Union[Unset, int]): number of screened rows.
        screening_columns (Union[Unset, List['DataPreparationColumn']]): list of columns that are available after both
            the query + preprocessing have run.
    """

    count: Union[Unset, int] = UNSET
    preprocessing_columns: Union[Unset, List["DataPreparationColumn"]] = UNSET
    screened_count: Union[Unset, int] = UNSET
    screening_columns: Union[Unset, List["DataPreparationColumn"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        count = self.count
        preprocessing_columns: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.preprocessing_columns, Unset):
            preprocessing_columns = []
            for preprocessing_columns_item_data in self.preprocessing_columns:
                preprocessing_columns_item = preprocessing_columns_item_data.to_dict()

                preprocessing_columns.append(preprocessing_columns_item)

        screened_count = self.screened_count
        screening_columns: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.screening_columns, Unset):
            screening_columns = []
            for screening_columns_item_data in self.screening_columns:
                screening_columns_item = screening_columns_item_data.to_dict()

                screening_columns.append(screening_columns_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if preprocessing_columns is not UNSET:
            field_dict["preprocessingColumns"] = preprocessing_columns
        if screened_count is not UNSET:
            field_dict["screenedCount"] = screened_count
        if screening_columns is not UNSET:
            field_dict["screeningColumns"] = screening_columns

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.data_preparation_column import DataPreparationColumn

        d = src_dict.copy()
        count = d.pop("count", UNSET)

        preprocessing_columns = []
        _preprocessing_columns = d.pop("preprocessingColumns", UNSET)
        for preprocessing_columns_item_data in _preprocessing_columns or []:
            preprocessing_columns_item = DataPreparationColumn.from_dict(preprocessing_columns_item_data)

            preprocessing_columns.append(preprocessing_columns_item)

        screened_count = d.pop("screenedCount", UNSET)

        screening_columns = []
        _screening_columns = d.pop("screeningColumns", UNSET)
        for screening_columns_item_data in _screening_columns or []:
            screening_columns_item = DataPreparationColumn.from_dict(screening_columns_item_data)

            screening_columns.append(screening_columns_item)

        data_preparation_metadata = cls(
            count=count,
            preprocessing_columns=preprocessing_columns,
            screened_count=screened_count,
            screening_columns=screening_columns,
        )

        data_preparation_metadata.additional_properties = d
        return data_preparation_metadata

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
