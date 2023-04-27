from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.computation import Computation
from ...models.get_computation_response_403 import GetComputationResponse403
from ...types import Response


def _get_kwargs(
    computation_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/computations/{computationId}".format(client.base_url, computationId=computation_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Computation, GetComputationResponse403, str]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Computation.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = GetComputationResponse403.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(str, response.json())
        return response_404
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = cast(str, response.json())
        return response_422
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = cast(str, response.json())
        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[Computation, GetComputationResponse403, str]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    computation_id: str,
    *,
    client: Client,
) -> Response[Union[Computation, GetComputationResponse403, str]]:
    """Get a computation.

    Args:
        computation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Computation, GetComputationResponse403, str]]
    """

    kwargs = _get_kwargs(
        computation_id=computation_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    computation_id: str,
    *,
    client: Client,
) -> Optional[Union[Computation, GetComputationResponse403, str]]:
    """Get a computation.

    Args:
        computation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Computation, GetComputationResponse403, str]]
    """

    return sync_detailed(
        computation_id=computation_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    computation_id: str,
    *,
    client: Client,
) -> Response[Union[Computation, GetComputationResponse403, str]]:
    """Get a computation.

    Args:
        computation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Computation, GetComputationResponse403, str]]
    """

    kwargs = _get_kwargs(
        computation_id=computation_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    computation_id: str,
    *,
    client: Client,
) -> Optional[Union[Computation, GetComputationResponse403, str]]:
    """Get a computation.

    Args:
        computation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Computation, GetComputationResponse403, str]]
    """

    return (
        await asyncio_detailed(
            computation_id=computation_id,
            client=client,
        )
    ).parsed
