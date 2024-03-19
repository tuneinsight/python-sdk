from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.post_project_data_source_query_json_body_aggregation_type import (
    PostProjectDataSourceQueryJsonBodyAggregationType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_project_data_source_query_json_body_output_data_objects_shared_i_ds import (
        PostProjectDataSourceQueryJsonBodyOutputDataObjectsSharedIDs,
    )
    from ..models.post_project_data_source_query_json_body_parameters import (
        PostProjectDataSourceQueryJsonBodyParameters,
    )


T = TypeVar("T", bound="PostProjectDataSourceQueryJsonBody")


@attr.s(auto_attribs=True)
class PostProjectDataSourceQueryJsonBody:
    """
    Attributes:
        operation (Union[Unset, str]): Is the string describing the type of operation to run in the data source
        parameters (Union[Unset, PostProjectDataSourceQueryJsonBodyParameters]): Parameters for the requested operation.
        wait (Union[Unset, bool]): If true, the request will wait for the result (synchronous). If false, the request
            will return immediately with a query id (asynchronous). Default: True.
        broadcast (Union[Unset, bool]): Temporary field. Always set to false. Only used for server-server communication
        output_data_objects_names (Union[Unset, List[str]]): (Only for client) List of output data object names for the
            requested operation. It should match the specific data source requirements. (e.g. ["count", "patientList"])
        output_data_objects_shared_i_ds (Union[Unset, PostProjectDataSourceQueryJsonBodyOutputDataObjectsSharedIDs]):
            (Only for node-to-node) Map with of key/value pairs containing the shared IDs of the output data objects for the
            requested operation.
        target_public_key (Union[Unset, str]): if provided, the results are key switched to this public key (should be
            encoded in base64 from its bytes representation) and the resulting ciphertables returned
        target_public_key_id (Union[Unset, str]): If specified, id of the dataobject of thew public key to encrypt the
            data objects with.
        aggregation_type (Union[Unset, PostProjectDataSourceQueryJsonBodyAggregationType]): Requests if and how results
            should be aggregated across the nodes
    """

    operation: Union[Unset, str] = UNSET
    parameters: Union[Unset, "PostProjectDataSourceQueryJsonBodyParameters"] = UNSET
    wait: Union[Unset, bool] = True
    broadcast: Union[Unset, bool] = UNSET
    output_data_objects_names: Union[Unset, List[str]] = UNSET
    output_data_objects_shared_i_ds: Union[Unset, "PostProjectDataSourceQueryJsonBodyOutputDataObjectsSharedIDs"] = (
        UNSET
    )
    target_public_key: Union[Unset, str] = UNSET
    target_public_key_id: Union[Unset, str] = UNSET
    aggregation_type: Union[Unset, PostProjectDataSourceQueryJsonBodyAggregationType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        operation = self.operation
        parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = self.parameters.to_dict()

        wait = self.wait
        broadcast = self.broadcast
        output_data_objects_names: Union[Unset, List[str]] = UNSET
        if not isinstance(self.output_data_objects_names, Unset):
            output_data_objects_names = self.output_data_objects_names

        output_data_objects_shared_i_ds: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.output_data_objects_shared_i_ds, Unset):
            output_data_objects_shared_i_ds = self.output_data_objects_shared_i_ds.to_dict()

        target_public_key = self.target_public_key
        target_public_key_id = self.target_public_key_id
        aggregation_type: Union[Unset, str] = UNSET
        if not isinstance(self.aggregation_type, Unset):
            aggregation_type = self.aggregation_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if operation is not UNSET:
            field_dict["operation"] = operation
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if wait is not UNSET:
            field_dict["wait"] = wait
        if broadcast is not UNSET:
            field_dict["broadcast"] = broadcast
        if output_data_objects_names is not UNSET:
            field_dict["outputDataObjectsNames"] = output_data_objects_names
        if output_data_objects_shared_i_ds is not UNSET:
            field_dict["outputDataObjectsSharedIDs"] = output_data_objects_shared_i_ds
        if target_public_key is not UNSET:
            field_dict["targetPublicKey"] = target_public_key
        if target_public_key_id is not UNSET:
            field_dict["targetPublicKeyId"] = target_public_key_id
        if aggregation_type is not UNSET:
            field_dict["aggregationType"] = aggregation_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.post_project_data_source_query_json_body_output_data_objects_shared_i_ds import (
            PostProjectDataSourceQueryJsonBodyOutputDataObjectsSharedIDs,
        )
        from ..models.post_project_data_source_query_json_body_parameters import (
            PostProjectDataSourceQueryJsonBodyParameters,
        )

        d = src_dict.copy()
        operation = d.pop("operation", UNSET)

        _parameters = d.pop("parameters", UNSET)
        parameters: Union[Unset, PostProjectDataSourceQueryJsonBodyParameters]
        if isinstance(_parameters, Unset):
            parameters = UNSET
        else:
            parameters = PostProjectDataSourceQueryJsonBodyParameters.from_dict(_parameters)

        wait = d.pop("wait", UNSET)

        broadcast = d.pop("broadcast", UNSET)

        output_data_objects_names = cast(List[str], d.pop("outputDataObjectsNames", UNSET))

        _output_data_objects_shared_i_ds = d.pop("outputDataObjectsSharedIDs", UNSET)
        output_data_objects_shared_i_ds: Union[Unset, PostProjectDataSourceQueryJsonBodyOutputDataObjectsSharedIDs]
        if isinstance(_output_data_objects_shared_i_ds, Unset):
            output_data_objects_shared_i_ds = UNSET
        else:
            output_data_objects_shared_i_ds = PostProjectDataSourceQueryJsonBodyOutputDataObjectsSharedIDs.from_dict(
                _output_data_objects_shared_i_ds
            )

        target_public_key = d.pop("targetPublicKey", UNSET)

        target_public_key_id = d.pop("targetPublicKeyId", UNSET)

        _aggregation_type = d.pop("aggregationType", UNSET)
        aggregation_type: Union[Unset, PostProjectDataSourceQueryJsonBodyAggregationType]
        if isinstance(_aggregation_type, Unset):
            aggregation_type = UNSET
        else:
            aggregation_type = PostProjectDataSourceQueryJsonBodyAggregationType(_aggregation_type)

        post_project_data_source_query_json_body = cls(
            operation=operation,
            parameters=parameters,
            wait=wait,
            broadcast=broadcast,
            output_data_objects_names=output_data_objects_names,
            output_data_objects_shared_i_ds=output_data_objects_shared_i_ds,
            target_public_key=target_public_key,
            target_public_key_id=target_public_key_id,
            aggregation_type=aggregation_type,
        )

        post_project_data_source_query_json_body.additional_properties = d
        return post_project_data_source_query_json_body

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
