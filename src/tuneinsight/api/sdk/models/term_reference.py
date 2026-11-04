from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="TermReference")


@attr.s(auto_attribs=True)
class TermReference:
    """identifies a term by its vocabulary and code.

    Attributes:
        code (str): code identifying the term within its vocabulary.
        vocabulary (str): name of the vocabulary containing the term.
    """

    code: str
    vocabulary: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        code = self.code
        vocabulary = self.vocabulary

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "vocabulary": vocabulary,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        code = d.pop("code")

        vocabulary = d.pop("vocabulary")

        term_reference = cls(
            code=code,
            vocabulary=vocabulary,
        )

        term_reference.additional_properties = d
        return term_reference

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
