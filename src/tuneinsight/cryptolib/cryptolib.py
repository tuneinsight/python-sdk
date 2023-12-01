import ctypes
from pathlib import Path
from os.path import exists
from typing import List
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
    if "not found" in str(error_message):
        return ValueError(error_message)
    return Exception(error_message)

def new_hefloat_operator_from_b64_hefloat_parameters(hefloat_parameters_b64: str) -> bytes:
    """Instantiates a new HeFloat Operator from a base64 encoded hefloat parameters.

    Args:
        hefloat_parameters_b64 (str): Base64 encoded marshalled hefloat parameters

    Returns:
        hefloat_operator_id (bytes): The HEFloat Operator id
    """
    b64_hefloat_operator = so.NewHEFloatOperatorFromB64Parameters
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
    b64_hefloat_operator = so.NewHEFloatOperatorFromB64SchemeContext
    b64_hefloat_operator.restype = ctypes.c_char_p
    hefloat_operator_id = b64_hefloat_operator(scheme_context_b64.encode())
    if hefloat_operator_id is None:
        raise go_error()
    return hefloat_operator_id

def get_relin_key_bytes(hefloat_operator_id: bytes) -> bytes:
    '''
    get_relin_key_bytes retrieves the relinearization key bytes from the cryptosystem

    Args:
        hefloat_operator_id (bytes): the id of the cryptosystem

    Returns:
        bytes: the relinearization key bytes
    '''
    get_relin_key = so.GetRelinearizationKeyBytes
    get_relin_key.restype = ctypes.c_void_p
    res = get_relin_key(hefloat_operator_id)
    return _handle_bytes_result(res)

def encrypt_prediction_dataset(hefloat_operator_id:bytes,csv_bytes: bytes,b64_params: str,remove_header: bool) -> bytes:
    '''
    encrypt_prediction_dataset encrypts a provided dataset in prediction format using the secret key of the cryptosystem

    Args:
        hefloat_operator_id (bytes): the cryptosystem id
        csv_bytes (bytes): the csv data to encrypt
        b64_params (str): the base64 machine learning model parameters
        remove_header (bool): whether or not the csv data contains a header

    Returns:
        bytes: the encrypted version of the dataset that can be used as input to a encrypted prediction computation
    '''
    encrypt_pred = so.EncryptPredictionDataset
    encrypt_pred.restype = ctypes.c_void_p
    res = encrypt_pred(hefloat_operator_id,csv_bytes,len(csv_bytes),b64_params.encode(),ctypes.c_bool(remove_header))
    return _handle_bytes_result(res)


def decrypt_prediction(hefloat_operator_id: bytes,ct: bytes) -> bytes:
    '''
    decrypt_prediction decrypts the encrypted prediction ciphertext

    Args:
        hefloat_operator_id (bytes): the id of the cryptosystem storing the secret key
        ct (bytes): the encrypted prediction bytes

    Returns:
        bytes: the decrypted predicted values as a csv in byte format
    '''
    decrypt_pred = so.DecryptPredictionResult
    decrypt_pred.restype = ctypes.c_void_p
    res = decrypt_pred(hefloat_operator_id,ct,len(ct))
    return _handle_bytes_result(res)

def key_generation(hefloat_operator_id: bytes) -> bytes:
    """Generate a key for a given cryptosystem.

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

def relinearization_key_generation(hefloat_operator_id: bytes) -> bytes:
    """Generate a key for a given cryptosystem.

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
    """Instantiate a scheme for a given cryptosystem.

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
    """Encrypt a numeric pandas dataframe. Column names will be lost, index names are recovered.

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
    """Encrypt a csv formatted table of numbers.

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

def decrypt_dataframe(hefloat_operator_id: bytes,
                      dataframe_ciphertext: bytes,
                      headers: List[str] = None) -> pd.DataFrame:
    """Turn an encrypted pandas dataframe into a new decrypted pandas dataframe.
    Indices are recovered, column names can optionally be provided by the user.

    Args:
        hefloat_operator_id (bytes): The crypto system id
        dataframe_ciphertext (bytes): The encrypted pandas dataframe
        headers (list[str]): List of column names of the dataframe

    Returns:
        plaintext_dataframe (pandas.DataFrame): The decrypted dataframe
    """
    plaintext_csv_bytes = decrypt_csv(hefloat_operator_id, dataframe_ciphertext)
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


def decrypt_csv(hefloat_operator_id: bytes, csv_ciphertext: bytes) -> bytes:
    """Decrypt a cipher table into a CSV formatted string. The column names are not recovered.

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
        hefloat_operator_id, csv_ciphertext, ctxt_length)
    if csv_plaintext is None:
        raise go_error()
    return csv_plaintext


