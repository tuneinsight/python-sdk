from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_data_source_query_json_body_output_data_objects_shared_i_ds import (
        PostDataSourceQueryJsonBodyOutputDataObjectsSharedIDs,
    )
    from ..models.post_data_source_query_json_body_parameters import PostDataSourceQueryJsonBodyParameters


T = TypeVar("T", bound="PostDataSourceQueryJsonBody")


@attr.s(auto_attribs=True)
class PostDataSourceQueryJsonBody:
    """
    Attributes:
        operation (Union[Unset, str]):
        output_data_objects_shared_i_ds (Union[Unset, PostDataSourceQueryJsonBodyOutputDataObjectsSharedIDs]): Map with
            of key/value pairs containing the shared IDs of the output data objects for the requested operation.
        parameters (Union[Unset, PostDataSourceQueryJsonBodyParameters]): Parameters for the requested operation.
        target_public_key (Union[Unset, str]): If specified, b64 encoded public key to encrypt the data objects with.
        target_public_key_id (Union[Unset, str]): If specified, id of the dataobject of thew public key to encrypt the
            data objects with.
    """

    operation: Union[Unset, str] = UNSET
    output_data_objects_shared_i_ds: Union[Unset, "PostDataSourceQueryJsonBodyOutputDataObjectsSharedIDs"] = UNSET
    parameters: Union[Unset, "PostDataSourceQueryJsonBodyParameters"] = UNSET
    target_public_key: Union[Unset, str] = UNSET
    target_public_key_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        operation = self.operation
        output_data_objects_shared_i_ds: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.output_data_objects_shared_i_ds, Unset):
            output_data_objects_shared_i_ds = self.output_data_objects_shared_i_ds.to_dict()

        parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = self.parameters.to_dict()

        target_public_key = self.target_public_key
        target_public_key_id = self.target_public_key_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if operation is not UNSET:
            field_dict["operation"] = operation
        if output_data_objects_shared_i_ds is not UNSET:
            field_dict["outputDataObjectsSharedIDs"] = output_data_objects_shared_i_ds
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if target_public_key is not UNSET:
            field_dict["targetPublicKey"] = target_public_key
        if target_public_key_id is not UNSET:
            field_dict["targetPublicKeyId"] = target_public_key_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.post_data_source_query_json_body_output_data_objects_shared_i_ds import (
            PostDataSourceQueryJsonBodyOutputDataObjectsSharedIDs,
        )
        from ..models.post_data_source_query_json_body_parameters import PostDataSourceQueryJsonBodyParameters

        d = src_dict.copy()
        operation = d.pop("operation", UNSET)

        _output_data_objects_shared_i_ds = d.pop("outputDataObjectsSharedIDs", UNSET)
        output_data_objects_shared_i_ds: Union[Unset, PostDataSourceQueryJsonBodyOutputDataObjectsSharedIDs]
        if isinstance(_output_data_objects_shared_i_ds, Unset):
            output_data_objects_shared_i_ds = UNSET
        else:
            output_data_objects_shared_i_ds = PostDataSourceQueryJsonBodyOutputDataObjectsSharedIDs.from_dict(
                _output_data_objects_shared_i_ds
            )

        _parameters = d.pop("parameters", UNSET)
        parameters: Union[Unset, PostDataSourceQueryJsonBodyParameters]
        if isinstance(_parameters, Unset):
            parameters = UNSET
        else:
            parameters = PostDataSourceQueryJsonBodyParameters.from_dict(_parameters)

        target_public_key = d.pop("targetPublicKey", UNSET)

        target_public_key_id = d.pop("targetPublicKeyId", UNSET)

        post_data_source_query_json_body = cls(
            operation=operation,
            output_data_objects_shared_i_ds=output_data_objects_shared_i_ds,
            parameters=parameters,
            target_public_key=target_public_key,
            target_public_key_id=target_public_key_id,
        )

        post_data_source_query_json_body.additional_properties = d
        return post_data_source_query_json_body

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
