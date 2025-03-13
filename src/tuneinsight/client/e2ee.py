"""Utilities to interact with results under end-to-end encryption."""

import base64
import json
from typing import Callable, Dict
from tuneinsight.client.dataobject import Result
from tuneinsight.client.validation import validate_response

from tuneinsight.cryptolib import (
    get_public_key_b64,
    new_hefloat_operator_from_b64_scheme_context,
    decrypt_dataframe,
    decrypt_stats,
)

from tuneinsight.cryptolib.postprocessing import post_process_statistics

from tuneinsight.api.sdk import models
from tuneinsight.api.sdk import client as api_client
from tuneinsight.api.sdk.types import Unset
from tuneinsight.api.sdk.api.api_computations import release_result


def decrypt(client: api_client, result: Result) -> Result:
    """
    Decrypts a result (DataObject) computed under end-to-end encryption.

    This generates public and private keys for the result, requests a key switch
    for the result, retrieves the result and decrypts it. New keys are generated
    each time, and keys are not stored.

    Args:
        client: the client to connect to the instance.
        result: the result to be decrypted.

    Returns:
        result: the input result with its content decrypted in-place.
    """
    # Some computations don't support E2EE, as identified by their switching params (in that case the result is in plaintext).
    switching_params = result.model.result.switching_params
    if isinstance(switching_params, Unset):
        return result

    ## Create a cryptosystem. This will be used to generate a public and private key.
    hefloat_operator_id = new_hefloat_operator_from_b64_scheme_context(switching_params)

    ## Generate a public key for this cryptosystem.
    public_key = get_public_key_b64(hefloat_operator_id)

    ## Keyswitch the result for this public key.
    response = release_result.sync_detailed(
        result_id=result.get_id(),
        json_body=models.ResultRelease(public_key.decode("utf-8")),
        client=client,
    )
    validate_response(response)
    key_switched_result: models.ResultContent = response.parsed

    ## Decrypt the key-switched result using the private key (in the cryptosystem).
    # First, cast the generic result to the EncryptedContent type.
    if key_switched_result.content.type != models.ContentType.ENCRYPTEDCONTENT:
        raise TypeError(
            f"Cannot decrypt result: result is not encrypted (type {key_switched_result.content.type})"
        )
    encrypted_content = models.EncryptedContent.from_dict(
        key_switched_result.content.to_dict()
    )

    # Different encrypted data types (specified by encrypted_type) must be processed differently.
    decryptor = DECRYPTION_METHODS.get(encrypted_content.encrypted_type)
    if decryptor is None:
        raise ValueError(
            f"Cannot decrypt encrypted content of type {encrypted_content.encrypted_type}"
        )
    decrypted_content = decryptor(encrypted_content, hefloat_operator_id)

    ## Apply required postprocessing operations on the decrypted result.
    content = post_process(
        result.model.computation.definition,
        decrypted_content,
        result.model.result.required_post_processing,
    )

    # Decorate the decrypted and post-processed content with additional metadata.
    content.contextual_info = result.model.content.contextual_info
    if hasattr(content, "columns"):
        content.columns = decrypted_content.columns

    ## Overwrite the content of the results with the decrypted dataframe (as a float matrix).
    result.model.content = content

    return result


def post_process(
    comp: models.ComputationDefinition, content: models.Content, postprocessing: str
) -> models.Content:
    """post_process applies the specified post-processing operation to a decrypted result.

    Args:
        comp (models.ComputationDefinition): the computation for which the result was obtained.
        content (models.Content): the decrypted/plaintext result of the computation.
        postprocessing (str): a description of the post-processing operation.
    """
    if postprocessing == "dp-statistics":
        stat_def = models.DatasetStatistics.from_dict(comp.to_dict())
        assert isinstance(
            content, models.FloatMatrix
        ), "cannot post-process statistics (expected float matrix)"
        return post_process_statistics(stat_def, content.data)
    return content


def _decrypt_dataframe(
    encrypted_content: models.EncryptedContent, hefloat_operator_id: bytes
) -> models.FloatMatrix:
    """Decrypts an encrypted dataframe to a floatmatrix.

    Args:
        encrypted_content (models.EncryptedContent): The model of the encrypted object's content.
        hefloat_operator_id (bytes): the ID of the cryptosystem to use.

    """
    ciphertext = base64.urlsafe_b64decode(encrypted_content.value.encode("utf-8"))
    df = decrypt_dataframe(hefloat_operator_id, ciphertext)
    return models.FloatMatrix(
        type=models.ContentType.FLOATMATRIX,
        columns=encrypted_content.columns,
        # Convert the data from DataFrame to List[List[float]]
        data=list(list(row) for row in df.values),
    )


def _decrypt_statistics(
    encrypted_content: models.EncryptedContent, hefloat_operator_id: bytes
) -> models.Statistics:
    """Decrypts encrypted statistics.

    Args:
        encrypted_content (models.EncryptedContent): The model of the encrypted object's content.
        hefloat_operator_id (bytes): the ID of the cryptosystem to use.

    """
    ciphertext = base64.urlsafe_b64decode(encrypted_content.value.encode("utf-8"))
    json_data = decrypt_stats(hefloat_operator_id, ciphertext)
    stat_results = [models.StatisticResult.from_dict(d) for d in json.loads(json_data)]
    return models.Statistics(type=models.ContentType.STATISTICS, results=stat_results)


# Each encrypted content type has its own decryption handler.
DECRYPTION_METHODS: Dict[
    models.ContentType, Callable[[models.EncryptedContent, bytes], models.Content]
] = {
    models.ContentType.STATISTICS: _decrypt_statistics,
    # All of the following use the same handler.
    models.ContentType.FLOATMATRIX: _decrypt_dataframe,
    models.ContentType.STRINGMATRIX: _decrypt_dataframe,
    models.ContentType.PREDICTION: _decrypt_dataframe,
    # Other types are currently unsupported.
}
