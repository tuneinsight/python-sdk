from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import Client
from ...models.data_object import DataObject
from ...models.get_data_object_list_response_403 import GetDataObjectListResponse403
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/dataobjects".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[GetDataObjectListResponse403, List[DataObject], str]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = DataObject.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 403:
        response_403 = GetDataObjectListResponse403.from_dict(response.json())

        return response_403
    if response.status_code == 500:
        response_500 = cast(str, response.json())
        return response_500
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[GetDataObjectListResponse403, List[DataObject], str]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[Union[GetDataObjectListResponse403, List[DataObject], str]]:
    """Get the list of available data objects.

    Returns:
        Response[Union[GetDataObjectListResponse403, List[DataObject], str]]
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
) -> Optional[Union[GetDataObjectListResponse403, List[DataObject], str]]:
    """Get the list of available data objects.

    Returns:
        Response[Union[GetDataObjectListResponse403, List[DataObject], str]]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[Union[GetDataObjectListResponse403, List[DataObject], str]]:
    """Get the list of available data objects.

    Returns:
        Response[Union[GetDataObjectListResponse403, List[DataObject], str]]
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
) -> Optional[Union[GetDataObjectListResponse403, List[DataObject], str]]:
    """Get the list of available data objects.

    Returns:
        Response[Union[GetDataObjectListResponse403, List[DataObject], str]]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
