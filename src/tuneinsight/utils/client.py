"""Soon-to-be-deprecated module to set a client timeout in a with statement.

This module is (to be) deprecated because its only method, with_timeout, has
become a method of the Diapason class (Diapason.timeout).

"""

from contextlib import contextmanager
from tuneinsight.api.sdk.client import Client
from tuneinsight.utils import deprecation


@contextmanager
def with_timeout(c: Client, timeout: int):
    """
    Sets a custom timeout to the client temporarily to be used in a with statement.

    Use this as:
        with with_timeout(client, 600) as client:
            [your code here]

    Args:
        c (Client): the client to set the timeout to
        timeout (int): the timeout in seconds

    Yields:
        Client: the client with updated timeout
    """
    deprecation.warn("with_timeout", "Diapason.timeout")
    old_timeout = c.timeout
    c.timeout = timeout
    yield c
    c.timeout = old_timeout
