from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.error import Error
from ...models.post_summarize_query_json_body import PostSummarizeQueryJsonBody
from ...models.post_summarize_query_response_200 import PostSummarizeQueryResponse200
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: PostSummarizeQueryJsonBody,
) -> Dict[str, Any]:
    url = "{}/pythonserver/aiquerybuilder/summarize".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

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
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Error, PostSummarizeQueryResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PostSummarizeQueryResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = Error.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = Error.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code} ({response})")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[Error, PostSummarizeQueryResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: PostSummarizeQueryJsonBody,
) -> Response[Union[Error, PostSummarizeQueryResponse200]]:
    """Summarize a query from the UI state JSON into a natural language description.

    Args:
        json_body (PostSummarizeQueryJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, PostSummarizeQueryResponse200]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    json_body: PostSummarizeQueryJsonBody,
) -> Optional[Union[Error, PostSummarizeQueryResponse200]]:
    """Summarize a query from the UI state JSON into a natural language description.

    Args:
        json_body (PostSummarizeQueryJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, PostSummarizeQueryResponse200]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: PostSummarizeQueryJsonBody,
) -> Response[Union[Error, PostSummarizeQueryResponse200]]:
    """Summarize a query from the UI state JSON into a natural language description.

    Args:
        json_body (PostSummarizeQueryJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, PostSummarizeQueryResponse200]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    json_body: PostSummarizeQueryJsonBody,
) -> Optional[Union[Error, PostSummarizeQueryResponse200]]:
    """Summarize a query from the UI state JSON into a natural language description.

    Args:
        json_body (PostSummarizeQueryJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, PostSummarizeQueryResponse200]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
