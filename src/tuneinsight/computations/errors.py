from typing import List
from tuneinsight.utils.errors import hidden_traceback_scope
from tuneinsight.api.sdk.models import ComputationError
from tuneinsight.api.sdk.models import ComputationErrorType as ErrorType


class DisclosurePreventionError(Exception):
    """
    DisclosurePreventionError Exception class for the disclosure prevention error
    """

    def __init__(self, comp_error: ComputationError):
        self.message = format_computation_error("computation aborted", comp_error)
        super().__init__(self.message)


class PreprocessingError(Exception):
    """
    PreprocessingError is used to represent error that happen during preprocessing
    """

    def __init__(self, comp_error: ComputationError):
        self.message = format_computation_error("error while preprocessing", comp_error)
        super().__init__(self.message)


class QueryError(Exception):
    def __init__(self, comp_error: ComputationError):
        self.message = format_computation_error("error while querying data", comp_error)
        super().__init__(self.message)


class InternalError(Exception):
    """
    InternalError is used represent unexpected errors that happened internally in the computation
    """

    def __init__(self, comp_error: ComputationError):
        self.message = format_computation_error("error happened internally", comp_error)
        super().__init__(self.message)


class ValidationError(Exception):
    """
    ValidationError is used represent unexpected errors that happened while validating the data or user-defined parameters
    """

    def __init__(self, comp_error: ComputationError):
        self.message = format_computation_error(
            "error while validating inputs", comp_error
        )
        super().__init__(self.message)


error_types = {
    ErrorType.DISCLOSUREPREVENTION: DisclosurePreventionError,
    ErrorType.INTERNAL: InternalError,
    ErrorType.PREPROCESSING: PreprocessingError,
    ErrorType.QUERY: QueryError,
    ErrorType.VALIDATION: ValidationError,
}
"""
Mapping from computation error type to the appropriate exception
"""


def format_computation_error(prefix: str, error: ComputationError) -> str:
    """
    format_computation_error formats the computation error to a string that is displayed to the user

    Args:
        prefix (str): the prefix that depends on the error type
        error (ComputationError): the error that was returned from the computation

    Returns:
        str: the formatted error
    """
    return f"{prefix}: {error.message}"


def raise_computation_error(errors: List[ComputationError]):
    """
    raise_computation_error raises the appropriate given the list of errors from the computation and suppresses any traceback

    Args:
        errors (List[ComputationError]): the list of errors returned with the computation

    Raises:
        exc: the appropriate computation error when a common pattern is detected
        ComputationError: the default computation error when no common pattern is detected
    """
    with hidden_traceback_scope():
        if len(errors) > 0:
            # Only take the first error
            err = errors[0]
        if err.type in error_types:
            exc = error_types[err.type]
            raise exc(comp_error=err)
        raise InternalError(comp_error=err)