def test_prediction_params() -> str:
    """Generated HEFloat parameters for a crypto system. (for testing purposes only)

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
    """Generated HEFloat parameters for a crypto system. (for testing purposes only)

    Returns:
        cryptoparameters_b64 (str): Base64 encoded marshalled HEFloat cryptoparameters
    """
    new_test_polynomial_hefloat_params = so.NewPolynomialHEFloatParams
    new_test_polynomial_hefloat_params.restype = ctypes.c_char_p
    cryptoparameters_b64 = new_test_polynomial_hefloat_params()
    if cryptoparameters_b64 is None:
        raise go_error()
    return cryptoparameters_b64

def encrypted_addition(hefloat_operator_id: bytes,
                       number1: bytes,
                       number2: bytes) -> bytes:
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

def encrypted_multiplication(hefloat_operator_id: bytes, number1: bytes, number2: bytes) -> bytes:
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

def encrypted_polynomial_evaluation(hefloat_operator_id: bytes, polynomial_coefficients: list[int, float], number: bytes) -> bytes:
    polynomial_evaluation = so.PolynomialEvaluation
    polynomial_evaluation.restype = ctypes.c_void_p
    number_size = len(number)

    polynomial_coefficients = [str(i) for i in polynomial_coefficients]
    polynomial_coefficients = ",".join(polynomial_coefficients)
    polynomial_coefficients = polynomial_coefficients.encode('UTF-8')
    polynomial_size = len(polynomial_coefficients)

    result = polynomial_evaluation(hefloat_operator_id, polynomial_coefficients, polynomial_size, number, number_size)
    if result is None:
        raise go_error()
    res_length = int.from_bytes(ctypes.string_at(result, 8), "little")
    ciphertext = ctypes.string_at(result, res_length + 8)
    ciphertext = ciphertext[8:]
    return ciphertext

def encrypt_number(hefloat_operator_id: bytes, number1: int) -> bytes:
    encrypt = so.EncryptNumber
    encrypt.restype = ctypes.c_void_p
    byte_number = str(number1).encode('UTF-8')
    result = encrypt(hefloat_operator_id, byte_number)
    if result is None:
        raise go_error()
    result_length = int.from_bytes(ctypes.string_at(result, 8), "little")
    ciphertext = ctypes.string_at(result, result_length + 8)
    ciphertext = ciphertext[8:]
    return ciphertext

def decrypt_number(hefloat_operator_id: bytes, encrypted_number: bytes) -> int:
    decrypt = so.DecryptNumber
    decrypt.restype = ctypes.c_void_p
    encrypted_number_length = len(encrypted_number)
    result = decrypt(hefloat_operator_id, encrypted_number, encrypted_number_length)
    if result is None:
        raise go_error()
    result_length = int.from_bytes(ctypes.string_at(result, 8), "little")
    return result_length

def _handle_bytes_result(result) -> bytes:
    if result is None:
        raise go_error()
    result_length = int.from_bytes(ctypes.string_at(result, 8), "little")
    result_bytes = ctypes.string_at(result, result_length + 8)
    result_bytes = result_bytes[8:]
    return result_bytes

############################################### PIR ###############################################

class PIRContext:
    '''
    Represents a PIR context for client side PIR operations

    Raises:
        go_error: upon getting invalid parameters
    '''


    ctx_id: bytes

    def __init__(self,pir_b64:str,index_b64: str):
        '''
        __init__ initializes a PIR context

        Args:
            pir_b64 (str): base64-encoded PIR parameters
            index_b64 (str): base64-encoded Index

        Raises:
            go_error: upon invalid parameters
        '''
        func = so.NewPIRContext
        func.restype = ctypes.c_char_p
        self.ctx_id = func(pir_b64.encode(),index_b64.encode())
        if self.ctx_id is None:
            raise go_error()


    def get_eva_key(self) -> bytes:
        '''
        get_eva_key returns the bytes of the evaluation key set

        Returns:
            bytes: the bytes of the evaluation key set
        '''
        get_func = so.GetPIREvaluationKeyBytes
        get_func.restype = ctypes.c_void_p
        result = get_func(self.ctx_id)
        return _handle_bytes_result(result)

    def encrypt_query(self, query: str) -> bytes:
        '''
        encrypt_query encrypts the given query

        Args:
            query (str): query string

        Returns:
            bytes: the encrypted query as bytes ready to be uploaded
        '''
        encrypt_pir = so.EncryptPIRQuery
        encrypt_pir.restype = ctypes.c_void_p
        result = encrypt_pir(self.ctx_id, query.encode())
        return _handle_bytes_result(result)

    def decrypt_response(self, pir_result: bytes) -> bytes:
        '''
        decrypt_response decrypts the encrypted bytes as a plaintext csv string

        Args:
            pir_result (bytes): the encrypted bytes result

        Returns:
            bytes: the decrypted csv as a byte string
        '''
        decrypt_pir = so.DecryptPIRResult
        decrypt_pir.restype = ctypes.c_void_p
        result = decrypt_pir(self.ctx_id, pir_result, len(pir_result))
        return _handle_bytes_result(result)
