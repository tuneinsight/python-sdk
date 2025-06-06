from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.error import Error
from ...models.result_content import ResultContent
from ...models.result_release import ResultRelease
from ...types import Response


def _get_kwargs(
    result_id: str,
    *,
    client: Client,
    json_body: ResultRelease,
) -> Dict[str, Any]:
    url = "{}/results/{resultId}/release".format(client.base_url, resultId=result_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

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
        "json": json_json_body,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Error, ResultContent]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ResultContent.from_dict(response.json())

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
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = Error.from_dict(response.json())

        return response_422
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = Error.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code} ({response})")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Error, ResultContent]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    result_id: str,
    *,
    client: Client,
    json_body: ResultRelease,
) -> Response[Union[Error, ResultContent]]:
    """Re-encrypt a result with for a fresh public key

    Args:
        result_id (str):
        json_body (ResultRelease): required data to re-encrypt a result

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, ResultContent]]
    """

    kwargs = _get_kwargs(
        result_id=result_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    result_id: str,
    *,
    client: Client,
    json_body: ResultRelease,
) -> Optional[Union[Error, ResultContent]]:
    """Re-encrypt a result with for a fresh public key

    Args:
        result_id (str):
        json_body (ResultRelease): required data to re-encrypt a result

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, ResultContent]]
    """

    return sync_detailed(
        result_id=result_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    result_id: str,
    *,
    client: Client,
    json_body: ResultRelease,
) -> Response[Union[Error, ResultContent]]:
    """Re-encrypt a result with for a fresh public key

    Args:
        result_id (str):
        json_body (ResultRelease): required data to re-encrypt a result

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, ResultContent]]
    """

    kwargs = _get_kwargs(
        result_id=result_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    result_id: str,
    *,
    client: Client,
    json_body: ResultRelease,
) -> Optional[Union[Error, ResultContent]]:
    """Re-encrypt a result with for a fresh public key

    Args:
        result_id (str):
        json_body (ResultRelease): required data to re-encrypt a result

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, ResultContent]]
    """

    return (
        await asyncio_detailed(
            result_id=result_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
