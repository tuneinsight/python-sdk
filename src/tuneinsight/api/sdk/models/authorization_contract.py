from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthorizationContract")


@attr.s(auto_attribs=True)
class AuthorizationContract:
    """describes what parts of the computation are allowed to change when a project is authorized

    Attributes:
        computation_parameters (Union[Unset, bool]): whether the computation parameters are allowed to change
        computation_type (Union[Unset, bool]): whether the computation type is allowed to change
        data_query (Union[Unset, bool]): whether the data query parameters are allowed to change
        data_source (Union[Unset, bool]): whether the data source is allowed to change
        preprocessing (Union[Unset, bool]): whether the preprocessing parameters are allowed to change
    """

    computation_parameters: Union[Unset, bool] = False
    computation_type: Union[Unset, bool] = False
    data_query: Union[Unset, bool] = False
    data_source: Union[Unset, bool] = False
    preprocessing: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        computation_parameters = self.computation_parameters
        computation_type = self.computation_type
        data_query = self.data_query
        data_source = self.data_source
        preprocessing = self.preprocessing

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if computation_parameters is not UNSET:
            field_dict["computationParameters"] = computation_parameters
        if computation_type is not UNSET:
            field_dict["computationType"] = computation_type
        if data_query is not UNSET:
            field_dict["dataQuery"] = data_query
        if data_source is not UNSET:
            field_dict["dataSource"] = data_source
        if preprocessing is not UNSET:
            field_dict["preprocessing"] = preprocessing

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        computation_parameters = d.pop("computationParameters", UNSET)

        computation_type = d.pop("computationType", UNSET)

        data_query = d.pop("dataQuery", UNSET)

        data_source = d.pop("dataSource", UNSET)

        preprocessing = d.pop("preprocessing", UNSET)

        authorization_contract = cls(
            computation_parameters=computation_parameters,
            computation_type=computation_type,
            data_query=data_query,
            data_source=data_source,
            preprocessing=preprocessing,
        )

        authorization_contract.additional_properties = d
        return authorization_contract

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
