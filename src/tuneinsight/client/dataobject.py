"""Classes to interact with data objects and results stored in a Tune Insight instance."""

from __future__ import annotations

from abc import abstractmethod
import io
from typing import Dict, Callable, List
import attr
import pandas as pd

from tuneinsight.api.sdk.types import Response
from tuneinsight.api.sdk.types import File
from tuneinsight.api.sdk import Client
from tuneinsight.api.sdk import models
from tuneinsight.api.sdk.types import UNSET, Unset, false_if_unset
from tuneinsight.api.sdk.api.api_dataobject import (
    get_data_object_data,
    get_data_object,
    delete_data_object,
    post_data_object,
    put_data_object_data,
    get_data_object_raw_data,
)
from tuneinsight.api.sdk.api.api_computations import get_result
from tuneinsight.client.validation import validate_response


def _float_matrix_to_dataframe(fm: models.FloatMatrix) -> pd.DataFrame:
    """
    Converts a FloatMatrix to a dataframe.

    Args:
        fm (models.FloatMatrix): the float matrix content

    Returns:
        pd.DataFrame: the output dataframe
    """
    fm = models.FloatMatrix.from_dict(fm.to_dict())
    return pd.DataFrame(data=fm.data, columns=fm.columns)


def _string_matrix_to_dataframe(t: models.StringMatrix) -> pd.DataFrame:
    """
    Converts a StringMatrix to a dataframe.

    Args:
        t (models.StringMatrix): the input string matrix content

    Returns:
        pd.DataFrame: the output dataframe
    """
    t = models.StringMatrix.from_dict(t.to_dict())
    return pd.DataFrame(data=t.data, columns=t.columns)


# Maps content type to their appropriate dataframe converter
content_to_dataframe: Dict[
    models.ContentType, Callable[[models.Content], pd.DataFrame]
] = {
    models.ContentType.FLOATMATRIX: _float_matrix_to_dataframe,
    models.ContentType.STRINGMATRIX: _string_matrix_to_dataframe,
}


class DataContent:
    """
    Abstract class that defines methods to interact with data.

    This class abstracts both low-level structures like data objects, and
    higher-level structure like models.Results. It implements methods to
    extract data from the API data structures into Python types.

    """

    @abstractmethod
    def get_content(self) -> models.Content:
        """
        Returns the content of this object as a models.Content.

        """

    @abstractmethod
    def get_raw_data(self) -> bytes:
        """
        Returns the data of this object as raw bytes.

        """

    @abstractmethod
    def get_id(self) -> str:
        """
        Returns the unique identifier of this object in the instance.

        """

    @abstractmethod
    def get_dataobject(self) -> models.DataObject:
        """
        Returns the data object associated with the content.
        """

    @abstractmethod
    def is_encrypted(self) -> bool:
        """
        Returns whether the content of this object is encrypted.

        """

    def _get_as_type(self, model_class, model_type: models.ContentType):
        """Returns the content of this object as a specific Content model.type."""
        m = self.get_content()
        # Check if this content is already of the correct type.
        if isinstance(m, model_class):
            return m
        # Otherwise, check that the .type attribute is compatible.
        if m.type != model_type:
            raise TypeError(
                f"Content is not of type {model_class}, but of type: {m.type}."
            )
        # Convert the content to the target class.
        return model_class.from_dict(m.to_dict())

    def get_float_matrix(self) -> models.FloatMatrix:
        """
        Returns the content as a float matrix, if possible.

        Returns:
            models.FloatMatrix: the float matrix of the data content.
        """
        return self._get_as_type(models.FloatMatrix, models.ContentType.FLOATMATRIX)

    def get_ml_result(self) -> models.ExternalMlResult:
        """
        Returns the content as an external ML result, if possible.

        Returns:
            models.ExternalMlResult: the external ML result of the data content.
        """
        return self._get_as_type(
            models.ExternalMlResult, models.ContentType.EXTERNALMLRESULT
        )

    def get_string_matrix(self) -> models.StringMatrix:
        """
        Returns the content of the dataobject as a string matrix, if possible.

        Returns:
            models.StringMatrix: the string matrix of the dataobject
        """
        return self._get_as_type(models.StringMatrix, models.ContentType.STRINGMATRIX)

    def get_stats(self) -> models.Statistics:
        """
        Returns the content of the dataobject as a models.Statistics, if possible.
        """
        return self._get_as_type(models.Statistics, models.ContentType.STATISTICS)

    def get_prediction(self) -> models.Prediction:
        """
        Returns the content of the dataobject as a models.Prediction, if possible.
        """
        return self._get_as_type(models.Prediction, models.ContentType.PREDICTION)

    def get_dataframe(self) -> pd.DataFrame:
        """
        Returns the content of the dataobject as a dataframe.

        Raises:
            ValueError: if the content type returned is not supported.

        Returns:
            pd.DataFrame: dataframe containing the data from the dataobject, format depending on the content type.
        """
        content = self.get_content()
        content_type = content.type
        if not content_type in content_to_dataframe:
            raise ValueError(f"Invalid content type: {content_type}.")
        converter = content_to_dataframe[content_type]
        return converter(content)


