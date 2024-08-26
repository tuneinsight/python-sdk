from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.access_scope import AccessScope
from ..models.data_selection_type import DataSelectionType
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
        preview_content_disabled (Union[Unset, None, bool]): whether to disable previewing the content (metadata only)
        store_in_database (Union[Unset, None, bool]): whether to store the selection in the database
        type (Union[Unset, DataSelectionType]):
        visibility_scope (Union[Unset, AccessScope]): defines the scope of access given to a resource
        created_at (Union[Unset, str]):
        created_by_user (Union[Unset, str]): creator of the selection
        data_source (Union[Unset, DataSource]):
        id (Union[Unset, str]): id of the selection
        num_local_records (Union[Unset, int]): holds the total number of local records from the selection (only
            displayed when the selection is saved to the database)
        preview (Union[Unset, DataSourceQueryPreview]): preview of a datasource query
        query (Union[Unset, Query]): Data source query
        remote (Union[Unset, bool]): whether the selection was fetched remotely
        remote_instance_id (Union[Unset, str]): the name of the remote instance id this selection was retrieved from.
        updated_at (Union[Unset, str]):
    """

    data_selection: Union[Unset, "ComputationDataSourceParameters"] = UNSET
    description: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    preprocessing: Union[Unset, "ComputationPreprocessingParameters"] = UNSET
    preview_content_disabled: Union[Unset, None, bool] = UNSET
    store_in_database: Union[Unset, None, bool] = UNSET
    type: Union[Unset, DataSelectionType] = UNSET
    visibility_scope: Union[Unset, AccessScope] = UNSET
    created_at: Union[Unset, str] = UNSET
    created_by_user: Union[Unset, str] = UNSET
    data_source: Union[Unset, "DataSource"] = UNSET
    id: Union[Unset, str] = UNSET
    num_local_records: Union[Unset, int] = UNSET
    preview: Union[Unset, "DataSourceQueryPreview"] = UNSET
    query: Union[Unset, "Query"] = UNSET
    remote: Union[Unset, bool] = UNSET
    remote_instance_id: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
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

        created_at = self.created_at
        created_by_user = self.created_by_user
        data_source: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data_source, Unset):
            data_source = self.data_source.to_dict()

        id = self.id
        num_local_records = self.num_local_records
        preview: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.preview, Unset):
            preview = self.preview.to_dict()

        query: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.query, Unset):
            query = self.query.to_dict()

        remote = self.remote
        remote_instance_id = self.remote_instance_id
        updated_at = self.updated_at

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
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if created_by_user is not UNSET:
            field_dict["createdByUser"] = created_by_user
        if data_source is not UNSET:
            field_dict["dataSource"] = data_source
        if id is not UNSET:
            field_dict["id"] = id
        if num_local_records is not UNSET:
            field_dict["numLocalRecords"] = num_local_records
        if preview is not UNSET:
            field_dict["preview"] = preview
        if query is not UNSET:
            field_dict["query"] = query
        if remote is not UNSET:
            field_dict["remote"] = remote
        if remote_instance_id is not UNSET:
            field_dict["remoteInstanceId"] = remote_instance_id
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

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

        created_at = d.pop("createdAt", UNSET)

        created_by_user = d.pop("createdByUser", UNSET)

        _data_source = d.pop("dataSource", UNSET)
        data_source: Union[Unset, DataSource]
        if isinstance(_data_source, Unset):
            data_source = UNSET
        else:
            data_source = DataSource.from_dict(_data_source)

        id = d.pop("id", UNSET)

        num_local_records = d.pop("numLocalRecords", UNSET)

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

        remote = d.pop("remote", UNSET)

        remote_instance_id = d.pop("remoteInstanceId", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        local_data_selection = cls(
            data_selection=data_selection,
            description=description,
            name=name,
            preprocessing=preprocessing,
            preview_content_disabled=preview_content_disabled,
            store_in_database=store_in_database,
            type=type,
            visibility_scope=visibility_scope,
            created_at=created_at,
            created_by_user=created_by_user,
            data_source=data_source,
            id=id,
            num_local_records=num_local_records,
            preview=preview,
            query=query,
            remote=remote,
            remote_instance_id=remote_instance_id,
            updated_at=updated_at,
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
