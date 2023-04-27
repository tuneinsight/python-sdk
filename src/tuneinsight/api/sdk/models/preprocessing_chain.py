from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.preprocessing_operation import PreprocessingOperation


T = TypeVar("T", bound="PreprocessingChain")


@attr.s(auto_attribs=True)
class PreprocessingChain:
    """Chain of preprocessing operations applied to the input dataframe

    Attributes:
        chain (Union[Unset, List['PreprocessingOperation']]):
    """

    chain: Union[Unset, List["PreprocessingOperation"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        chain: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.chain, Unset):
            chain = []
            for chain_item_data in self.chain:
                chain_item = chain_item_data.to_dict()

                chain.append(chain_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if chain is not UNSET:
            field_dict["chain"] = chain

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.preprocessing_operation import PreprocessingOperation

        d = src_dict.copy()
        chain = []
        _chain = d.pop("chain", UNSET)
        for chain_item_data in _chain or []:
            chain_item = PreprocessingOperation.from_dict(chain_item_data)

            chain.append(chain_item)

        preprocessing_chain = cls(
            chain=chain,
        )

        preprocessing_chain.additional_properties = d
        return preprocessing_chain

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
