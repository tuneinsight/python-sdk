from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelMetadata")


@attr.s(auto_attribs=True)
class ModelMetadata:
    """public metadata about the model

    Attributes:
        classes (Union[Unset, List[str]]): optional labels for classes
        description (Union[Unset, str]): optional description for the model
        features (Union[Unset, List[str]]): optional labels for features
        num_classes (Union[Unset, int]): number classes
        num_features (Union[Unset, int]): number of features
    """

    classes: Union[Unset, List[str]] = UNSET
    description: Union[Unset, str] = UNSET
    features: Union[Unset, List[str]] = UNSET
    num_classes: Union[Unset, int] = UNSET
    num_features: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        classes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.classes, Unset):
            classes = self.classes

        description = self.description
        features: Union[Unset, List[str]] = UNSET
        if not isinstance(self.features, Unset):
            features = self.features

        num_classes = self.num_classes
        num_features = self.num_features

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if classes is not UNSET:
            field_dict["classes"] = classes
        if description is not UNSET:
            field_dict["description"] = description
        if features is not UNSET:
            field_dict["features"] = features
        if num_classes is not UNSET:
            field_dict["numClasses"] = num_classes
        if num_features is not UNSET:
            field_dict["numFeatures"] = num_features

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        classes = cast(List[str], d.pop("classes", UNSET))

        description = d.pop("description", UNSET)

        features = cast(List[str], d.pop("features", UNSET))

        num_classes = d.pop("numClasses", UNSET)

        num_features = d.pop("numFeatures", UNSET)

        model_metadata = cls(
            classes=classes,
            description=description,
            features=features,
            num_classes=num_classes,
            num_features=num_features,
        )

        model_metadata.additional_properties = d
        return model_metadata

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
