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
        output (Union[Unset, str]): column to use as output
        cuts (Union[Unset, List[float]]): cuts to use
        input_ (Union[Unset, str]): column to use as input
        labels (Union[Unset, List[str]]): labels to use for the cuts
    """

    type: PreprocessingOperationType
    output: Union[Unset, str] = UNSET
    cuts: Union[Unset, List[float]] = UNSET
    input_: Union[Unset, str] = UNSET
    labels: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        output = self.output
        cuts: Union[Unset, List[float]] = UNSET
        if not isinstance(self.cuts, Unset):
            cuts = self.cuts

        input_ = self.input_
        labels: Union[Unset, List[str]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if output is not UNSET:
            field_dict["output"] = output
        if cuts is not UNSET:
            field_dict["cuts"] = cuts
        if input_ is not UNSET:
            field_dict["input"] = input_
        if labels is not UNSET:
            field_dict["labels"] = labels

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = PreprocessingOperationType(d.pop("type"))

        output = d.pop("output", UNSET)

        cuts = cast(List[float], d.pop("cuts", UNSET))

        input_ = d.pop("input", UNSET)

        labels = cast(List[str], d.pop("labels", UNSET))

        cut = cls(
            type=type,
            output=output,
            cuts=cuts,
            input_=input_,
            labels=labels,
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