@attr.s(auto_attribs=True)
class DataObject(DataContent):
    """
    A DataObject stored in a Tune Insight instance and its associated model.

    Raises:
        Exception: when requests performed result in an error

    """

    model: models.DataObject
    client: Client

    @classmethod
    def create(
        cls,
        client: Client,
        do_type: models.DataObjectType,
        session_id: str = "",
        encrypted: bool = False,
        key_info: models.KeyInfo = None,
        data: bytes = None,
    ):
        """
        Creates a data object in the Tune Insight instance.

        Returns:
            The data object newly created.
        """
        body = models.PostDataObjectJsonBody()
        body.method = models.DataObjectCreationMethod.CREATE
        body.encrypted = encrypted
        body.type = do_type
        body.session_id = session_id
        if key_info is not None:
            body.key_info = key_info
        response: Response[models.DataObject] = post_data_object.sync_detailed(
            client=client, json_body=body
        )
        validate_response(response)

        data_object = cls(model=response.parsed, client=client)
        if data is not None:
            data_object.load_data_from_bytes(data)
        return data_object

    @classmethod
    def create_from_dataframe(cls, client: Client, data: pd.DataFrame):
        """
        Creates a (plaintext) DataObject in the Tune Insight instance from a DataFrame.

        Args:
            client: the client to connect to the API.
            data (pd.DataFrame): the data to upload as a Pandas DataFrame.

        """
        return cls.create(
            client,
            do_type=models.DataObjectType.TABLE,
            data=data.to_csv().encode("utf-8"),
        )

    @classmethod
    def fetch_from_id(cls, dataobject_id: str, client: Client):
        """Fetches a dataobject from the instance."""
        response: Response[models.DataObject] = get_data_object.sync_detailed(
            client=client, data_object_id=dataobject_id
        )
        validate_response(response)
        return cls(model=response.parsed, client=client)

    def get_id(self) -> str:
        """
        Returns the unique ID of this dataobject.

        Returns:
            str: the ID
        """
        return self.model.unique_id

    def get_content(self) -> models.Content:
        """
        Returns the content of the dataobject.

        Returns:
            models.Content the content which can be of multiple of types
        """
        response: Response[models.Content] = get_data_object_data.sync_detailed(
            client=self.client, data_object_id=self.get_id()
        )
        validate_response(response)
        return response.parsed

    def get_dataobject(self) -> models.DataObject:
        """
        Returns the data object model

        Returns:
            models.DataObject: the data object model
        """
        return self.model

    def is_encrypted(self) -> bool:
        """
        Returns whether the content of this object is encrypted.

        """
        return false_if_unset(self.model.encrypted)

    def delete(self):
        """
        Requests the deletion of the dataobject.

        """
        response: Response["models.Any"] = delete_data_object.sync_detailed(
            client=self.client, data_object_id=self.get_id()
        )
        validate_response(response)

    def decrypt(self) -> DataObject:
        """
        Requests the decryption of the dataobject, yielding a new decrypted dataobject.

        Returns:
            DataObject: the decrypted dataobject
        """
        method = models.DataObjectCreationMethod(
            models.DataObjectCreationMethod.DECRYPT
        )
        definition = models.PostDataObjectJsonBody(
            method=method, data_object_id=self.get_id()
        )
        do_resp: Response[models.DataObject] = post_data_object.sync_detailed(
            client=self.client, json_body=definition
        )
        validate_response(do_resp)
        return DataObject(model=do_resp.parsed, client=self.client)

    def load_data_from_bytes(self, data: bytes):
        """
        Set the content of this data object.

        Args:
            data: the (raw) bytes to set the content to.

        """
        definition = models.PutDataObjectDataMultipartData(
            File(payload=io.BytesIO(initial_bytes=data), file_name="test")
        )
        do_resp: Response[models.DataObject] = put_data_object_data.sync_detailed(
            data_object_id=self.get_id(), client=self.client, multipart_data=definition
        )
        validate_response(do_resp)
        self.model = do_resp.parsed

    def get_raw_data(
        self, object_key: str = UNSET, start_index: int = UNSET, end_index: int = UNSET
    ) -> bytes:
        """
        Returns the raw content of this data object.

        Returns
            bytes: the raw content.
        """

        resp: Response[File] = get_data_object_raw_data.sync_detailed(
            data_object_id=self.get_id(),
            client=self.client,
            object_key=object_key,
            start_index=start_index,
            end_index=end_index,
        )
        validate_response(resp)
        return resp.content


