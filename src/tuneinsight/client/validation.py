
from tuneinsight.api.sdk.types import Response



def validate_response(response: Response):
    """
    validate_response validates a given response, if the status code is erroneous it raises an InvalidResponse error

    Args:
        response (Response): the response

    Raises:
        InvalidResponseError: the exception if the response's status code is not successfull
    """
    if response.status_code < 200 or response.status_code > 210:
        raise InvalidResponseError(response=response)


class InvalidResponseError(Exception):
    """
    InvalidResponseError represents an exception when the response status code is erroneous

    Args:
        Exception: the base exception class
    """

    def __init__(self,response: Response):
        message = f'Got Invalid Reponse with status code {response.status_code} and message {response.content}'
        if b'when parsing token' in response.content or b'unsuccessful token validation' in response.content:
            message += "\n\nInvalid or expired token used. To obtain a valid token log in with your credentials at sdk.tuneinsight.com and insert the token in the static_token field of the sdk-config.yml file."
        elif b'permission denied by the authorization provider' in response.content:
            message += "\n\nCheck credentials or token validity. To obtain a valid token log in with your credentials at sdk.tuneinsight.com and insert the token in the static_token field of the sdk-config.yml file."
        super().__init__(message)
