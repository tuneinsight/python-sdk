from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.local_data_selection import LocalDataSelection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    remote: Union[Unset, None, bool] = UNSET,
    local: Union[Unset, None, bool] = UNSET,
    ignored_instance: Union[Unset, None, str] = UNSET,
    timeout: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/datasources/selections/remote".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["remote"] = remote

    params["local"] = local

    params["ignoredInstance"] = ignored_instance

    params["timeout"] = timeout

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
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "proxies": proxies,
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[List["LocalDataSelection"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = LocalDataSelection.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code} ({response})")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[List["LocalDataSelection"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    remote: Union[Unset, None, bool] = UNSET,
    local: Union[Unset, None, bool] = UNSET,
    ignored_instance: Union[Unset, None, str] = UNSET,
    timeout: Union[Unset, None, int] = UNSET,
) -> Response[List["LocalDataSelection"]]:
    """retrieves all of the local data selections that are visible to the network

    Args:
        remote (Union[Unset, None, bool]):
        local (Union[Unset, None, bool]):
        ignored_instance (Union[Unset, None, str]):
        timeout (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['LocalDataSelection']]
    """

    kwargs = _get_kwargs(
        client=client,
        remote=remote,
        local=local,
        ignored_instance=ignored_instance,
        timeout=timeout,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    remote: Union[Unset, None, bool] = UNSET,
    local: Union[Unset, None, bool] = UNSET,
    ignored_instance: Union[Unset, None, str] = UNSET,
    timeout: Union[Unset, None, int] = UNSET,
) -> Optional[List["LocalDataSelection"]]:
    """retrieves all of the local data selections that are visible to the network

    Args:
        remote (Union[Unset, None, bool]):
        local (Union[Unset, None, bool]):
        ignored_instance (Union[Unset, None, str]):
        timeout (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['LocalDataSelection']]
    """

    return sync_detailed(
        client=client,
        remote=remote,
        local=local,
        ignored_instance=ignored_instance,
        timeout=timeout,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    remote: Union[Unset, None, bool] = UNSET,
    local: Union[Unset, None, bool] = UNSET,
    ignored_instance: Union[Unset, None, str] = UNSET,
    timeout: Union[Unset, None, int] = UNSET,
) -> Response[List["LocalDataSelection"]]:
    """retrieves all of the local data selections that are visible to the network

    Args:
        remote (Union[Unset, None, bool]):
        local (Union[Unset, None, bool]):
        ignored_instance (Union[Unset, None, str]):
        timeout (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['LocalDataSelection']]
    """

    kwargs = _get_kwargs(
        client=client,
        remote=remote,
        local=local,
        ignored_instance=ignored_instance,
        timeout=timeout,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    remote: Union[Unset, None, bool] = UNSET,
    local: Union[Unset, None, bool] = UNSET,
    ignored_instance: Union[Unset, None, str] = UNSET,
    timeout: Union[Unset, None, int] = UNSET,
) -> Optional[List["LocalDataSelection"]]:
    """retrieves all of the local data selections that are visible to the network

    Args:
        remote (Union[Unset, None, bool]):
        local (Union[Unset, None, bool]):
        ignored_instance (Union[Unset, None, str]):
        timeout (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['LocalDataSelection']]
    """

    return (
        await asyncio_detailed(
            client=client,
            remote=remote,
            local=local,
            ignored_instance=ignored_instance,
            timeout=timeout,
        )
    ).parsed
