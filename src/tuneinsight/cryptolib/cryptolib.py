import ctypes
from pathlib import Path
from os.path import exists
import platform
import pandas as pd

# Location of shared library
cwd = Path(__file__).absolute().parent
arch = platform.machine()
os = platform.system().lower()
cryptolib_path = cwd / f"cryptolib-{os}_{arch}.so"
if not exists(cryptolib_path):
    raise FileNotFoundError("Could not find the cryptolib library. Your platform might not be supported.")
so = ctypes.cdll.LoadLibrary(cryptolib_path)

def go_error() -> Exception:
    """Raise a python exception from the latest go error."""

    get_go_error = so.GetLastError
    get_go_error.restype = ctypes.c_char_p
    error_message = get_go_error()
    return Exception(error_message)

def load_b64_cryptosystem(cryptoparams_b64: str) -> bytes:
    """Load a cryptosystem with base64 encoded parameters.

    Args:
        cryptoparams_b64 (str): Base64 encoded marshalled cryptoparameters

    Returns:
        crypto_system_id (bytes): The crypto system id
    """
    b64_crypto_system = so.LoadB64CryptoSystem
    b64_crypto_system.restype = ctypes.c_char_p
    crypto_system_id = b64_crypto_system(cryptoparams_b64)
    if crypto_system_id is None:
        raise go_error()
    return crypto_system_id


def key_generation(crypto_system_id: bytes) -> bytes:
    """Generate a key for a given cryptosystem.

    Args:
        crypto_system_id (bytes): The crypto system id

    Returns:
        key_response (bytes): The response message of the key generation
    """
    key_gen = so.GenKeyPair
    key_gen.restype = ctypes.c_char_p
    key_response = key_gen(crypto_system_id)
    if key_response is None:
        raise go_error()
    return key_response

def relinearization_key_generation(crypto_system_id: bytes) -> bytes:
    """Generate a key for a given cryptosystem.

    Args:
        crypto_system_id (bytes): The crypto system id

    Returns:
        key_response (bytes): The response message of the key generation
    """
    relin_key_gen = so.GenRelinearizationKey
    relin_key_gen.restype = ctypes.c_char_p
    key_response = relin_key_gen(crypto_system_id)
    if key_response is None:
        raise go_error()
    return key_response


def instantiate_scheme(crypto_system_id: bytes) -> bytes:
    """Instantiate a scheme for a given cryptosystem.

    Args:
        crypto_system_id (bytes): The crypto system id

    Returns:
        scheme_response (bytes): The response message of the scheme instantiation
    """
    instantiate_crypto_scheme = so.InstantiateScheme
    instantiate_crypto_scheme.restype = ctypes.c_char_p
    scheme_response = instantiate_crypto_scheme(crypto_system_id)
    if scheme_response is None:
        raise go_error()
    return scheme_response


def encrypt_dataframe(crypto_system_id: bytes, dataframe: pd.DataFrame) -> bytes:
    """Encrypt a numeric pandas dataframe. Column names will be lost, index names are recovered.

    Args:
        crypto_system_id (bytes): The crypto system id
        dataframe (bytes): The pandas.DataFrame that will be encrypted

    Returns:
        ciphertext (bytes): The generated ciphertext
    """
    plaintext_dataframe = dataframe.to_csv().encode("UTF-8")
    ciphertext = encrypt_matrix(crypto_system_id, plaintext_dataframe)
    if ciphertext is None:
        raise go_error()
    return ciphertext


def encrypt_matrix(crypto_system_id: bytes, csv_string: bytes) -> bytes:
    """Encrypt a csv formatted table of numbers.

    Args:
        crypto_system_id (bytes): The crypto system id
        csv_string (bytes): The csv content that will be encrypted

    Returns:
        ciphertext (bytes): The generated ciphertext
    """
    encrypt_float_matrix = so.EncryptFloatMatrix
    encrypt_float_matrix.restype = ctypes.c_void_p
    res = encrypt_float_matrix(crypto_system_id, csv_string)
    if res is None:
        raise go_error()
    res_length = int.from_bytes(ctypes.string_at(res, 8), "little")
    ciphertext = ctypes.string_at(res, res_length + 8)
    ciphertext = ciphertext[8:]
    return ciphertext

def decrypt_dataframe(crypto_system_id: bytes,
                      dataframe_ciphertext: bytes,
                      headers: list[str] = None) -> pd.DataFrame:
    """Turn an encrypted pandas dataframe into a new decrypted pandas dataframe.
    Indices are recovered, column names can optionally be provided by the user.

    Args:
        crypto_system_id (bytes): The crypto system id
        dataframe_ciphertext (bytes): The encrypted pandas dataframe
        headers (list[str]): List of column names of the dataframe

    Returns:
        plaintext_dataframe (pandas.DataFrame): The decrypted dataframe
    """
    plaintext_csv_bytes = decrypt_csv(crypto_system_id, dataframe_ciphertext)
    if plaintext_csv_bytes is None:
        raise go_error()
    plaintext_csv = plaintext_csv_bytes.decode('utf8')
    plaintext_dataframe = pd.DataFrame(
        [row.split(',') for row in plaintext_csv.split('\n')])
    plaintext_dataframe = plaintext_dataframe.set_index(
        plaintext_dataframe.columns[0])
    plaintext_dataframe.index.name = None
    if headers is not None:
        if len(headers) != len(plaintext_dataframe.columns):
            raise IndexError("There must be as many headers as columns.")
        plaintext_dataframe.columns = headers
    # Convert values back to numeric
    plaintext_dataframe = plaintext_dataframe.applymap(float)
    return plaintext_dataframe


