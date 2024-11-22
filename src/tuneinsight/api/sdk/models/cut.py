from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.preprocessing_operation_type import PreprocessingOperationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Cut")


@attr.s(auto_attribs=True)
class Cut:
    """
    Attributes:
        type (PreprocessingOperationType): type of preprocessing operation
        cuts (Union[Unset, List[float]]): cuts to use
        input_column (Union[Unset, str]): column to use as input
        labels (Union[Unset, List[str]]): labels to use for the cuts
        output_column (Union[Unset, str]): column to use as output. If not specified, the input column is used (in
            place).
    """

    type: PreprocessingOperationType
    cuts: Union[Unset, List[float]] = UNSET
    input_column: Union[Unset, str] = UNSET
    labels: Union[Unset, List[str]] = UNSET
    output_column: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        cuts: Union[Unset, List[float]] = UNSET
        if not isinstance(self.cuts, Unset):
            cuts = self.cuts

        input_column = self.input_column
        labels: Union[Unset, List[str]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels

        output_column = self.output_column

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if cuts is not UNSET:
            field_dict["cuts"] = cuts
        if input_column is not UNSET:
            field_dict["inputColumn"] = input_column
        if labels is not UNSET:
            field_dict["labels"] = labels
        if output_column is not UNSET:
            field_dict["outputColumn"] = output_column

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = PreprocessingOperationType(d.pop("type"))

        cuts = cast(List[float], d.pop("cuts", UNSET))

        input_column = d.pop("inputColumn", UNSET)

        labels = cast(List[str], d.pop("labels", UNSET))

        output_column = d.pop("outputColumn", UNSET)

        cut = cls(
            type=type,
            cuts=cuts,
            input_column=input_column,
            labels=labels,
            output_column=output_column,
        )

        cut.additional_properties = d
        return cut

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
