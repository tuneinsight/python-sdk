from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.error import Error
from ...models.term import Term
from ...types import UNSET, Response, Unset


def _get_kwargs(
    term_id: str,
    *,
    client: Client,
    care_sites: Union[Unset, None, List[str]] = UNSET,
) -> Dict[str, Any]:
    url = "{}/terms/{termId}".format(client.base_url, termId=term_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_care_sites: Union[Unset, None, List[str]] = UNSET
    if not isinstance(care_sites, Unset):
        if care_sites is None:
            json_care_sites = None
        else:
            json_care_sites = care_sites

    params["careSites[]"] = json_care_sites

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
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "proxies": proxies,
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Error, Term]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Term.from_dict(response.json())

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
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = Error.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.NOT_IMPLEMENTED:
        response_501 = Error.from_dict(response.json())

        return response_501
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code} ({response})")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Error, Term]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    term_id: str,
    *,
    client: Client,
    care_sites: Union[Unset, None, List[str]] = UNSET,
) -> Response[Union[Error, Term]]:
    """Fetch all the data related to one specific code.

    Args:
        term_id (str):
        care_sites (Union[Unset, None, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Term]]
    """

    kwargs = _get_kwargs(
        term_id=term_id,
        client=client,
        care_sites=care_sites,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    term_id: str,
    *,
    client: Client,
    care_sites: Union[Unset, None, List[str]] = UNSET,
) -> Optional[Union[Error, Term]]:
    """Fetch all the data related to one specific code.

    Args:
        term_id (str):
        care_sites (Union[Unset, None, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Term]]
    """

    return sync_detailed(
        term_id=term_id,
        client=client,
        care_sites=care_sites,
    ).parsed


async def asyncio_detailed(
    term_id: str,
    *,
    client: Client,
    care_sites: Union[Unset, None, List[str]] = UNSET,
) -> Response[Union[Error, Term]]:
    """Fetch all the data related to one specific code.

    Args:
        term_id (str):
        care_sites (Union[Unset, None, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Term]]
    """

    kwargs = _get_kwargs(
        term_id=term_id,
        client=client,
        care_sites=care_sites,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    term_id: str,
    *,
    client: Client,
    care_sites: Union[Unset, None, List[str]] = UNSET,
) -> Optional[Union[Error, Term]]:
    """Fetch all the data related to one specific code.

    Args:
        term_id (str):
        care_sites (Union[Unset, None, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Term]]
    """

    return (
        await asyncio_detailed(
            term_id=term_id,
            client=client,
            care_sites=care_sites,
        )
    ).parsed
