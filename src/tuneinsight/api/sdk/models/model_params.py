from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelParams")


@attr.s(auto_attribs=True)
class ModelParams:
    """detailed parameters about the model, only returned when getting specific model

    Attributes:
        cryptolib_params (Union[Unset, str]): cryptolib.Parameters marshaled and encoded in base64 for client operations
        prediction_params (Union[Unset, str]): base64 encoded prediction parameters
    """

    cryptolib_params: Union[Unset, str] = UNSET
    prediction_params: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cryptolib_params = self.cryptolib_params
        prediction_params = self.prediction_params

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cryptolib_params is not UNSET:
            field_dict["cryptolibParams"] = cryptolib_params
        if prediction_params is not UNSET:
            field_dict["predictionParams"] = prediction_params

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cryptolib_params = d.pop("cryptolibParams", UNSET)

        prediction_params = d.pop("predictionParams", UNSET)

        model_params = cls(
            cryptolib_params=cryptolib_params,
            prediction_params=prediction_params,
        )

        model_params.additional_properties = d
        return model_params

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
