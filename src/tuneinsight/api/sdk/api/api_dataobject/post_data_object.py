from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.data_object import DataObject
from ...models.post_data_object_json_body import PostDataObjectJsonBody
from ...models.post_data_object_response_403 import PostDataObjectResponse403
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: PostDataObjectJsonBody,
) -> Dict[str, Any]:
    url = "{}/dataobject".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[DataObject, PostDataObjectResponse403, str]]:
    if response.status_code == 200:
        response_200 = DataObject.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(str, response.json())
        return response_400
    if response.status_code == 403:
        response_403 = PostDataObjectResponse403.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = cast(str, response.json())
        return response_404
    if response.status_code == 500:
        response_500 = cast(str, response.json())
        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[DataObject, PostDataObjectResponse403, str]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: PostDataObjectJsonBody,
) -> Response[Union[DataObject, PostDataObjectResponse403, str]]:
    """Add a new data object based on the columns of a data source or by encrypting or decrypting another
    one.

    Args:
        json_body (PostDataObjectJsonBody):

    Returns:
        Response[Union[DataObject, PostDataObjectResponse403, str]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: PostDataObjectJsonBody,
) -> Optional[Union[DataObject, PostDataObjectResponse403, str]]:
    """Add a new data object based on the columns of a data source or by encrypting or decrypting another
    one.

    Args:
        json_body (PostDataObjectJsonBody):

    Returns:
        Response[Union[DataObject, PostDataObjectResponse403, str]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: PostDataObjectJsonBody,
) -> Response[Union[DataObject, PostDataObjectResponse403, str]]:
    """Add a new data object based on the columns of a data source or by encrypting or decrypting another
    one.

    Args:
        json_body (PostDataObjectJsonBody):

    Returns:
        Response[Union[DataObject, PostDataObjectResponse403, str]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: PostDataObjectJsonBody,
) -> Optional[Union[DataObject, PostDataObjectResponse403, str]]:
    """Add a new data object based on the columns of a data source or by encrypting or decrypting another
    one.

    Args:
        json_body (PostDataObjectJsonBody):

    Returns:
        Response[Union[DataObject, PostDataObjectResponse403, str]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
