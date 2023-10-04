from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.computation_data_source_parameters import ComputationDataSourceParameters
    from ..models.computation_preprocessing_parameters import ComputationPreprocessingParameters
    from ..models.data_source import DataSource
    from ..models.data_source_query_preview import DataSourceQueryPreview
    from ..models.query import Query


T = TypeVar("T", bound="LocalDataSelection")


@attr.s(auto_attribs=True)
class LocalDataSelection:
    """selection to retrieve data from the datasource and preprocess it

    Attributes:
        data_selection (Union[Unset, ComputationDataSourceParameters]): Parameters used to query the datasource from
            each node before the computation
        description (Union[Unset, str]): optional description for the selection
        name (Union[Unset, str]): name given to the selection
        preprocessing (Union[Unset, ComputationPreprocessingParameters]): dataframe pre-processing parameters applied to
            the input retrieved from the datasource, if applicable
        updated_at (Union[Unset, str]):
        created_at (Union[Unset, str]):
        created_by_user (Union[Unset, str]): creator of the selection
        data_source (Union[Unset, DataSource]):
        id (Union[Unset, str]): id of the selection
        preview (Union[Unset, DataSourceQueryPreview]): preview of a datasource query
        query (Union[Unset, Query]): Data source query
    """

    data_selection: Union[Unset, "ComputationDataSourceParameters"] = UNSET
    description: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    preprocessing: Union[Unset, "ComputationPreprocessingParameters"] = UNSET
    updated_at: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    created_by_user: Union[Unset, str] = UNSET
    data_source: Union[Unset, "DataSource"] = UNSET
    id: Union[Unset, str] = UNSET
    preview: Union[Unset, "DataSourceQueryPreview"] = UNSET
    query: Union[Unset, "Query"] = UNSET
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

        updated_at = self.updated_at
        created_at = self.created_at
        created_by_user = self.created_by_user
        data_source: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data_source, Unset):
            data_source = self.data_source.to_dict()

        id = self.id
        preview: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.preview, Unset):
            preview = self.preview.to_dict()

        query: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.query, Unset):
            query = self.query.to_dict()

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
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if created_by_user is not UNSET:
            field_dict["createdByUser"] = created_by_user
        if data_source is not UNSET:
            field_dict["dataSource"] = data_source
        if id is not UNSET:
            field_dict["id"] = id
        if preview is not UNSET:
            field_dict["preview"] = preview
        if query is not UNSET:
            field_dict["query"] = query

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.computation_data_source_parameters import ComputationDataSourceParameters
        from ..models.computation_preprocessing_parameters import ComputationPreprocessingParameters
        from ..models.data_source import DataSource
        from ..models.data_source_query_preview import DataSourceQueryPreview
        from ..models.query import Query

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

        updated_at = d.pop("updatedAt", UNSET)

        created_at = d.pop("createdAt", UNSET)

        created_by_user = d.pop("createdByUser", UNSET)

        _data_source = d.pop("dataSource", UNSET)
        data_source: Union[Unset, DataSource]
        if isinstance(_data_source, Unset):
            data_source = UNSET
        else:
            data_source = DataSource.from_dict(_data_source)

        id = d.pop("id", UNSET)

        _preview = d.pop("preview", UNSET)
        preview: Union[Unset, DataSourceQueryPreview]
        if isinstance(_preview, Unset):
            preview = UNSET
        else:
            preview = DataSourceQueryPreview.from_dict(_preview)

        _query = d.pop("query", UNSET)
        query: Union[Unset, Query]
        if isinstance(_query, Unset):
            query = UNSET
        else:
            query = Query.from_dict(_query)

        local_data_selection = cls(
            data_selection=data_selection,
            description=description,
            name=name,
            preprocessing=preprocessing,
            updated_at=updated_at,
            created_at=created_at,
            created_by_user=created_by_user,
            data_source=data_source,
            id=id,
            preview=preview,
            query=query,
        )

        local_data_selection.additional_properties = d
        return local_data_selection

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
