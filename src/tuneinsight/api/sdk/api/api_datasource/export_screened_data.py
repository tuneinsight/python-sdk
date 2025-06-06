from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.data_source import DataSource
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    session_id: str,
    *,
    client: Client,
    data_source_name: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/screening-sessions/{sessionId}/export".format(client.base_url, sessionId=session_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["dataSourceName"] = data_source_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

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
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "proxies": proxies,
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[DataSource, Error]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = DataSource.from_dict(response.json())

        return response_201
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


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[DataSource, Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    session_id: str,
    *,
    client: Client,
    data_source_name: Union[Unset, None, str] = UNSET,
) -> Response[Union[DataSource, Error]]:
    """exports the screened data from a session to a local data source

    Args:
        session_id (str):
        data_source_name (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DataSource, Error]]
    """

    kwargs = _get_kwargs(
        session_id=session_id,
        client=client,
        data_source_name=data_source_name,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    session_id: str,
    *,
    client: Client,
    data_source_name: Union[Unset, None, str] = UNSET,
) -> Optional[Union[DataSource, Error]]:
    """exports the screened data from a session to a local data source

    Args:
        session_id (str):
        data_source_name (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DataSource, Error]]
    """

    return sync_detailed(
        session_id=session_id,
        client=client,
        data_source_name=data_source_name,
    ).parsed


async def asyncio_detailed(
    session_id: str,
    *,
    client: Client,
    data_source_name: Union[Unset, None, str] = UNSET,
) -> Response[Union[DataSource, Error]]:
    """exports the screened data from a session to a local data source

    Args:
        session_id (str):
        data_source_name (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DataSource, Error]]
    """

    kwargs = _get_kwargs(
        session_id=session_id,
        client=client,
        data_source_name=data_source_name,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    session_id: str,
    *,
    client: Client,
    data_source_name: Union[Unset, None, str] = UNSET,
) -> Optional[Union[DataSource, Error]]:
    """exports the screened data from a session to a local data source

    Args:
        session_id (str):
        data_source_name (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DataSource, Error]]
    """

    return (
        await asyncio_detailed(
            session_id=session_id,
            client=client,
            data_source_name=data_source_name,
        )
    ).parsed
