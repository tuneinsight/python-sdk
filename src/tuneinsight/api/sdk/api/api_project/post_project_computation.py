from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.post_project_computation_response_403 import PostProjectComputationResponse403
from ...models.project import Project
from ...types import Response


def _get_kwargs(
    project_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/projects/{projectId}/computation".format(client.base_url, projectId=project_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[PostProjectComputationResponse403, Project, str]]:
    if response.status_code == 201:
        response_201 = Project.from_dict(response.json())

        return response_201
    if response.status_code == 400:
        response_400 = cast(str, response.json())
        return response_400
    if response.status_code == 403:
        response_403 = PostProjectComputationResponse403.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = cast(str, response.json())
        return response_404
    if response.status_code == 500:
        response_500 = cast(str, response.json())
        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[PostProjectComputationResponse403, Project, str]]:
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
) -> Response[Union[PostProjectComputationResponse403, Project, str]]:
    """Run the computation defined on the project

    Args:
        project_id (str):

    Returns:
        Response[Union[PostProjectComputationResponse403, Project, str]]
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
) -> Optional[Union[PostProjectComputationResponse403, Project, str]]:
    """Run the computation defined on the project

    Args:
        project_id (str):

    Returns:
        Response[Union[PostProjectComputationResponse403, Project, str]]
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: Client,
) -> Response[Union[PostProjectComputationResponse403, Project, str]]:
    """Run the computation defined on the project

    Args:
        project_id (str):

    Returns:
        Response[Union[PostProjectComputationResponse403, Project, str]]
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
) -> Optional[Union[PostProjectComputationResponse403, Project, str]]:
    """Run the computation defined on the project

    Args:
        project_id (str):

    Returns:
        Response[Union[PostProjectComputationResponse403, Project, str]]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
        )
    ).parsed
