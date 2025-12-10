from http import HTTPStatus
from typing import Any, Dict, List, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.data_source_variable import DataSourceVariable
from ...models.get_preprocessing_dry_run_json_body import GetPreprocessingDryRunJsonBody
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: GetPreprocessingDryRunJsonBody,
) -> Dict[str, Any]:
    url = "{}/preprocessing/dryrun".format(client.base_url)

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[List[List["DataSourceVariable"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = []
            _response_200_item = response_200_item_data
            for response_200_item_item_data in _response_200_item:
                response_200_item_item = DataSourceVariable.from_dict(response_200_item_item_data)

                response_200_item.append(response_200_item_item)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code} ({response})")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[List[List["DataSourceVariable"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: GetPreprocessingDryRunJsonBody,
) -> Response[List[List["DataSourceVariable"]]]:
    """Computes the dataset columns at every stage of a preprocessing chain. This also checks that the
    preprocessing chain is valid.

    Args:
        json_body (GetPreprocessingDryRunJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List[List['DataSourceVariable']]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    json_body: GetPreprocessingDryRunJsonBody,
) -> Optional[List[List["DataSourceVariable"]]]:
    """Computes the dataset columns at every stage of a preprocessing chain. This also checks that the
    preprocessing chain is valid.

    Args:
        json_body (GetPreprocessingDryRunJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List[List['DataSourceVariable']]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: GetPreprocessingDryRunJsonBody,
) -> Response[List[List["DataSourceVariable"]]]:
    """Computes the dataset columns at every stage of a preprocessing chain. This also checks that the
    preprocessing chain is valid.

    Args:
        json_body (GetPreprocessingDryRunJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List[List['DataSourceVariable']]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    json_body: GetPreprocessingDryRunJsonBody,
) -> Optional[List[List["DataSourceVariable"]]]:
    """Computes the dataset columns at every stage of a preprocessing chain. This also checks that the
    preprocessing chain is valid.

    Args:
        json_body (GetPreprocessingDryRunJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List[List['DataSourceVariable']]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
