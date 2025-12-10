from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_source_variable import DataSourceVariable


T = TypeVar("T", bound="GetAvailableColumnsResponse200")


@attr.s(auto_attribs=True)
class GetAvailableColumnsResponse200:
    """
    Attributes:
        computation (Union[Unset, List['DataSourceVariable']]): the columns available for the computations (i.e.,
            columns of the input table).
        preprocessing (Union[Unset, List['DataSourceVariable']]): the columns available before the preprocessing (to use
            in a dry-run).
    """

    computation: Union[Unset, List["DataSourceVariable"]] = UNSET
    preprocessing: Union[Unset, List["DataSourceVariable"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        computation: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.computation, Unset):
            computation = []
            for computation_item_data in self.computation:
                computation_item = computation_item_data.to_dict()

                computation.append(computation_item)

        preprocessing: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.preprocessing, Unset):
            preprocessing = []
            for preprocessing_item_data in self.preprocessing:
                preprocessing_item = preprocessing_item_data.to_dict()

                preprocessing.append(preprocessing_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if computation is not UNSET:
            field_dict["computation"] = computation
        if preprocessing is not UNSET:
            field_dict["preprocessing"] = preprocessing

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.data_source_variable import DataSourceVariable

        d = src_dict.copy()
        computation = []
        _computation = d.pop("computation", UNSET)
        for computation_item_data in _computation or []:
            computation_item = DataSourceVariable.from_dict(computation_item_data)

            computation.append(computation_item)

        preprocessing = []
        _preprocessing = d.pop("preprocessing", UNSET)
        for preprocessing_item_data in _preprocessing or []:
            preprocessing_item = DataSourceVariable.from_dict(preprocessing_item_data)

            preprocessing.append(preprocessing_item)

        get_available_columns_response_200 = cls(
            computation=computation,
            preprocessing=preprocessing,
        )

        get_available_columns_response_200.additional_properties = d
        return get_available_columns_response_200

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
