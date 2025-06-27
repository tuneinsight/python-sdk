"""
# High-level Python interface to the Tune Insight crypto library.

This library provides Python bindings to the Lattigo library. It is intended mostly
for internal use.

In case you see recurrent warnings or errors related to the cryptolib, consult
[the documentation](https://dev.tuneinsight.com/docs/Usage/python-sdk/reference_docs/cryptolib/)
for troubleshooting options.

### Importing from `cryptolib`

```python
from tuneinsight.cryptolib import *
```
"""

import ctypes
from pathlib import Path
from os.path import exists
from typing import List, Union
import platform
import warnings
import pandas as pd


class _ErrorObject:
    """
    An empty object that raises error whenever one of its attributes is accessed.

    This is used as the "shared library object" when the cryptolib is not found,
    so that users get friendlier error messages when trying to use it (in case
    they missed the initial warning).

    """

    def __getattr__(self, _):
        raise ImportError("Could not load the cryptolib: contact your administrator.")


# Find the shared library for the compiled Go Cryptolib.
cwd = Path(__file__).absolute().parent
arch = platform.machine()
if arch == "aarch64":
    arch = "arm64"  # Handle special case for Linux in docker.
os = platform.system().lower()
ext = "dll" if os == "windows" else "so"
cryptolib_path = cwd / "build" / f"cryptolib-{os}_{arch}.{ext}"

# If not found, the shared library will be an object that raises errors whenever it is used.
so = _ErrorObject()
LOADED = False

if not exists(cryptolib_path):
    warnings.warn(
        "Could not find the cryptolib library. Your platform might not be supported."
    )
else:
    try:
        so = ctypes.cdll.LoadLibrary(str(cryptolib_path))
        LOADED = True
    except OSError as err:
        warnings.warn(
            f"Failed to load cryptolib ({err}). Some functionality might be affected."
        )


def go_error() -> Exception:
    """Raises a python exception from the latest go error."""
    get_go_error = so.GetLastGoError
    get_go_error.restype = ctypes.c_char_p
    error_message = get_go_error()
    if "not found" in str(error_message):
        return ValueError(error_message)
    return Exception(error_message)


def new_hefloat_operator_from_b64_hefloat_parameters(
    hefloat_parameters_b64: str,
) -> bytes:
    """Instantiates a new HeFloat Operator from a base64 encoded hefloat parameters.

    Args:
        hefloat_parameters_b64 (str): Base64 encoded marshalled hefloat parameters

    Returns:
        hefloat_operator_id (bytes): The HEFloat Operator id
    """
    b64_hefloat_operator = so.NewCkksOperatorFromB64Parameters
    b64_hefloat_operator.restype = ctypes.c_char_p
    hefloat_operator_id = b64_hefloat_operator(hefloat_parameters_b64.encode())
    if hefloat_operator_id is None:
        raise go_error()
    return hefloat_operator_id


def new_hefloat_operator_from_b64_scheme_context(scheme_context_b64: str) -> bytes:
    """Instantiates a new HEFloat Operator from a base64 encoded scheme.Context.

    Args:
        scheme_context_b64 (str): Base64 encoded marshalled scheme.Context

    Returns:
        hefloat_operator_id (bytes): The HEFloat Operator id
    """
    b64_hefloat_operator = so.NewCkksOperatorFromB64SchemeContext
    b64_hefloat_operator.restype = ctypes.c_char_p
    hefloat_operator_id = b64_hefloat_operator(scheme_context_b64.encode())
    if hefloat_operator_id is None:
        raise go_error()
    return hefloat_operator_id


def get_relin_key_bytes(hefloat_operator_id: bytes) -> bytes:
    """Retrieves the relinearization key bytes from the cryptosystem.

    Args:
        hefloat_operator_id (bytes): the id of the cryptosystem

    Returns:
        bytes: the relinearization key bytes
    """
    get_relin_key = so.GetRelinearizationKeyBytes
    get_relin_key.restype = ctypes.c_void_p
    res = get_relin_key(hefloat_operator_id)
    return _handle_bytes_result(res)


