from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostLlmRequestJsonBodyPromptArgs")


@attr.s(auto_attribs=True)
class PostLlmRequestJsonBodyPromptArgs:
    """Parameters of the prompt as a dict

    Attributes:
        computation_labels (Union[Unset, str]): (AI-Explainer) Labels of the computation to explain
        computation_results (Union[Unset, str]): (AI-Explainer) Results of the computation to explain
        computation_type (Union[Unset, str]): (AI-Explainer) Type of the computation to explain
        query (Union[Unset, str]): User's additional query
        rdf_filter (Union[Unset, str]): (SPARQL) Filter for SPARQL relations and subclasses to include
        rdf_schema (Union[Unset, str]): (SPARQL) SPARQL schema
        sql_schema (Union[Unset, str]): (SQL) SQL schema
    """

    computation_labels: Union[Unset, str] = UNSET
    computation_results: Union[Unset, str] = UNSET
    computation_type: Union[Unset, str] = UNSET
    query: Union[Unset, str] = UNSET
    rdf_filter: Union[Unset, str] = UNSET
    rdf_schema: Union[Unset, str] = UNSET
    sql_schema: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        computation_labels = self.computation_labels
        computation_results = self.computation_results
        computation_type = self.computation_type
        query = self.query
        rdf_filter = self.rdf_filter
        rdf_schema = self.rdf_schema
        sql_schema = self.sql_schema

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if computation_labels is not UNSET:
            field_dict["computation_labels"] = computation_labels
        if computation_results is not UNSET:
            field_dict["computation_results"] = computation_results
        if computation_type is not UNSET:
            field_dict["computation_type"] = computation_type
        if query is not UNSET:
            field_dict["query"] = query
        if rdf_filter is not UNSET:
            field_dict["rdf_filter"] = rdf_filter
        if rdf_schema is not UNSET:
            field_dict["rdf_schema"] = rdf_schema
        if sql_schema is not UNSET:
            field_dict["sql_schema"] = sql_schema

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        computation_labels = d.pop("computation_labels", UNSET)

        computation_results = d.pop("computation_results", UNSET)

        computation_type = d.pop("computation_type", UNSET)

        query = d.pop("query", UNSET)

        rdf_filter = d.pop("rdf_filter", UNSET)

        rdf_schema = d.pop("rdf_schema", UNSET)

        sql_schema = d.pop("sql_schema", UNSET)

        post_llm_request_json_body_prompt_args = cls(
            computation_labels=computation_labels,
            computation_results=computation_results,
            computation_type=computation_type,
            query=query,
            rdf_filter=rdf_filter,
            rdf_schema=rdf_schema,
            sql_schema=sql_schema,
        )

        post_llm_request_json_body_prompt_args.additional_properties = d
        return post_llm_request_json_body_prompt_args

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
