from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.get_network_metadata_response_403 import GetNetworkMetadataResponse403
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/network".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[GetNetworkMetadataResponse403, str]]:
    if response.status_code == 403:
        response_403 = GetNetworkMetadataResponse403.from_dict(response.json())

        return response_403
    if response.status_code == 500:
        response_500 = cast(str, response.json())
        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[GetNetworkMetadataResponse403, str]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[Union[GetNetworkMetadataResponse403, str]]:
    """Get network metadata (nodes URLs, public keys, etc.).

    Returns:
        Response[Union[GetNetworkMetadataResponse403, str]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
) -> Optional[Union[GetNetworkMetadataResponse403, str]]:
    """Get network metadata (nodes URLs, public keys, etc.).

    Returns:
        Response[Union[GetNetworkMetadataResponse403, str]]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[Union[GetNetworkMetadataResponse403, str]]:
    """Get network metadata (nodes URLs, public keys, etc.).

    Returns:
        Response[Union[GetNetworkMetadataResponse403, str]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
) -> Optional[Union[GetNetworkMetadataResponse403, str]]:
    """Get network metadata (nodes URLs, public keys, etc.).

    Returns:
        Response[Union[GetNetworkMetadataResponse403, str]]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
