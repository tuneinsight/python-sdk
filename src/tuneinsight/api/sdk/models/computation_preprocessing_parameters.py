from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.computation_preprocessing_parameters_compound_preprocessing import (
        ComputationPreprocessingParametersCompoundPreprocessing,
    )
    from ..models.dataset_schema import DatasetSchema
    from ..models.logical_formula import LogicalFormula
    from ..models.preprocessing_chain import PreprocessingChain
    from ..models.select import Select


T = TypeVar("T", bound="ComputationPreprocessingParameters")


@attr.s(auto_attribs=True)
class ComputationPreprocessingParameters:
    """dataframe pre-processing parameters applied to the input retrieved from the datasource, if applicable

    Attributes:
        compound_preprocessing (Union[Unset, ComputationPreprocessingParametersCompoundPreprocessing]): preprocessing to
            be applied for each node
        dataset_schema (Union[Unset, DatasetSchema]): dataset schema definition used to validate input datasets.
        filters (Union[Unset, List['LogicalFormula']]): list of filters to apply to the input dataframe (applied after
            the preprocessing is run)
        global_preprocessing (Union[Unset, PreprocessingChain]): Chain of preprocessing operations applied to the input
            dataframe
        select (Union[Unset, Select]):
    """

    compound_preprocessing: Union[Unset, "ComputationPreprocessingParametersCompoundPreprocessing"] = UNSET
    dataset_schema: Union[Unset, "DatasetSchema"] = UNSET
    filters: Union[Unset, List["LogicalFormula"]] = UNSET
    global_preprocessing: Union[Unset, "PreprocessingChain"] = UNSET
    select: Union[Unset, "Select"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        compound_preprocessing: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.compound_preprocessing, Unset):
            compound_preprocessing = self.compound_preprocessing.to_dict()

        dataset_schema: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dataset_schema, Unset):
            dataset_schema = self.dataset_schema.to_dict()

        filters: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.filters, Unset):
            filters = []
            for filters_item_data in self.filters:
                filters_item = filters_item_data.to_dict()

                filters.append(filters_item)

        global_preprocessing: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.global_preprocessing, Unset):
            global_preprocessing = self.global_preprocessing.to_dict()

        select: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.select, Unset):
            select = self.select.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if compound_preprocessing is not UNSET:
            field_dict["compoundPreprocessing"] = compound_preprocessing
        if dataset_schema is not UNSET:
            field_dict["datasetSchema"] = dataset_schema
        if filters is not UNSET:
            field_dict["filters"] = filters
        if global_preprocessing is not UNSET:
            field_dict["globalPreprocessing"] = global_preprocessing
        if select is not UNSET:
            field_dict["select"] = select

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.computation_preprocessing_parameters_compound_preprocessing import (
            ComputationPreprocessingParametersCompoundPreprocessing,
        )
        from ..models.dataset_schema import DatasetSchema
        from ..models.logical_formula import LogicalFormula
        from ..models.preprocessing_chain import PreprocessingChain
        from ..models.select import Select

        d = src_dict.copy()
        _compound_preprocessing = d.pop("compoundPreprocessing", UNSET)
        compound_preprocessing: Union[Unset, ComputationPreprocessingParametersCompoundPreprocessing]
        if isinstance(_compound_preprocessing, Unset):
            compound_preprocessing = UNSET
        else:
            compound_preprocessing = ComputationPreprocessingParametersCompoundPreprocessing.from_dict(
                _compound_preprocessing
            )

        _dataset_schema = d.pop("datasetSchema", UNSET)
        dataset_schema: Union[Unset, DatasetSchema]
        if isinstance(_dataset_schema, Unset):
            dataset_schema = UNSET
        else:
            dataset_schema = DatasetSchema.from_dict(_dataset_schema)

        filters = []
        _filters = d.pop("filters", UNSET)
        for filters_item_data in _filters or []:
            filters_item = LogicalFormula.from_dict(filters_item_data)

            filters.append(filters_item)

        _global_preprocessing = d.pop("globalPreprocessing", UNSET)
        global_preprocessing: Union[Unset, PreprocessingChain]
        if isinstance(_global_preprocessing, Unset):
            global_preprocessing = UNSET
        else:
            global_preprocessing = PreprocessingChain.from_dict(_global_preprocessing)

        _select = d.pop("select", UNSET)
        select: Union[Unset, Select]
        if isinstance(_select, Unset):
            select = UNSET
        else:
            select = Select.from_dict(_select)

        computation_preprocessing_parameters = cls(
            compound_preprocessing=compound_preprocessing,
            dataset_schema=dataset_schema,
            filters=filters,
            global_preprocessing=global_preprocessing,
            select=select,
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
