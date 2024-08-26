from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.access_scope import AccessScope
from ..models.data_selection_type import DataSelectionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.computation_data_source_parameters import ComputationDataSourceParameters
    from ..models.computation_preprocessing_parameters import ComputationPreprocessingParameters


T = TypeVar("T", bound="LocalDataSelectionDefinition")


@attr.s(auto_attribs=True)
class LocalDataSelectionDefinition:
    """datasource selection definition. A selection is a "query" or data selection definition to run on the datasource

    Attributes:
        data_selection (Union[Unset, ComputationDataSourceParameters]): Parameters used to query the datasource from
            each node before the computation
        description (Union[Unset, str]): optional description for the selection
        name (Union[Unset, str]): name given to the selection
        preprocessing (Union[Unset, ComputationPreprocessingParameters]): dataframe pre-processing parameters applied to
            the input retrieved from the datasource, if applicable
        preview_content_disabled (Union[Unset, None, bool]): whether to disable previewing the content (metadata only)
        store_in_database (Union[Unset, None, bool]): whether to store the selection in the database
        type (Union[Unset, DataSelectionType]):
        visibility_scope (Union[Unset, AccessScope]): defines the scope of access given to a resource
    """

    data_selection: Union[Unset, "ComputationDataSourceParameters"] = UNSET
    description: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    preprocessing: Union[Unset, "ComputationPreprocessingParameters"] = UNSET
    preview_content_disabled: Union[Unset, None, bool] = UNSET
    store_in_database: Union[Unset, None, bool] = UNSET
    type: Union[Unset, DataSelectionType] = UNSET
    visibility_scope: Union[Unset, AccessScope] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data_selection: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data_selection, Unset):
            data_selection = self.data_selection.to_dict()

        description = self.description
        name = self.name
        preprocessing: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.preprocessing, Unset):
            preprocessing = self.preprocessing.to_dict()

        preview_content_disabled = self.preview_content_disabled
        store_in_database = self.store_in_database
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        visibility_scope: Union[Unset, str] = UNSET
        if not isinstance(self.visibility_scope, Unset):
            visibility_scope = self.visibility_scope.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data_selection is not UNSET:
            field_dict["dataSelection"] = data_selection
        if description is not UNSET:
            field_dict["description"] = description
        if name is not UNSET:
            field_dict["name"] = name
        if preprocessing is not UNSET:
            field_dict["preprocessing"] = preprocessing
        if preview_content_disabled is not UNSET:
            field_dict["previewContentDisabled"] = preview_content_disabled
        if store_in_database is not UNSET:
            field_dict["storeInDatabase"] = store_in_database
        if type is not UNSET:
            field_dict["type"] = type
        if visibility_scope is not UNSET:
            field_dict["visibilityScope"] = visibility_scope

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.computation_data_source_parameters import ComputationDataSourceParameters
        from ..models.computation_preprocessing_parameters import ComputationPreprocessingParameters

        d = src_dict.copy()
        _data_selection = d.pop("dataSelection", UNSET)
        data_selection: Union[Unset, ComputationDataSourceParameters]
        if isinstance(_data_selection, Unset):
            data_selection = UNSET
        else:
            data_selection = ComputationDataSourceParameters.from_dict(_data_selection)

        description = d.pop("description", UNSET)

        name = d.pop("name", UNSET)

        _preprocessing = d.pop("preprocessing", UNSET)
        preprocessing: Union[Unset, ComputationPreprocessingParameters]
        if isinstance(_preprocessing, Unset):
            preprocessing = UNSET
        else:
            preprocessing = ComputationPreprocessingParameters.from_dict(_preprocessing)

        preview_content_disabled = d.pop("previewContentDisabled", UNSET)

        store_in_database = d.pop("storeInDatabase", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, DataSelectionType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = DataSelectionType(_type)

        _visibility_scope = d.pop("visibilityScope", UNSET)
        visibility_scope: Union[Unset, AccessScope]
        if isinstance(_visibility_scope, Unset):
            visibility_scope = UNSET
        else:
            visibility_scope = AccessScope(_visibility_scope)

        local_data_selection_definition = cls(
            data_selection=data_selection,
            description=description,
            name=name,
            preprocessing=preprocessing,
            preview_content_disabled=preview_content_disabled,
            store_in_database=store_in_database,
            type=type,
            visibility_scope=visibility_scope,
        )

        local_data_selection_definition.additional_properties = d
        return local_data_selection_definition

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
