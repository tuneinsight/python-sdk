from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.computation_preprocessing_parameters_compound_preprocessing import (
    ComputationPreprocessingParametersCompoundPreprocessing,
)
from ..models.preprocessing_chain import PreprocessingChain
from ..types import UNSET, Unset

T = TypeVar("T", bound="ComputationPreprocessingParameters")


@attr.s(auto_attribs=True)
class ComputationPreprocessingParameters:
    """dataframe pre-processing parameters applied to the input retrieved from the datasource, if applicable

    Attributes:
        compound_preprocessing (Union[Unset, ComputationPreprocessingParametersCompoundPreprocessing]): preprocessing to
            be applied for each node
        global_preprocessing (Union[Unset, PreprocessingChain]): Chain of preprocessing operations applied to the input
            dataframe
    """

    compound_preprocessing: Union[Unset, ComputationPreprocessingParametersCompoundPreprocessing] = UNSET
    global_preprocessing: Union[Unset, PreprocessingChain] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        compound_preprocessing: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.compound_preprocessing, Unset):
            compound_preprocessing = self.compound_preprocessing.to_dict()

        global_preprocessing: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.global_preprocessing, Unset):
            global_preprocessing = self.global_preprocessing.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if compound_preprocessing is not UNSET:
            field_dict["compoundPreprocessing"] = compound_preprocessing
        if global_preprocessing is not UNSET:
            field_dict["globalPreprocessing"] = global_preprocessing

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _compound_preprocessing = d.pop("compoundPreprocessing", UNSET)
        compound_preprocessing: Union[Unset, ComputationPreprocessingParametersCompoundPreprocessing]
        if isinstance(_compound_preprocessing, Unset):
            compound_preprocessing = UNSET
        else:
            compound_preprocessing = ComputationPreprocessingParametersCompoundPreprocessing.from_dict(
                _compound_preprocessing
            )

        _global_preprocessing = d.pop("globalPreprocessing", UNSET)
        global_preprocessing: Union[Unset, PreprocessingChain]
        if isinstance(_global_preprocessing, Unset):
            global_preprocessing = UNSET
        else:
            global_preprocessing = PreprocessingChain.from_dict(_global_preprocessing)

        computation_preprocessing_parameters = cls(
            compound_preprocessing=compound_preprocessing,
            global_preprocessing=global_preprocessing,
        )

        computation_preprocessing_parameters.additional_properties = d
        return computation_preprocessing_parameters

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
