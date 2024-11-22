from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.preprocessing_operation_type import PreprocessingOperationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Select")


@attr.s(auto_attribs=True)
class Select:
    """
    Attributes:
        type (PreprocessingOperationType): type of preprocessing operation
        columns (List[str]): list of selected columns
        create_if_missing (Union[Unset, bool]): if true, a dummy column is created for each selected columns that is
            missing
        dummy_value (Union[Unset, str]): dummy value set to the missing columns if 'createIfMissing' is set to true
    """

    type: PreprocessingOperationType
    columns: List[str]
    create_if_missing: Union[Unset, bool] = UNSET
    dummy_value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        columns = self.columns

        create_if_missing = self.create_if_missing
        dummy_value = self.dummy_value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "columns": columns,
            }
        )
        if create_if_missing is not UNSET:
            field_dict["createIfMissing"] = create_if_missing
        if dummy_value is not UNSET:
            field_dict["dummyValue"] = dummy_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = PreprocessingOperationType(d.pop("type"))

        columns = cast(List[str], d.pop("columns"))

        create_if_missing = d.pop("createIfMissing", UNSET)

        dummy_value = d.pop("dummyValue", UNSET)

        select = cls(
            type=type,
            columns=columns,
            create_if_missing=create_if_missing,
            dummy_value=dummy_value,
        )

        select.additional_properties = d
        return select

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
