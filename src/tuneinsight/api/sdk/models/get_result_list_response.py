from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.result import Result


T = TypeVar("T", bound="GetResultListResponse")


@attr.s(auto_attribs=True)
class GetResultListResponse:
    """returned response on the GET result list route.

    Attributes:
        results (Union[Unset, List['Result']]): List of results
        total (Union[Unset, int]): the total number of available results for pagination purposes.
    """

    results: Union[Unset, List["Result"]] = UNSET
    total: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        results: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.results, Unset):
            results = []
            for results_item_data in self.results:
                results_item = results_item_data.to_dict()

                results.append(results_item)

        total = self.total

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if results is not UNSET:
            field_dict["results"] = results
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.result import Result

        d = src_dict.copy()
        results = []
        _results = d.pop("results", UNSET)
        for results_item_data in _results or []:
            results_item = Result.from_dict(results_item_data)

            results.append(results_item)

        total = d.pop("total", UNSET)

        get_result_list_response = cls(
            results=results,
            total=total,
        )

        get_result_list_response.additional_properties = d
        return get_result_list_response

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
