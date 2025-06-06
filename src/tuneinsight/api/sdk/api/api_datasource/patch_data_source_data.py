from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.data_upload_params import DataUploadParams
from ...models.data_upload_response import DataUploadResponse
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    data_source_id: str,
    *,
    client: Client,
    json_body: DataUploadParams,
    preview: Union[Unset, None, bool] = UNSET,
    preview_rows: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/datasources/{dataSourceId}/data".format(client.base_url, dataSourceId=data_source_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["preview"] = preview

    params["previewRows"] = preview_rows

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

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
        "method": "patch",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "proxies": proxies,
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[DataUploadResponse, Error]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DataUploadResponse.from_dict(response.json())

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
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = Error.from_dict(response.json())

        return response_422
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = Error.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code} ({response})")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[DataUploadResponse, Error]]:
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
    json_body: DataUploadParams,
    preview: Union[Unset, None, bool] = UNSET,
    preview_rows: Union[Unset, None, int] = UNSET,
) -> Response[Union[DataUploadResponse, Error]]:
    """Load data into a data source

    Args:
        data_source_id (str):
        preview (Union[Unset, None, bool]):
        preview_rows (Union[Unset, None, int]):
        json_body (DataUploadParams): parameters used when uploading data to a data source

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DataUploadResponse, Error]]
    """

    kwargs = _get_kwargs(
        data_source_id=data_source_id,
        client=client,
        json_body=json_body,
        preview=preview,
        preview_rows=preview_rows,
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
    json_body: DataUploadParams,
    preview: Union[Unset, None, bool] = UNSET,
    preview_rows: Union[Unset, None, int] = UNSET,
) -> Optional[Union[DataUploadResponse, Error]]:
    """Load data into a data source

    Args:
        data_source_id (str):
        preview (Union[Unset, None, bool]):
        preview_rows (Union[Unset, None, int]):
        json_body (DataUploadParams): parameters used when uploading data to a data source

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DataUploadResponse, Error]]
    """

    return sync_detailed(
        data_source_id=data_source_id,
        client=client,
        json_body=json_body,
        preview=preview,
        preview_rows=preview_rows,
    ).parsed


async def asyncio_detailed(
    data_source_id: str,
    *,
    client: Client,
    json_body: DataUploadParams,
    preview: Union[Unset, None, bool] = UNSET,
    preview_rows: Union[Unset, None, int] = UNSET,
) -> Response[Union[DataUploadResponse, Error]]:
    """Load data into a data source

    Args:
        data_source_id (str):
        preview (Union[Unset, None, bool]):
        preview_rows (Union[Unset, None, int]):
        json_body (DataUploadParams): parameters used when uploading data to a data source

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DataUploadResponse, Error]]
    """

    kwargs = _get_kwargs(
        data_source_id=data_source_id,
        client=client,
        json_body=json_body,
        preview=preview,
        preview_rows=preview_rows,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    data_source_id: str,
    *,
    client: Client,
    json_body: DataUploadParams,
    preview: Union[Unset, None, bool] = UNSET,
    preview_rows: Union[Unset, None, int] = UNSET,
) -> Optional[Union[DataUploadResponse, Error]]:
    """Load data into a data source

    Args:
        data_source_id (str):
        preview (Union[Unset, None, bool]):
        preview_rows (Union[Unset, None, int]):
        json_body (DataUploadParams): parameters used when uploading data to a data source

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DataUploadResponse, Error]]
    """

    return (
        await asyncio_detailed(
            data_source_id=data_source_id,
            client=client,
            json_body=json_body,
            preview=preview,
            preview_rows=preview_rows,
        )
    ).parsed
