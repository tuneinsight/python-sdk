from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.get_query_response_403 import GetQueryResponse403
from ...models.query import Query
from ...types import Response


def _get_kwargs(
    query_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/queries/{queryId}".format(client.base_url, queryId=query_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[GetQueryResponse403, Query, str]]:
    if response.status_code == 200:
        response_200 = Query.from_dict(response.json())

        return response_200
    if response.status_code == 403:
        response_403 = GetQueryResponse403.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = cast(str, response.json())
        return response_404
    if response.status_code == 500:
        response_500 = cast(str, response.json())
        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[GetQueryResponse403, Query, str]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    query_id: str,
    *,
    client: Client,
) -> Response[Union[GetQueryResponse403, Query, str]]:
    """Gets a query

    Args:
        query_id (str):

    Returns:
        Response[Union[GetQueryResponse403, Query, str]]
    """

    kwargs = _get_kwargs(
        query_id=query_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    query_id: str,
    *,
    client: Client,
) -> Optional[Union[GetQueryResponse403, Query, str]]:
    """Gets a query

    Args:
        query_id (str):

    Returns:
        Response[Union[GetQueryResponse403, Query, str]]
    """

    return sync_detailed(
        query_id=query_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    query_id: str,
    *,
    client: Client,
) -> Response[Union[GetQueryResponse403, Query, str]]:
    """Gets a query

    Args:
        query_id (str):

    Returns:
        Response[Union[GetQueryResponse403, Query, str]]
    """

    kwargs = _get_kwargs(
        query_id=query_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    query_id: str,
    *,
    client: Client,
) -> Optional[Union[GetQueryResponse403, Query, str]]:
    """Gets a query

    Args:
        query_id (str):

    Returns:
        Response[Union[GetQueryResponse403, Query, str]]
    """

    return (
        await asyncio_detailed(
            query_id=query_id,
            client=client,
        )
    ).parsed
