from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.post_private_search_query_response_403 import PostPrivateSearchQueryResponse403
from ...models.private_search_query import PrivateSearchQuery
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: PrivateSearchQuery,
) -> Dict[str, Any]:
    url = "{}/private-search-queries".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[PostPrivateSearchQueryResponse403, PrivateSearchQuery, str]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PrivateSearchQuery.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(str, response.json())
        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = PostPrivateSearchQueryResponse403.from_dict(response.json())

        return response_403
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
) -> Response[Union[PostPrivateSearchQueryResponse403, PrivateSearchQuery, str]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: PrivateSearchQuery,
) -> Response[Union[PostPrivateSearchQueryResponse403, PrivateSearchQuery, str]]:
    """upload a private search query

    Args:
        json_body (PrivateSearchQuery): Definition of a private search query to upload

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PostPrivateSearchQueryResponse403, PrivateSearchQuery, str]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    json_body: PrivateSearchQuery,
) -> Optional[Union[PostPrivateSearchQueryResponse403, PrivateSearchQuery, str]]:
    """upload a private search query

    Args:
        json_body (PrivateSearchQuery): Definition of a private search query to upload

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PostPrivateSearchQueryResponse403, PrivateSearchQuery, str]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: PrivateSearchQuery,
) -> Response[Union[PostPrivateSearchQueryResponse403, PrivateSearchQuery, str]]:
    """upload a private search query

    Args:
        json_body (PrivateSearchQuery): Definition of a private search query to upload

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PostPrivateSearchQueryResponse403, PrivateSearchQuery, str]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    json_body: PrivateSearchQuery,
) -> Optional[Union[PostPrivateSearchQueryResponse403, PrivateSearchQuery, str]]:
    """upload a private search query

    Args:
        json_body (PrivateSearchQuery): Definition of a private search query to upload

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PostPrivateSearchQueryResponse403, PrivateSearchQuery, str]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
