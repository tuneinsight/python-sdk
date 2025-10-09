from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetInfosResponse200CatalogStatus")


@attr.s(auto_attribs=True)
class GetInfosResponse200CatalogStatus:
    """Status of the node's catalog

    Attributes:
        last_updated (Union[Unset, str]): Timestamp of the last catalog update
        progress (Union[Unset, float]): Progress percentage of catalog building process
    """

    last_updated: Union[Unset, str] = UNSET
    progress: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        last_updated = self.last_updated
        progress = self.progress

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
        if progress is not UNSET:
            field_dict["progress"] = progress

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        last_updated = d.pop("lastUpdated", UNSET)

        progress = d.pop("progress", UNSET)

        get_infos_response_200_catalog_status = cls(
            last_updated=last_updated,
            progress=progress,
        )

        get_infos_response_200_catalog_status.additional_properties = d
        return get_infos_response_200_catalog_status

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
