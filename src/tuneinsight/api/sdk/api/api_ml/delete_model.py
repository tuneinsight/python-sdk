from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.delete_model_response_403 import DeleteModelResponse403
from ...types import UNSET, Response


def _get_kwargs(
    *,
    client: Client,
    model_id: str,
) -> Dict[str, Any]:
    url = "{}/model".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["modelId"] = model_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, DeleteModelResponse403, str]]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == 403:
        response_403 = DeleteModelResponse403.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = cast(str, response.json())
        return response_404
    if response.status_code == 500:
        response_500 = cast(str, response.json())
        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, DeleteModelResponse403, str]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    model_id: str,
) -> Response[Union[Any, DeleteModelResponse403, str]]:
    """Delete a model its associated data.

    Args:
        model_id (str):

    Returns:
        Response[Union[Any, DeleteModelResponse403, str]]
    """

    kwargs = _get_kwargs(
        client=client,
        model_id=model_id,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    model_id: str,
) -> Optional[Union[Any, DeleteModelResponse403, str]]:
    """Delete a model its associated data.

    Args:
        model_id (str):

    Returns:
        Response[Union[Any, DeleteModelResponse403, str]]
    """

    return sync_detailed(
        client=client,
        model_id=model_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    model_id: str,
) -> Response[Union[Any, DeleteModelResponse403, str]]:
    """Delete a model its associated data.

    Args:
        model_id (str):

    Returns:
        Response[Union[Any, DeleteModelResponse403, str]]
    """

    kwargs = _get_kwargs(
        client=client,
        model_id=model_id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    model_id: str,
) -> Optional[Union[Any, DeleteModelResponse403, str]]:
    """Delete a model its associated data.

    Args:
        model_id (str):

    Returns:
        Response[Union[Any, DeleteModelResponse403, str]]
    """

    return (
        await asyncio_detailed(
            client=client,
            model_id=model_id,
        )
    ).parsed