def decrypt_csv(crypto_system_id: bytes, csv_ciphertext: bytes) -> bytes:
    """Decrypt a cipher table into a CSV formatted string. The column names are not recovered.

    Args:
        crypto_system_id (bytes): The crypto system id
        csv_ciphertext (bytes): The encrypted pandas dataframe

    Returns:
        csv_plaintext (bytes): The decrypted csv string
    """
    decrypt_cipher_table = so.DecryptCipherTable
    decrypt_cipher_table.restype = ctypes.c_char_p
    ctxt_length = len(csv_ciphertext)
    csv_plaintext = decrypt_cipher_table(
        crypto_system_id, csv_ciphertext, ctxt_length)
    if csv_plaintext is None:
        raise go_error()
    return csv_plaintext


def test_prediction_ckks_params() -> str:
    """Generated CKKS parameters for a crypto system. (for testing purposes only)

    Returns:
        cryptoparameters_b64 (str): Base64 encoded marshalled CKKS cryptoparameters
    """
    new_test_prediction_CKKS_params = so.NewTestPredictionCKKSParams
    new_test_prediction_CKKS_params.restype = ctypes.c_char_p
    cryptoparameters_b64 = new_test_prediction_CKKS_params()
    if cryptoparameters_b64 is None:
        raise go_error()
    return cryptoparameters_b64


def test_polynomial_evaluation_ckks_params() -> str:
    """Generated CKKS parameters for a crypto system. (for testing purposes only)

    Returns:
        cryptoparameters_b64 (str): Base64 encoded marshalled CKKS cryptoparameters
    """
    new_test_polynomial_CKKS_params = so.NewPolynomialCKKSParams
    new_test_polynomial_CKKS_params.restype = ctypes.c_char_p
    cryptoparameters_b64 = new_test_polynomial_CKKS_params()
    if cryptoparameters_b64 is None:
        raise go_error()
    return cryptoparameters_b64

def encrypted_addition(crypto_system_id: bytes,
                       number1: bytes,
                       number2: bytes) -> bytes:
    add = so.Add
    add.restype = ctypes.c_void_p
    number1_size = len(number1)
    number2_size = len(number2)
    result = add(crypto_system_id, number1, number2, number1_size, number2_size)
    if result is None:
        raise go_error()
    res_length = int.from_bytes(ctypes.string_at(result, 8), "little")
    ciphertext = ctypes.string_at(result, res_length + 8)
    ciphertext = ciphertext[8:]
    return ciphertext

def encrypted_multiplication(crypto_system_id: bytes, number1: bytes, number2: bytes) -> bytes:
    multiply = so.Multiply
    multiply.restype = ctypes.c_void_p
    number1_size = len(number1)
    number2_size = len(number2)
    result = multiply(crypto_system_id, number1, number2, number1_size, number2_size)
    if result is None:
        raise go_error()
    res_length = int.from_bytes(ctypes.string_at(result, 8), "little")
    ciphertext = ctypes.string_at(result, res_length + 8)
    ciphertext = ciphertext[8:]
    return ciphertext

def encrypted_polynomial_evaluation(crypto_system_id: bytes, number: bytes) -> bytes:
    polynomial_evaluation = so.PolynomialEvaluation
    polynomial_evaluation.restype = ctypes.c_void_p
    number_size = len(number)
    result = polynomial_evaluation(crypto_system_id, number, number_size)
    if result is None:
        raise go_error()
    res_length = int.from_bytes(ctypes.string_at(result, 8), "little")
    ciphertext = ctypes.string_at(result, res_length + 8)
    ciphertext = ciphertext[8:]
    return ciphertext

def create_polynomial(crypto_system_id: bytes, polynomial_coefficients: list[float]) -> bytes:
    generate_polynomial = so.GenPolynomial
    generate_polynomial.restype = ctypes.c_char_p
    # Convert coefficients into csv byte string
    polynomial_coefficients = [str(i) for i in polynomial_coefficients]
    polynomial_coefficients = ",".join(polynomial_coefficients)
    polynomial_coefficients = polynomial_coefficients.encode('UTF-8')
    polynomial_size = len(polynomial_coefficients)
    result = generate_polynomial(crypto_system_id, polynomial_coefficients, polynomial_size)
    if result is None:
        raise go_error()
    return result

def encrypt_number(crypto_system_id: bytes, number1: int) -> bytes:
    encrypt = so.EncryptNumber
    encrypt.restype = ctypes.c_void_p
    byte_number = str(number1).encode('UTF-8')
    result = encrypt(crypto_system_id, byte_number)
    if result is None:
        raise go_error()
    result_length = int.from_bytes(ctypes.string_at(result, 8), "little")
    ciphertext = ctypes.string_at(result, result_length + 8)
    ciphertext = ciphertext[8:]
    return ciphertext

def decrypt_number(crypto_system_id: bytes, encrypted_number: bytes) -> int:
    decrypt = so.DecryptNumber
    decrypt.restype = ctypes.c_void_p
    encrypted_number_length = len(encrypted_number)
    result = decrypt(crypto_system_id, encrypted_number, encrypted_number_length)
    if result is None:
        raise go_error()
    result_length = int.from_bytes(ctypes.string_at(result, 8), "little")
    return result_length
