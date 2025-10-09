from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="JupyterNotebook")


@attr.s(auto_attribs=True)
class JupyterNotebook:
    """Describes a jupyter notebook generated for a project (including its data and possibly its URL if it is hosted on the
    instance).

        Attributes:
            data (Union[Unset, str]): The content of the Jupyter notebook (a JSON file).
            error (Union[Unset, str]): Error message in case the notebook could not be retrieved or generated.
            url (Union[Unset, str]): The URL at which the notebook can be accessed if it is hosted on the instance.
    """

    data: Union[Unset, str] = UNSET
    error: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data = self.data
        error = self.error
        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if error is not UNSET:
            field_dict["error"] = error
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        data = d.pop("data", UNSET)

        error = d.pop("error", UNSET)

        url = d.pop("url", UNSET)

        jupyter_notebook = cls(
            data=data,
            error=error,
            url=url,
        )

        jupyter_notebook.additional_properties = d
        return jupyter_notebook

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
