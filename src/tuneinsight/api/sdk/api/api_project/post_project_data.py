from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.post_project_data_json_body import PostProjectDataJsonBody
from ...models.post_project_data_response_403 import PostProjectDataResponse403
from ...types import Response


def _get_kwargs(
    project_id: str,
    *,
    client: Client,
    json_body: PostProjectDataJsonBody,
) -> Dict[str, Any]:
    url = "{}/projects/{projectId}/data".format(client.base_url, projectId=project_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[PostProjectDataResponse403, str]]:
    if response.status_code == 201:
        response_201 = cast(str, response.json())
        return response_201
    if response.status_code == 403:
        response_403 = PostProjectDataResponse403.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = cast(str, response.json())
        return response_404
    if response.status_code == 500:
        response_500 = cast(str, response.json())
        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[PostProjectDataResponse403, str]]:
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
    json_body: PostProjectDataJsonBody,
) -> Response[Union[PostProjectDataResponse403, str]]:
    """Run the query defined in the project to create a dataobject from the datasource

    Args:
        project_id (str):
        json_body (PostProjectDataJsonBody):

    Returns:
        Response[Union[PostProjectDataResponse403, str]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        client=client,
        json_body=json_body,
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
    json_body: PostProjectDataJsonBody,
) -> Optional[Union[PostProjectDataResponse403, str]]:
    """Run the query defined in the project to create a dataobject from the datasource

    Args:
        project_id (str):
        json_body (PostProjectDataJsonBody):

    Returns:
        Response[Union[PostProjectDataResponse403, str]]
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: Client,
    json_body: PostProjectDataJsonBody,
) -> Response[Union[PostProjectDataResponse403, str]]:
    """Run the query defined in the project to create a dataobject from the datasource

    Args:
        project_id (str):
        json_body (PostProjectDataJsonBody):

    Returns:
        Response[Union[PostProjectDataResponse403, str]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    project_id: str,
    *,
    client: Client,
    json_body: PostProjectDataJsonBody,
) -> Optional[Union[PostProjectDataResponse403, str]]:
    """Run the query defined in the project to create a dataobject from the datasource

    Args:
        project_id (str):
        json_body (PostProjectDataJsonBody):

    Returns:
        Response[Union[PostProjectDataResponse403, str]]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
