from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.get_project_list_order import GetProjectListOrder
from ...models.get_project_list_response_403 import GetProjectListResponse403
from ...models.get_project_list_sort_by import GetProjectListSortBy
from ...models.project import Project
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    limit: Union[Unset, None, int] = 50,
    sort_by: Union[Unset, None, GetProjectListSortBy] = UNSET,
    order: Union[Unset, None, GetProjectListOrder] = UNSET,
) -> Dict[str, Any]:
    url = "{}/projects".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["limit"] = limit

    json_sort_by: Union[Unset, None, str] = UNSET
    if not isinstance(sort_by, Unset):
        json_sort_by = sort_by.value if sort_by else None

    params["sortBy"] = json_sort_by

    json_order: Union[Unset, None, str] = UNSET
    if not isinstance(order, Unset):
        json_order = order.value if order else None

    params["order"] = json_order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[GetProjectListResponse403, List["Project"], str]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Project.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = GetProjectListResponse403.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = cast(str, response.json())
        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[GetProjectListResponse403, List["Project"], str]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    limit: Union[Unset, None, int] = 50,
    sort_by: Union[Unset, None, GetProjectListSortBy] = UNSET,
    order: Union[Unset, None, GetProjectListOrder] = UNSET,
) -> Response[Union[GetProjectListResponse403, List["Project"], str]]:
    """Get the list of projects

    Args:
        limit (Union[Unset, None, int]):  Default: 50.
        sort_by (Union[Unset, None, GetProjectListSortBy]):
        order (Union[Unset, None, GetProjectListOrder]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetProjectListResponse403, List['Project'], str]]
    """

    kwargs = _get_kwargs(
        client=client,
        limit=limit,
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
    limit: Union[Unset, None, int] = 50,
    sort_by: Union[Unset, None, GetProjectListSortBy] = UNSET,
    order: Union[Unset, None, GetProjectListOrder] = UNSET,
) -> Optional[Union[GetProjectListResponse403, List["Project"], str]]:
    """Get the list of projects

    Args:
        limit (Union[Unset, None, int]):  Default: 50.
        sort_by (Union[Unset, None, GetProjectListSortBy]):
        order (Union[Unset, None, GetProjectListOrder]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetProjectListResponse403, List['Project'], str]]
    """

    return sync_detailed(
        client=client,
        limit=limit,
        sort_by=sort_by,
        order=order,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    limit: Union[Unset, None, int] = 50,
    sort_by: Union[Unset, None, GetProjectListSortBy] = UNSET,
    order: Union[Unset, None, GetProjectListOrder] = UNSET,
) -> Response[Union[GetProjectListResponse403, List["Project"], str]]:
    """Get the list of projects

    Args:
        limit (Union[Unset, None, int]):  Default: 50.
        sort_by (Union[Unset, None, GetProjectListSortBy]):
        order (Union[Unset, None, GetProjectListOrder]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetProjectListResponse403, List['Project'], str]]
    """

    kwargs = _get_kwargs(
        client=client,
        limit=limit,
        sort_by=sort_by,
        order=order,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    limit: Union[Unset, None, int] = 50,
    sort_by: Union[Unset, None, GetProjectListSortBy] = UNSET,
    order: Union[Unset, None, GetProjectListOrder] = UNSET,
) -> Optional[Union[GetProjectListResponse403, List["Project"], str]]:
    """Get the list of projects

    Args:
        limit (Union[Unset, None, int]):  Default: 50.
        sort_by (Union[Unset, None, GetProjectListSortBy]):
        order (Union[Unset, None, GetProjectListOrder]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetProjectListResponse403, List['Project'], str]]
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            sort_by=sort_by,
            order=order,
        )
    ).parsed
