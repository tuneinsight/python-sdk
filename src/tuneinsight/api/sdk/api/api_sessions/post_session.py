from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.post_session_response_403 import PostSessionResponse403
from ...models.session import Session
from ...models.session_definition import SessionDefinition
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: SessionDefinition,
) -> Dict[str, Any]:
    url = "{}/session".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[PostSessionResponse403, Session, str]]:
    if response.status_code == 200:
        response_200 = Session.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(str, response.json())
        return response_400
    if response.status_code == 403:
        response_403 = PostSessionResponse403.from_dict(response.json())

        return response_403
    if response.status_code == 422:
        response_422 = cast(str, response.json())
        return response_422
    if response.status_code == 500:
        response_500 = cast(str, response.json())
        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[PostSessionResponse403, Session, str]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: SessionDefinition,
) -> Response[Union[PostSessionResponse403, Session, str]]:
    """create a session

    Args:
        json_body (SessionDefinition): a session definition, sent in POST

    Returns:
        Response[Union[PostSessionResponse403, Session, str]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: SessionDefinition,
) -> Optional[Union[PostSessionResponse403, Session, str]]:
    """create a session

    Args:
        json_body (SessionDefinition): a session definition, sent in POST

    Returns:
        Response[Union[PostSessionResponse403, Session, str]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: SessionDefinition,
) -> Response[Union[PostSessionResponse403, Session, str]]:
    """create a session

    Args:
        json_body (SessionDefinition): a session definition, sent in POST

    Returns:
        Response[Union[PostSessionResponse403, Session, str]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: SessionDefinition,
) -> Optional[Union[PostSessionResponse403, Session, str]]:
    """create a session

    Args:
        json_body (SessionDefinition): a session definition, sent in POST

    Returns:
        Response[Union[PostSessionResponse403, Session, str]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