@attr.s(auto_attribs=True)
class Result(DataContent):
    """
    The result of a computation stored in a Tune Insight instance.
    """

    model: models.ResultContent
    client: Client

    @classmethod
    def fetch_from_id(cls, result_id: str, client: Client):
        """Fetches a result from the instance."""
        response: Response[models.ResultContent] = get_result.sync_detailed(
            client=client, result_id=result_id
        )
        validate_response(response)
        return cls(model=response.parsed, client=client)

    def get_id(self) -> str:
        """Returns the unique ID of this result."""
        return self.model.result.id

    def is_local(self) -> bool:
        """Returns whether the result was produced by a local or collective computation."""
        return self.model.computation.run_mode == models.RunMode.LOCAL

    def get_content(self) -> models.Content:
        """Returns the data content of this result."""
        # since the SDK does not run combined mode for now, the local content is only returned when the run mode is local.
        if self.is_local():
            return self.model.local_content
        return self.model.content

    def get_dataobject_id(self) -> str:
        """Returns the appropriate data object id based on the locality of the result"""
        if self.is_local():
            return self.model.result.local_data_object_id
        return self.model.result.data_object_id

    def get_dataobject(self) -> models.DataObject:
        """
        Returns the data object model associated with this result.

        Returns:
            models.DataObject: the data object model
        """
        return DataObject.fetch_from_id(self.get_dataobject_id(), self.client).model

    def is_encrypted(self) -> bool:
        """
        Returns whether the content of this object is encrypted.

        """
        if isinstance(self.model.content, Unset):
            return self.get_dataobject().encrypted
        return self.model.content.type == models.ContentType.ENCRYPTEDCONTENT

    # get_dataframe etc. is inherited from _Content.

    def get_dataobjects(self) -> List[DataObject]:
        """
        Fetches the dataobjects for all the data of this result.

        This method is intended for internal use: only use this if you really
        need to manipulate data objects directly.

        """
        return [DataObject.fetch_from_id(self.get_dataobject_id(), self.client)]

    def get_raw_data(self) -> bytes:
        resp: Response[File] = get_data_object_raw_data.sync_detailed(
            data_object_id=self.get_dataobject_id(), client=self.client
        )
        validate_response(resp)
        return resp.content

    @property
    def end_to_end_encrypted(self) -> bool:
        """Returns whether this result is end-to-end encrypted."""
        if isinstance(self.model.result, Unset):
            return False
        answer = self.model.result.end_to_end_encrypted
        if isinstance(answer, Unset):
            return False
        return answer

    @property
    def title(self) -> str:
        """Returns the title of this computation (if any)."""
        title = self.model.result.title
        if isinstance(title, Unset):
            return ""
        return title

    @property
    def tags(self) -> List[str]:
        """Returns the list of tags assigned to this result (if any)."""
        tags = self.model.result.tags
        if isinstance(tags, Unset):
            return []
        return tags

    @property
    def dp_metadata(self) -> models.ResultMetadata:
        """Returns the metadata of differentially private noise added to this result."""
        return self.model.result.metadata
