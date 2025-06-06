from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.error import Error
from ...models.put_user_preference_json_body import PutUserPreferenceJsonBody
from ...models.put_user_preference_key import PutUserPreferenceKey
from ...types import Response


def _get_kwargs(
    key: PutUserPreferenceKey,
    *,
    client: Client,
    json_body: PutUserPreferenceJsonBody,
) -> Dict[str, Any]:
    url = "{}/user-preferences/{key}".format(client.base_url, key=key)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

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
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "proxies": proxies,
        "json": json_json_body,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, Error]]:
    if response.status_code == HTTPStatus.NO_CONTENT:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = Error.from_dict(response.json())

        return response_400
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


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    key: PutUserPreferenceKey,
    *,
    client: Client,
    json_body: PutUserPreferenceJsonBody,
) -> Response[Union[Any, Error]]:
    """Update user preference

    Args:
        key (PutUserPreferenceKey):
        json_body (PutUserPreferenceJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error]]
    """

    kwargs = _get_kwargs(
        key=key,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    key: PutUserPreferenceKey,
    *,
    client: Client,
    json_body: PutUserPreferenceJsonBody,
) -> Optional[Union[Any, Error]]:
    """Update user preference

    Args:
        key (PutUserPreferenceKey):
        json_body (PutUserPreferenceJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error]]
    """

    return sync_detailed(
        key=key,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    key: PutUserPreferenceKey,
    *,
    client: Client,
    json_body: PutUserPreferenceJsonBody,
) -> Response[Union[Any, Error]]:
    """Update user preference

    Args:
        key (PutUserPreferenceKey):
        json_body (PutUserPreferenceJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error]]
    """

    kwargs = _get_kwargs(
        key=key,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    key: PutUserPreferenceKey,
    *,
    client: Client,
    json_body: PutUserPreferenceJsonBody,
) -> Optional[Union[Any, Error]]:
    """Update user preference

    Args:
        key (PutUserPreferenceKey):
        json_body (PutUserPreferenceJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error]]
    """

    return (
        await asyncio_detailed(
            key=key,
            client=client,
            json_body=json_body,
        )
    ).parsed
