from contextlib import contextmanager
from tuneinsight.api.sdk.client import Client


@contextmanager
def with_timeout(c: Client, timeout: int):
    """
    with_timeout sets a custom timeout to the client temporarily to be used in a with statement

    Args:
        c (Client): the client to set the timeout to
        timeout (int): the timeout in seconds

    Yields:
        Client: the client with updated timeout
    """
    old_timeout = c.timeout
    c.timeout = timeout
    yield c
    c.timeout = old_timeout
