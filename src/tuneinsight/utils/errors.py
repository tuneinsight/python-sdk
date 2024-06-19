"""Tools to hide long tracebacks when errors occur."""

from contextlib import contextmanager
import sys

from IPython.core.getipython import get_ipython


# Whether iPython is used.
IPYTHON_SET = False

try:
    ipython = get_ipython()
    ipython_traceback = ipython._showtraceback  # pylint: disable=W0212
    IPYTHON_SET = True
except AttributeError:
    pass


@contextmanager
def _custom_exception_handler(exc_handler):
    """Sets a custom exception handler for the scope of a 'with' block."""
    sys.excepthook = exc_handler
    if IPYTHON_SET:
        ipython._showtraceback = exc_handler  # pylint: disable=W0212
    yield


def _hiding_traceback(err_type, value, traceback):  # pylint: disable=W0613
    """
    Custom exception handler function that does not display the traceback.

    Args:
        err_type (_type_): the type of the exception
        value (_type_): the value of the exception
        traceback (_type_): the traceback which is not used
    """
    print(": ".join([str(err_type.__name__), str(value)]))
    sys.excepthook = sys.__excepthook__  # pylint: disable=W0212
    if IPYTHON_SET:
        ipython._showtraceback = ipython_traceback  # pylint: disable=W0212


def hidden_traceback_scope():
    """
    Hides the traceback of all errors occurring within the scope of a 'with' block.

    Typically, use this as
        with hidden_traceback_scope():
            [your code here]

    """
    return _custom_exception_handler(_hiding_traceback)
