from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.post_protocol_message_multipart_data import PostProtocolMessageMultipartData
from ...models.post_protocol_message_response_403 import PostProtocolMessageResponse403
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    multipart_data: PostProtocolMessageMultipartData,
) -> Dict[str, Any]:
    url = "{}/protocol/message".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    multipart_multipart_data = multipart_data.to_multipart()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "files": multipart_multipart_data,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[PostProtocolMessageResponse403, str]]:
    if response.status_code == 200:
        response_200 = cast(str, response.json())
        return response_200
    if response.status_code == 400:
        response_400 = cast(str, response.json())
        return response_400
    if response.status_code == 403:
        response_403 = PostProtocolMessageResponse403.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = cast(str, response.json())
        return response_404
    if response.status_code == 500:
        response_500 = cast(str, response.json())
        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[PostProtocolMessageResponse403, str]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    multipart_data: PostProtocolMessageMultipartData,
) -> Response[Union[PostProtocolMessageResponse403, str]]:
    """send data to a node

    Args:
        multipart_data (PostProtocolMessageMultipartData):

    Returns:
        Response[Union[PostProtocolMessageResponse403, str]]
    """

    kwargs = _get_kwargs(
        client=client,
        multipart_data=multipart_data,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    multipart_data: PostProtocolMessageMultipartData,
) -> Optional[Union[PostProtocolMessageResponse403, str]]:
    """send data to a node

    Args:
        multipart_data (PostProtocolMessageMultipartData):

    Returns:
        Response[Union[PostProtocolMessageResponse403, str]]
    """

    return sync_detailed(
        client=client,
        multipart_data=multipart_data,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    multipart_data: PostProtocolMessageMultipartData,
) -> Response[Union[PostProtocolMessageResponse403, str]]:
    """send data to a node

    Args:
        multipart_data (PostProtocolMessageMultipartData):

    Returns:
        Response[Union[PostProtocolMessageResponse403, str]]
    """

    kwargs = _get_kwargs(
        client=client,
        multipart_data=multipart_data,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    multipart_data: PostProtocolMessageMultipartData,
) -> Optional[Union[PostProtocolMessageResponse403, str]]:
    """send data to a node

    Args:
        multipart_data (PostProtocolMessageMultipartData):

    Returns:
        Response[Union[PostProtocolMessageResponse403, str]]
    """

    return (
        await asyncio_detailed(
            client=client,
            multipart_data=multipart_data,
        )
    ).parsed
