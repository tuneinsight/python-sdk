from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.content import Content
from ...models.get_shared_data_object_data_response_403 import GetSharedDataObjectDataResponse403
from ...types import Response


def _get_kwargs(
    data_object_shared_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/shared-dataobjects/{dataObjectSharedId}/data".format(
        client.base_url, dataObjectSharedId=data_object_shared_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Content, GetSharedDataObjectDataResponse403, str]]:
    if response.status_code == 200:
        response_200 = Content.from_dict(response.json())

        return response_200
    if response.status_code == 403:
        response_403 = GetSharedDataObjectDataResponse403.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = cast(str, response.json())
        return response_404
    if response.status_code == 500:
        response_500 = cast(str, response.json())
        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Content, GetSharedDataObjectDataResponse403, str]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    data_object_shared_id: str,
    *,
    client: Client,
) -> Response[Union[Content, GetSharedDataObjectDataResponse403, str]]:
    """Get the content of a data object from its shared ID.

    Args:
        data_object_shared_id (str):

    Returns:
        Response[Union[Content, GetSharedDataObjectDataResponse403, str]]
    """

    kwargs = _get_kwargs(
        data_object_shared_id=data_object_shared_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    data_object_shared_id: str,
    *,
    client: Client,
) -> Optional[Union[Content, GetSharedDataObjectDataResponse403, str]]:
    """Get the content of a data object from its shared ID.

    Args:
        data_object_shared_id (str):

    Returns:
        Response[Union[Content, GetSharedDataObjectDataResponse403, str]]
    """

    return sync_detailed(
        data_object_shared_id=data_object_shared_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    data_object_shared_id: str,
    *,
    client: Client,
) -> Response[Union[Content, GetSharedDataObjectDataResponse403, str]]:
    """Get the content of a data object from its shared ID.

    Args:
        data_object_shared_id (str):

    Returns:
        Response[Union[Content, GetSharedDataObjectDataResponse403, str]]
    """

    kwargs = _get_kwargs(
        data_object_shared_id=data_object_shared_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    data_object_shared_id: str,
    *,
    client: Client,
) -> Optional[Union[Content, GetSharedDataObjectDataResponse403, str]]:
    """Get the content of a data object from its shared ID.

    Args:
        data_object_shared_id (str):

    Returns:
        Response[Union[Content, GetSharedDataObjectDataResponse403, str]]
    """

    return (
        await asyncio_detailed(
            data_object_shared_id=data_object_shared_id,
            client=client,
        )
    ).parsed