def encrypt_prediction_dataset(
    hefloat_operator_id: bytes, csv_bytes: bytes, b64_params: str, remove_header: bool
) -> bytes:
    """Encrypts a provided dataset in prediction format using the secret key of the cryptosystem.

    Args:
        hefloat_operator_id (bytes): the cryptosystem id
        csv_bytes (bytes): the csv data to encrypt
        b64_params (str): the base64 machine learning model parameters
        remove_header (bool): whether or not the csv data contains a header

    Returns:
        bytes: the encrypted version of the dataset that can be used as input to a encrypted prediction computation
    """
    encrypt_pred = so.EncryptPredictionDataset
    encrypt_pred.restype = ctypes.c_void_p
    res = encrypt_pred(
        hefloat_operator_id,
        csv_bytes,
        len(csv_bytes),
        b64_params.encode(),
        ctypes.c_bool(remove_header),
    )
    return _handle_bytes_result(res)


def decrypt_prediction(hefloat_operator_id: bytes, ct: bytes) -> bytes:
    """Decrypts the encrypted prediction ciphertext.

    Args:
        hefloat_operator_id (bytes): the id of the cryptosystem storing the secret key
        ct (bytes): the encrypted prediction bytes

    Returns:
        bytes: the decrypted predicted values as a csv in byte format
    """
    decrypt_pred = so.DecryptPredictionResult
    decrypt_pred.restype = ctypes.c_void_p
    res = decrypt_pred(hefloat_operator_id, ct, len(ct))
    return _handle_bytes_result(res)


def key_generation(hefloat_operator_id: bytes) -> bytes:
    """Generates a key for a given cryptosystem.

    Args:
        hefloat_operator_id (bytes): The crypto system id

    Returns:
        key_response (bytes): The response message of the key generation
    """
    key_gen = so.GenKeyPair
    key_gen.restype = ctypes.c_char_p
    key_response = key_gen(hefloat_operator_id)
    if key_response is None:
        raise go_error()
    return key_response


def get_secret_key_b64(hefloat_operator_id: bytes) -> bytes:
    """Returns the bytes of the secret key.

    Args:
        hefloat_operator_id (bytes): The crypto system id
    Returns:
        get_sk_response (bytes): The bytes of the secret key
    """
    get_sk = so.GetSecretKeyB64
    get_sk.restype = ctypes.c_char_p
    get_sk_response = get_sk(hefloat_operator_id)
    if get_sk_response is None:
        raise go_error()
    return get_sk_response


def get_public_key_b64(hefloat_operator_id: bytes) -> bytes:
    """Returns the bytes of the public key.

    Args:
        hefloat_operator_id (bytes): The crypto system id
    Returns:
        get_pk_response (bytes): The bytes of the public key
    """
    get_pk = so.GetPublicKeyB64
    get_pk.restype = ctypes.c_char_p
    get_pk_response = get_pk(hefloat_operator_id)
    if get_pk_response is None:
        raise go_error()
    return get_pk_response


def relinearization_key_generation(hefloat_operator_id: bytes) -> bytes:
    """Generates a key for a given cryptosystem.

    Args:
        hefloat_operator_id (bytes): The crypto system id

    Returns:
        key_response (bytes): The response message of the key generation
    """
    relin_key_gen = so.GenRelinearizationKey
    relin_key_gen.restype = ctypes.c_char_p
    key_response = relin_key_gen(hefloat_operator_id)
    if key_response is None:
        raise go_error()
    return key_response


def instantiate_scheme(hefloat_operator_id: bytes) -> bytes:
    """Instantiates a scheme for a given cryptosystem.

    Args:
        hefloat_operator_id (bytes): The crypto system id

    Returns:
        scheme_response (bytes): The response message of the scheme instantiation
    """
    instantiate_crypto_scheme = so.InstantiateScheme
    instantiate_crypto_scheme.restype = ctypes.c_char_p
    scheme_response = instantiate_crypto_scheme(hefloat_operator_id)
    if scheme_response is None:
        raise go_error()
    return scheme_response


