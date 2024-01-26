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
        columns (Union[Unset, List[str]]):
        data_object_id (Union[Unset, str]): Unique identifier of a data object.
        shared (Union[Unset, bool]): whether the dataobject is meant to be used as a collective input
        visibility_status (Union[Unset, DataObjectVisibilityStatus]): type of visibility set to the dataobject
        data_object_shared_id (Union[Unset, str]): Shared identifier of a data object.
        json_path (Union[Unset, str]):
        private_key (Union[Unset, str]): Unique identifier of a data object.
        public_key (Union[Unset, str]): Unique identifier of a data object.
        query (Union[Unset, str]):
        session_id (Union[Unset, str]): Unique identifier of a session
        type (Union[Unset, DataObjectType]): type of the dataobject
        encrypted (Union[Unset, bool]): indicator whether or not the uploaded dataobject is encrypted
        method (Union[Unset, DataObjectCreationMethod]): Method of creation: from a data source or by
            encrypting/decrypting a data object, or simply create a new one
        project_id (Union[Unset, str]): Unique identifier of a project.
        data_source_id (Union[Unset, str]): Data source adapting into data object
        key_info (Union[Unset, KeyInfo]): information about keys
    """

    columns: Union[Unset, List[str]] = UNSET
    data_object_id: Union[Unset, str] = UNSET
    shared: Union[Unset, bool] = UNSET
    visibility_status: Union[Unset, DataObjectVisibilityStatus] = UNSET
    data_object_shared_id: Union[Unset, str] = UNSET
    json_path: Union[Unset, str] = UNSET
    private_key: Union[Unset, str] = UNSET
    public_key: Union[Unset, str] = UNSET
    query: Union[Unset, str] = UNSET
    session_id: Union[Unset, str] = UNSET
    type: Union[Unset, DataObjectType] = UNSET
    encrypted: Union[Unset, bool] = UNSET
    method: Union[Unset, DataObjectCreationMethod] = UNSET
    project_id: Union[Unset, str] = UNSET
    data_source_id: Union[Unset, str] = UNSET
    key_info: Union[Unset, "KeyInfo"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        columns: Union[Unset, List[str]] = UNSET
        if not isinstance(self.columns, Unset):
            columns = self.columns

        data_object_id = self.data_object_id
        shared = self.shared
        visibility_status: Union[Unset, str] = UNSET
        if not isinstance(self.visibility_status, Unset):
            visibility_status = self.visibility_status.value

        data_object_shared_id = self.data_object_shared_id
        json_path = self.json_path
        private_key = self.private_key
        public_key = self.public_key
        query = self.query
        session_id = self.session_id
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        encrypted = self.encrypted
        method: Union[Unset, str] = UNSET
        if not isinstance(self.method, Unset):
            method = self.method.value

        project_id = self.project_id
        data_source_id = self.data_source_id
        key_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.key_info, Unset):
            key_info = self.key_info.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if columns is not UNSET:
            field_dict["columns"] = columns
        if data_object_id is not UNSET:
            field_dict["dataObjectId"] = data_object_id
        if shared is not UNSET:
            field_dict["shared"] = shared
        if visibility_status is not UNSET:
            field_dict["visibilityStatus"] = visibility_status
        if data_object_shared_id is not UNSET:
            field_dict["dataObjectSharedId"] = data_object_shared_id
        if json_path is not UNSET:
            field_dict["jsonPath"] = json_path
        if private_key is not UNSET:
            field_dict["privateKey"] = private_key
        if public_key is not UNSET:
            field_dict["publicKey"] = public_key
        if query is not UNSET:
            field_dict["query"] = query
        if session_id is not UNSET:
            field_dict["sessionId"] = session_id
        if type is not UNSET:
            field_dict["type"] = type
        if encrypted is not UNSET:
            field_dict["encrypted"] = encrypted
        if method is not UNSET:
            field_dict["method"] = method
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if data_source_id is not UNSET:
            field_dict["dataSourceId"] = data_source_id
        if key_info is not UNSET:
            field_dict["keyInfo"] = key_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.key_info import KeyInfo

        d = src_dict.copy()
        columns = cast(List[str], d.pop("columns", UNSET))

        data_object_id = d.pop("dataObjectId", UNSET)

        shared = d.pop("shared", UNSET)

        _visibility_status = d.pop("visibilityStatus", UNSET)
        visibility_status: Union[Unset, DataObjectVisibilityStatus]
        if isinstance(_visibility_status, Unset):
            visibility_status = UNSET
        else:
            visibility_status = DataObjectVisibilityStatus(_visibility_status)

        data_object_shared_id = d.pop("dataObjectSharedId", UNSET)

        json_path = d.pop("jsonPath", UNSET)

        private_key = d.pop("privateKey", UNSET)

        public_key = d.pop("publicKey", UNSET)

        query = d.pop("query", UNSET)

        session_id = d.pop("sessionId", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, DataObjectType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = DataObjectType(_type)

        encrypted = d.pop("encrypted", UNSET)

        _method = d.pop("method", UNSET)
        method: Union[Unset, DataObjectCreationMethod]
        if isinstance(_method, Unset):
            method = UNSET
        else:
            method = DataObjectCreationMethod(_method)

        project_id = d.pop("projectId", UNSET)

        data_source_id = d.pop("dataSourceId", UNSET)

        _key_info = d.pop("keyInfo", UNSET)
        key_info: Union[Unset, KeyInfo]
        if isinstance(_key_info, Unset):
            key_info = UNSET
        else:
            key_info = KeyInfo.from_dict(_key_info)

        post_data_object_json_body = cls(
            columns=columns,
            data_object_id=data_object_id,
            shared=shared,
            visibility_status=visibility_status,
            data_object_shared_id=data_object_shared_id,
            json_path=json_path,
            private_key=private_key,
            public_key=public_key,
            query=query,
            session_id=session_id,
            type=type,
            encrypted=encrypted,
            method=method,
            project_id=project_id,
            data_source_id=data_source_id,
            key_info=key_info,
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
