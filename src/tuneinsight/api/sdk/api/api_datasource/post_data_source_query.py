from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.error import Error
from ...models.post_data_source_query_json_body import PostDataSourceQueryJsonBody
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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Error, Query]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Query.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = Error.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = Error.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = Error.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = Error.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.NOT_IMPLEMENTED:
        response_501 = Error.from_dict(response.json())

        return response_501
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Error, Query]]:
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
    json_body: PostDataSourceQueryJsonBody,
) -> Response[Union[Error, Query]]:
    """Query a data source.

    Args:
        data_source_id (str):
        json_body (PostDataSourceQueryJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Query]]
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

    return _build_response(client=client, response=response)


def sync(
    data_source_id: str,
    *,
    client: Client,
    json_body: PostDataSourceQueryJsonBody,
) -> Optional[Union[Error, Query]]:
    """Query a data source.

    Args:
        data_source_id (str):
        json_body (PostDataSourceQueryJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Query]]
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
) -> Response[Union[Error, Query]]:
    """Query a data source.

    Args:
        data_source_id (str):
        json_body (PostDataSourceQueryJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Query]]
    """

    kwargs = _get_kwargs(
        data_source_id=data_source_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    data_source_id: str,
    *,
    client: Client,
    json_body: PostDataSourceQueryJsonBody,
) -> Optional[Union[Error, Query]]:
    """Query a data source.

    Args:
        data_source_id (str):
        json_body (PostDataSourceQueryJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Query]]
    """

    return (
        await asyncio_detailed(
            data_source_id=data_source_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