def encrypt_dataframe(hefloat_operator_id: bytes, dataframe: pd.DataFrame) -> bytes:
    """Encrypts a numeric pandas dataframe.

    Column names will be lost, index names are recovered.

    Args:
        hefloat_operator_id (bytes): The crypto system id
        dataframe (bytes): The pandas.DataFrame that will be encrypted

    Returns:
        ciphertext (bytes): The generated ciphertext
    """
    plaintext_dataframe = dataframe.to_csv().encode("UTF-8")
    ciphertext = encrypt_matrix(hefloat_operator_id, plaintext_dataframe)
    if ciphertext is None:
        raise go_error()
    return ciphertext


def encrypt_matrix(hefloat_operator_id: bytes, csv_string: bytes) -> bytes:
    """Encrypts a csv formatted table of numbers.

    Args:
        hefloat_operator_id (bytes): The crypto system id
        csv_string (bytes): The csv content that will be encrypted

    Returns:
        ciphertext (bytes): The generated ciphertext
    """
    encrypt_float_matrix = so.EncryptFloatMatrix
    encrypt_float_matrix.restype = ctypes.c_void_p
    res = encrypt_float_matrix(hefloat_operator_id, csv_string)
    if res is None:
        raise go_error()
    res_length = int.from_bytes(ctypes.string_at(res, 8), "little")
    ciphertext = ctypes.string_at(res, res_length + 8)
    ciphertext = ciphertext[8:]
    return ciphertext


def decrypt_dataframe(
    hefloat_operator_id: bytes,
    dataframe_ciphertext: bytes,
    headers: List[str] = None,
    with_index: bool = False,
) -> pd.DataFrame:
    """
    Turns an encrypted pandas dataframe into a new decrypted pandas dataframe.

    Indices are recovered, column names can optionally be provided by the user.

    Args:
        hefloat_operator_id (bytes): The crypto system id
        dataframe_ciphertext (bytes): The encrypted pandas dataframe
        headers (list[str]): List of column names of the dataframe. If not provided, default
            names ("0", "1", ...) are used. If too many columns are provided, only the first
            ones are used.
        with_index (bool): whether to treat the first column as an index column. False by default.

    Returns:
        plaintext_dataframe (pandas.DataFrame): The decrypted dataframe
    """
    plaintext_csv_bytes = decrypt_csv(hefloat_operator_id, dataframe_ciphertext)
    if plaintext_csv_bytes is None:
        raise go_error()
    plaintext_csv = plaintext_csv_bytes.decode("utf8")
    plaintext_dataframe = pd.DataFrame(
        [row.split(",") for row in plaintext_csv.split("\n")]
    )
    # Treat the first column as an index if (1) there are more columns than headers, or
    # (2) headers are None and there is more than one column.
    num_cols = len(plaintext_dataframe.columns)
    if with_index:
        plaintext_dataframe = plaintext_dataframe.set_index(
            plaintext_dataframe.columns[0]
        )
    plaintext_dataframe.index.name = None
    if headers is not None:
        num_cols = len(plaintext_dataframe.columns)
        if len(headers) < num_cols:
            raise IndexError("Not enough columns in headers.")
        # Allow the user to give too many headers -- additional ones are ignored.
        if len(headers) > num_cols:
            headers = headers[:num_cols]
        plaintext_dataframe.columns = headers
    # Convert values back to numeric
    plaintext_dataframe = plaintext_dataframe.map(float)
    return plaintext_dataframe


def decrypt_csv(hefloat_operator_id: bytes, csv_ciphertext: bytes) -> bytes:
    """
    Decrypts a cipher table into a CSV formatted string.

    The column names are not recovered.

    Args:
        hefloat_operator_id (bytes): The crypto system id
        csv_ciphertext (bytes): The encrypted pandas dataframe

    Returns:
        csv_plaintext (bytes): The decrypted csv string
    """
    decrypt_cipher_table = so.DecryptCipherTable
    decrypt_cipher_table.restype = ctypes.c_char_p
    ctxt_length = len(csv_ciphertext)
    csv_plaintext = decrypt_cipher_table(
        hefloat_operator_id, csv_ciphertext, ctxt_length
    )
    if csv_plaintext is None:
        raise go_error()
    return csv_plaintext


