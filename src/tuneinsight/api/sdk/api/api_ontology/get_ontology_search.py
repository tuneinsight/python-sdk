from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.error import Error
from ...models.get_ontology_search_order import GetOntologySearchOrder
from ...models.get_ontology_search_response_200_item import GetOntologySearchResponse200Item
from ...models.get_ontology_search_sort_by import GetOntologySearchSortBy
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    page: Union[Unset, None, int] = 1,
    per_page: Union[Unset, None, int] = 20,
    sort_by: Union[Unset, None, GetOntologySearchSortBy] = UNSET,
    order: Union[Unset, None, GetOntologySearchOrder] = UNSET,
    query: str,
    with_occurrence: Union[Unset, None, bool] = UNSET,
    with_network_occurrence: Union[Unset, None, bool] = UNSET,
    ontologies: List[str],
    care_sites: Union[Unset, None, List[str]] = UNSET,
    domains: Union[Unset, None, List[str]] = UNSET,
    favorite: Union[Unset, None, bool] = UNSET,
    simplify_outputs: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    url = "{}/ontology-search".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["page"] = page

    params["perPage"] = per_page

    json_sort_by: Union[Unset, None, str] = UNSET
    if not isinstance(sort_by, Unset):
        json_sort_by = sort_by.value if sort_by else None

    params["sortBy"] = json_sort_by

    json_order: Union[Unset, None, str] = UNSET
    if not isinstance(order, Unset):
        json_order = order.value if order else None

    params["order"] = json_order

    params["query"] = query

    params["withOccurrence"] = with_occurrence

    params["withNetworkOccurrence"] = with_network_occurrence

    json_ontologies = ontologies

    params["ontologies[]"] = json_ontologies

    json_care_sites: Union[Unset, None, List[str]] = UNSET
    if not isinstance(care_sites, Unset):
        if care_sites is None:
            json_care_sites = None
        else:
            json_care_sites = care_sites

    params["careSites[]"] = json_care_sites

    json_domains: Union[Unset, None, List[str]] = UNSET
    if not isinstance(domains, Unset):
        if domains is None:
            json_domains = None
        else:
            json_domains = domains

    params["domains[]"] = json_domains

    params["favorite"] = favorite

    params["simplifyOutputs"] = simplify_outputs

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


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Error, List["GetOntologySearchResponse200Item"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GetOntologySearchResponse200Item.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = Error.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = Error.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = Error.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code} ({response})")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[Error, List["GetOntologySearchResponse200Item"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    page: Union[Unset, None, int] = 1,
    per_page: Union[Unset, None, int] = 20,
    sort_by: Union[Unset, None, GetOntologySearchSortBy] = UNSET,
    order: Union[Unset, None, GetOntologySearchOrder] = UNSET,
    query: str,
    with_occurrence: Union[Unset, None, bool] = UNSET,
    with_network_occurrence: Union[Unset, None, bool] = UNSET,
    ontologies: List[str],
    care_sites: Union[Unset, None, List[str]] = UNSET,
    domains: Union[Unset, None, List[str]] = UNSET,
    favorite: Union[Unset, None, bool] = UNSET,
    simplify_outputs: Union[Unset, None, bool] = UNSET,
) -> Response[Union[Error, List["GetOntologySearchResponse200Item"]]]:
    """Search ontologies with a search term

    Args:
        page (Union[Unset, None, int]):  Default: 1.
        per_page (Union[Unset, None, int]):  Default: 20.
        sort_by (Union[Unset, None, GetOntologySearchSortBy]):
        order (Union[Unset, None, GetOntologySearchOrder]):
        query (str):
        with_occurrence (Union[Unset, None, bool]):
        with_network_occurrence (Union[Unset, None, bool]):
        ontologies (List[str]):
        care_sites (Union[Unset, None, List[str]]):
        domains (Union[Unset, None, List[str]]):
        favorite (Union[Unset, None, bool]):
        simplify_outputs (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, List['GetOntologySearchResponse200Item']]]
    """

    kwargs = _get_kwargs(
        client=client,
        page=page,
        per_page=per_page,
        sort_by=sort_by,
        order=order,
        query=query,
        with_occurrence=with_occurrence,
        with_network_occurrence=with_network_occurrence,
        ontologies=ontologies,
        care_sites=care_sites,
        domains=domains,
        favorite=favorite,
        simplify_outputs=simplify_outputs,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    page: Union[Unset, None, int] = 1,
    per_page: Union[Unset, None, int] = 20,
    sort_by: Union[Unset, None, GetOntologySearchSortBy] = UNSET,
    order: Union[Unset, None, GetOntologySearchOrder] = UNSET,
    query: str,
    with_occurrence: Union[Unset, None, bool] = UNSET,
    with_network_occurrence: Union[Unset, None, bool] = UNSET,
    ontologies: List[str],
    care_sites: Union[Unset, None, List[str]] = UNSET,
    domains: Union[Unset, None, List[str]] = UNSET,
    favorite: Union[Unset, None, bool] = UNSET,
    simplify_outputs: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[Error, List["GetOntologySearchResponse200Item"]]]:
    """Search ontologies with a search term

    Args:
        page (Union[Unset, None, int]):  Default: 1.
        per_page (Union[Unset, None, int]):  Default: 20.
        sort_by (Union[Unset, None, GetOntologySearchSortBy]):
        order (Union[Unset, None, GetOntologySearchOrder]):
        query (str):
        with_occurrence (Union[Unset, None, bool]):
        with_network_occurrence (Union[Unset, None, bool]):
        ontologies (List[str]):
        care_sites (Union[Unset, None, List[str]]):
        domains (Union[Unset, None, List[str]]):
        favorite (Union[Unset, None, bool]):
        simplify_outputs (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, List['GetOntologySearchResponse200Item']]]
    """

    return sync_detailed(
        client=client,
        page=page,
        per_page=per_page,
        sort_by=sort_by,
        order=order,
        query=query,
        with_occurrence=with_occurrence,
        with_network_occurrence=with_network_occurrence,
        ontologies=ontologies,
        care_sites=care_sites,
        domains=domains,
        favorite=favorite,
        simplify_outputs=simplify_outputs,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    page: Union[Unset, None, int] = 1,
    per_page: Union[Unset, None, int] = 20,
    sort_by: Union[Unset, None, GetOntologySearchSortBy] = UNSET,
    order: Union[Unset, None, GetOntologySearchOrder] = UNSET,
    query: str,
    with_occurrence: Union[Unset, None, bool] = UNSET,
    with_network_occurrence: Union[Unset, None, bool] = UNSET,
    ontologies: List[str],
    care_sites: Union[Unset, None, List[str]] = UNSET,
    domains: Union[Unset, None, List[str]] = UNSET,
    favorite: Union[Unset, None, bool] = UNSET,
    simplify_outputs: Union[Unset, None, bool] = UNSET,
) -> Response[Union[Error, List["GetOntologySearchResponse200Item"]]]:
    """Search ontologies with a search term

    Args:
        page (Union[Unset, None, int]):  Default: 1.
        per_page (Union[Unset, None, int]):  Default: 20.
        sort_by (Union[Unset, None, GetOntologySearchSortBy]):
        order (Union[Unset, None, GetOntologySearchOrder]):
        query (str):
        with_occurrence (Union[Unset, None, bool]):
        with_network_occurrence (Union[Unset, None, bool]):
        ontologies (List[str]):
        care_sites (Union[Unset, None, List[str]]):
        domains (Union[Unset, None, List[str]]):
        favorite (Union[Unset, None, bool]):
        simplify_outputs (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, List['GetOntologySearchResponse200Item']]]
    """

    kwargs = _get_kwargs(
        client=client,
        page=page,
        per_page=per_page,
        sort_by=sort_by,
        order=order,
        query=query,
        with_occurrence=with_occurrence,
        with_network_occurrence=with_network_occurrence,
        ontologies=ontologies,
        care_sites=care_sites,
        domains=domains,
        favorite=favorite,
        simplify_outputs=simplify_outputs,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    page: Union[Unset, None, int] = 1,
    per_page: Union[Unset, None, int] = 20,
    sort_by: Union[Unset, None, GetOntologySearchSortBy] = UNSET,
    order: Union[Unset, None, GetOntologySearchOrder] = UNSET,
    query: str,
    with_occurrence: Union[Unset, None, bool] = UNSET,
    with_network_occurrence: Union[Unset, None, bool] = UNSET,
    ontologies: List[str],
    care_sites: Union[Unset, None, List[str]] = UNSET,
    domains: Union[Unset, None, List[str]] = UNSET,
    favorite: Union[Unset, None, bool] = UNSET,
    simplify_outputs: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[Error, List["GetOntologySearchResponse200Item"]]]:
    """Search ontologies with a search term

    Args:
        page (Union[Unset, None, int]):  Default: 1.
        per_page (Union[Unset, None, int]):  Default: 20.
        sort_by (Union[Unset, None, GetOntologySearchSortBy]):
        order (Union[Unset, None, GetOntologySearchOrder]):
        query (str):
        with_occurrence (Union[Unset, None, bool]):
        with_network_occurrence (Union[Unset, None, bool]):
        ontologies (List[str]):
        care_sites (Union[Unset, None, List[str]]):
        domains (Union[Unset, None, List[str]]):
        favorite (Union[Unset, None, bool]):
        simplify_outputs (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, List['GetOntologySearchResponse200Item']]]
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            per_page=per_page,
            sort_by=sort_by,
            order=order,
            query=query,
            with_occurrence=with_occurrence,
            with_network_occurrence=with_network_occurrence,
            ontologies=ontologies,
            care_sites=care_sites,
            domains=domains,
            favorite=favorite,
            simplify_outputs=simplify_outputs,
        )
    ).parsed
