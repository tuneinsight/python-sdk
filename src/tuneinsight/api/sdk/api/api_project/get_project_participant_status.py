from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import Client
from ...models.get_project_participant_status_response_403 import GetProjectParticipantStatusResponse403
from ...models.node_status import NodeStatus
from ...types import Response


def _get_kwargs(
    project_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/projects/{projectId}/participant-status".format(client.base_url, projectId=project_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[GetProjectParticipantStatusResponse403, List[NodeStatus], str]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = NodeStatus.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 403:
        response_403 = GetProjectParticipantStatusResponse403.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = cast(str, response.json())
        return response_404
    if response.status_code == 500:
        response_500 = cast(str, response.json())
        return response_500
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[GetProjectParticipantStatusResponse403, List[NodeStatus], str]]:
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
) -> Response[Union[GetProjectParticipantStatusResponse403, List[NodeStatus], str]]:
    """Gets the network status of the participants of the project

    Args:
        project_id (str):

    Returns:
        Response[Union[GetProjectParticipantStatusResponse403, List[NodeStatus], str]]
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
) -> Optional[Union[GetProjectParticipantStatusResponse403, List[NodeStatus], str]]:
    """Gets the network status of the participants of the project

    Args:
        project_id (str):

    Returns:
        Response[Union[GetProjectParticipantStatusResponse403, List[NodeStatus], str]]
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: Client,
) -> Response[Union[GetProjectParticipantStatusResponse403, List[NodeStatus], str]]:
    """Gets the network status of the participants of the project

    Args:
        project_id (str):

    Returns:
        Response[Union[GetProjectParticipantStatusResponse403, List[NodeStatus], str]]
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
) -> Optional[Union[GetProjectParticipantStatusResponse403, List[NodeStatus], str]]:
    """Gets the network status of the participants of the project

    Args:
        project_id (str):

    Returns:
        Response[Union[GetProjectParticipantStatusResponse403, List[NodeStatus], str]]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
        )
    ).parsed
