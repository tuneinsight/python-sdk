from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.get_model_response_403 import GetModelResponse403
from ...models.model import Model
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    model_id: Union[Unset, None, str] = UNSET,
    data_object_id: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/model".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["modelId"] = model_id

    params["dataObjectId"] = data_object_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[GetModelResponse403, Model, str]]:
    if response.status_code == 200:
        response_200 = Model.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(str, response.json())
        return response_400
    if response.status_code == 403:
        response_403 = GetModelResponse403.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = cast(str, response.json())
        return response_404
    if response.status_code == 422:
        response_422 = cast(str, response.json())
        return response_422
    if response.status_code == 500:
        response_500 = cast(str, response.json())
        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[GetModelResponse403, Model, str]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    model_id: Union[Unset, None, str] = UNSET,
    data_object_id: Union[Unset, None, str] = UNSET,
) -> Response[Union[GetModelResponse403, Model, str]]:
    """Get the metadata of a machine learning model.

    Args:
        model_id (Union[Unset, None, str]):
        data_object_id (Union[Unset, None, str]):

    Returns:
        Response[Union[GetModelResponse403, Model, str]]
    """

    kwargs = _get_kwargs(
        client=client,
        model_id=model_id,
        data_object_id=data_object_id,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    model_id: Union[Unset, None, str] = UNSET,
    data_object_id: Union[Unset, None, str] = UNSET,
) -> Optional[Union[GetModelResponse403, Model, str]]:
    """Get the metadata of a machine learning model.

    Args:
        model_id (Union[Unset, None, str]):
        data_object_id (Union[Unset, None, str]):

    Returns:
        Response[Union[GetModelResponse403, Model, str]]
    """

    return sync_detailed(
        client=client,
        model_id=model_id,
        data_object_id=data_object_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    model_id: Union[Unset, None, str] = UNSET,
    data_object_id: Union[Unset, None, str] = UNSET,
) -> Response[Union[GetModelResponse403, Model, str]]:
    """Get the metadata of a machine learning model.

    Args:
        model_id (Union[Unset, None, str]):
        data_object_id (Union[Unset, None, str]):

    Returns:
        Response[Union[GetModelResponse403, Model, str]]
    """

    kwargs = _get_kwargs(
        client=client,
        model_id=model_id,
        data_object_id=data_object_id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    model_id: Union[Unset, None, str] = UNSET,
    data_object_id: Union[Unset, None, str] = UNSET,
) -> Optional[Union[GetModelResponse403, Model, str]]:
    """Get the metadata of a machine learning model.

    Args:
        model_id (Union[Unset, None, str]):
        data_object_id (Union[Unset, None, str]):

    Returns:
        Response[Union[GetModelResponse403, Model, str]]
    """

    return (
        await asyncio_detailed(
            client=client,
            model_id=model_id,
            data_object_id=data_object_id,
        )
    ).parsed
