from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_source_query import DataSourceQuery
    from ..models.preprocessing_chain import PreprocessingChain
    from ..models.screening_operation import ScreeningOperation


T = TypeVar("T", bound="DataPreparationSessionDefinition")


@attr.s(auto_attribs=True)
class DataPreparationSessionDefinition:
    """part of the data preparation session defined by the user.

    Attributes:
        current_stage (Union[Unset, None, int]): current stage in the frontend data preparation session configuration
            steps.
        data_source_id (Union[Unset, None, str]): Unique identifier of a data source.
        name (Union[Unset, str]): name given to this session.
        operations (Union[Unset, List['ScreeningOperation']]): list of screening operations.
        preprocessing (Union[Unset, PreprocessingChain]): Chain of preprocessing operations applied to the input
            dataframe
        query (Union[Unset, DataSourceQuery]): schema used for the query
        row_identifier (Union[Unset, None, str]): column of the screened dataset to use as a unique row identifier.
            If empty, then the rows are identified using their index, which can lead to issues if rows are reordered in the
            underlying data source.
    """

    current_stage: Union[Unset, None, int] = UNSET
    data_source_id: Union[Unset, None, str] = UNSET
    name: Union[Unset, str] = UNSET
    operations: Union[Unset, List["ScreeningOperation"]] = UNSET
    preprocessing: Union[Unset, "PreprocessingChain"] = UNSET
    query: Union[Unset, "DataSourceQuery"] = UNSET
    row_identifier: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        current_stage = self.current_stage
        data_source_id = self.data_source_id
        name = self.name
        operations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.operations, Unset):
            operations = []
            for operations_item_data in self.operations:
                operations_item = operations_item_data.to_dict()

                operations.append(operations_item)

        preprocessing: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.preprocessing, Unset):
            preprocessing = self.preprocessing.to_dict()

        query: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.query, Unset):
            query = self.query.to_dict()

        row_identifier = self.row_identifier

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current_stage is not UNSET:
            field_dict["currentStage"] = current_stage
        if data_source_id is not UNSET:
            field_dict["dataSourceId"] = data_source_id
        if name is not UNSET:
            field_dict["name"] = name
        if operations is not UNSET:
            field_dict["operations"] = operations
        if preprocessing is not UNSET:
            field_dict["preprocessing"] = preprocessing
        if query is not UNSET:
            field_dict["query"] = query
        if row_identifier is not UNSET:
            field_dict["rowIdentifier"] = row_identifier

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.data_source_query import DataSourceQuery
        from ..models.preprocessing_chain import PreprocessingChain
        from ..models.screening_operation import ScreeningOperation

        d = src_dict.copy()
        current_stage = d.pop("currentStage", UNSET)

        data_source_id = d.pop("dataSourceId", UNSET)

        name = d.pop("name", UNSET)

        operations = []
        _operations = d.pop("operations", UNSET)
        for operations_item_data in _operations or []:
            operations_item = ScreeningOperation.from_dict(operations_item_data)

            operations.append(operations_item)

        _preprocessing = d.pop("preprocessing", UNSET)
        preprocessing: Union[Unset, PreprocessingChain]
        if isinstance(_preprocessing, Unset):
            preprocessing = UNSET
        else:
            preprocessing = PreprocessingChain.from_dict(_preprocessing)

        _query = d.pop("query", UNSET)
        query: Union[Unset, DataSourceQuery]
        if isinstance(_query, Unset):
            query = UNSET
        else:
            query = DataSourceQuery.from_dict(_query)

        row_identifier = d.pop("rowIdentifier", UNSET)

        data_preparation_session_definition = cls(
            current_stage=current_stage,
            data_source_id=data_source_id,
            name=name,
            operations=operations,
            preprocessing=preprocessing,
            query=query,
            row_identifier=row_identifier,
        )

        data_preparation_session_definition.additional_properties = d
        return data_preparation_session_definition

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
