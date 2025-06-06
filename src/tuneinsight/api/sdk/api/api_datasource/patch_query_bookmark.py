from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.error import Error
from ...models.query_bookmark_definition import QueryBookmarkDefinition
from ...types import Response


def _get_kwargs(
    bookmark_id: str,
    *,
    client: Client,
    json_body: QueryBookmarkDefinition,
) -> Dict[str, Any]:
    url = "{}/query-bookmarks/{bookmarkId}".format(client.base_url, bookmarkId=bookmark_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

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
        "json": json_json_body,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Error, QueryBookmarkDefinition]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = QueryBookmarkDefinition.from_dict(response.json())

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


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Error, QueryBookmarkDefinition]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    bookmark_id: str,
    *,
    client: Client,
    json_body: QueryBookmarkDefinition,
) -> Response[Union[Error, QueryBookmarkDefinition]]:
    """Updates a specific query bookmark by ID.

    Args:
        bookmark_id (str):
        json_body (QueryBookmarkDefinition): editable fields of a query bookmark

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, QueryBookmarkDefinition]]
    """

    kwargs = _get_kwargs(
        bookmark_id=bookmark_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    bookmark_id: str,
    *,
    client: Client,
    json_body: QueryBookmarkDefinition,
) -> Optional[Union[Error, QueryBookmarkDefinition]]:
    """Updates a specific query bookmark by ID.

    Args:
        bookmark_id (str):
        json_body (QueryBookmarkDefinition): editable fields of a query bookmark

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, QueryBookmarkDefinition]]
    """

    return sync_detailed(
        bookmark_id=bookmark_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    bookmark_id: str,
    *,
    client: Client,
    json_body: QueryBookmarkDefinition,
) -> Response[Union[Error, QueryBookmarkDefinition]]:
    """Updates a specific query bookmark by ID.

    Args:
        bookmark_id (str):
        json_body (QueryBookmarkDefinition): editable fields of a query bookmark

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, QueryBookmarkDefinition]]
    """

    kwargs = _get_kwargs(
        bookmark_id=bookmark_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    bookmark_id: str,
    *,
    client: Client,
    json_body: QueryBookmarkDefinition,
) -> Optional[Union[Error, QueryBookmarkDefinition]]:
    """Updates a specific query bookmark by ID.

    Args:
        bookmark_id (str):
        json_body (QueryBookmarkDefinition): editable fields of a query bookmark

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, QueryBookmarkDefinition]]
    """

    return (
        await asyncio_detailed(
            bookmark_id=bookmark_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