def decrypt_stats(hefloat_operator_id: bytes, stat_ciphertext: bytes) -> bytes:
    """
    Decrypts an encrypted statistics results into a JSON string to create the API model.

    Args:
        hefloat_operator_id (bytes): The crypto system id
        stat_ciphertext (bytes): The encrypted statistics

    Returns:
        bytes: a JSON string representing a List[models.StatisticalResult].
    """
    decrypt_encrypted_stats = so.DecryptStatistics
    decrypt_encrypted_stats.restype = ctypes.c_char_p
    ctxt_length = len(stat_ciphertext)
    stats_plaintext = decrypt_encrypted_stats(
        hefloat_operator_id, stat_ciphertext, ctxt_length
    )
    if stats_plaintext is None:
        raise go_error()
    return stats_plaintext


def test_prediction_params() -> str:
    """Generates HEFloat parameters for a crypto system. (for testing purposes only)

    Returns:
        cryptoparameters_b64 (str): Base64 encoded marshalled HEFloat cryptoparameters
    """
    new_test_prediction_params = so.NewTestPredictionParams
    new_test_prediction_params.restype = ctypes.c_char_p
    cryptoparameters_b64 = new_test_prediction_params()
    if cryptoparameters_b64 is None:
        raise go_error()
    return cryptoparameters_b64


def test_polynomial_evaluation_hefloat_params() -> str:
    """Generates HEFloat parameters for a crypto system. (for testing purposes only)

    Returns:
        cryptoparameters_b64 (str): Base64 encoded marshalled HEFloat cryptoparameters
    """
    new_test_polynomial_hefloat_params = so.NewPolynomialCkksParams
    new_test_polynomial_hefloat_params.restype = ctypes.c_char_p
    cryptoparameters_b64 = new_test_polynomial_hefloat_params()
    if cryptoparameters_b64 is None:
        raise go_error()
    return cryptoparameters_b64


def encrypted_addition(
    hefloat_operator_id: bytes, number1: bytes, number2: bytes
) -> bytes:
    """
    Adds two encrypted numbers together.

    Args:
        hefloat_operator_id (bytes): The crypto system id
        number1, number2 (bytes): cyphertexts of the operands
    """
    add = so.Add
    add.restype = ctypes.c_void_p
    number1_size = len(number1)
    number2_size = len(number2)
    result = add(hefloat_operator_id, number1, number2, number1_size, number2_size)
    if result is None:
        raise go_error()
    res_length = int.from_bytes(ctypes.string_at(result, 8), "little")
    ciphertext = ctypes.string_at(result, res_length + 8)
    ciphertext = ciphertext[8:]
    return ciphertext


def encrypted_multiplication(
    hefloat_operator_id: bytes, number1: bytes, number2: bytes
) -> bytes:
    """
    Multiplies two encrypted numbers together.

    Args:
        hefloat_operator_id (bytes): The crypto system id
        number1, number2 (bytes): cyphertexts of the operands
    """
    multiply = so.Multiply
    multiply.restype = ctypes.c_void_p
    number1_size = len(number1)
    number2_size = len(number2)
    result = multiply(hefloat_operator_id, number1, number2, number1_size, number2_size)
    if result is None:
        raise go_error()
    res_length = int.from_bytes(ctypes.string_at(result, 8), "little")
    ciphertext = ctypes.string_at(result, res_length + 8)
    ciphertext = ciphertext[8:]
    return ciphertext


def encrypted_polynomial_evaluation(
    hefloat_operator_id: bytes,
    polynomial_coefficients: List[Union[int, float]],
    number: bytes,
) -> bytes:
    """
    Evaluates a plaintext polynomial on an encrypted number.

    Args:
        hefloat_operator_id (bytes): The crypto system id
        polynomial_coefficients (list[int, float]): the polynomial to evaluate.
        number1 (bytes): ciphertexts of the operand
    """
    polynomial_evaluation = so.PolynomialEvaluation
    polynomial_evaluation.restype = ctypes.c_void_p
    number_size = len(number)

    polynomial_coefficients = [str(i) for i in polynomial_coefficients]
    polynomial_coefficients = ",".join(polynomial_coefficients)
    polynomial_coefficients = polynomial_coefficients.encode("UTF-8")
    polynomial_size = len(polynomial_coefficients)

    result = polynomial_evaluation(
        hefloat_operator_id,
        polynomial_coefficients,
        polynomial_size,
        number,
        number_size,
    )
    if result is None:
        raise go_error()
    res_length = int.from_bytes(ctypes.string_at(result, 8), "little")
    ciphertext = ctypes.string_at(result, res_length + 8)
    ciphertext = ciphertext[8:]
    return ciphertext


