from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.data_source_query import DataSourceQuery
from ...models.dataset_schema import DatasetSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    data_source_id: str,
    *,
    client: Client,
    json_body: DataSourceQuery,
    dp_epsilon: Union[Unset, None, float] = UNSET,
    schema_name: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/datasources/{dataSourceId}/inferSchema".format(client.base_url, dataSourceId=data_source_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["dpEpsilon"] = dp_epsilon

    params["schemaName"] = schema_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

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
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "proxies": proxies,
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[DatasetSchema]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DatasetSchema.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code} ({response})")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[DatasetSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    data_source_id: str,
    *,
    client: Client,
    json_body: DataSourceQuery,
    dp_epsilon: Union[Unset, None, float] = UNSET,
    schema_name: Union[Unset, None, str] = UNSET,
) -> Response[DatasetSchema]:
    """automatically infer the data schema of this data

    Args:
        data_source_id (str):
        dp_epsilon (Union[Unset, None, float]):
        schema_name (Union[Unset, None, str]):
        json_body (DataSourceQuery): schema used for the query

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatasetSchema]
    """

    kwargs = _get_kwargs(
        data_source_id=data_source_id,
        client=client,
        json_body=json_body,
        dp_epsilon=dp_epsilon,
        schema_name=schema_name,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    data_source_id: str,
    *,
    client: Client,
    json_body: DataSourceQuery,
    dp_epsilon: Union[Unset, None, float] = UNSET,
    schema_name: Union[Unset, None, str] = UNSET,
) -> Optional[DatasetSchema]:
    """automatically infer the data schema of this data

    Args:
        data_source_id (str):
        dp_epsilon (Union[Unset, None, float]):
        schema_name (Union[Unset, None, str]):
        json_body (DataSourceQuery): schema used for the query

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatasetSchema]
    """

    return sync_detailed(
        data_source_id=data_source_id,
        client=client,
        json_body=json_body,
        dp_epsilon=dp_epsilon,
        schema_name=schema_name,
    ).parsed


async def asyncio_detailed(
    data_source_id: str,
    *,
    client: Client,
    json_body: DataSourceQuery,
    dp_epsilon: Union[Unset, None, float] = UNSET,
    schema_name: Union[Unset, None, str] = UNSET,
) -> Response[DatasetSchema]:
    """automatically infer the data schema of this data

    Args:
        data_source_id (str):
        dp_epsilon (Union[Unset, None, float]):
        schema_name (Union[Unset, None, str]):
        json_body (DataSourceQuery): schema used for the query

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatasetSchema]
    """

    kwargs = _get_kwargs(
        data_source_id=data_source_id,
        client=client,
        json_body=json_body,
        dp_epsilon=dp_epsilon,
        schema_name=schema_name,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    data_source_id: str,
    *,
    client: Client,
    json_body: DataSourceQuery,
    dp_epsilon: Union[Unset, None, float] = UNSET,
    schema_name: Union[Unset, None, str] = UNSET,
) -> Optional[DatasetSchema]:
    """automatically infer the data schema of this data

    Args:
        data_source_id (str):
        dp_epsilon (Union[Unset, None, float]):
        schema_name (Union[Unset, None, str]):
        json_body (DataSourceQuery): schema used for the query

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatasetSchema]
    """

    return (
        await asyncio_detailed(
            data_source_id=data_source_id,
            client=client,
            json_body=json_body,
            dp_epsilon=dp_epsilon,
            schema_name=schema_name,
        )
    ).parsed
