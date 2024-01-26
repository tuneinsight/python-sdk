from __future__ import print_function
from contextlib import contextmanager
import sys
import warnings
from IPython.core.getipython import get_ipython

ipython_set = False


try:
    ipython = get_ipython()
    ipython_traceback = ipython._showtraceback  # pylint: disable=W0212
    ipython_set = True
except AttributeError:
    warnings.warn("unable to get ipython, traceback suppression is disabled")


@contextmanager
def except_handler(exc_handler):
    "Sets a custom exception handler for the scope of a 'with' block."
    sys.excepthook = exc_handler
    if ipython_set:
        ipython._showtraceback = exc_handler  # pylint: disable=W0212
    yield


def hide_traceback(err_type, value, traceback):  # pylint: disable=W0613
    """
    hide_traceback is a custom exception handler function which does not display the traceback

    Args:
        err_type (_type_): the type of the exceptionc
        value (_type_): the value of the exception
        traceback (_type_): the traceback which is not used
    """
    print(": ".join([str(err_type.__name__), str(value)]))
    sys.excepthook = sys.__excepthook__  # pylint: disable=W0212
    if ipython_set:
        ipython._showtraceback = ipython_traceback  # pylint: disable=W0212


def hidden_traceback_scope():
    """
    hided_traceback_scope returns a hided traceback scope that is such that any error raised in this scope will have its traceback hideen
    """
    return except_handler(hide_traceback)
