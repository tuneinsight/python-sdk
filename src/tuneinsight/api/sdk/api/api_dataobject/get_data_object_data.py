from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.ciphertable import Ciphertable
from ...models.float_matrix import FloatMatrix
from ...models.get_data_object_data_response_403 import GetDataObjectDataResponse403
from ...models.prediction import Prediction
from ...models.statistics import Statistics
from ...models.string_matrix import StringMatrix
from ...types import Response


def _get_kwargs(
    data_object_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/dataobjects/{dataObjectId}/data".format(client.base_url, dataObjectId=data_object_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[
    Union[GetDataObjectDataResponse403, Union[Ciphertable, FloatMatrix, Prediction, Statistics, StringMatrix], str]
]:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> Union[Ciphertable, FloatMatrix, Prediction, Statistics, StringMatrix]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = FloatMatrix.from_dict(data)

                return response_200_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_1 = StringMatrix.from_dict(data)

                return response_200_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_2 = Ciphertable.from_dict(data)

                return response_200_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_3 = Prediction.from_dict(data)

                return response_200_type_3
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_4 = Statistics.from_dict(data)

            return response_200_type_4

        response_200 = _parse_response_200(response.json())

        return response_200
    if response.status_code == 403:
        response_403 = GetDataObjectDataResponse403.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = cast(str, response.json())
        return response_404
    if response.status_code == 500:
        response_500 = cast(str, response.json())
        return response_500
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[
    Union[GetDataObjectDataResponse403, Union[Ciphertable, FloatMatrix, Prediction, Statistics, StringMatrix], str]
]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    data_object_id: str,
    *,
    client: Client,
) -> Response[
    Union[GetDataObjectDataResponse403, Union[Ciphertable, FloatMatrix, Prediction, Statistics, StringMatrix], str]
]:
    """Get the content of a data object.

    Args:
        data_object_id (str):

    Returns:
        Response[Union[GetDataObjectDataResponse403, Union[Ciphertable, FloatMatrix, Prediction, Statistics, StringMatrix], str]]
    """

    kwargs = _get_kwargs(
        data_object_id=data_object_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    data_object_id: str,
    *,
    client: Client,
) -> Optional[
    Union[GetDataObjectDataResponse403, Union[Ciphertable, FloatMatrix, Prediction, Statistics, StringMatrix], str]
]:
    """Get the content of a data object.

    Args:
        data_object_id (str):

    Returns:
        Response[Union[GetDataObjectDataResponse403, Union[Ciphertable, FloatMatrix, Prediction, Statistics, StringMatrix], str]]
    """

    return sync_detailed(
        data_object_id=data_object_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    data_object_id: str,
    *,
    client: Client,
) -> Response[
    Union[GetDataObjectDataResponse403, Union[Ciphertable, FloatMatrix, Prediction, Statistics, StringMatrix], str]
]:
    """Get the content of a data object.

    Args:
        data_object_id (str):

    Returns:
        Response[Union[GetDataObjectDataResponse403, Union[Ciphertable, FloatMatrix, Prediction, Statistics, StringMatrix], str]]
    """

    kwargs = _get_kwargs(
        data_object_id=data_object_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    data_object_id: str,
    *,
    client: Client,
) -> Optional[
    Union[GetDataObjectDataResponse403, Union[Ciphertable, FloatMatrix, Prediction, Statistics, StringMatrix], str]
]:
    """Get the content of a data object.

    Args:
        data_object_id (str):

    Returns:
        Response[Union[GetDataObjectDataResponse403, Union[Ciphertable, FloatMatrix, Prediction, Statistics, StringMatrix], str]]
    """

    return (
        await asyncio_detailed(
            data_object_id=data_object_id,
            client=client,
        )
    ).parsed
