from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.computation_list_response import ComputationListResponse
from ...models.error import Error
from ...models.get_computation_list_order import GetComputationListOrder
from ...models.get_computation_list_sort_by import GetComputationListSortBy
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    page: Union[Unset, None, int] = 1,
    per_page: Union[Unset, None, int] = 50,
    with_total: Union[Unset, None, bool] = True,
    order: Union[Unset, None, GetComputationListOrder] = UNSET,
    sort_by: Union[Unset, None, GetComputationListSortBy] = UNSET,
    limit: Union[Unset, None, int] = 50,
    show_non_visible: Union[Unset, None, bool] = False,
    project_id: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/computations".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["page"] = page

    params["perPage"] = per_page

    params["withTotal"] = with_total

    json_order: Union[Unset, None, str] = UNSET
    if not isinstance(order, Unset):
        json_order = order.value if order else None

    params["order"] = json_order

    json_sort_by: Union[Unset, None, str] = UNSET
    if not isinstance(sort_by, Unset):
        json_sort_by = sort_by.value if sort_by else None

    params["sortBy"] = json_sort_by

    params["limit"] = limit

    params["showNonVisible"] = show_non_visible

    params["projectId"] = project_id

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[ComputationListResponse, Error]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ComputationListResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = Error.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = Error.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code} ({response})")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[ComputationListResponse, Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    page: Union[Unset, None, int] = 1,
    per_page: Union[Unset, None, int] = 50,
    with_total: Union[Unset, None, bool] = True,
    order: Union[Unset, None, GetComputationListOrder] = UNSET,
    sort_by: Union[Unset, None, GetComputationListSortBy] = UNSET,
    limit: Union[Unset, None, int] = 50,
    show_non_visible: Union[Unset, None, bool] = False,
    project_id: Union[Unset, None, str] = UNSET,
) -> Response[Union[ComputationListResponse, Error]]:
    """Get list of computations currently or previously running.

    Args:
        page (Union[Unset, None, int]):  Default: 1.
        per_page (Union[Unset, None, int]):  Default: 50.
        with_total (Union[Unset, None, bool]):  Default: True.
        order (Union[Unset, None, GetComputationListOrder]):
        sort_by (Union[Unset, None, GetComputationListSortBy]):
        limit (Union[Unset, None, int]):  Default: 50.
        show_non_visible (Union[Unset, None, bool]):
        project_id (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ComputationListResponse, Error]]
    """

    kwargs = _get_kwargs(
        client=client,
        page=page,
        per_page=per_page,
        with_total=with_total,
        order=order,
        sort_by=sort_by,
        limit=limit,
        show_non_visible=show_non_visible,
        project_id=project_id,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    page: Union[Unset, None, int] = 1,
    per_page: Union[Unset, None, int] = 50,
    with_total: Union[Unset, None, bool] = True,
    order: Union[Unset, None, GetComputationListOrder] = UNSET,
    sort_by: Union[Unset, None, GetComputationListSortBy] = UNSET,
    limit: Union[Unset, None, int] = 50,
    show_non_visible: Union[Unset, None, bool] = False,
    project_id: Union[Unset, None, str] = UNSET,
) -> Optional[Union[ComputationListResponse, Error]]:
    """Get list of computations currently or previously running.

    Args:
        page (Union[Unset, None, int]):  Default: 1.
        per_page (Union[Unset, None, int]):  Default: 50.
        with_total (Union[Unset, None, bool]):  Default: True.
        order (Union[Unset, None, GetComputationListOrder]):
        sort_by (Union[Unset, None, GetComputationListSortBy]):
        limit (Union[Unset, None, int]):  Default: 50.
        show_non_visible (Union[Unset, None, bool]):
        project_id (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ComputationListResponse, Error]]
    """

    return sync_detailed(
        client=client,
        page=page,
        per_page=per_page,
        with_total=with_total,
        order=order,
        sort_by=sort_by,
        limit=limit,
        show_non_visible=show_non_visible,
        project_id=project_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    page: Union[Unset, None, int] = 1,
    per_page: Union[Unset, None, int] = 50,
    with_total: Union[Unset, None, bool] = True,
    order: Union[Unset, None, GetComputationListOrder] = UNSET,
    sort_by: Union[Unset, None, GetComputationListSortBy] = UNSET,
    limit: Union[Unset, None, int] = 50,
    show_non_visible: Union[Unset, None, bool] = False,
    project_id: Union[Unset, None, str] = UNSET,
) -> Response[Union[ComputationListResponse, Error]]:
    """Get list of computations currently or previously running.

    Args:
        page (Union[Unset, None, int]):  Default: 1.
        per_page (Union[Unset, None, int]):  Default: 50.
        with_total (Union[Unset, None, bool]):  Default: True.
        order (Union[Unset, None, GetComputationListOrder]):
        sort_by (Union[Unset, None, GetComputationListSortBy]):
        limit (Union[Unset, None, int]):  Default: 50.
        show_non_visible (Union[Unset, None, bool]):
        project_id (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ComputationListResponse, Error]]
    """

    kwargs = _get_kwargs(
        client=client,
        page=page,
        per_page=per_page,
        with_total=with_total,
        order=order,
        sort_by=sort_by,
        limit=limit,
        show_non_visible=show_non_visible,
        project_id=project_id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    page: Union[Unset, None, int] = 1,
    per_page: Union[Unset, None, int] = 50,
    with_total: Union[Unset, None, bool] = True,
    order: Union[Unset, None, GetComputationListOrder] = UNSET,
    sort_by: Union[Unset, None, GetComputationListSortBy] = UNSET,
    limit: Union[Unset, None, int] = 50,
    show_non_visible: Union[Unset, None, bool] = False,
    project_id: Union[Unset, None, str] = UNSET,
) -> Optional[Union[ComputationListResponse, Error]]:
    """Get list of computations currently or previously running.

    Args:
        page (Union[Unset, None, int]):  Default: 1.
        per_page (Union[Unset, None, int]):  Default: 50.
        with_total (Union[Unset, None, bool]):  Default: True.
        order (Union[Unset, None, GetComputationListOrder]):
        sort_by (Union[Unset, None, GetComputationListSortBy]):
        limit (Union[Unset, None, int]):  Default: 50.
        show_non_visible (Union[Unset, None, bool]):
        project_id (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ComputationListResponse, Error]]
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            per_page=per_page,
            with_total=with_total,
            order=order,
            sort_by=sort_by,
            limit=limit,
            show_non_visible=show_non_visible,
            project_id=project_id,
        )
    ).parsed
