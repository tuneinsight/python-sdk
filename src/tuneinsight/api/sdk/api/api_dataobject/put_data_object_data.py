from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.data_object import DataObject
from ...models.error import Error
from ...models.put_data_object_data_multipart_data import PutDataObjectDataMultipartData
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
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "proxies": proxies,
        "files": multipart_multipart_data,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[DataObject, Error]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DataObject.from_dict(response.json())

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
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code} ({response})")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[DataObject, Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    data_object_id: str,
    *,
    client: Client,
    multipart_data: PutDataObjectDataMultipartData,
) -> Response[Union[DataObject, Error]]:
    """Add data to a dataobject

    Args:
        data_object_id (str):
        multipart_data (PutDataObjectDataMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DataObject, Error]]
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

    return _build_response(client=client, response=response)


def sync(
    data_object_id: str,
    *,
    client: Client,
    multipart_data: PutDataObjectDataMultipartData,
) -> Optional[Union[DataObject, Error]]:
    """Add data to a dataobject

    Args:
        data_object_id (str):
        multipart_data (PutDataObjectDataMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DataObject, Error]]
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
) -> Response[Union[DataObject, Error]]:
    """Add data to a dataobject

    Args:
        data_object_id (str):
        multipart_data (PutDataObjectDataMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DataObject, Error]]
    """

    kwargs = _get_kwargs(
        data_object_id=data_object_id,
        client=client,
        multipart_data=multipart_data,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    data_object_id: str,
    *,
    client: Client,
    multipart_data: PutDataObjectDataMultipartData,
) -> Optional[Union[DataObject, Error]]:
    """Add data to a dataobject

    Args:
        data_object_id (str):
        multipart_data (PutDataObjectDataMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DataObject, Error]]
    """

    return (
        await asyncio_detailed(
            data_object_id=data_object_id,
            client=client,
            multipart_data=multipart_data,
        )
    ).parsed
