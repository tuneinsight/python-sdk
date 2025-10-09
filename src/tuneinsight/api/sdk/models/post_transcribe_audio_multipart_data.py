from io import BytesIO
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, File, Unset

T = TypeVar("T", bound="PostTranscribeAudioMultipartData")


@attr.s(auto_attribs=True)
class PostTranscribeAudioMultipartData:
    """
    Attributes:
        file (File): Audio file to transcribe
        api_url_file (Union[Unset, str]): URL of the LLM API to use for transcription file
        api_url_results (Union[Unset, str]): URL of the LLM API to use for transcription results
        auth_token (Union[Unset, str]): Authentication token for the LLM API
    """

    file: File
    api_url_file: Union[Unset, str] = UNSET
    api_url_results: Union[Unset, str] = UNSET
    auth_token: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        file = self.file.to_tuple()

        api_url_file = self.api_url_file
        api_url_results = self.api_url_results
        auth_token = self.auth_token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file": file,
            }
        )
        if api_url_file is not UNSET:
            field_dict["api_url_file"] = api_url_file
        if api_url_results is not UNSET:
            field_dict["api_url_results"] = api_url_results
        if auth_token is not UNSET:
            field_dict["auth_token"] = auth_token

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        file = self.file.to_tuple()

        api_url_file = (
            self.api_url_file
            if isinstance(self.api_url_file, Unset)
            else (None, str(self.api_url_file).encode(), "text/plain")
        )
        api_url_results = (
            self.api_url_results
            if isinstance(self.api_url_results, Unset)
            else (None, str(self.api_url_results).encode(), "text/plain")
        )
        auth_token = (
            self.auth_token
            if isinstance(self.auth_token, Unset)
            else (None, str(self.auth_token).encode(), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "file": file,
            }
        )
        if api_url_file is not UNSET:
            field_dict["api_url_file"] = api_url_file
        if api_url_results is not UNSET:
            field_dict["api_url_results"] = api_url_results
        if auth_token is not UNSET:
            field_dict["auth_token"] = auth_token

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        file = File(payload=BytesIO(d.pop("file")))

        api_url_file = d.pop("api_url_file", UNSET)

        api_url_results = d.pop("api_url_results", UNSET)

        auth_token = d.pop("auth_token", UNSET)

        post_transcribe_audio_multipart_data = cls(
            file=file,
            api_url_file=api_url_file,
            api_url_results=api_url_results,
            auth_token=auth_token,
        )

        post_transcribe_audio_multipart_data.additional_properties = d
        return post_transcribe_audio_multipart_data

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
