from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.data_object_creation_method import DataObjectCreationMethod
from ..models.data_object_type import DataObjectType
from ..models.data_object_visibility_status import DataObjectVisibilityStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.key_info import KeyInfo


T = TypeVar("T", bound="PostDataObjectJsonBody")


@attr.s(auto_attribs=True)
class PostDataObjectJsonBody:
    """
    Attributes:
        query (Union[Unset, str]):
        visibility_status (Union[Unset, DataObjectVisibilityStatus]): type of visibility set to the dataobject
        json_path (Union[Unset, str]): JsonPath expression to retrieve data from within JSON-structured data.
        key_info (Union[Unset, KeyInfo]): information about keys
        public_key (Union[Unset, str]): Unique identifier of a data object.
        data_object_id (Union[Unset, str]): Unique identifier of a data object.
        data_object_shared_id (Union[Unset, str]): Shared identifier of a data object.
        method (Union[Unset, DataObjectCreationMethod]): Method of creation: from a data source or by
            encrypting/decrypting a data object, or simply create a new one
        private_key (Union[Unset, str]): Unique identifier of a data object.
        project_id (Union[Unset, str]): Unique identifier of a project.
        type (Union[Unset, DataObjectType]): type of the dataobject
        columns (Union[Unset, List[str]]):
        data_source_id (Union[Unset, str]): Data source adapting into data object
        shared (Union[Unset, bool]): whether the dataobject is meant to be used as a collective input
        encrypted (Union[Unset, bool]): indicator whether or not the uploaded dataobject is encrypted
        session_id (Union[Unset, str]): Unique identifier of a session
    """

    query: Union[Unset, str] = UNSET
    visibility_status: Union[Unset, DataObjectVisibilityStatus] = UNSET
    json_path: Union[Unset, str] = UNSET
    key_info: Union[Unset, "KeyInfo"] = UNSET
    public_key: Union[Unset, str] = UNSET
    data_object_id: Union[Unset, str] = UNSET
    data_object_shared_id: Union[Unset, str] = UNSET
    method: Union[Unset, DataObjectCreationMethod] = UNSET
    private_key: Union[Unset, str] = UNSET
    project_id: Union[Unset, str] = UNSET
    type: Union[Unset, DataObjectType] = UNSET
    columns: Union[Unset, List[str]] = UNSET
    data_source_id: Union[Unset, str] = UNSET
    shared: Union[Unset, bool] = UNSET
    encrypted: Union[Unset, bool] = UNSET
    session_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        query = self.query
        visibility_status: Union[Unset, str] = UNSET
        if not isinstance(self.visibility_status, Unset):
            visibility_status = self.visibility_status.value

        json_path = self.json_path
        key_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.key_info, Unset):
            key_info = self.key_info.to_dict()

        public_key = self.public_key
        data_object_id = self.data_object_id
        data_object_shared_id = self.data_object_shared_id
        method: Union[Unset, str] = UNSET
        if not isinstance(self.method, Unset):
            method = self.method.value

        private_key = self.private_key
        project_id = self.project_id
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        columns: Union[Unset, List[str]] = UNSET
        if not isinstance(self.columns, Unset):
            columns = self.columns

        data_source_id = self.data_source_id
        shared = self.shared
        encrypted = self.encrypted
        session_id = self.session_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if query is not UNSET:
            field_dict["query"] = query
        if visibility_status is not UNSET:
            field_dict["visibilityStatus"] = visibility_status
        if json_path is not UNSET:
            field_dict["jsonPath"] = json_path
        if key_info is not UNSET:
            field_dict["keyInfo"] = key_info
        if public_key is not UNSET:
            field_dict["publicKey"] = public_key
        if data_object_id is not UNSET:
            field_dict["dataObjectId"] = data_object_id
        if data_object_shared_id is not UNSET:
            field_dict["dataObjectSharedId"] = data_object_shared_id
        if method is not UNSET:
            field_dict["method"] = method
        if private_key is not UNSET:
            field_dict["privateKey"] = private_key
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if type is not UNSET:
            field_dict["type"] = type
        if columns is not UNSET:
            field_dict["columns"] = columns
        if data_source_id is not UNSET:
            field_dict["dataSourceId"] = data_source_id
        if shared is not UNSET:
            field_dict["shared"] = shared
        if encrypted is not UNSET:
            field_dict["encrypted"] = encrypted
        if session_id is not UNSET:
            field_dict["sessionId"] = session_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.key_info import KeyInfo

        d = src_dict.copy()
        query = d.pop("query", UNSET)

        _visibility_status = d.pop("visibilityStatus", UNSET)
        visibility_status: Union[Unset, DataObjectVisibilityStatus]
        if isinstance(_visibility_status, Unset):
            visibility_status = UNSET
        else:
            visibility_status = DataObjectVisibilityStatus(_visibility_status)

        json_path = d.pop("jsonPath", UNSET)

        _key_info = d.pop("keyInfo", UNSET)
        key_info: Union[Unset, KeyInfo]
        if isinstance(_key_info, Unset):
            key_info = UNSET
        else:
            key_info = KeyInfo.from_dict(_key_info)

        public_key = d.pop("publicKey", UNSET)

        data_object_id = d.pop("dataObjectId", UNSET)

        data_object_shared_id = d.pop("dataObjectSharedId", UNSET)

        _method = d.pop("method", UNSET)
        method: Union[Unset, DataObjectCreationMethod]
        if isinstance(_method, Unset):
            method = UNSET
        else:
            method = DataObjectCreationMethod(_method)

        private_key = d.pop("privateKey", UNSET)

        project_id = d.pop("projectId", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, DataObjectType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = DataObjectType(_type)

        columns = cast(List[str], d.pop("columns", UNSET))

        data_source_id = d.pop("dataSourceId", UNSET)

        shared = d.pop("shared", UNSET)

        encrypted = d.pop("encrypted", UNSET)

        session_id = d.pop("sessionId", UNSET)

        post_data_object_json_body = cls(
            query=query,
            visibility_status=visibility_status,
            json_path=json_path,
            key_info=key_info,
            public_key=public_key,
            data_object_id=data_object_id,
            data_object_shared_id=data_object_shared_id,
            method=method,
            private_key=private_key,
            project_id=project_id,
            type=type,
            columns=columns,
            data_source_id=data_source_id,
            shared=shared,
            encrypted=encrypted,
            session_id=session_id,
        )

        post_data_object_json_body.additional_properties = d
        return post_data_object_json_body

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
