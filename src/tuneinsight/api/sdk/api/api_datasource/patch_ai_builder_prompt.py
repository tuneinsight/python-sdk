from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.ai_builder_prompt_definition import AIBuilderPromptDefinition
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    prompt_id: str,
    *,
    client: Client,
    json_body: AIBuilderPromptDefinition,
) -> Dict[str, Any]:
    url = "{}/ai-builder-prompts/{promptId}".format(client.base_url, promptId=prompt_id)

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
        "method": "patch",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "proxies": proxies,
        "json": json_json_body,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[AIBuilderPromptDefinition, Error]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = AIBuilderPromptDefinition.from_dict(response.json())

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
    if response.status_code == HTTPStatus.NOT_IMPLEMENTED:
        response_501 = Error.from_dict(response.json())

        return response_501
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code} ({response})")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[AIBuilderPromptDefinition, Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    prompt_id: str,
    *,
    client: Client,
    json_body: AIBuilderPromptDefinition,
) -> Response[Union[AIBuilderPromptDefinition, Error]]:
    """Updates a specific prompt by ID.

    Args:
        prompt_id (str):
        json_body (AIBuilderPromptDefinition): definition of a prompt for the AI query builder

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AIBuilderPromptDefinition, Error]]
    """

    kwargs = _get_kwargs(
        prompt_id=prompt_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    prompt_id: str,
    *,
    client: Client,
    json_body: AIBuilderPromptDefinition,
) -> Optional[Union[AIBuilderPromptDefinition, Error]]:
    """Updates a specific prompt by ID.

    Args:
        prompt_id (str):
        json_body (AIBuilderPromptDefinition): definition of a prompt for the AI query builder

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AIBuilderPromptDefinition, Error]]
    """

    return sync_detailed(
        prompt_id=prompt_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    prompt_id: str,
    *,
    client: Client,
    json_body: AIBuilderPromptDefinition,
) -> Response[Union[AIBuilderPromptDefinition, Error]]:
    """Updates a specific prompt by ID.

    Args:
        prompt_id (str):
        json_body (AIBuilderPromptDefinition): definition of a prompt for the AI query builder

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AIBuilderPromptDefinition, Error]]
    """

    kwargs = _get_kwargs(
        prompt_id=prompt_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    prompt_id: str,
    *,
    client: Client,
    json_body: AIBuilderPromptDefinition,
) -> Optional[Union[AIBuilderPromptDefinition, Error]]:
    """Updates a specific prompt by ID.

    Args:
        prompt_id (str):
        json_body (AIBuilderPromptDefinition): definition of a prompt for the AI query builder

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AIBuilderPromptDefinition, Error]]
    """

    return (
        await asyncio_detailed(
            prompt_id=prompt_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
