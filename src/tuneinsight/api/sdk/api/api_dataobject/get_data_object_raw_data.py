from io import BytesIO
from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.get_data_object_raw_data_response_403 import GetDataObjectRawDataResponse403
from ...types import File, Response


def _get_kwargs(
    data_object_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/dataobjects/{dataObjectId}/rawData".format(client.base_url, dataObjectId=data_object_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[File, GetDataObjectRawDataResponse403, str]]:
    if response.status_code == 200:
        response_200 = File(payload=BytesIO(response.content))

        return response_200
    if response.status_code == 403:
        response_403 = GetDataObjectRawDataResponse403.from_dict(response.content)

        return response_403
    if response.status_code == 404:
        response_404 = cast(str, response.content)
        return response_404
    if response.status_code == 500:
        response_500 = cast(str, response.content)
        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[File, GetDataObjectRawDataResponse403, str]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    data_object_id: str,
    *,
    client: Client,
) -> Response[Union[File, GetDataObjectRawDataResponse403, str]]:
    """Get the raw content of a data object.

    Args:
        data_object_id (str):

    Returns:
        Response[Union[File, GetDataObjectRawDataResponse403, str]]
    """

    kwargs = _get_kwargs(
        data_object_id=data_object_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    data_object_id: str,
    *,
    client: Client,
) -> Optional[Union[File, GetDataObjectRawDataResponse403, str]]:
    """Get the raw content of a data object.

    Args:
        data_object_id (str):

    Returns:
        Response[Union[File, GetDataObjectRawDataResponse403, str]]
    """

    return sync_detailed(
        data_object_id=data_object_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    data_object_id: str,
    *,
    client: Client,
) -> Response[Union[File, GetDataObjectRawDataResponse403, str]]:
    """Get the raw content of a data object.

    Args:
        data_object_id (str):

    Returns:
        Response[Union[File, GetDataObjectRawDataResponse403, str]]
    """

    kwargs = _get_kwargs(
        data_object_id=data_object_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    data_object_id: str,
    *,
    client: Client,
) -> Optional[Union[File, GetDataObjectRawDataResponse403, str]]:
    """Get the raw content of a data object.

    Args:
        data_object_id (str):

    Returns:
        Response[Union[File, GetDataObjectRawDataResponse403, str]]
    """

    return (
        await asyncio_detailed(
            data_object_id=data_object_id,
            client=client,
        )
    ).parsed
