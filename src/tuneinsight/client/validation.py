"""Utilities and errors to validate responses from the API."""

from tuneinsight.api.sdk.types import Response
from tuneinsight.utils.errors import hidden_traceback_scope


def validate_response(response: Response):
    """
    Ensures that an API call was successful.

    This validates an API response and raises an Exception in case the response is not successful.

    Args:
        response (Response): the API response.

    Raises:
        AuthorizationError: if the response's status code is 403.
        InvalidResponseError: if the response's status code is not successful.
    """
    if response.status_code < 200 or response.status_code > 210:
        with hidden_traceback_scope():
            if response.status_code == 403:
                raise AuthorizationError(response=response)
            if response.status_code == 404:
                raise LookupError(str(response.content))
            raise InvalidResponseError(response=response)


class AuthorizationError(Exception):
    """
    AuthorizationError is the exception used when the response status code is 403.
    """

    def __init__(self, response: Response):
        pattern = '"message":"'
        content = str(response.content)
        ind = content.find(pattern)
        content = content[ind + len(pattern) :]
        msg = content.split('"}', maxsplit=1)[0]
        super().__init__(msg)


class InvalidResponseError(Exception):
    """
    InvalidResponseError represents an exception when the response status code is erroneous.
    """

    def __init__(self, response: Response):
        message = f"Got Invalid Response with status code {response.status_code} and message {response.content}"
        if (
            b"when parsing token" in response.content
            or b"unsuccessful token validation" in response.content
        ):
            message += (
                "\n\nInvalid or expired token used. To obtain a valid token log in"
                + " with your credentials at sdk.tuneinsight.com and insert the token"
                + " in the static_token field of the sdk-config.yml file."
            )
        elif b"permission denied by the authorization provider" in response.content:
            message += (
                "\n\nCheck credentials or token validity. To obtain a valid token log"
                + " in with your credentials at sdk.tuneinsight.com and insert the token"
                + " in the static_token field of the sdk-config.yml file."
            )
        super().__init__(message)
