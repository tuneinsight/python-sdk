from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.error import Error
from ...models.get_model_list_order import GetModelListOrder
from ...models.get_model_list_sort_by import GetModelListSortBy
from ...models.model import Model
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    sort_by: Union[Unset, None, GetModelListSortBy] = UNSET,
    order: Union[Unset, None, GetModelListOrder] = UNSET,
    project_id: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/models".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_sort_by: Union[Unset, None, str] = UNSET
    if not isinstance(sort_by, Unset):
        json_sort_by = sort_by.value if sort_by else None

    params["sortBy"] = json_sort_by

    json_order: Union[Unset, None, str] = UNSET
    if not isinstance(order, Unset):
        json_order = order.value if order else None

    params["order"] = json_order

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Error, List["Model"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Model.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Error, List["Model"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    sort_by: Union[Unset, None, GetModelListSortBy] = UNSET,
    order: Union[Unset, None, GetModelListOrder] = UNSET,
    project_id: Union[Unset, None, str] = UNSET,
) -> Response[Union[Error, List["Model"]]]:
    """Get the list of available machine learning models.

    Args:
        sort_by (Union[Unset, None, GetModelListSortBy]):
        order (Union[Unset, None, GetModelListOrder]):
        project_id (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, List['Model']]]
    """

    kwargs = _get_kwargs(
        client=client,
        sort_by=sort_by,
        order=order,
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
    sort_by: Union[Unset, None, GetModelListSortBy] = UNSET,
    order: Union[Unset, None, GetModelListOrder] = UNSET,
    project_id: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Error, List["Model"]]]:
    """Get the list of available machine learning models.

    Args:
        sort_by (Union[Unset, None, GetModelListSortBy]):
        order (Union[Unset, None, GetModelListOrder]):
        project_id (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, List['Model']]]
    """

    return sync_detailed(
        client=client,
        sort_by=sort_by,
        order=order,
        project_id=project_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    sort_by: Union[Unset, None, GetModelListSortBy] = UNSET,
    order: Union[Unset, None, GetModelListOrder] = UNSET,
    project_id: Union[Unset, None, str] = UNSET,
) -> Response[Union[Error, List["Model"]]]:
    """Get the list of available machine learning models.

    Args:
        sort_by (Union[Unset, None, GetModelListSortBy]):
        order (Union[Unset, None, GetModelListOrder]):
        project_id (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, List['Model']]]
    """

    kwargs = _get_kwargs(
        client=client,
        sort_by=sort_by,
        order=order,
        project_id=project_id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    sort_by: Union[Unset, None, GetModelListSortBy] = UNSET,
    order: Union[Unset, None, GetModelListOrder] = UNSET,
    project_id: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Error, List["Model"]]]:
    """Get the list of available machine learning models.

    Args:
        sort_by (Union[Unset, None, GetModelListSortBy]):
        order (Union[Unset, None, GetModelListOrder]):
        project_id (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, List['Model']]]
    """

    return (
        await asyncio_detailed(
            client=client,
            sort_by=sort_by,
            order=order,
            project_id=project_id,
        )
    ).parsed
