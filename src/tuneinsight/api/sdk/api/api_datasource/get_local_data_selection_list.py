from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.error import Error
from ...models.local_data_selection import LocalDataSelection
from ...types import Response


def _get_kwargs(
    data_source_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/datasources/{dataSourceId}/selections".format(client.base_url, dataSourceId=data_source_id)

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Error, List["LocalDataSelection"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = LocalDataSelection.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = Error.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = Error.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = Error.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = Error.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.NOT_IMPLEMENTED:
        response_501 = Error.from_dict(response.json())

        return response_501
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code} ({response})")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Error, List["LocalDataSelection"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    data_source_id: str,
    *,
    client: Client,
) -> Response[Union[Error, List["LocalDataSelection"]]]:
    """retrieves all of the selections that have been created for this datasource

    Args:
        data_source_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, List['LocalDataSelection']]]
    """

    kwargs = _get_kwargs(
        data_source_id=data_source_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    data_source_id: str,
    *,
    client: Client,
) -> Optional[Union[Error, List["LocalDataSelection"]]]:
    """retrieves all of the selections that have been created for this datasource

    Args:
        data_source_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, List['LocalDataSelection']]]
    """

    return sync_detailed(
        data_source_id=data_source_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    data_source_id: str,
    *,
    client: Client,
) -> Response[Union[Error, List["LocalDataSelection"]]]:
    """retrieves all of the selections that have been created for this datasource

    Args:
        data_source_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, List['LocalDataSelection']]]
    """

    kwargs = _get_kwargs(
        data_source_id=data_source_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    data_source_id: str,
    *,
    client: Client,
) -> Optional[Union[Error, List["LocalDataSelection"]]]:
    """retrieves all of the selections that have been created for this datasource

    Args:
        data_source_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, List['LocalDataSelection']]]
    """

    return (
        await asyncio_detailed(
            data_source_id=data_source_id,
            client=client,
        )
    ).parsed
