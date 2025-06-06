from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.error import Error
from ...models.get_query_bookmarks_data_source_type import GetQueryBookmarksDataSourceType
from ...models.get_query_bookmarks_order import GetQueryBookmarksOrder
from ...models.get_query_bookmarks_sort_by import GetQueryBookmarksSortBy
from ...models.query_bookmark_definition import QueryBookmarkDefinition
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    data_source_type: Union[Unset, None, GetQueryBookmarksDataSourceType] = UNSET,
    page: Union[Unset, None, int] = 1,
    per_page: Union[Unset, None, int] = 50,
    with_total: Union[Unset, None, bool] = True,
    sort_by: Union[Unset, None, GetQueryBookmarksSortBy] = UNSET,
    order: Union[Unset, None, GetQueryBookmarksOrder] = UNSET,
) -> Dict[str, Any]:
    url = "{}/query-bookmarks".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_data_source_type: Union[Unset, None, str] = UNSET
    if not isinstance(data_source_type, Unset):
        json_data_source_type = data_source_type.value if data_source_type else None

    params["dataSourceType"] = json_data_source_type

    params["page"] = page

    params["perPage"] = per_page

    params["withTotal"] = with_total

    json_sort_by: Union[Unset, None, str] = UNSET
    if not isinstance(sort_by, Unset):
        json_sort_by = sort_by.value if sort_by else None

    params["sortBy"] = json_sort_by

    json_order: Union[Unset, None, str] = UNSET
    if not isinstance(order, Unset):
        json_order = order.value if order else None

    params["order"] = json_order

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


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Error, List["QueryBookmarkDefinition"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = QueryBookmarkDefinition.from_dict(response_200_item_data)

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


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[Error, List["QueryBookmarkDefinition"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    data_source_type: Union[Unset, None, GetQueryBookmarksDataSourceType] = UNSET,
    page: Union[Unset, None, int] = 1,
    per_page: Union[Unset, None, int] = 50,
    with_total: Union[Unset, None, bool] = True,
    sort_by: Union[Unset, None, GetQueryBookmarksSortBy] = UNSET,
    order: Union[Unset, None, GetQueryBookmarksOrder] = UNSET,
) -> Response[Union[Error, List["QueryBookmarkDefinition"]]]:
    """returns the list of query bookmarks that are viewable by the requesting user.

    Args:
        data_source_type (Union[Unset, None, GetQueryBookmarksDataSourceType]):
        page (Union[Unset, None, int]):  Default: 1.
        per_page (Union[Unset, None, int]):  Default: 50.
        with_total (Union[Unset, None, bool]):  Default: True.
        sort_by (Union[Unset, None, GetQueryBookmarksSortBy]):
        order (Union[Unset, None, GetQueryBookmarksOrder]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, List['QueryBookmarkDefinition']]]
    """

    kwargs = _get_kwargs(
        client=client,
        data_source_type=data_source_type,
        page=page,
        per_page=per_page,
        with_total=with_total,
        sort_by=sort_by,
        order=order,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    data_source_type: Union[Unset, None, GetQueryBookmarksDataSourceType] = UNSET,
    page: Union[Unset, None, int] = 1,
    per_page: Union[Unset, None, int] = 50,
    with_total: Union[Unset, None, bool] = True,
    sort_by: Union[Unset, None, GetQueryBookmarksSortBy] = UNSET,
    order: Union[Unset, None, GetQueryBookmarksOrder] = UNSET,
) -> Optional[Union[Error, List["QueryBookmarkDefinition"]]]:
    """returns the list of query bookmarks that are viewable by the requesting user.

    Args:
        data_source_type (Union[Unset, None, GetQueryBookmarksDataSourceType]):
        page (Union[Unset, None, int]):  Default: 1.
        per_page (Union[Unset, None, int]):  Default: 50.
        with_total (Union[Unset, None, bool]):  Default: True.
        sort_by (Union[Unset, None, GetQueryBookmarksSortBy]):
        order (Union[Unset, None, GetQueryBookmarksOrder]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, List['QueryBookmarkDefinition']]]
    """

    return sync_detailed(
        client=client,
        data_source_type=data_source_type,
        page=page,
        per_page=per_page,
        with_total=with_total,
        sort_by=sort_by,
        order=order,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    data_source_type: Union[Unset, None, GetQueryBookmarksDataSourceType] = UNSET,
    page: Union[Unset, None, int] = 1,
    per_page: Union[Unset, None, int] = 50,
    with_total: Union[Unset, None, bool] = True,
    sort_by: Union[Unset, None, GetQueryBookmarksSortBy] = UNSET,
    order: Union[Unset, None, GetQueryBookmarksOrder] = UNSET,
) -> Response[Union[Error, List["QueryBookmarkDefinition"]]]:
    """returns the list of query bookmarks that are viewable by the requesting user.

    Args:
        data_source_type (Union[Unset, None, GetQueryBookmarksDataSourceType]):
        page (Union[Unset, None, int]):  Default: 1.
        per_page (Union[Unset, None, int]):  Default: 50.
        with_total (Union[Unset, None, bool]):  Default: True.
        sort_by (Union[Unset, None, GetQueryBookmarksSortBy]):
        order (Union[Unset, None, GetQueryBookmarksOrder]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, List['QueryBookmarkDefinition']]]
    """

    kwargs = _get_kwargs(
        client=client,
        data_source_type=data_source_type,
        page=page,
        per_page=per_page,
        with_total=with_total,
        sort_by=sort_by,
        order=order,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    data_source_type: Union[Unset, None, GetQueryBookmarksDataSourceType] = UNSET,
    page: Union[Unset, None, int] = 1,
    per_page: Union[Unset, None, int] = 50,
    with_total: Union[Unset, None, bool] = True,
    sort_by: Union[Unset, None, GetQueryBookmarksSortBy] = UNSET,
    order: Union[Unset, None, GetQueryBookmarksOrder] = UNSET,
) -> Optional[Union[Error, List["QueryBookmarkDefinition"]]]:
    """returns the list of query bookmarks that are viewable by the requesting user.

    Args:
        data_source_type (Union[Unset, None, GetQueryBookmarksDataSourceType]):
        page (Union[Unset, None, int]):  Default: 1.
        per_page (Union[Unset, None, int]):  Default: 50.
        with_total (Union[Unset, None, bool]):  Default: True.
        sort_by (Union[Unset, None, GetQueryBookmarksSortBy]):
        order (Union[Unset, None, GetQueryBookmarksOrder]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, List['QueryBookmarkDefinition']]]
    """

    return (
        await asyncio_detailed(
            client=client,
            data_source_type=data_source_type,
            page=page,
            per_page=per_page,
            with_total=with_total,
            sort_by=sort_by,
            order=order,
        )
    ).parsed
