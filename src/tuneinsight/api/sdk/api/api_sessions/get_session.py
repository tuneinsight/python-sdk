from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.get_session_response_403 import GetSessionResponse403
from ...models.session import Session
from ...types import Response


def _get_kwargs(
    session_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/sessions/{sessionId}".format(client.base_url, sessionId=session_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[GetSessionResponse403, Session, str]]:
    if response.status_code == 200:
        response_200 = Session.from_dict(response.json())

        return response_200
    if response.status_code == 403:
        response_403 = GetSessionResponse403.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = cast(str, response.json())
        return response_404
    if response.status_code == 500:
        response_500 = cast(str, response.json())
        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[GetSessionResponse403, Session, str]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    session_id: str,
    *,
    client: Client,
) -> Response[Union[GetSessionResponse403, Session, str]]:
    """Get basic information about a session

    Args:
        session_id (str):

    Returns:
        Response[Union[GetSessionResponse403, Session, str]]
    """

    kwargs = _get_kwargs(
        session_id=session_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    session_id: str,
    *,
    client: Client,
) -> Optional[Union[GetSessionResponse403, Session, str]]:
    """Get basic information about a session

    Args:
        session_id (str):

    Returns:
        Response[Union[GetSessionResponse403, Session, str]]
    """

    return sync_detailed(
        session_id=session_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    session_id: str,
    *,
    client: Client,
) -> Response[Union[GetSessionResponse403, Session, str]]:
    """Get basic information about a session

    Args:
        session_id (str):

    Returns:
        Response[Union[GetSessionResponse403, Session, str]]
    """

    kwargs = _get_kwargs(
        session_id=session_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    session_id: str,
    *,
    client: Client,
) -> Optional[Union[GetSessionResponse403, Session, str]]:
    """Get basic information about a session

    Args:
        session_id (str):

    Returns:
        Response[Union[GetSessionResponse403, Session, str]]
    """

    return (
        await asyncio_detailed(
            session_id=session_id,
            client=client,
        )
    ).parsed
