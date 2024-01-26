from __future__ import annotations
import io
from typing import Dict, Callable
import attr
import pandas as pd

from tuneinsight.api.sdk.types import Response
from tuneinsight.api.sdk.types import File
from tuneinsight.api.sdk import Client
from tuneinsight.api.sdk import models
from tuneinsight.api.sdk.api.api_dataobject import get_data_object_data
from tuneinsight.api.sdk.api.api_dataobject import delete_data_object
from tuneinsight.api.sdk.api.api_dataobject import post_data_object
from tuneinsight.api.sdk.api.api_dataobject import put_data_object_data
from tuneinsight.api.sdk.api.api_dataobject import get_data_object_raw_data
from tuneinsight.client.validation import validate_response


def float_matrix_to_dataframe(fm: models.FloatMatrix) -> pd.DataFrame:
    """
    float_matrix_to_dataframe converts FloatMatrix content to a dataframe

    Args:
        fm (models.FloatMatrix): the float matrix content

    Returns:
        pd.DataFrame: the output dataframe
    """
    return pd.DataFrame(data=fm.data, columns=fm.columns)


def string_matrix_to_dataframe(t: models.StringMatrix) -> pd.DataFrame:
    """
    string_matrix_to_dataframe converts a StringMatrix content to a dataframe

    Args:
        t (models.StringMatrix): the input string matrix content

    Returns:
        pd.DataFrame: the output dataframe
    """
    return pd.DataFrame(data=t.data, columns=t.columns)


# Maps content type to their appropriate dataframe converter
content_to_dataframe: Dict[type, Callable[[models.Content], pd.DataFrame]] = {
    models.FloatMatrix: float_matrix_to_dataframe,
    models.StringMatrix: string_matrix_to_dataframe,
}


@attr.s(auto_attribs=True)
class DataObject:
    """
     represents DataObject in Geco and its associated model

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

    def get_id(self) -> str:
        """
        get_id returns the ID of the dataobject

        Returns:
            str: the ID
        """
        return self.model.unique_id

    def get_content(self) -> models.Content:
        """
        get_content returns the content of the dataobject

        Returns:
            models.Content the content which can be of multiple of types
        """
        response: Response[models.Content] = get_data_object_data.sync_detailed(
            client=self.client, data_object_id=self.get_id()
        )
        validate_response(response)
        return response.parsed

    def get_float_matrix(self) -> models.FloatMatrix:
        """
        get_float_matrix returns the content of the dataobject as a float matrix if possible

        Returns:
            models.FloatMatrix: the float matrix of the dataobject
        """
        fm: models.FloatMatrix = self.get_content()
        return fm

    def get_ml_result(self) -> models.ExternalMlResult:
        """
        get_ml_result returns the content of the dataobject as an external ml result if possible

        Returns:
            models.ExternalMlResult: the external ml result of the dataobject
        """
        fm: models.ExternalMlResult = self.get_content()
        return fm

    def get_string_matrix(self) -> models.StringMatrix:
        """
        get_string_matrix returns the content of the dataobject as a string matrix if possible
        Returns:
            models.StringMatrix: the string matrix of the dataobject
        """
        sm: models.StringMatrix = self.get_content()
        return sm

    def get_stats(self) -> models.Statistics:
        stats: models.Statistics = self.get_content()
        return stats

    def get_dataframe(self) -> pd.DataFrame:
        """
        get_dataframe returns the content of the dataobject as a dataframe

        Raises:
            Exception: if the content type returned is not registered in this library

        Returns:
            pd.DataFrame: dataframe containing the data from the dataobject, format depends on the content type
        """
        content = self.get_content()
        content_type = type(content)
        if not content_type in content_to_dataframe:
            raise Exception(f"invalid content type: {content_type}")
        converter = content_to_dataframe[content_type]
        return converter(content)

    def delete(self):
        """
        delete requests a deletion of the dataobject
        """
        response: Response["models.Any"] = delete_data_object.sync_detailed(
            client=self.client, data_object_id=self.get_id()
        )  # pylint: disable=no-member
        validate_response(response)

    def decrypt(self) -> DataObject:
        """
        decrypt requests a decryption of the dataobject yielding a new decrypted dataobject

        Returns:
            DataObject: the decrypted dataobject
        """
        method = models.DataObjectCreationMethod(
            models.DataObjectCreationMethod.DECRYPT
        )
        definition = models.PostDataObjectJsonBody(
            method=method, data_object_id=self.get_id()
        )
        doResp: Response[models.DataObject] = post_data_object.sync_detailed(
            client=self.client, json_body=definition
        )
        validate_response(doResp)
        return DataObject(model=doResp.parsed, client=self.client)

    def load_data_from_bytes(self, data: bytes):
        definition = models.PutDataObjectDataMultipartData(
            File(payload=io.BytesIO(initial_bytes=data), file_name="test")
        )
        doResp: Response[models.DataObject] = put_data_object_data.sync_detailed(
            data_object_id=self.get_id(), client=self.client, multipart_data=definition
        )
        validate_response(doResp)
        self.model = doResp.parsed

    def get_raw_data(self) -> bytes:
        resp: Response[File] = get_data_object_raw_data.sync_detailed(
            data_object_id=self.get_id(), client=self.client
        )
        validate_response(resp)
        return resp.content
