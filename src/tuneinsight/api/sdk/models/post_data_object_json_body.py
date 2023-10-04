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
        json_path (Union[Unset, str]):
        key_info (Union[Unset, KeyInfo]): information about keys
        project_id (Union[Unset, str]): Unique identifier of a project.
        query (Union[Unset, str]):
        type (Union[Unset, DataObjectType]): type of the dataobject
        data_object_shared_id (Union[Unset, str]): Shared identifier of a data object.
        encrypted (Union[Unset, bool]): indicator whether or not the uploaded dataobject is encrypted
        private_key (Union[Unset, str]): Unique identifier of a data object.
        public_key (Union[Unset, str]): Unique identifier of a data object.
        visibility_status (Union[Unset, DataObjectVisibilityStatus]): type of visibility set to the dataobject
        columns (Union[Unset, List[str]]):
        data_object_id (Union[Unset, str]): Unique identifier of a data object.
        method (Union[Unset, DataObjectCreationMethod]): Method of creation: from a data source or by
            encrypting/decrypting a data object, or simply create a new one
        session_id (Union[Unset, str]): Unique identifier of a session
        data_source_id (Union[Unset, str]): Data source adapting into data object
        shared (Union[Unset, bool]): whether the dataobject is meant to be used as a collective input
    """

    json_path: Union[Unset, str] = UNSET
    key_info: Union[Unset, "KeyInfo"] = UNSET
    project_id: Union[Unset, str] = UNSET
    query: Union[Unset, str] = UNSET
    type: Union[Unset, DataObjectType] = UNSET
    data_object_shared_id: Union[Unset, str] = UNSET
    encrypted: Union[Unset, bool] = UNSET
    private_key: Union[Unset, str] = UNSET
    public_key: Union[Unset, str] = UNSET
    visibility_status: Union[Unset, DataObjectVisibilityStatus] = UNSET
    columns: Union[Unset, List[str]] = UNSET
    data_object_id: Union[Unset, str] = UNSET
    method: Union[Unset, DataObjectCreationMethod] = UNSET
    session_id: Union[Unset, str] = UNSET
    data_source_id: Union[Unset, str] = UNSET
    shared: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        json_path = self.json_path
        key_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.key_info, Unset):
            key_info = self.key_info.to_dict()

        project_id = self.project_id
        query = self.query
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        data_object_shared_id = self.data_object_shared_id
        encrypted = self.encrypted
        private_key = self.private_key
        public_key = self.public_key
        visibility_status: Union[Unset, str] = UNSET
        if not isinstance(self.visibility_status, Unset):
            visibility_status = self.visibility_status.value

        columns: Union[Unset, List[str]] = UNSET
        if not isinstance(self.columns, Unset):
            columns = self.columns

        data_object_id = self.data_object_id
        method: Union[Unset, str] = UNSET
        if not isinstance(self.method, Unset):
            method = self.method.value

        session_id = self.session_id
        data_source_id = self.data_source_id
        shared = self.shared

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if json_path is not UNSET:
            field_dict["jsonPath"] = json_path
        if key_info is not UNSET:
            field_dict["keyInfo"] = key_info
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if query is not UNSET:
            field_dict["query"] = query
        if type is not UNSET:
            field_dict["type"] = type
        if data_object_shared_id is not UNSET:
            field_dict["dataObjectSharedId"] = data_object_shared_id
        if encrypted is not UNSET:
            field_dict["encrypted"] = encrypted
        if private_key is not UNSET:
            field_dict["privateKey"] = private_key
        if public_key is not UNSET:
            field_dict["publicKey"] = public_key
        if visibility_status is not UNSET:
            field_dict["visibilityStatus"] = visibility_status
        if columns is not UNSET:
            field_dict["columns"] = columns
        if data_object_id is not UNSET:
            field_dict["dataObjectId"] = data_object_id
        if method is not UNSET:
            field_dict["method"] = method
        if session_id is not UNSET:
            field_dict["sessionId"] = session_id
        if data_source_id is not UNSET:
            field_dict["dataSourceId"] = data_source_id
        if shared is not UNSET:
            field_dict["shared"] = shared

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.key_info import KeyInfo

        d = src_dict.copy()
        json_path = d.pop("jsonPath", UNSET)

        _key_info = d.pop("keyInfo", UNSET)
        key_info: Union[Unset, KeyInfo]
        if isinstance(_key_info, Unset):
            key_info = UNSET
        else:
            key_info = KeyInfo.from_dict(_key_info)

        project_id = d.pop("projectId", UNSET)

        query = d.pop("query", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, DataObjectType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = DataObjectType(_type)

        data_object_shared_id = d.pop("dataObjectSharedId", UNSET)

        encrypted = d.pop("encrypted", UNSET)

        private_key = d.pop("privateKey", UNSET)

        public_key = d.pop("publicKey", UNSET)

        _visibility_status = d.pop("visibilityStatus", UNSET)
        visibility_status: Union[Unset, DataObjectVisibilityStatus]
        if isinstance(_visibility_status, Unset):
            visibility_status = UNSET
        else:
            visibility_status = DataObjectVisibilityStatus(_visibility_status)

        columns = cast(List[str], d.pop("columns", UNSET))

        data_object_id = d.pop("dataObjectId", UNSET)

        _method = d.pop("method", UNSET)
        method: Union[Unset, DataObjectCreationMethod]
        if isinstance(_method, Unset):
            method = UNSET
        else:
            method = DataObjectCreationMethod(_method)

        session_id = d.pop("sessionId", UNSET)

        data_source_id = d.pop("dataSourceId", UNSET)

        shared = d.pop("shared", UNSET)

        post_data_object_json_body = cls(
            json_path=json_path,
            key_info=key_info,
            project_id=project_id,
            query=query,
            type=type,
            data_object_shared_id=data_object_shared_id,
            encrypted=encrypted,
            private_key=private_key,
            public_key=public_key,
            visibility_status=visibility_status,
            columns=columns,
            data_object_id=data_object_id,
            method=method,
            session_id=session_id,
            data_source_id=data_source_id,
            shared=shared,
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
