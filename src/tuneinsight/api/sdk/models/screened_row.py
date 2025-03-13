from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ScreenedRow")


@attr.s(auto_attribs=True)
class ScreenedRow:
    """Represents a row from a dataset that is being screened. This model contains the original data,
    as well as the data after applying the screening operations.

        Attributes:
            data (Union[Unset, List[str]]): original data from the row.
            filtered_by_operation (Union[Unset, int]): index of the operation that filtered out this data.
            index (Union[Unset, int]): index of the row in the original data.
            reason (Union[Unset, str]): reason why this data point was discarded
            screened (Union[Unset, bool]): Indicates if the row has been screened, meaning that the screening process has
                approved/kept this row.
                This is set to false when the row is discarded by a screening operation that invalidates it.
            screened_data (Union[Unset, List[str]]): the data after applying the screening operations.
    """

    data: Union[Unset, List[str]] = UNSET
    filtered_by_operation: Union[Unset, int] = UNSET
    index: Union[Unset, int] = UNSET
    reason: Union[Unset, str] = UNSET
    screened: Union[Unset, bool] = UNSET
    screened_data: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data: Union[Unset, List[str]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data

        filtered_by_operation = self.filtered_by_operation
        index = self.index
        reason = self.reason
        screened = self.screened
        screened_data: Union[Unset, List[str]] = UNSET
        if not isinstance(self.screened_data, Unset):
            screened_data = self.screened_data

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if filtered_by_operation is not UNSET:
            field_dict["filteredByOperation"] = filtered_by_operation
        if index is not UNSET:
            field_dict["index"] = index
        if reason is not UNSET:
            field_dict["reason"] = reason
        if screened is not UNSET:
            field_dict["screened"] = screened
        if screened_data is not UNSET:
            field_dict["screenedData"] = screened_data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        data = cast(List[str], d.pop("data", UNSET))

        filtered_by_operation = d.pop("filteredByOperation", UNSET)

        index = d.pop("index", UNSET)

        reason = d.pop("reason", UNSET)

        screened = d.pop("screened", UNSET)

        screened_data = cast(List[str], d.pop("screenedData", UNSET))

        screened_row = cls(
            data=data,
            filtered_by_operation=filtered_by_operation,
            index=index,
            reason=reason,
            screened=screened,
            screened_data=screened_data,
        )

        screened_row.additional_properties = d
        return screened_row

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