def encrypt_number(hefloat_operator_id: bytes, number1: int) -> bytes:
    """
    Encrypt an integer.

    Args:
        hefloat_operator_id (bytes): The crypto system id
        number1 (int): the number to encrypt
    """
    encrypt = so.EncryptNumber
    encrypt.restype = ctypes.c_void_p
    byte_number = str(number1).encode("UTF-8")
    result = encrypt(hefloat_operator_id, byte_number)
    if result is None:
        raise go_error()
    result_length = int.from_bytes(ctypes.string_at(result, 8), "little")
    ciphertext = ctypes.string_at(result, result_length + 8)
    ciphertext = ciphertext[8:]
    return ciphertext


def decrypt_number(hefloat_operator_id: bytes, encrypted_number: bytes) -> int:
    """
    Decrypts an encrypted integer.

    Args:
        hefloat_operator_id (bytes): The crypto system id
        encrypted_number (int): the number to decrypt
    """
    decrypt = so.DecryptNumber
    decrypt.restype = ctypes.c_void_p
    encrypted_number_length = len(encrypted_number)
    result = decrypt(hefloat_operator_id, encrypted_number, encrypted_number_length)
    if result is None:
        raise go_error()
    result_length = int.from_bytes(ctypes.string_at(result, 8), "little")
    return result_length


def _handle_bytes_result(result) -> bytes:
    """Converts a result to bytes."""
    if result is None:
        raise go_error()
    result_length = int.from_bytes(ctypes.string_at(result, 8), "little")
    result_bytes = ctypes.string_at(result, result_length + 8)
    result_bytes = result_bytes[8:]
    return result_bytes


############################################### PIR ###############################################


class PIRContext:
    """
    Represents a PIR context for client side PIR operations

    Raises:
        go_error: upon getting invalid parameters
    """

    ctx_id: bytes

    def __init__(self, pir_b64: str, index_b64: str):
        """
        Initializes a PIR context.

        Args:
            pir_b64 (str): base64-encoded PIR parameters
            index_b64 (str): base64-encoded Index

        Raises:
            go_error: upon invalid parameters
        """
        func = so.NewPIRContext
        func.restype = ctypes.c_char_p
        self.ctx_id = func(pir_b64.encode(), index_b64.encode())
        if self.ctx_id is None:
            raise go_error()

    def get_eva_key(self) -> bytes:
        """
        Returns the bytes of the evaluation key set.

        Returns:
            bytes: the bytes of the evaluation key set
        """
        get_func = so.GetPIREvaluationKeyBytes
        get_func.restype = ctypes.c_void_p
        result = get_func(self.ctx_id)
        return _handle_bytes_result(result)

    def encrypt_query(self, query: str) -> bytes:
        """
        Encrypts a PIR query.

        Args:
            query (str): query string

        Returns:
            bytes: the encrypted query as bytes ready to be uploaded
        """
        encrypt_pir = so.EncryptPIRQuery
        encrypt_pir.restype = ctypes.c_void_p
        result = encrypt_pir(self.ctx_id, query.encode())
        return _handle_bytes_result(result)

    def decrypt_response(self, pir_result: bytes) -> bytes:
        """
        Decrypts the encrypted bytes as a plaintext CSV string.

        Args:
            pir_result (bytes): the encrypted bytes result

        Returns:
            bytes: the decrypted CSV as a byte string
        """
        decrypt_pir = so.DecryptPIRResult
        decrypt_pir.restype = ctypes.c_void_p
        result = decrypt_pir(self.ctx_id, pir_result, len(pir_result))
        return _handle_bytes_result(result)
