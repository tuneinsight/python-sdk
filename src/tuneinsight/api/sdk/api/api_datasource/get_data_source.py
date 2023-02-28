from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.data_source import DataSource
from ...models.get_data_source_response_403 import GetDataSourceResponse403
from ...types import Response


def _get_kwargs(
    data_source_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/datasources/{dataSourceId}".format(client.base_url, dataSourceId=data_source_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[DataSource, GetDataSourceResponse403, str]]:
    if response.status_code == 200:
        response_200 = DataSource.from_dict(response.json())

        return response_200
    if response.status_code == 403:
        response_403 = GetDataSourceResponse403.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = cast(str, response.json())
        return response_404
    if response.status_code == 500:
        response_500 = cast(str, response.json())
        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[DataSource, GetDataSourceResponse403, str]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    data_source_id: str,
    *,
    client: Client,
) -> Response[Union[DataSource, GetDataSourceResponse403, str]]:
    """Get data source

    Args:
        data_source_id (str):

    Returns:
        Response[Union[DataSource, GetDataSourceResponse403, str]]
    """

    kwargs = _get_kwargs(
        data_source_id=data_source_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    data_source_id: str,
    *,
    client: Client,
) -> Optional[Union[DataSource, GetDataSourceResponse403, str]]:
    """Get data source

    Args:
        data_source_id (str):

    Returns:
        Response[Union[DataSource, GetDataSourceResponse403, str]]
    """

    return sync_detailed(
        data_source_id=data_source_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    data_source_id: str,
    *,
    client: Client,
) -> Response[Union[DataSource, GetDataSourceResponse403, str]]:
    """Get data source

    Args:
        data_source_id (str):

    Returns:
        Response[Union[DataSource, GetDataSourceResponse403, str]]
    """

    kwargs = _get_kwargs(
        data_source_id=data_source_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    data_source_id: str,
    *,
    client: Client,
) -> Optional[Union[DataSource, GetDataSourceResponse403, str]]:
    """Get data source

    Args:
        data_source_id (str):

    Returns:
        Response[Union[DataSource, GetDataSourceResponse403, str]]
    """

    return (
        await asyncio_detailed(
            data_source_id=data_source_id,
            client=client,
        )
    ).parsed
