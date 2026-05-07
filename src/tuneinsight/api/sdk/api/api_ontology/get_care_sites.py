from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.care_site import CareSite
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    data_source_id: Union[Unset, None, str] = UNSET,
    countries: Union[Unset, None, List[str]] = UNSET,
    regions: Union[Unset, None, List[str]] = UNSET,
    districts: Union[Unset, None, List[str]] = UNSET,
) -> Dict[str, Any]:
    url = "{}/care-sites".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["dataSourceId"] = data_source_id

    json_countries: Union[Unset, None, List[str]] = UNSET
    if not isinstance(countries, Unset):
        if countries is None:
            json_countries = None
        else:
            json_countries = countries

    params["countries[]"] = json_countries

    json_regions: Union[Unset, None, List[str]] = UNSET
    if not isinstance(regions, Unset):
        if regions is None:
            json_regions = None
        else:
            json_regions = regions

    params["regions[]"] = json_regions

    json_districts: Union[Unset, None, List[str]] = UNSET
    if not isinstance(districts, Unset):
        if districts is None:
            json_districts = None
        else:
            json_districts = districts

    params["districts[]"] = json_districts

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[List["CareSite"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = CareSite.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code} ({response})")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[List["CareSite"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    data_source_id: Union[Unset, None, str] = UNSET,
    countries: Union[Unset, None, List[str]] = UNSET,
    regions: Union[Unset, None, List[str]] = UNSET,
    districts: Union[Unset, None, List[str]] = UNSET,
) -> Response[List["CareSite"]]:
    """Get the list of all care sites along with metadata.

    Args:
        data_source_id (Union[Unset, None, str]):
        countries (Union[Unset, None, List[str]]):
        regions (Union[Unset, None, List[str]]):
        districts (Union[Unset, None, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['CareSite']]
    """

    kwargs = _get_kwargs(
        client=client,
        data_source_id=data_source_id,
        countries=countries,
        regions=regions,
        districts=districts,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    data_source_id: Union[Unset, None, str] = UNSET,
    countries: Union[Unset, None, List[str]] = UNSET,
    regions: Union[Unset, None, List[str]] = UNSET,
    districts: Union[Unset, None, List[str]] = UNSET,
) -> Optional[List["CareSite"]]:
    """Get the list of all care sites along with metadata.

    Args:
        data_source_id (Union[Unset, None, str]):
        countries (Union[Unset, None, List[str]]):
        regions (Union[Unset, None, List[str]]):
        districts (Union[Unset, None, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['CareSite']]
    """

    return sync_detailed(
        client=client,
        data_source_id=data_source_id,
        countries=countries,
        regions=regions,
        districts=districts,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    data_source_id: Union[Unset, None, str] = UNSET,
    countries: Union[Unset, None, List[str]] = UNSET,
    regions: Union[Unset, None, List[str]] = UNSET,
    districts: Union[Unset, None, List[str]] = UNSET,
) -> Response[List["CareSite"]]:
    """Get the list of all care sites along with metadata.

    Args:
        data_source_id (Union[Unset, None, str]):
        countries (Union[Unset, None, List[str]]):
        regions (Union[Unset, None, List[str]]):
        districts (Union[Unset, None, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['CareSite']]
    """

    kwargs = _get_kwargs(
        client=client,
        data_source_id=data_source_id,
        countries=countries,
        regions=regions,
        districts=districts,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    data_source_id: Union[Unset, None, str] = UNSET,
    countries: Union[Unset, None, List[str]] = UNSET,
    regions: Union[Unset, None, List[str]] = UNSET,
    districts: Union[Unset, None, List[str]] = UNSET,
) -> Optional[List["CareSite"]]:
    """Get the list of all care sites along with metadata.

    Args:
        data_source_id (Union[Unset, None, str]):
        countries (Union[Unset, None, List[str]]):
        regions (Union[Unset, None, List[str]]):
        districts (Union[Unset, None, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['CareSite']]
    """

    return (
        await asyncio_detailed(
            client=client,
            data_source_id=data_source_id,
            countries=countries,
            regions=regions,
            districts=districts,
        )
    ).parsed
