from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.delete_project_response_403 import DeleteProjectResponse403
from ...types import Response


def _get_kwargs(
    project_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/projects/{projectId}".format(client.base_url, projectId=project_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, DeleteProjectResponse403, str]]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == 403:
        response_403 = DeleteProjectResponse403.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = cast(str, response.json())
        return response_404
    if response.status_code == 500:
        response_500 = cast(str, response.json())
        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, DeleteProjectResponse403, str]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    project_id: str,
    *,
    client: Client,
) -> Response[Union[Any, DeleteProjectResponse403, str]]:
    """Delete a project

    Args:
        project_id (str):

    Returns:
        Response[Union[Any, DeleteProjectResponse403, str]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    project_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, DeleteProjectResponse403, str]]:
    """Delete a project

    Args:
        project_id (str):

    Returns:
        Response[Union[Any, DeleteProjectResponse403, str]]
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: Client,
) -> Response[Union[Any, DeleteProjectResponse403, str]]:
    """Delete a project

    Args:
        project_id (str):

    Returns:
        Response[Union[Any, DeleteProjectResponse403, str]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    project_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, DeleteProjectResponse403, str]]:
    """Delete a project

    Args:
        project_id (str):

    Returns:
        Response[Union[Any, DeleteProjectResponse403, str]]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
        )
    ).parsed
