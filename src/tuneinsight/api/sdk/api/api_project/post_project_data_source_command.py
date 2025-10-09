from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.data_source_command_result import DataSourceCommandResult
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    *,
    client: Client,
    global_execution: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    url = "{}/projects/{projectId}/datasource-command".format(client.base_url, projectId=project_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["globalExecution"] = global_execution

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[DataSourceCommandResult, Error]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DataSourceCommandResult.from_dict(response.json())

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
    if response.status_code == HTTPStatus.REQUEST_TIMEOUT:
        response_408 = Error.from_dict(response.json())

        return response_408
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = Error.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code} ({response})")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[DataSourceCommandResult, Error]]:
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
    global_execution: Union[Unset, None, bool] = UNSET,
) -> Response[Union[DataSourceCommandResult, Error]]:
    """Execute a data source's command (e.g. to fetch metadata) on the project's datasource.

    Args:
        project_id (str):
        global_execution (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DataSourceCommandResult, Error]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        client=client,
        global_execution=global_execution,
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
    global_execution: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[DataSourceCommandResult, Error]]:
    """Execute a data source's command (e.g. to fetch metadata) on the project's datasource.

    Args:
        project_id (str):
        global_execution (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DataSourceCommandResult, Error]]
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        global_execution=global_execution,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: Client,
    global_execution: Union[Unset, None, bool] = UNSET,
) -> Response[Union[DataSourceCommandResult, Error]]:
    """Execute a data source's command (e.g. to fetch metadata) on the project's datasource.

    Args:
        project_id (str):
        global_execution (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DataSourceCommandResult, Error]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        client=client,
        global_execution=global_execution,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: Client,
    global_execution: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[DataSourceCommandResult, Error]]:
    """Execute a data source's command (e.g. to fetch metadata) on the project's datasource.

    Args:
        project_id (str):
        global_execution (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DataSourceCommandResult, Error]]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            global_execution=global_execution,
        )
    ).parsed
