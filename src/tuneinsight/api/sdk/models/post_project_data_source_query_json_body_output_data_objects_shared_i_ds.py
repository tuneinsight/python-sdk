from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="PostProjectDataSourceQueryJsonBodyOutputDataObjectsSharedIDs")


@attr.s(auto_attribs=True)
class PostProjectDataSourceQueryJsonBodyOutputDataObjectsSharedIDs:
    """(Only for node-to-node) Map with of key/value pairs containing the shared IDs of the output data objects for the
    requested operation.

    """

    additional_properties: Dict[str, str] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        post_project_data_source_query_json_body_output_data_objects_shared_i_ds = cls()

        post_project_data_source_query_json_body_output_data_objects_shared_i_ds.additional_properties = d
        return post_project_data_source_query_json_body_output_data_objects_shared_i_ds

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> str:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: str) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
