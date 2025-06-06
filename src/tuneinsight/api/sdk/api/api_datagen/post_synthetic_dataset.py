from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.data_source import DataSource
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    data_source_id: str,
    table: Union[Unset, None, str] = UNSET,
    query: Union[Unset, None, str] = UNSET,
    table_name: Union[Unset, None, str] = UNSET,
    num_rows: Union[Unset, None, int] = UNSET,
    dp_epsilon: Union[Unset, None, float] = UNSET,
    tracking_id: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/synthetic/dataset".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["dataSourceId"] = data_source_id

    params["table"] = table

    params["query"] = query

    params["tableName"] = table_name

    params["numRows"] = num_rows

    params["dpEpsilon"] = dp_epsilon

    params["trackingId"] = tracking_id

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
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "proxies": proxies,
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[DataSource, Error]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = DataSource.from_dict(response.json())

        return response_201
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = Error.from_dict(response.json())

        return response_400
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


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[DataSource, Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    data_source_id: str,
    table: Union[Unset, None, str] = UNSET,
    query: Union[Unset, None, str] = UNSET,
    table_name: Union[Unset, None, str] = UNSET,
    num_rows: Union[Unset, None, int] = UNSET,
    dp_epsilon: Union[Unset, None, float] = UNSET,
    tracking_id: Union[Unset, None, str] = UNSET,
) -> Response[Union[DataSource, Error]]:
    """Request the creation of a synthetic dataset from a real dataset.

    Args:
        data_source_id (str):
        table (Union[Unset, None, str]):
        query (Union[Unset, None, str]):
        table_name (Union[Unset, None, str]):
        num_rows (Union[Unset, None, int]):
        dp_epsilon (Union[Unset, None, float]):
        tracking_id (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DataSource, Error]]
    """

    kwargs = _get_kwargs(
        client=client,
        data_source_id=data_source_id,
        table=table,
        query=query,
        table_name=table_name,
        num_rows=num_rows,
        dp_epsilon=dp_epsilon,
        tracking_id=tracking_id,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    data_source_id: str,
    table: Union[Unset, None, str] = UNSET,
    query: Union[Unset, None, str] = UNSET,
    table_name: Union[Unset, None, str] = UNSET,
    num_rows: Union[Unset, None, int] = UNSET,
    dp_epsilon: Union[Unset, None, float] = UNSET,
    tracking_id: Union[Unset, None, str] = UNSET,
) -> Optional[Union[DataSource, Error]]:
    """Request the creation of a synthetic dataset from a real dataset.

    Args:
        data_source_id (str):
        table (Union[Unset, None, str]):
        query (Union[Unset, None, str]):
        table_name (Union[Unset, None, str]):
        num_rows (Union[Unset, None, int]):
        dp_epsilon (Union[Unset, None, float]):
        tracking_id (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DataSource, Error]]
    """

    return sync_detailed(
        client=client,
        data_source_id=data_source_id,
        table=table,
        query=query,
        table_name=table_name,
        num_rows=num_rows,
        dp_epsilon=dp_epsilon,
        tracking_id=tracking_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    data_source_id: str,
    table: Union[Unset, None, str] = UNSET,
    query: Union[Unset, None, str] = UNSET,
    table_name: Union[Unset, None, str] = UNSET,
    num_rows: Union[Unset, None, int] = UNSET,
    dp_epsilon: Union[Unset, None, float] = UNSET,
    tracking_id: Union[Unset, None, str] = UNSET,
) -> Response[Union[DataSource, Error]]:
    """Request the creation of a synthetic dataset from a real dataset.

    Args:
        data_source_id (str):
        table (Union[Unset, None, str]):
        query (Union[Unset, None, str]):
        table_name (Union[Unset, None, str]):
        num_rows (Union[Unset, None, int]):
        dp_epsilon (Union[Unset, None, float]):
        tracking_id (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DataSource, Error]]
    """

    kwargs = _get_kwargs(
        client=client,
        data_source_id=data_source_id,
        table=table,
        query=query,
        table_name=table_name,
        num_rows=num_rows,
        dp_epsilon=dp_epsilon,
        tracking_id=tracking_id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    data_source_id: str,
    table: Union[Unset, None, str] = UNSET,
    query: Union[Unset, None, str] = UNSET,
    table_name: Union[Unset, None, str] = UNSET,
    num_rows: Union[Unset, None, int] = UNSET,
    dp_epsilon: Union[Unset, None, float] = UNSET,
    tracking_id: Union[Unset, None, str] = UNSET,
) -> Optional[Union[DataSource, Error]]:
    """Request the creation of a synthetic dataset from a real dataset.

    Args:
        data_source_id (str):
        table (Union[Unset, None, str]):
        query (Union[Unset, None, str]):
        table_name (Union[Unset, None, str]):
        num_rows (Union[Unset, None, int]):
        dp_epsilon (Union[Unset, None, float]):
        tracking_id (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DataSource, Error]]
    """

    return (
        await asyncio_detailed(
            client=client,
            data_source_id=data_source_id,
            table=table,
            query=query,
            table_name=table_name,
            num_rows=num_rows,
            dp_epsilon=dp_epsilon,
            tracking_id=tracking_id,
        )
    ).parsed
