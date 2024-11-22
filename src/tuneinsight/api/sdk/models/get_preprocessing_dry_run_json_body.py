from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.preprocessing_chain import PreprocessingChain


T = TypeVar("T", bound="GetPreprocessingDryRunJsonBody")


@attr.s(auto_attribs=True)
class GetPreprocessingDryRunJsonBody:
    """
    Attributes:
        chain (Union[Unset, PreprocessingChain]): Chain of preprocessing operations applied to the input dataframe
        columns (Union[Unset, List[str]]): the list of names of input columns before preprocessing.
    """

    chain: Union[Unset, "PreprocessingChain"] = UNSET
    columns: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        chain: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.chain, Unset):
            chain = self.chain.to_dict()

        columns: Union[Unset, List[str]] = UNSET
        if not isinstance(self.columns, Unset):
            columns = self.columns

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if chain is not UNSET:
            field_dict["chain"] = chain
        if columns is not UNSET:
            field_dict["columns"] = columns

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.preprocessing_chain import PreprocessingChain

        d = src_dict.copy()
        _chain = d.pop("chain", UNSET)
        chain: Union[Unset, PreprocessingChain]
        if isinstance(_chain, Unset):
            chain = UNSET
        else:
            chain = PreprocessingChain.from_dict(_chain)

        columns = cast(List[str], d.pop("columns", UNSET))

        get_preprocessing_dry_run_json_body = cls(
            chain=chain,
            columns=columns,
        )

        get_preprocessing_dry_run_json_body.additional_properties = d
        return get_preprocessing_dry_run_json_body

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
