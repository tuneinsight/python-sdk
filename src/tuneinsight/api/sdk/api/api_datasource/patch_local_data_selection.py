from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.error import Error
from ...models.local_data_selection import LocalDataSelection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    selection_id: str,
    num_rows: Union[Unset, None, int] = UNSET,
    tolerate_query_errors: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    url = "{}/datasources/selections".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["selectionId"] = selection_id

    params["numRows"] = num_rows

    params["tolerateQueryErrors"] = tolerate_query_errors

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
        "method": "patch",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "proxies": proxies,
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Error, LocalDataSelection]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = LocalDataSelection.from_dict(response.json())

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


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Error, LocalDataSelection]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    selection_id: str,
    num_rows: Union[Unset, None, int] = UNSET,
    tolerate_query_errors: Union[Unset, None, bool] = UNSET,
) -> Response[Union[Error, LocalDataSelection]]:
    """modify the selection identified by selectionId

    Args:
        selection_id (str):
        num_rows (Union[Unset, None, int]):
        tolerate_query_errors (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, LocalDataSelection]]
    """

    kwargs = _get_kwargs(
        client=client,
        selection_id=selection_id,
        num_rows=num_rows,
        tolerate_query_errors=tolerate_query_errors,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    selection_id: str,
    num_rows: Union[Unset, None, int] = UNSET,
    tolerate_query_errors: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[Error, LocalDataSelection]]:
    """modify the selection identified by selectionId

    Args:
        selection_id (str):
        num_rows (Union[Unset, None, int]):
        tolerate_query_errors (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, LocalDataSelection]]
    """

    return sync_detailed(
        client=client,
        selection_id=selection_id,
        num_rows=num_rows,
        tolerate_query_errors=tolerate_query_errors,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    selection_id: str,
    num_rows: Union[Unset, None, int] = UNSET,
    tolerate_query_errors: Union[Unset, None, bool] = UNSET,
) -> Response[Union[Error, LocalDataSelection]]:
    """modify the selection identified by selectionId

    Args:
        selection_id (str):
        num_rows (Union[Unset, None, int]):
        tolerate_query_errors (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, LocalDataSelection]]
    """

    kwargs = _get_kwargs(
        client=client,
        selection_id=selection_id,
        num_rows=num_rows,
        tolerate_query_errors=tolerate_query_errors,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    selection_id: str,
    num_rows: Union[Unset, None, int] = UNSET,
    tolerate_query_errors: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[Error, LocalDataSelection]]:
    """modify the selection identified by selectionId

    Args:
        selection_id (str):
        num_rows (Union[Unset, None, int]):
        tolerate_query_errors (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, LocalDataSelection]]
    """

    return (
        await asyncio_detailed(
            client=client,
            selection_id=selection_id,
            num_rows=num_rows,
            tolerate_query_errors=tolerate_query_errors,
        )
    ).parsed
