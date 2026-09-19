from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    msp_id: str,
    *,
    page: int,
    page_size: int,
    search_macs: str | Unset = UNSET,
    search_names: str | Unset = UNSET,
    search_models: str | Unset = UNSET,
    search_sns: str | Unset = UNSET,
    filters_tag: str | Unset = UNSET,
    filters_device_series_type: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["pageSize"] = page_size

    params["searchMacs"] = search_macs

    params["searchNames"] = search_names

    params["searchModels"] = search_models

    params["searchSns"] = search_sns

    params["filters.tag"] = filters_tag

    params["filters.deviceSeriesType"] = filters_device_series_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/openapi/v1/msp/{msp_id}/devices/known-devices".format(
            msp_id=quote(str(msp_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | None:
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    msp_id: str,
    *,
    client: AuthenticatedClient | Client,
    page: int,
    page_size: int,
    search_macs: str | Unset = UNSET,
    search_names: str | Unset = UNSET,
    search_models: str | Unset = UNSET,
    search_sns: str | Unset = UNSET,
    filters_tag: str | Unset = UNSET,
    filters_device_series_type: str | Unset = UNSET,
) -> Response[Any]:
    """Get MSP known device list

     Get MSP known device list<br/><br/>The interface requires one of the permissions: <br/>MSP Device
    Manager View Only

    Args:
        msp_id (str):
        page (int):
        page_size (int):
        search_macs (str | Unset):
        search_names (str | Unset):
        search_models (str | Unset):
        search_sns (str | Unset):
        filters_tag (str | Unset):
        filters_device_series_type (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        msp_id=msp_id,
        page=page,
        page_size=page_size,
        search_macs=search_macs,
        search_names=search_names,
        search_models=search_models,
        search_sns=search_sns,
        filters_tag=filters_tag,
        filters_device_series_type=filters_device_series_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    msp_id: str,
    *,
    client: AuthenticatedClient | Client,
    page: int,
    page_size: int,
    search_macs: str | Unset = UNSET,
    search_names: str | Unset = UNSET,
    search_models: str | Unset = UNSET,
    search_sns: str | Unset = UNSET,
    filters_tag: str | Unset = UNSET,
    filters_device_series_type: str | Unset = UNSET,
) -> Response[Any]:
    """Get MSP known device list

     Get MSP known device list<br/><br/>The interface requires one of the permissions: <br/>MSP Device
    Manager View Only

    Args:
        msp_id (str):
        page (int):
        page_size (int):
        search_macs (str | Unset):
        search_names (str | Unset):
        search_models (str | Unset):
        search_sns (str | Unset):
        filters_tag (str | Unset):
        filters_device_series_type (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        msp_id=msp_id,
        page=page,
        page_size=page_size,
        search_macs=search_macs,
        search_names=search_names,
        search_models=search_models,
        search_sns=search_sns,
        filters_tag=filters_tag,
        filters_device_series_type=filters_device_series_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
