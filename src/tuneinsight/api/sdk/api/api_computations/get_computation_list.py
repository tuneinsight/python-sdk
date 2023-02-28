from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import Client
from ...models.computation import Computation
from ...models.get_computation_list_order import GetComputationListOrder
from ...models.get_computation_list_response_403 import GetComputationListResponse403
from ...models.get_computation_list_sort_by import GetComputationListSortBy
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    limit: Union[Unset, None, int] = 50,
    sort_by: Union[Unset, None, GetComputationListSortBy] = UNSET,
    order: Union[Unset, None, GetComputationListOrder] = UNSET,
    show_non_visible: Union[Unset, None, bool] = False,
) -> Dict[str, Any]:
    url = "{}/computations".format(client.base_url)

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

    params["showNonVisible"] = show_non_visible

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
    *, response: httpx.Response
) -> Optional[Union[GetComputationListResponse403, List[Computation], str]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Computation.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 403:
        response_403 = GetComputationListResponse403.from_dict(response.json())

        return response_403
    if response.status_code == 500:
        response_500 = cast(str, response.json())
        return response_500
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[GetComputationListResponse403, List[Computation], str]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    limit: Union[Unset, None, int] = 50,
    sort_by: Union[Unset, None, GetComputationListSortBy] = UNSET,
    order: Union[Unset, None, GetComputationListOrder] = UNSET,
    show_non_visible: Union[Unset, None, bool] = False,
) -> Response[Union[GetComputationListResponse403, List[Computation], str]]:
    """Get list of computations currently or previously running.

    Args:
        limit (Union[Unset, None, int]):  Default: 50.
        sort_by (Union[Unset, None, GetComputationListSortBy]):
        order (Union[Unset, None, GetComputationListOrder]):
        show_non_visible (Union[Unset, None, bool]):

    Returns:
        Response[Union[GetComputationListResponse403, List[Computation], str]]
    """

    kwargs = _get_kwargs(
        client=client,
        limit=limit,
        sort_by=sort_by,
        order=order,
        show_non_visible=show_non_visible,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    limit: Union[Unset, None, int] = 50,
    sort_by: Union[Unset, None, GetComputationListSortBy] = UNSET,
    order: Union[Unset, None, GetComputationListOrder] = UNSET,
    show_non_visible: Union[Unset, None, bool] = False,
) -> Optional[Union[GetComputationListResponse403, List[Computation], str]]:
    """Get list of computations currently or previously running.

    Args:
        limit (Union[Unset, None, int]):  Default: 50.
        sort_by (Union[Unset, None, GetComputationListSortBy]):
        order (Union[Unset, None, GetComputationListOrder]):
        show_non_visible (Union[Unset, None, bool]):

    Returns:
        Response[Union[GetComputationListResponse403, List[Computation], str]]
    """

    return sync_detailed(
        client=client,
        limit=limit,
        sort_by=sort_by,
        order=order,
        show_non_visible=show_non_visible,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    limit: Union[Unset, None, int] = 50,
    sort_by: Union[Unset, None, GetComputationListSortBy] = UNSET,
    order: Union[Unset, None, GetComputationListOrder] = UNSET,
    show_non_visible: Union[Unset, None, bool] = False,
) -> Response[Union[GetComputationListResponse403, List[Computation], str]]:
    """Get list of computations currently or previously running.

    Args:
        limit (Union[Unset, None, int]):  Default: 50.
        sort_by (Union[Unset, None, GetComputationListSortBy]):
        order (Union[Unset, None, GetComputationListOrder]):
        show_non_visible (Union[Unset, None, bool]):

    Returns:
        Response[Union[GetComputationListResponse403, List[Computation], str]]
    """

    kwargs = _get_kwargs(
        client=client,
        limit=limit,
        sort_by=sort_by,
        order=order,
        show_non_visible=show_non_visible,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    limit: Union[Unset, None, int] = 50,
    sort_by: Union[Unset, None, GetComputationListSortBy] = UNSET,
    order: Union[Unset, None, GetComputationListOrder] = UNSET,
    show_non_visible: Union[Unset, None, bool] = False,
) -> Optional[Union[GetComputationListResponse403, List[Computation], str]]:
    """Get list of computations currently or previously running.

    Args:
        limit (Union[Unset, None, int]):  Default: 50.
        sort_by (Union[Unset, None, GetComputationListSortBy]):
        order (Union[Unset, None, GetComputationListOrder]):
        show_non_visible (Union[Unset, None, bool]):

    Returns:
        Response[Union[GetComputationListResponse403, List[Computation], str]]
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            sort_by=sort_by,
            order=order,
            show_non_visible=show_non_visible,
        )
    ).parsed
