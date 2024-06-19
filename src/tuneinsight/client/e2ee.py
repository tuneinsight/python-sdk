"""Utilities to interact with results under end-to-end encryption."""

import base64
from tuneinsight.client.dataobject import Result
from tuneinsight.client.validation import validate_response

from tuneinsight.cryptolib import (
    get_public_key_b64,
    new_hefloat_operator_from_b64_scheme_context,
    decrypt_dataframe,
)

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
    ciphertable = models.Ciphertable.from_dict(key_switched_result.content.to_dict())
    ciphertext = base64.urlsafe_b64decode(ciphertable.value.encode("utf-8"))
    df = decrypt_dataframe(hefloat_operator_id, ciphertext)

    # Overwrite the content of the results with the decrypted dataframe (as a float matrix).
    result.model.content = models.FloatMatrix(
        type=models.ContentType.FLOATMATRIX,
        columns=ciphertable.columns,
        # Convert the data from DataFrame to List[List[float]]
        data=list(list(row) for row in df.values),
        contextual_info=result.model.content.contextual_info,
    )

    return result
