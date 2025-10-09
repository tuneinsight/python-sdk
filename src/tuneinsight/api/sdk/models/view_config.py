from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ViewConfig")


@attr.s(auto_attribs=True)
class ViewConfig:
    """holds data source parameters that are applicable only for data views.

    Attributes:
        base_data_source_id (Union[Unset, None, str]): Unique identifier of a data source.
        data_preparation_session_id (Union[Unset, str]): id of the data preparation session used on this data source.
    """

    base_data_source_id: Union[Unset, None, str] = UNSET
    data_preparation_session_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        base_data_source_id = self.base_data_source_id
        data_preparation_session_id = self.data_preparation_session_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if base_data_source_id is not UNSET:
            field_dict["baseDataSourceId"] = base_data_source_id
        if data_preparation_session_id is not UNSET:
            field_dict["dataPreparationSessionId"] = data_preparation_session_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        base_data_source_id = d.pop("baseDataSourceId", UNSET)

        data_preparation_session_id = d.pop("dataPreparationSessionId", UNSET)

        view_config = cls(
            base_data_source_id=base_data_source_id,
            data_preparation_session_id=data_preparation_session_id,
        )

        view_config.additional_properties = d
        return view_config

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
