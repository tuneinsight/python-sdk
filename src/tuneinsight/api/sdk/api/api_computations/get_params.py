from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.get_params_response_200 import GetParamsResponse200
from ...models.get_params_response_403 import GetParamsResponse403
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/params".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[GetParamsResponse200, GetParamsResponse403, str]]:
    if response.status_code == 200:
        response_200 = GetParamsResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 403:
        response_403 = GetParamsResponse403.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = cast(str, response.json())
        return response_404
    if response.status_code == 422:
        response_422 = cast(str, response.json())
        return response_422
    if response.status_code == 500:
        response_500 = cast(str, response.json())
        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[GetParamsResponse200, GetParamsResponse403, str]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[Union[GetParamsResponse200, GetParamsResponse403, str]]:
    """Returns the serialized parameters depending on the computation type

    Returns:
        Response[Union[GetParamsResponse200, GetParamsResponse403, str]]
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
) -> Optional[Union[GetParamsResponse200, GetParamsResponse403, str]]:
    """Returns the serialized parameters depending on the computation type

    Returns:
        Response[Union[GetParamsResponse200, GetParamsResponse403, str]]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[Union[GetParamsResponse200, GetParamsResponse403, str]]:
    """Returns the serialized parameters depending on the computation type

    Returns:
        Response[Union[GetParamsResponse200, GetParamsResponse403, str]]
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
) -> Optional[Union[GetParamsResponse200, GetParamsResponse403, str]]:
    """Returns the serialized parameters depending on the computation type

    Returns:
        Response[Union[GetParamsResponse200, GetParamsResponse403, str]]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
