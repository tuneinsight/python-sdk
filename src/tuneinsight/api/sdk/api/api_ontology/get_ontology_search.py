from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.error import Error
from ...models.get_ontology_search_ontologies_item import GetOntologySearchOntologiesItem
from ...models.get_ontology_search_response_200_item import GetOntologySearchResponse200Item
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    per_page: Union[Unset, None, int] = 30,
    page: Union[Unset, None, int] = 1,
    query: str,
    with_occurrence: Union[Unset, None, bool] = UNSET,
    with_network_occurrence: Union[Unset, None, bool] = UNSET,
    ontologies: List[GetOntologySearchOntologiesItem],
) -> Dict[str, Any]:
    url = "{}/ontology-search".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["perPage"] = per_page

    params["page"] = page

    params["query"] = query

    params["withOccurrence"] = with_occurrence

    params["withNetworkOccurrence"] = with_network_occurrence

    json_ontologies = []
    for ontologies_item_data in ontologies:
        ontologies_item = ontologies_item_data.value

        json_ontologies.append(ontologies_item)

    params["ontologies[]"] = json_ontologies

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
    per_page: Union[Unset, None, int] = 30,
    page: Union[Unset, None, int] = 1,
    query: str,
    with_occurrence: Union[Unset, None, bool] = UNSET,
    with_network_occurrence: Union[Unset, None, bool] = UNSET,
    ontologies: List[GetOntologySearchOntologiesItem],
) -> Response[Union[Error, List["GetOntologySearchResponse200Item"]]]:
    """Search ontologies with a search term

    Args:
        per_page (Union[Unset, None, int]):  Default: 30.
        page (Union[Unset, None, int]):  Default: 1.
        query (str):
        with_occurrence (Union[Unset, None, bool]):
        with_network_occurrence (Union[Unset, None, bool]):
        ontologies (List[GetOntologySearchOntologiesItem]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, List['GetOntologySearchResponse200Item']]]
    """

    kwargs = _get_kwargs(
        client=client,
        per_page=per_page,
        page=page,
        query=query,
        with_occurrence=with_occurrence,
        with_network_occurrence=with_network_occurrence,
        ontologies=ontologies,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    per_page: Union[Unset, None, int] = 30,
    page: Union[Unset, None, int] = 1,
    query: str,
    with_occurrence: Union[Unset, None, bool] = UNSET,
    with_network_occurrence: Union[Unset, None, bool] = UNSET,
    ontologies: List[GetOntologySearchOntologiesItem],
) -> Optional[Union[Error, List["GetOntologySearchResponse200Item"]]]:
    """Search ontologies with a search term

    Args:
        per_page (Union[Unset, None, int]):  Default: 30.
        page (Union[Unset, None, int]):  Default: 1.
        query (str):
        with_occurrence (Union[Unset, None, bool]):
        with_network_occurrence (Union[Unset, None, bool]):
        ontologies (List[GetOntologySearchOntologiesItem]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, List['GetOntologySearchResponse200Item']]]
    """

    return sync_detailed(
        client=client,
        per_page=per_page,
        page=page,
        query=query,
        with_occurrence=with_occurrence,
        with_network_occurrence=with_network_occurrence,
        ontologies=ontologies,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    per_page: Union[Unset, None, int] = 30,
    page: Union[Unset, None, int] = 1,
    query: str,
    with_occurrence: Union[Unset, None, bool] = UNSET,
    with_network_occurrence: Union[Unset, None, bool] = UNSET,
    ontologies: List[GetOntologySearchOntologiesItem],
) -> Response[Union[Error, List["GetOntologySearchResponse200Item"]]]:
    """Search ontologies with a search term

    Args:
        per_page (Union[Unset, None, int]):  Default: 30.
        page (Union[Unset, None, int]):  Default: 1.
        query (str):
        with_occurrence (Union[Unset, None, bool]):
        with_network_occurrence (Union[Unset, None, bool]):
        ontologies (List[GetOntologySearchOntologiesItem]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, List['GetOntologySearchResponse200Item']]]
    """

    kwargs = _get_kwargs(
        client=client,
        per_page=per_page,
        page=page,
        query=query,
        with_occurrence=with_occurrence,
        with_network_occurrence=with_network_occurrence,
        ontologies=ontologies,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    per_page: Union[Unset, None, int] = 30,
    page: Union[Unset, None, int] = 1,
    query: str,
    with_occurrence: Union[Unset, None, bool] = UNSET,
    with_network_occurrence: Union[Unset, None, bool] = UNSET,
    ontologies: List[GetOntologySearchOntologiesItem],
) -> Optional[Union[Error, List["GetOntologySearchResponse200Item"]]]:
    """Search ontologies with a search term

    Args:
        per_page (Union[Unset, None, int]):  Default: 30.
        page (Union[Unset, None, int]):  Default: 1.
        query (str):
        with_occurrence (Union[Unset, None, bool]):
        with_network_occurrence (Union[Unset, None, bool]):
        ontologies (List[GetOntologySearchOntologiesItem]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, List['GetOntologySearchResponse200Item']]]
    """

    return (
        await asyncio_detailed(
            client=client,
            per_page=per_page,
            page=page,
            query=query,
            with_occurrence=with_occurrence,
            with_network_occurrence=with_network_occurrence,
            ontologies=ontologies,
        )
    ).parsed
