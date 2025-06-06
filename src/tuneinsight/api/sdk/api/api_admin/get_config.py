from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.error import Error
from ...models.instance_configuration import InstanceConfiguration
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    force_config_portal_sync: Union[Unset, None, bool] = False,
) -> Dict[str, Any]:
    url = "{}/config".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["forceConfigPortalSync"] = force_config_portal_sync

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Error, InstanceConfiguration]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = InstanceConfiguration.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = Error.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = Error.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = Error.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code} ({response})")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Error, InstanceConfiguration]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    force_config_portal_sync: Union[Unset, None, bool] = False,
) -> Response[Union[Error, InstanceConfiguration]]:
    """get information about the instance's configuration (requires administrative privileges)

    Args:
        force_config_portal_sync (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, InstanceConfiguration]]
    """

    kwargs = _get_kwargs(
        client=client,
        force_config_portal_sync=force_config_portal_sync,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    force_config_portal_sync: Union[Unset, None, bool] = False,
) -> Optional[Union[Error, InstanceConfiguration]]:
    """get information about the instance's configuration (requires administrative privileges)

    Args:
        force_config_portal_sync (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, InstanceConfiguration]]
    """

    return sync_detailed(
        client=client,
        force_config_portal_sync=force_config_portal_sync,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    force_config_portal_sync: Union[Unset, None, bool] = False,
) -> Response[Union[Error, InstanceConfiguration]]:
    """get information about the instance's configuration (requires administrative privileges)

    Args:
        force_config_portal_sync (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, InstanceConfiguration]]
    """

    kwargs = _get_kwargs(
        client=client,
        force_config_portal_sync=force_config_portal_sync,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    force_config_portal_sync: Union[Unset, None, bool] = False,
) -> Optional[Union[Error, InstanceConfiguration]]:
    """get information about the instance's configuration (requires administrative privileges)

    Args:
        force_config_portal_sync (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, InstanceConfiguration]]
    """

    return (
        await asyncio_detailed(
            client=client,
            force_config_portal_sync=force_config_portal_sync,
        )
    ).parsed
