"""Utilities to parse errors in computations and raise appropriate Python errors."""

from typing import List
from tuneinsight.utils.errors import hidden_traceback_scope

from tuneinsight.api.sdk.models import ComputationError
from tuneinsight.api.sdk.models import ComputationErrorType as ErrorType


class DisclosurePreventionError(Exception):
    """
    Error raised when a computation is aborted because of a policy violation.
    """

    def __init__(self, comp_error: ComputationError):
        self.message = format_computation_error("computation aborted", comp_error)
        super().__init__(self.message)


class PreprocessingError(Exception):
    """
    Error that happens during preprocessing.
    """

    def __init__(self, comp_error: ComputationError):
        self.message = format_computation_error("error while preprocessing", comp_error)
        super().__init__(self.message)


class QueryError(Exception):
    """
    Error that happens when querying the data.
    """

    def __init__(self, comp_error: ComputationError):
        self.message = format_computation_error("error while querying data", comp_error)
        super().__init__(self.message)


class InternalError(Exception):
    """
    Unexpected error that happened on the Tune Insight instance in the computation.
    """

    def __init__(self, comp_error: ComputationError):
        self.message = format_computation_error("error happened internally", comp_error)
        super().__init__(self.message)


class ValidationError(Exception):
    """
    Error that happened while validating the data or user-defined parameters.
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
    Formats the computation error to a string that is displayed to the user.

    Args:
        prefix (str): the prefix that depends on the error type
        error (ComputationError): the error that was returned from the computation

    Returns:
        str: the formatted error
    """
    return f"{prefix}: {error.message}"


def raise_computation_error(errors: List[ComputationError]):
    """
    Raises the appropriate Python error, given the list of errors from the computation.

    The traceback of the errors is suppressed. If several errors are found, raise
    a Python exception for the first error, errors[0].

    Args:
        errors (List[ComputationError]): the list of errors returned with the computation

    Raises:
        exc: the appropriate computation error when a common pattern is detected
        ComputationError: the default computation error when no common pattern is detected
    """
    with hidden_traceback_scope():
        # Only take the first error.
        err = errors[0]
        if err.type in error_types:
            exc = error_types[err.type]
            raise exc(comp_error=err)
        raise InternalError(comp_error=err)
