from http import HTTPStatus
from typing import Any, Dict, Optional, Union

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

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[DataSource, Error]]:
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


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[DataSource, Error]]:
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
) -> Response[Union[DataSource, Error]]:
    """Request the creation of a mock dataset.

    Args:
        method (PostMockDatasetMethod):
        name (Union[Unset, None, str]):
        numrows (int):
        seed (Union[Unset, None, str]):
        json_body (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DataSource, Error]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        method=method,
        name=name,
        numrows=numrows,
        seed=seed,
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
) -> Optional[Union[DataSource, Error]]:
    """Request the creation of a mock dataset.

    Args:
        method (PostMockDatasetMethod):
        name (Union[Unset, None, str]):
        numrows (int):
        seed (Union[Unset, None, str]):
        json_body (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DataSource, Error]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        method=method,
        name=name,
        numrows=numrows,
        seed=seed,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: str,
    method: PostMockDatasetMethod,
    name: Union[Unset, None, str] = UNSET,
    numrows: int,
    seed: Union[Unset, None, str] = UNSET,
) -> Response[Union[DataSource, Error]]:
    """Request the creation of a mock dataset.

    Args:
        method (PostMockDatasetMethod):
        name (Union[Unset, None, str]):
        numrows (int):
        seed (Union[Unset, None, str]):
        json_body (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DataSource, Error]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        method=method,
        name=name,
        numrows=numrows,
        seed=seed,
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
) -> Optional[Union[DataSource, Error]]:
    """Request the creation of a mock dataset.

    Args:
        method (PostMockDatasetMethod):
        name (Union[Unset, None, str]):
        numrows (int):
        seed (Union[Unset, None, str]):
        json_body (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DataSource, Error]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            method=method,
            name=name,
            numrows=numrows,
            seed=seed,
        )
    ).parsed
