from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    *,
    client: Client,
    revoke: Union[Unset, None, bool] = UNSET,
    notify: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    url = "{}/projects/{projectId}/request-authorization".format(client.base_url, projectId=project_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["revoke"] = revoke

    params["notify"] = notify

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
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "proxies": proxies,
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, Error]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = cast(Any, None)
        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = Error.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = Error.from_dict(response.json())

        return response_401
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


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    *,
    client: Client,
    revoke: Union[Unset, None, bool] = UNSET,
    notify: Union[Unset, None, bool] = UNSET,
) -> Response[Union[Any, Error]]:
    """Request authorization to run this project.

    Args:
        project_id (str):
        revoke (Union[Unset, None, bool]):
        notify (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        client=client,
        revoke=revoke,
        notify=notify,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: Client,
    revoke: Union[Unset, None, bool] = UNSET,
    notify: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[Any, Error]]:
    """Request authorization to run this project.

    Args:
        project_id (str):
        revoke (Union[Unset, None, bool]):
        notify (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error]]
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        revoke=revoke,
        notify=notify,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: Client,
    revoke: Union[Unset, None, bool] = UNSET,
    notify: Union[Unset, None, bool] = UNSET,
) -> Response[Union[Any, Error]]:
    """Request authorization to run this project.

    Args:
        project_id (str):
        revoke (Union[Unset, None, bool]):
        notify (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        client=client,
        revoke=revoke,
        notify=notify,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: Client,
    revoke: Union[Unset, None, bool] = UNSET,
    notify: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[Any, Error]]:
    """Request authorization to run this project.

    Args:
        project_id (str):
        revoke (Union[Unset, None, bool]):
        notify (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error]]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            revoke=revoke,
            notify=notify,
        )
    ).parsed
