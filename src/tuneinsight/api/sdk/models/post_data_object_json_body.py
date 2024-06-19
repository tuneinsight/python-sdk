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
        key_info (Union[Unset, KeyInfo]): information about keys
        type (Union[Unset, DataObjectType]): type of the dataobject
        columns (Union[Unset, List[str]]):
        data_object_shared_id (Union[Unset, str]): Shared identifier of a data object.
        data_source_id (Union[Unset, str]): Data source adapting into data object
        json_path (Union[Unset, str]): JsonPath expression to retrieve data from within JSON-structured data.
        method (Union[Unset, DataObjectCreationMethod]): Method of creation: from a data source or by
            encrypting/decrypting a data object, or simply create a new one
        query (Union[Unset, str]):
        data_object_id (Union[Unset, str]): Unique identifier of a data object.
        encrypted (Union[Unset, bool]): indicator whether or not the uploaded dataobject is encrypted
        project_id (Union[Unset, str]): Unique identifier of a project.
        session_id (Union[Unset, str]): Unique identifier of a session
        shared (Union[Unset, bool]): whether the dataobject is meant to be used as a collective input
        visibility_status (Union[Unset, DataObjectVisibilityStatus]): type of visibility set to the dataobject
        private_key (Union[Unset, str]): Unique identifier of a data object.
        public_key (Union[Unset, str]): Unique identifier of a data object.
    """

    key_info: Union[Unset, "KeyInfo"] = UNSET
    type: Union[Unset, DataObjectType] = UNSET
    columns: Union[Unset, List[str]] = UNSET
    data_object_shared_id: Union[Unset, str] = UNSET
    data_source_id: Union[Unset, str] = UNSET
    json_path: Union[Unset, str] = UNSET
    method: Union[Unset, DataObjectCreationMethod] = UNSET
    query: Union[Unset, str] = UNSET
    data_object_id: Union[Unset, str] = UNSET
    encrypted: Union[Unset, bool] = UNSET
    project_id: Union[Unset, str] = UNSET
    session_id: Union[Unset, str] = UNSET
    shared: Union[Unset, bool] = UNSET
    visibility_status: Union[Unset, DataObjectVisibilityStatus] = UNSET
    private_key: Union[Unset, str] = UNSET
    public_key: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.key_info, Unset):
            key_info = self.key_info.to_dict()

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        columns: Union[Unset, List[str]] = UNSET
        if not isinstance(self.columns, Unset):
            columns = self.columns

        data_object_shared_id = self.data_object_shared_id
        data_source_id = self.data_source_id
        json_path = self.json_path
        method: Union[Unset, str] = UNSET
        if not isinstance(self.method, Unset):
            method = self.method.value

        query = self.query
        data_object_id = self.data_object_id
        encrypted = self.encrypted
        project_id = self.project_id
        session_id = self.session_id
        shared = self.shared
        visibility_status: Union[Unset, str] = UNSET
        if not isinstance(self.visibility_status, Unset):
            visibility_status = self.visibility_status.value

        private_key = self.private_key
        public_key = self.public_key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key_info is not UNSET:
            field_dict["keyInfo"] = key_info
        if type is not UNSET:
            field_dict["type"] = type
        if columns is not UNSET:
            field_dict["columns"] = columns
        if data_object_shared_id is not UNSET:
            field_dict["dataObjectSharedId"] = data_object_shared_id
        if data_source_id is not UNSET:
            field_dict["dataSourceId"] = data_source_id
        if json_path is not UNSET:
            field_dict["jsonPath"] = json_path
        if method is not UNSET:
            field_dict["method"] = method
        if query is not UNSET:
            field_dict["query"] = query
        if data_object_id is not UNSET:
            field_dict["dataObjectId"] = data_object_id
        if encrypted is not UNSET:
            field_dict["encrypted"] = encrypted
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if session_id is not UNSET:
            field_dict["sessionId"] = session_id
        if shared is not UNSET:
            field_dict["shared"] = shared
        if visibility_status is not UNSET:
            field_dict["visibilityStatus"] = visibility_status
        if private_key is not UNSET:
            field_dict["privateKey"] = private_key
        if public_key is not UNSET:
            field_dict["publicKey"] = public_key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.key_info import KeyInfo

        d = src_dict.copy()
        _key_info = d.pop("keyInfo", UNSET)
        key_info: Union[Unset, KeyInfo]
        if isinstance(_key_info, Unset):
            key_info = UNSET
        else:
            key_info = KeyInfo.from_dict(_key_info)

        _type = d.pop("type", UNSET)
        type: Union[Unset, DataObjectType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = DataObjectType(_type)

        columns = cast(List[str], d.pop("columns", UNSET))

        data_object_shared_id = d.pop("dataObjectSharedId", UNSET)

        data_source_id = d.pop("dataSourceId", UNSET)

        json_path = d.pop("jsonPath", UNSET)

        _method = d.pop("method", UNSET)
        method: Union[Unset, DataObjectCreationMethod]
        if isinstance(_method, Unset):
            method = UNSET
        else:
            method = DataObjectCreationMethod(_method)

        query = d.pop("query", UNSET)

        data_object_id = d.pop("dataObjectId", UNSET)

        encrypted = d.pop("encrypted", UNSET)

        project_id = d.pop("projectId", UNSET)

        session_id = d.pop("sessionId", UNSET)

        shared = d.pop("shared", UNSET)

        _visibility_status = d.pop("visibilityStatus", UNSET)
        visibility_status: Union[Unset, DataObjectVisibilityStatus]
        if isinstance(_visibility_status, Unset):
            visibility_status = UNSET
        else:
            visibility_status = DataObjectVisibilityStatus(_visibility_status)

        private_key = d.pop("privateKey", UNSET)

        public_key = d.pop("publicKey", UNSET)

        post_data_object_json_body = cls(
            key_info=key_info,
            type=type,
            columns=columns,
            data_object_shared_id=data_object_shared_id,
            data_source_id=data_source_id,
            json_path=json_path,
            method=method,
            query=query,
            data_object_id=data_object_id,
            encrypted=encrypted,
            project_id=project_id,
            session_id=session_id,
            shared=shared,
            visibility_status=visibility_status,
            private_key=private_key,
            public_key=public_key,
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
