from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.error import Error
from ...models.get_jobs_order import GetJobsOrder
from ...models.get_jobs_response_200 import GetJobsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    page: Union[Unset, None, int] = 1,
    per_page: Union[Unset, None, int] = 50,
    with_total: Union[Unset, None, bool] = True,
    order: Union[Unset, None, GetJobsOrder] = UNSET,
    types: Union[Unset, None, List[str]] = UNSET,
    states: Union[Unset, None, List[str]] = UNSET,
) -> Dict[str, Any]:
    url = "{}/jobs".format(client.base_url)

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

    json_types: Union[Unset, None, List[str]] = UNSET
    if not isinstance(types, Unset):
        if types is None:
            json_types = None
        else:
            json_types = types

    params["types"] = json_types

    json_states: Union[Unset, None, List[str]] = UNSET
    if not isinstance(states, Unset):
        if states is None:
            json_states = None
        else:
            json_states = states

    params["states"] = json_states

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Error, GetJobsResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetJobsResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = Error.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = Error.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = Error.from_dict(response.json())

        return response_403
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


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Error, GetJobsResponse200]]:
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
    order: Union[Unset, None, GetJobsOrder] = UNSET,
    types: Union[Unset, None, List[str]] = UNSET,
    states: Union[Unset, None, List[str]] = UNSET,
) -> Response[Union[Error, GetJobsResponse200]]:
    """retrieve the list of background jobs running on the instance.

    Args:
        page (Union[Unset, None, int]):  Default: 1.
        per_page (Union[Unset, None, int]):  Default: 50.
        with_total (Union[Unset, None, bool]):  Default: True.
        order (Union[Unset, None, GetJobsOrder]):
        types (Union[Unset, None, List[str]]):
        states (Union[Unset, None, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, GetJobsResponse200]]
    """

    kwargs = _get_kwargs(
        client=client,
        page=page,
        per_page=per_page,
        with_total=with_total,
        order=order,
        types=types,
        states=states,
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
    order: Union[Unset, None, GetJobsOrder] = UNSET,
    types: Union[Unset, None, List[str]] = UNSET,
    states: Union[Unset, None, List[str]] = UNSET,
) -> Optional[Union[Error, GetJobsResponse200]]:
    """retrieve the list of background jobs running on the instance.

    Args:
        page (Union[Unset, None, int]):  Default: 1.
        per_page (Union[Unset, None, int]):  Default: 50.
        with_total (Union[Unset, None, bool]):  Default: True.
        order (Union[Unset, None, GetJobsOrder]):
        types (Union[Unset, None, List[str]]):
        states (Union[Unset, None, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, GetJobsResponse200]]
    """

    return sync_detailed(
        client=client,
        page=page,
        per_page=per_page,
        with_total=with_total,
        order=order,
        types=types,
        states=states,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    page: Union[Unset, None, int] = 1,
    per_page: Union[Unset, None, int] = 50,
    with_total: Union[Unset, None, bool] = True,
    order: Union[Unset, None, GetJobsOrder] = UNSET,
    types: Union[Unset, None, List[str]] = UNSET,
    states: Union[Unset, None, List[str]] = UNSET,
) -> Response[Union[Error, GetJobsResponse200]]:
    """retrieve the list of background jobs running on the instance.

    Args:
        page (Union[Unset, None, int]):  Default: 1.
        per_page (Union[Unset, None, int]):  Default: 50.
        with_total (Union[Unset, None, bool]):  Default: True.
        order (Union[Unset, None, GetJobsOrder]):
        types (Union[Unset, None, List[str]]):
        states (Union[Unset, None, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, GetJobsResponse200]]
    """

    kwargs = _get_kwargs(
        client=client,
        page=page,
        per_page=per_page,
        with_total=with_total,
        order=order,
        types=types,
        states=states,
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
    order: Union[Unset, None, GetJobsOrder] = UNSET,
    types: Union[Unset, None, List[str]] = UNSET,
    states: Union[Unset, None, List[str]] = UNSET,
) -> Optional[Union[Error, GetJobsResponse200]]:
    """retrieve the list of background jobs running on the instance.

    Args:
        page (Union[Unset, None, int]):  Default: 1.
        per_page (Union[Unset, None, int]):  Default: 50.
        with_total (Union[Unset, None, bool]):  Default: True.
        order (Union[Unset, None, GetJobsOrder]):
        types (Union[Unset, None, List[str]]):
        states (Union[Unset, None, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, GetJobsResponse200]]
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            per_page=per_page,
            with_total=with_total,
            order=order,
            types=types,
            states=states,
        )
    ).parsed
