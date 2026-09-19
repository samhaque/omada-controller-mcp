from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    omadac_id: str,
    site_id: str,
    history_id: str,
    *,
    page: int,
    page_size: int,
    filters_type: str,
    filters_radio_id: str | Unset = UNSET,
    filters_mac: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["pageSize"] = page_size

    params["filters.type"] = filters_type

    params["filters.radioId"] = filters_radio_id

    params["filters.mac"] = filters_mac

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/openapi/v1/{omadac_id}/sites/{site_id}/full-channel-detect/{history_id}/grid/wifi-interference".format(
            omadac_id=quote(str(omadac_id), safe=""),
            site_id=quote(str(site_id), safe=""),
            history_id=quote(str(history_id), safe=""),
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
    omadac_id: str,
    site_id: str,
    history_id: str,
    *,
    client: AuthenticatedClient | Client,
    page: int,
    page_size: int,
    filters_type: str,
    filters_radio_id: str | Unset = UNSET,
    filters_mac: str | Unset = UNSET,
) -> Response[Any]:
    """Get WiFi interference results of batch interference detection

     Get WiFi interference results of batch interference detection<br/><br/>The interface requires one of
    the permissions: <br/>Site Tools Manager View Only<br/><br/>The possible error code for the
    interface in the returned body is one of the following error codes (non generic error codes):
    <br/>-39050  -  This device does not exist.<br/>-39303  -  AP does not exist.

    Args:
        omadac_id (str):
        site_id (str):
        history_id (str):
        page (int):
        page_size (int):
        filters_type (str):
        filters_radio_id (str | Unset):
        filters_mac (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        history_id=history_id,
        page=page,
        page_size=page_size,
        filters_type=filters_type,
        filters_radio_id=filters_radio_id,
        filters_mac=filters_mac,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    omadac_id: str,
    site_id: str,
    history_id: str,
    *,
    client: AuthenticatedClient | Client,
    page: int,
    page_size: int,
    filters_type: str,
    filters_radio_id: str | Unset = UNSET,
    filters_mac: str | Unset = UNSET,
) -> Response[Any]:
    """Get WiFi interference results of batch interference detection

     Get WiFi interference results of batch interference detection<br/><br/>The interface requires one of
    the permissions: <br/>Site Tools Manager View Only<br/><br/>The possible error code for the
    interface in the returned body is one of the following error codes (non generic error codes):
    <br/>-39050  -  This device does not exist.<br/>-39303  -  AP does not exist.

    Args:
        omadac_id (str):
        site_id (str):
        history_id (str):
        page (int):
        page_size (int):
        filters_type (str):
        filters_radio_id (str | Unset):
        filters_mac (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        history_id=history_id,
        page=page,
        page_size=page_size,
        filters_type=filters_type,
        filters_radio_id=filters_radio_id,
        filters_mac=filters_mac,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
