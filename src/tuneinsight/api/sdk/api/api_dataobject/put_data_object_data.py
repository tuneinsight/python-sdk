from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.data_object import DataObject
from ...models.put_data_object_data_multipart_data import PutDataObjectDataMultipartData
from ...models.put_data_object_data_response_403 import PutDataObjectDataResponse403
from ...types import Response


def _get_kwargs(
    data_object_id: str,
    *,
    client: Client,
    multipart_data: PutDataObjectDataMultipartData,
) -> Dict[str, Any]:
    url = "{}/dataobjects/{dataObjectId}/data".format(client.base_url, dataObjectId=data_object_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    multipart_multipart_data = multipart_data.to_multipart()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "files": multipart_multipart_data,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[DataObject, PutDataObjectDataResponse403, str]]:
    if response.status_code == 200:
        response_200 = DataObject.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(str, response.json())
        return response_400
    if response.status_code == 403:
        response_403 = PutDataObjectDataResponse403.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = cast(str, response.json())
        return response_404
    if response.status_code == 500:
        response_500 = cast(str, response.json())
        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[DataObject, PutDataObjectDataResponse403, str]]:
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
    multipart_data: PutDataObjectDataMultipartData,
) -> Response[Union[DataObject, PutDataObjectDataResponse403, str]]:
    """Add data to a dataobject

    Args:
        data_object_id (str):
        multipart_data (PutDataObjectDataMultipartData):

    Returns:
        Response[Union[DataObject, PutDataObjectDataResponse403, str]]
    """

    kwargs = _get_kwargs(
        data_object_id=data_object_id,
        client=client,
        multipart_data=multipart_data,
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
    multipart_data: PutDataObjectDataMultipartData,
) -> Optional[Union[DataObject, PutDataObjectDataResponse403, str]]:
    """Add data to a dataobject

    Args:
        data_object_id (str):
        multipart_data (PutDataObjectDataMultipartData):

    Returns:
        Response[Union[DataObject, PutDataObjectDataResponse403, str]]
    """

    return sync_detailed(
        data_object_id=data_object_id,
        client=client,
        multipart_data=multipart_data,
    ).parsed


async def asyncio_detailed(
    data_object_id: str,
    *,
    client: Client,
    multipart_data: PutDataObjectDataMultipartData,
) -> Response[Union[DataObject, PutDataObjectDataResponse403, str]]:
    """Add data to a dataobject

    Args:
        data_object_id (str):
        multipart_data (PutDataObjectDataMultipartData):

    Returns:
        Response[Union[DataObject, PutDataObjectDataResponse403, str]]
    """

    kwargs = _get_kwargs(
        data_object_id=data_object_id,
        client=client,
        multipart_data=multipart_data,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    data_object_id: str,
    *,
    client: Client,
    multipart_data: PutDataObjectDataMultipartData,
) -> Optional[Union[DataObject, PutDataObjectDataResponse403, str]]:
    """Add data to a dataobject

    Args:
        data_object_id (str):
        multipart_data (PutDataObjectDataMultipartData):

    Returns:
        Response[Union[DataObject, PutDataObjectDataResponse403, str]]
    """

    return (
        await asyncio_detailed(
            data_object_id=data_object_id,
            client=client,
            multipart_data=multipart_data,
        )
    ).parsed
