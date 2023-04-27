from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.aggregated_dataset_length import AggregatedDatasetLength
from ...models.bootstrap import Bootstrap
from ...models.collective_key_gen import CollectiveKeyGen
from ...models.collective_key_switch import CollectiveKeySwitch
from ...models.computation import Computation
from ...models.compute_response_403 import ComputeResponse403
from ...models.dataset_statistics import DatasetStatistics
from ...models.distributed_join import DistributedJoin
from ...models.dummy import Dummy
from ...models.encrypted_aggregation import EncryptedAggregation
from ...models.encrypted_prediction import EncryptedPrediction
from ...models.encrypted_regression import EncryptedRegression
from ...models.gwas import GWAS
from ...models.hybrid_fl import HybridFL
from ...models.key_switched_computation import KeySwitchedComputation
from ...models.private_search import PrivateSearch
from ...models.relin_key_gen import RelinKeyGen
from ...models.rot_key_gen import RotKeyGen
from ...models.sample_extraction import SampleExtraction
from ...models.set_intersection import SetIntersection
from ...models.setup_session import SetupSession
from ...models.statistical_aggregation import StatisticalAggregation
from ...models.survival_aggregation import SurvivalAggregation
from ...models.v_binned_aggregation import VBinnedAggregation
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: Union[
        "AggregatedDatasetLength",
        "Bootstrap",
        "CollectiveKeyGen",
        "CollectiveKeySwitch",
        "DatasetStatistics",
        "DistributedJoin",
        "Dummy",
        "EncryptedAggregation",
        "EncryptedPrediction",
        "EncryptedRegression",
        "GWAS",
        "HybridFL",
        "KeySwitchedComputation",
        "PrivateSearch",
        "RelinKeyGen",
        "RotKeyGen",
        "SampleExtraction",
        "SetIntersection",
        "SetupSession",
        "StatisticalAggregation",
        "SurvivalAggregation",
        "VBinnedAggregation",
    ],
) -> Dict[str, Any]:
    url = "{}/computation".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body: Dict[str, Any]

    if isinstance(json_body, Dummy):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, CollectiveKeyGen):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, RelinKeyGen):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, RotKeyGen):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, Bootstrap):
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

    elif isinstance(json_body, KeySwitchedComputation):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, VBinnedAggregation):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, StatisticalAggregation):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, SetupSession):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, DistributedJoin):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, SampleExtraction):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, GWAS):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, SurvivalAggregation):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, HybridFL):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, DatasetStatistics):
        json_json_body = json_body.to_dict()

    else:
        json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Computation, ComputeResponse403, str]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = Computation.from_dict(response.json())

        return response_201
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(str, response.json())
        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = ComputeResponse403.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = cast(str, response.json())
        return response_422
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = cast(str, response.json())
        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[Computation, ComputeResponse403, str]]:
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
        "Bootstrap",
        "CollectiveKeyGen",
        "CollectiveKeySwitch",
        "DatasetStatistics",
        "DistributedJoin",
        "Dummy",
        "EncryptedAggregation",
        "EncryptedPrediction",
        "EncryptedRegression",
        "GWAS",
        "HybridFL",
        "KeySwitchedComputation",
        "PrivateSearch",
        "RelinKeyGen",
        "RotKeyGen",
        "SampleExtraction",
        "SetIntersection",
        "SetupSession",
        "StatisticalAggregation",
        "SurvivalAggregation",
        "VBinnedAggregation",
    ],
) -> Response[Union[Computation, ComputeResponse403, str]]:
    """Request a computation.

    Args:
        json_body (Union['AggregatedDatasetLength', 'Bootstrap', 'CollectiveKeyGen',
            'CollectiveKeySwitch', 'DatasetStatistics', 'DistributedJoin', 'Dummy',
            'EncryptedAggregation', 'EncryptedPrediction', 'EncryptedRegression', 'GWAS', 'HybridFL',
            'KeySwitchedComputation', 'PrivateSearch', 'RelinKeyGen', 'RotKeyGen', 'SampleExtraction',
            'SetIntersection', 'SetupSession', 'StatisticalAggregation', 'SurvivalAggregation',
            'VBinnedAggregation']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Computation, ComputeResponse403, str]]
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
        "Bootstrap",
        "CollectiveKeyGen",
        "CollectiveKeySwitch",
        "DatasetStatistics",
        "DistributedJoin",
        "Dummy",
        "EncryptedAggregation",
        "EncryptedPrediction",
        "EncryptedRegression",
        "GWAS",
        "HybridFL",
        "KeySwitchedComputation",
        "PrivateSearch",
        "RelinKeyGen",
        "RotKeyGen",
        "SampleExtraction",
        "SetIntersection",
        "SetupSession",
        "StatisticalAggregation",
        "SurvivalAggregation",
        "VBinnedAggregation",
    ],
) -> Optional[Union[Computation, ComputeResponse403, str]]:
    """Request a computation.

    Args:
        json_body (Union['AggregatedDatasetLength', 'Bootstrap', 'CollectiveKeyGen',
            'CollectiveKeySwitch', 'DatasetStatistics', 'DistributedJoin', 'Dummy',
            'EncryptedAggregation', 'EncryptedPrediction', 'EncryptedRegression', 'GWAS', 'HybridFL',
            'KeySwitchedComputation', 'PrivateSearch', 'RelinKeyGen', 'RotKeyGen', 'SampleExtraction',
            'SetIntersection', 'SetupSession', 'StatisticalAggregation', 'SurvivalAggregation',
            'VBinnedAggregation']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Computation, ComputeResponse403, str]]
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
        "Bootstrap",
        "CollectiveKeyGen",
        "CollectiveKeySwitch",
        "DatasetStatistics",
        "DistributedJoin",
        "Dummy",
        "EncryptedAggregation",
        "EncryptedPrediction",
        "EncryptedRegression",
        "GWAS",
        "HybridFL",
        "KeySwitchedComputation",
        "PrivateSearch",
        "RelinKeyGen",
        "RotKeyGen",
        "SampleExtraction",
        "SetIntersection",
        "SetupSession",
        "StatisticalAggregation",
        "SurvivalAggregation",
        "VBinnedAggregation",
    ],
) -> Response[Union[Computation, ComputeResponse403, str]]:
    """Request a computation.

    Args:
        json_body (Union['AggregatedDatasetLength', 'Bootstrap', 'CollectiveKeyGen',
            'CollectiveKeySwitch', 'DatasetStatistics', 'DistributedJoin', 'Dummy',
            'EncryptedAggregation', 'EncryptedPrediction', 'EncryptedRegression', 'GWAS', 'HybridFL',
            'KeySwitchedComputation', 'PrivateSearch', 'RelinKeyGen', 'RotKeyGen', 'SampleExtraction',
            'SetIntersection', 'SetupSession', 'StatisticalAggregation', 'SurvivalAggregation',
            'VBinnedAggregation']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Computation, ComputeResponse403, str]]
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
        "Bootstrap",
        "CollectiveKeyGen",
        "CollectiveKeySwitch",
        "DatasetStatistics",
        "DistributedJoin",
        "Dummy",
        "EncryptedAggregation",
        "EncryptedPrediction",
        "EncryptedRegression",
        "GWAS",
        "HybridFL",
        "KeySwitchedComputation",
        "PrivateSearch",
        "RelinKeyGen",
        "RotKeyGen",
        "SampleExtraction",
        "SetIntersection",
        "SetupSession",
        "StatisticalAggregation",
        "SurvivalAggregation",
        "VBinnedAggregation",
    ],
) -> Optional[Union[Computation, ComputeResponse403, str]]:
    """Request a computation.

    Args:
        json_body (Union['AggregatedDatasetLength', 'Bootstrap', 'CollectiveKeyGen',
            'CollectiveKeySwitch', 'DatasetStatistics', 'DistributedJoin', 'Dummy',
            'EncryptedAggregation', 'EncryptedPrediction', 'EncryptedRegression', 'GWAS', 'HybridFL',
            'KeySwitchedComputation', 'PrivateSearch', 'RelinKeyGen', 'RotKeyGen', 'SampleExtraction',
            'SetIntersection', 'SetupSession', 'StatisticalAggregation', 'SurvivalAggregation',
            'VBinnedAggregation']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Computation, ComputeResponse403, str]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
