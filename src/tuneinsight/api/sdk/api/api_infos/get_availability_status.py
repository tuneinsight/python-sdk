from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.availability_status import AvailabilityStatus
from ...models.error import Error
from ...models.get_availability_status_resource_type import GetAvailabilityStatusResourceType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    resource_type: GetAvailabilityStatusResourceType,
    resource_name: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/resources/availability-status".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_resource_type = resource_type.value

    params["resourceType"] = json_resource_type

    params["resourceName"] = resource_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

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
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "proxies": proxies,
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[AvailabilityStatus, Error]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = AvailabilityStatus.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = Error.from_dict(response.json())

        return response_403
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


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[AvailabilityStatus, Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    resource_type: GetAvailabilityStatusResourceType,
    resource_name: Union[Unset, None, str] = UNSET,
) -> Response[Union[AvailabilityStatus, Error]]:
    """Gets the availability status of resource names.

    Args:
        resource_type (GetAvailabilityStatusResourceType):
        resource_name (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AvailabilityStatus, Error]]
    """

    kwargs = _get_kwargs(
        client=client,
        resource_type=resource_type,
        resource_name=resource_name,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    resource_type: GetAvailabilityStatusResourceType,
    resource_name: Union[Unset, None, str] = UNSET,
) -> Optional[Union[AvailabilityStatus, Error]]:
    """Gets the availability status of resource names.

    Args:
        resource_type (GetAvailabilityStatusResourceType):
        resource_name (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AvailabilityStatus, Error]]
    """

    return sync_detailed(
        client=client,
        resource_type=resource_type,
        resource_name=resource_name,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    resource_type: GetAvailabilityStatusResourceType,
    resource_name: Union[Unset, None, str] = UNSET,
) -> Response[Union[AvailabilityStatus, Error]]:
    """Gets the availability status of resource names.

    Args:
        resource_type (GetAvailabilityStatusResourceType):
        resource_name (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AvailabilityStatus, Error]]
    """

    kwargs = _get_kwargs(
        client=client,
        resource_type=resource_type,
        resource_name=resource_name,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    resource_type: GetAvailabilityStatusResourceType,
    resource_name: Union[Unset, None, str] = UNSET,
) -> Optional[Union[AvailabilityStatus, Error]]:
    """Gets the availability status of resource names.

    Args:
        resource_type (GetAvailabilityStatusResourceType):
        resource_name (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AvailabilityStatus, Error]]
    """

    return (
        await asyncio_detailed(
            client=client,
            resource_type=resource_type,
            resource_name=resource_name,
        )
    ).parsed
