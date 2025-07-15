from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    json_body: List[str],
    read_all: Union[Unset, None, bool] = UNSET,
    archive_all: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    url = "{}/notifications".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["readAll"] = read_all

    params["archiveAll"] = archive_all

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body

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
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, Error]]:
    if response.status_code == HTTPStatus.NO_CONTENT:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = Error.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = Error.from_dict(response.json())

        return response_401
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


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: List[str],
    read_all: Union[Unset, None, bool] = UNSET,
    archive_all: Union[Unset, None, bool] = UNSET,
) -> Response[Union[Any, Error]]:
    """perform a batch operation on notifications.

    Args:
        read_all (Union[Unset, None, bool]):
        archive_all (Union[Unset, None, bool]):
        json_body (List[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        read_all=read_all,
        archive_all=archive_all,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    json_body: List[str],
    read_all: Union[Unset, None, bool] = UNSET,
    archive_all: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[Any, Error]]:
    """perform a batch operation on notifications.

    Args:
        read_all (Union[Unset, None, bool]):
        archive_all (Union[Unset, None, bool]):
        json_body (List[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        read_all=read_all,
        archive_all=archive_all,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: List[str],
    read_all: Union[Unset, None, bool] = UNSET,
    archive_all: Union[Unset, None, bool] = UNSET,
) -> Response[Union[Any, Error]]:
    """perform a batch operation on notifications.

    Args:
        read_all (Union[Unset, None, bool]):
        archive_all (Union[Unset, None, bool]):
        json_body (List[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        read_all=read_all,
        archive_all=archive_all,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    json_body: List[str],
    read_all: Union[Unset, None, bool] = UNSET,
    archive_all: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[Any, Error]]:
    """perform a batch operation on notifications.

    Args:
        read_all (Union[Unset, None, bool]):
        archive_all (Union[Unset, None, bool]):
        json_body (List[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            read_all=read_all,
            archive_all=archive_all,
        )
    ).parsed
