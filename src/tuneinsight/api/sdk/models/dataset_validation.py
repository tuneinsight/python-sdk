from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.preprocessing_operation_type import PreprocessingOperationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dataset_schema import DatasetSchema


T = TypeVar("T", bound="DatasetValidation")


@attr.s(auto_attribs=True)
class DatasetValidation:
    """
    Attributes:
        type (PreprocessingOperationType): type of preprocessing operation
        schema (Union[Unset, DatasetSchema]): dataset schema definition used to validate input datasets.
    """

    type: PreprocessingOperationType
    schema: Union[Unset, "DatasetSchema"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        schema: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.schema, Unset):
            schema = self.schema.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if schema is not UNSET:
            field_dict["schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dataset_schema import DatasetSchema

        d = src_dict.copy()
        type = PreprocessingOperationType(d.pop("type"))

        _schema = d.pop("schema", UNSET)
        schema: Union[Unset, DatasetSchema]
        if isinstance(_schema, Unset):
            schema = UNSET
        else:
            schema = DatasetSchema.from_dict(_schema)

        dataset_validation = cls(
            type=type,
            schema=schema,
        )

        dataset_validation.additional_properties = d
        return dataset_validation

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
