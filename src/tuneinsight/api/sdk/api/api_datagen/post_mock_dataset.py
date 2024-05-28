from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.data_source import DataSource
from ...models.error import Error
from ...models.post_mock_dataset_method import PostMockDatasetMethod
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    json_body: str,
    method: PostMockDatasetMethod,
    name: Union[Unset, None, str] = UNSET,
    numrows: int,
    seed: Union[Unset, None, str] = UNSET,
    create_datasource: Union[Unset, None, bool] = UNSET,
    clear_if_exists: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    url = "{}/mock/dataset".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_method = method.value

    params["method"] = json_method

    params["name"] = name

    params["numrows"] = numrows

    params["seed"] = seed

    params["createDatasource"] = create_datasource

    params["clearIfExists"] = clear_if_exists

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body

    # Set the proxies if the client has proxies set.
    proxies = None
    if hasattr(client, "proxies") and client.proxies is not None:
        https_proxy = client.proxies.get("https")
        if https_proxy:
            proxies = https_proxy
        else:
            http_proxy = client.proxies.get("http")
            if http_proxy:
                proxies = http_proxy

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "proxies": proxies,
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, DataSource, Error]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = cast(Any, None)
        return response_200
    if response.status_code == HTTPStatus.CREATED:
        response_201 = DataSource.from_dict(response.json())

        return response_201
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = Error.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = Error.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = Error.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, DataSource, Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: str,
    method: PostMockDatasetMethod,
    name: Union[Unset, None, str] = UNSET,
    numrows: int,
    seed: Union[Unset, None, str] = UNSET,
    create_datasource: Union[Unset, None, bool] = UNSET,
    clear_if_exists: Union[Unset, None, bool] = UNSET,
) -> Response[Union[Any, DataSource, Error]]:
    """Request the creation of a mock dataset.

    Args:
        method (PostMockDatasetMethod):
        name (Union[Unset, None, str]):
        numrows (int):
        seed (Union[Unset, None, str]):
        create_datasource (Union[Unset, None, bool]):
        clear_if_exists (Union[Unset, None, bool]):
        json_body (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DataSource, Error]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        method=method,
        name=name,
        numrows=numrows,
        seed=seed,
        create_datasource=create_datasource,
        clear_if_exists=clear_if_exists,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    json_body: str,
    method: PostMockDatasetMethod,
    name: Union[Unset, None, str] = UNSET,
    numrows: int,
    seed: Union[Unset, None, str] = UNSET,
    create_datasource: Union[Unset, None, bool] = UNSET,
    clear_if_exists: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[Any, DataSource, Error]]:
    """Request the creation of a mock dataset.

    Args:
        method (PostMockDatasetMethod):
        name (Union[Unset, None, str]):
        numrows (int):
        seed (Union[Unset, None, str]):
        create_datasource (Union[Unset, None, bool]):
        clear_if_exists (Union[Unset, None, bool]):
        json_body (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DataSource, Error]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        method=method,
        name=name,
        numrows=numrows,
        seed=seed,
        create_datasource=create_datasource,
        clear_if_exists=clear_if_exists,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: str,
    method: PostMockDatasetMethod,
    name: Union[Unset, None, str] = UNSET,
    numrows: int,
    seed: Union[Unset, None, str] = UNSET,
    create_datasource: Union[Unset, None, bool] = UNSET,
    clear_if_exists: Union[Unset, None, bool] = UNSET,
) -> Response[Union[Any, DataSource, Error]]:
    """Request the creation of a mock dataset.

    Args:
        method (PostMockDatasetMethod):
        name (Union[Unset, None, str]):
        numrows (int):
        seed (Union[Unset, None, str]):
        create_datasource (Union[Unset, None, bool]):
        clear_if_exists (Union[Unset, None, bool]):
        json_body (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DataSource, Error]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        method=method,
        name=name,
        numrows=numrows,
        seed=seed,
        create_datasource=create_datasource,
        clear_if_exists=clear_if_exists,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    json_body: str,
    method: PostMockDatasetMethod,
    name: Union[Unset, None, str] = UNSET,
    numrows: int,
    seed: Union[Unset, None, str] = UNSET,
    create_datasource: Union[Unset, None, bool] = UNSET,
    clear_if_exists: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[Any, DataSource, Error]]:
    """Request the creation of a mock dataset.

    Args:
        method (PostMockDatasetMethod):
        name (Union[Unset, None, str]):
        numrows (int):
        seed (Union[Unset, None, str]):
        create_datasource (Union[Unset, None, bool]):
        clear_if_exists (Union[Unset, None, bool]):
        json_body (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DataSource, Error]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            method=method,
            name=name,
            numrows=numrows,
            seed=seed,
            create_datasource=create_datasource,
            clear_if_exists=clear_if_exists,
        )
    ).parsed
