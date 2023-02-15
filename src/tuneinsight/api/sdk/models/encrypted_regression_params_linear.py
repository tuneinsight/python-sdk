from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="EncryptedRegressionParamsLinear")


@attr.s(auto_attribs=True)
class EncryptedRegressionParamsLinear:
    """Parameters specific for the linear regression.

    Attributes:
        continuous_labels (bool): If true, then expects continuous labels (i.e. not binary).
    """

    continuous_labels: bool
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        continuous_labels = self.continuous_labels

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "continuousLabels": continuous_labels,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        continuous_labels = d.pop("continuousLabels")

        encrypted_regression_params_linear = cls(
            continuous_labels=continuous_labels,
        )

        encrypted_regression_params_linear.additional_properties = d
        return encrypted_regression_params_linear

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
