from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.encrypted_content import EncryptedContent
from ...models.error import Error
from ...models.external_ml_result import ExternalMlResult
from ...models.float_matrix import FloatMatrix
from ...models.prediction import Prediction
from ...models.statistics import Statistics
from ...models.string_matrix import StringMatrix
from ...types import Response


def _get_kwargs(
    data_object_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/dataobjects/{dataObjectId}/data".format(client.base_url, dataObjectId=data_object_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    # Set the proxies if the client has proxies set.
    proxies = None
    if hasattr(client, "proxies") and client.proxies is not None:
        https_proxy = client.proxies.get("https://")
        if https_proxy:
            proxies = https_proxy
        else:
            http_proxy = client.proxies.get("http://")
            if http_proxy:
                proxies = http_proxy

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "proxies": proxies,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[
    Union[
        Error, Union["EncryptedContent", "ExternalMlResult", "FloatMatrix", "Prediction", "Statistics", "StringMatrix"]
    ]
]:
    if response.status_code == HTTPStatus.OK:

        def _parse_response_200(
            data: object,
        ) -> Union["EncryptedContent", "ExternalMlResult", "FloatMatrix", "Prediction", "Statistics", "StringMatrix"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = FloatMatrix.from_dict(data)

                return response_200_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_1 = StringMatrix.from_dict(data)

                return response_200_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_2 = EncryptedContent.from_dict(data)

                return response_200_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_3 = Prediction.from_dict(data)

                return response_200_type_3
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_4 = ExternalMlResult.from_dict(data)

                return response_200_type_4
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_5 = Statistics.from_dict(data)

            return response_200_type_5

        response_200 = _parse_response_200(response.json())

        return response_200
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = Error.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = Error.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = Error.from_dict(response.json())

        return response_422
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = Error.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code} ({response})")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[
    Union[
        Error, Union["EncryptedContent", "ExternalMlResult", "FloatMatrix", "Prediction", "Statistics", "StringMatrix"]
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    data_object_id: str,
    *,
    client: Client,
) -> Response[
    Union[
        Error, Union["EncryptedContent", "ExternalMlResult", "FloatMatrix", "Prediction", "Statistics", "StringMatrix"]
    ]
]:
    """Get the content of a data object.

    Args:
        data_object_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Union['EncryptedContent', 'ExternalMlResult', 'FloatMatrix', 'Prediction', 'Statistics', 'StringMatrix']]]
    """

    kwargs = _get_kwargs(
        data_object_id=data_object_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    data_object_id: str,
    *,
    client: Client,
) -> Optional[
    Union[
        Error, Union["EncryptedContent", "ExternalMlResult", "FloatMatrix", "Prediction", "Statistics", "StringMatrix"]
    ]
]:
    """Get the content of a data object.

    Args:
        data_object_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Union['EncryptedContent', 'ExternalMlResult', 'FloatMatrix', 'Prediction', 'Statistics', 'StringMatrix']]]
    """

    return sync_detailed(
        data_object_id=data_object_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    data_object_id: str,
    *,
    client: Client,
) -> Response[
    Union[
        Error, Union["EncryptedContent", "ExternalMlResult", "FloatMatrix", "Prediction", "Statistics", "StringMatrix"]
    ]
]:
    """Get the content of a data object.

    Args:
        data_object_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Union['EncryptedContent', 'ExternalMlResult', 'FloatMatrix', 'Prediction', 'Statistics', 'StringMatrix']]]
    """

    kwargs = _get_kwargs(
        data_object_id=data_object_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    data_object_id: str,
    *,
    client: Client,
) -> Optional[
    Union[
        Error, Union["EncryptedContent", "ExternalMlResult", "FloatMatrix", "Prediction", "Statistics", "StringMatrix"]
    ]
]:
    """Get the content of a data object.

    Args:
        data_object_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Union['EncryptedContent', 'ExternalMlResult', 'FloatMatrix', 'Prediction', 'Statistics', 'StringMatrix']]]
    """

    return (
        await asyncio_detailed(
            data_object_id=data_object_id,
            client=client,
        )
    ).parsed
