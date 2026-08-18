from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_source_variable import DataSourceVariable
    from ..models.dp_noise_metadata import DpNoiseMetadata


T = TypeVar("T", bound="ResultMetadata")


@attr.s(auto_attribs=True)
class ResultMetadata:
    """various metadata field along with the result to provide additional context

    Attributes:
        dp_noise (Union[Unset, List['DpNoiseMetadata']]): when using differential privacy, the metadata on the noise
            added to results.
        matrix_record_count_mask (Union[Unset, List[bool]]): Array of booleans that indicates which slots in the result
            matrix can be summed to obtain the total record count.
            This is used to deduce the total record count from matrix results on the client side without the need of
            additional context.
            if mask[i] = true then it means that the i'th slot of the matrix (row by row) contains the full or partial
            record count.
            An empty array or array without any true values indicates that the record count cannot be deduced from data
            returned in the matrix.
        queried_columns (Union[Unset, List['DataSourceVariable']]): contains the list of columns that were queried from
            all of the participant's data sources.
    """

    dp_noise: Union[Unset, List["DpNoiseMetadata"]] = UNSET
    matrix_record_count_mask: Union[Unset, List[bool]] = UNSET
    queried_columns: Union[Unset, List["DataSourceVariable"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dp_noise: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.dp_noise, Unset):
            dp_noise = []
            for dp_noise_item_data in self.dp_noise:
                dp_noise_item = dp_noise_item_data.to_dict()

                dp_noise.append(dp_noise_item)

        matrix_record_count_mask: Union[Unset, List[bool]] = UNSET
        if not isinstance(self.matrix_record_count_mask, Unset):
            matrix_record_count_mask = self.matrix_record_count_mask

        queried_columns: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.queried_columns, Unset):
            queried_columns = []
            for queried_columns_item_data in self.queried_columns:
                queried_columns_item = queried_columns_item_data.to_dict()

                queried_columns.append(queried_columns_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dp_noise is not UNSET:
            field_dict["dpNoise"] = dp_noise
        if matrix_record_count_mask is not UNSET:
            field_dict["matrixRecordCountMask"] = matrix_record_count_mask
        if queried_columns is not UNSET:
            field_dict["queriedColumns"] = queried_columns

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.data_source_variable import DataSourceVariable
        from ..models.dp_noise_metadata import DpNoiseMetadata

        d = src_dict.copy()
        dp_noise = []
        _dp_noise = d.pop("dpNoise", UNSET)
        for dp_noise_item_data in _dp_noise or []:
            dp_noise_item = DpNoiseMetadata.from_dict(dp_noise_item_data)

            dp_noise.append(dp_noise_item)

        matrix_record_count_mask = cast(List[bool], d.pop("matrixRecordCountMask", UNSET))

        queried_columns = []
        _queried_columns = d.pop("queriedColumns", UNSET)
        for queried_columns_item_data in _queried_columns or []:
            queried_columns_item = DataSourceVariable.from_dict(queried_columns_item_data)

            queried_columns.append(queried_columns_item)

        result_metadata = cls(
            dp_noise=dp_noise,
            matrix_record_count_mask=matrix_record_count_mask,
            queried_columns=queried_columns,
        )

        result_metadata.additional_properties = d
        return result_metadata

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
