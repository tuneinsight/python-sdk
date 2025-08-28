from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.aggregated_dataset_length import AggregatedDatasetLength
from ...models.collective_key_switch import CollectiveKeySwitch
from ...models.computation import Computation
from ...models.dataset_statistics import DatasetStatistics
from ...models.dummy import Dummy
from ...models.encrypted_aggregation import EncryptedAggregation
from ...models.encrypted_mean import EncryptedMean
from ...models.encrypted_prediction import EncryptedPrediction
from ...models.encrypted_regression import EncryptedRegression
from ...models.error import Error
from ...models.feasibility import Feasibility
from ...models.filtered_aggregation import FilteredAggregation
from ...models.gwas import GWAS
from ...models.hybrid_fl import HybridFL
from ...models.private_search import PrivateSearch
from ...models.private_search_setup import PrivateSearchSetup
from ...models.set_intersection import SetIntersection
from ...models.setup_session import SetupSession
from ...models.survival_aggregation import SurvivalAggregation
from ...models.undefined import Undefined
from ...models.v_binned_aggregation import VBinnedAggregation
from ...models.value_distribution import ValueDistribution
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: Union[
        "AggregatedDatasetLength",
        "CollectiveKeySwitch",
        "DatasetStatistics",
        "Dummy",
        "EncryptedAggregation",
        "EncryptedMean",
        "EncryptedPrediction",
        "EncryptedRegression",
        "Feasibility",
        "FilteredAggregation",
        "GWAS",
        "HybridFL",
        "PrivateSearch",
        "PrivateSearchSetup",
        "SetIntersection",
        "SetupSession",
        "SurvivalAggregation",
        "Undefined",
        "VBinnedAggregation",
        "ValueDistribution",
    ],
) -> Dict[str, Any]:
    url = "{}/computation".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body: Dict[str, Any]

    if isinstance(json_body, Dummy):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, Undefined):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, CollectiveKeySwitch):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, EncryptedAggregation):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, AggregatedDatasetLength):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, EncryptedRegression):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, EncryptedPrediction):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, SetIntersection):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, VBinnedAggregation):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, SetupSession):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, GWAS):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, SurvivalAggregation):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, HybridFL):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, DatasetStatistics):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, PrivateSearch):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, PrivateSearchSetup):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, EncryptedMean):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, Feasibility):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, FilteredAggregation):
        json_json_body = json_body.to_dict()

    else:
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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Computation, Error]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = Computation.from_dict(response.json())

        return response_201
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = Error.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = Error.from_dict(response.json())

        return response_403
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


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Computation, Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: Union[
        "AggregatedDatasetLength",
        "CollectiveKeySwitch",
        "DatasetStatistics",
        "Dummy",
        "EncryptedAggregation",
        "EncryptedMean",
        "EncryptedPrediction",
        "EncryptedRegression",
        "Feasibility",
        "FilteredAggregation",
        "GWAS",
        "HybridFL",
        "PrivateSearch",
        "PrivateSearchSetup",
        "SetIntersection",
        "SetupSession",
        "SurvivalAggregation",
        "Undefined",
        "VBinnedAggregation",
        "ValueDistribution",
    ],
) -> Response[Union[Computation, Error]]:
    """Request a computation.

    Args:
        json_body (Union['AggregatedDatasetLength', 'CollectiveKeySwitch', 'DatasetStatistics',
            'Dummy', 'EncryptedAggregation', 'EncryptedMean', 'EncryptedPrediction',
            'EncryptedRegression', 'Feasibility', 'FilteredAggregation', 'GWAS', 'HybridFL',
            'PrivateSearch', 'PrivateSearchSetup', 'SetIntersection', 'SetupSession',
            'SurvivalAggregation', 'Undefined', 'VBinnedAggregation', 'ValueDistribution']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Computation, Error]]
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
    json_body: Union[
        "AggregatedDatasetLength",
        "CollectiveKeySwitch",
        "DatasetStatistics",
        "Dummy",
        "EncryptedAggregation",
        "EncryptedMean",
        "EncryptedPrediction",
        "EncryptedRegression",
        "Feasibility",
        "FilteredAggregation",
        "GWAS",
        "HybridFL",
        "PrivateSearch",
        "PrivateSearchSetup",
        "SetIntersection",
        "SetupSession",
        "SurvivalAggregation",
        "Undefined",
        "VBinnedAggregation",
        "ValueDistribution",
    ],
) -> Optional[Union[Computation, Error]]:
    """Request a computation.

    Args:
        json_body (Union['AggregatedDatasetLength', 'CollectiveKeySwitch', 'DatasetStatistics',
            'Dummy', 'EncryptedAggregation', 'EncryptedMean', 'EncryptedPrediction',
            'EncryptedRegression', 'Feasibility', 'FilteredAggregation', 'GWAS', 'HybridFL',
            'PrivateSearch', 'PrivateSearchSetup', 'SetIntersection', 'SetupSession',
            'SurvivalAggregation', 'Undefined', 'VBinnedAggregation', 'ValueDistribution']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Computation, Error]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: Union[
        "AggregatedDatasetLength",
        "CollectiveKeySwitch",
        "DatasetStatistics",
        "Dummy",
        "EncryptedAggregation",
        "EncryptedMean",
        "EncryptedPrediction",
        "EncryptedRegression",
        "Feasibility",
        "FilteredAggregation",
        "GWAS",
        "HybridFL",
        "PrivateSearch",
        "PrivateSearchSetup",
        "SetIntersection",
        "SetupSession",
        "SurvivalAggregation",
        "Undefined",
        "VBinnedAggregation",
        "ValueDistribution",
    ],
) -> Response[Union[Computation, Error]]:
    """Request a computation.

    Args:
        json_body (Union['AggregatedDatasetLength', 'CollectiveKeySwitch', 'DatasetStatistics',
            'Dummy', 'EncryptedAggregation', 'EncryptedMean', 'EncryptedPrediction',
            'EncryptedRegression', 'Feasibility', 'FilteredAggregation', 'GWAS', 'HybridFL',
            'PrivateSearch', 'PrivateSearchSetup', 'SetIntersection', 'SetupSession',
            'SurvivalAggregation', 'Undefined', 'VBinnedAggregation', 'ValueDistribution']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Computation, Error]]
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
    json_body: Union[
        "AggregatedDatasetLength",
        "CollectiveKeySwitch",
        "DatasetStatistics",
        "Dummy",
        "EncryptedAggregation",
        "EncryptedMean",
        "EncryptedPrediction",
        "EncryptedRegression",
        "Feasibility",
        "FilteredAggregation",
        "GWAS",
        "HybridFL",
        "PrivateSearch",
        "PrivateSearchSetup",
        "SetIntersection",
        "SetupSession",
        "SurvivalAggregation",
        "Undefined",
        "VBinnedAggregation",
        "ValueDistribution",
    ],
) -> Optional[Union[Computation, Error]]:
    """Request a computation.

    Args:
        json_body (Union['AggregatedDatasetLength', 'CollectiveKeySwitch', 'DatasetStatistics',
            'Dummy', 'EncryptedAggregation', 'EncryptedMean', 'EncryptedPrediction',
            'EncryptedRegression', 'Feasibility', 'FilteredAggregation', 'GWAS', 'HybridFL',
            'PrivateSearch', 'PrivateSearchSetup', 'SetIntersection', 'SetupSession',
            'SurvivalAggregation', 'Undefined', 'VBinnedAggregation', 'ValueDistribution']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Computation, Error]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
