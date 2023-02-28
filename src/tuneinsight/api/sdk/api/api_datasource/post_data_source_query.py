from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.post_data_source_query_json_body import PostDataSourceQueryJsonBody
from ...models.post_data_source_query_response_403 import PostDataSourceQueryResponse403
from ...models.query import Query
from ...types import Response


def _get_kwargs(
    data_source_id: str,
    *,
    client: Client,
    json_body: PostDataSourceQueryJsonBody,
) -> Dict[str, Any]:
    url = "{}/datasources/{dataSourceId}/query".format(client.base_url, dataSourceId=data_source_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[PostDataSourceQueryResponse403, Query, str]]:
    if response.status_code == 200:
        response_200 = Query.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(str, response.json())
        return response_400
    if response.status_code == 403:
        response_403 = PostDataSourceQueryResponse403.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = cast(str, response.json())
        return response_404
    if response.status_code == 500:
        response_500 = cast(str, response.json())
        return response_500
    if response.status_code == 501:
        response_501 = cast(str, response.json())
        return response_501
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[PostDataSourceQueryResponse403, Query, str]]:
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
    json_body: PostDataSourceQueryJsonBody,
) -> Response[Union[PostDataSourceQueryResponse403, Query, str]]:
    """Query a data source.

    Args:
        data_source_id (str):
        json_body (PostDataSourceQueryJsonBody):

    Returns:
        Response[Union[PostDataSourceQueryResponse403, Query, str]]
    """

    kwargs = _get_kwargs(
        data_source_id=data_source_id,
        client=client,
        json_body=json_body,
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
    json_body: PostDataSourceQueryJsonBody,
) -> Optional[Union[PostDataSourceQueryResponse403, Query, str]]:
    """Query a data source.

    Args:
        data_source_id (str):
        json_body (PostDataSourceQueryJsonBody):

    Returns:
        Response[Union[PostDataSourceQueryResponse403, Query, str]]
    """

    return sync_detailed(
        data_source_id=data_source_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    data_source_id: str,
    *,
    client: Client,
    json_body: PostDataSourceQueryJsonBody,
) -> Response[Union[PostDataSourceQueryResponse403, Query, str]]:
    """Query a data source.

    Args:
        data_source_id (str):
        json_body (PostDataSourceQueryJsonBody):

    Returns:
        Response[Union[PostDataSourceQueryResponse403, Query, str]]
    """

    kwargs = _get_kwargs(
        data_source_id=data_source_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    data_source_id: str,
    *,
    client: Client,
    json_body: PostDataSourceQueryJsonBody,
) -> Optional[Union[PostDataSourceQueryResponse403, Query, str]]:
    """Query a data source.

    Args:
        data_source_id (str):
        json_body (PostDataSourceQueryJsonBody):

    Returns:
        Response[Union[PostDataSourceQueryResponse403, Query, str]]
    """

    return (
        await asyncio_detailed(
            data_source_id=data_source_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
