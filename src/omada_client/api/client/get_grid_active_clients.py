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
    *,
    page: int,
    page_size: int,
    sorts_name: str | Unset = UNSET,
    sorts_mac: str | Unset = UNSET,
    sorts_ip: str | Unset = UNSET,
    filters_wireless: str | Unset = UNSET,
    filters_radio_id: str | Unset = UNSET,
    filters_ap_mac: str | Unset = UNSET,
    filters_switch_mac: str | Unset = UNSET,
    filters_gateway_mac: str | Unset = UNSET,
    search_key: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["pageSize"] = page_size

    params["sorts.name"] = sorts_name

    params["sorts.mac"] = sorts_mac

    params["sorts.ip"] = sorts_ip

    params["filters.wireless"] = filters_wireless

    params["filters.radioId"] = filters_radio_id

    params["filters.apMac"] = filters_ap_mac

    params["filters.switchMac"] = filters_switch_mac

    params["filters.gatewayMac"] = filters_gateway_mac

    params["searchKey"] = search_key

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/openapi/v1/{omadac_id}/sites/{site_id}/clients".format(
            omadac_id=quote(str(omadac_id), safe=""),
            site_id=quote(str(site_id), safe=""),
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
    *,
    client: AuthenticatedClient | Client,
    page: int,
    page_size: int,
    sorts_name: str | Unset = UNSET,
    sorts_mac: str | Unset = UNSET,
    sorts_ip: str | Unset = UNSET,
    filters_wireless: str | Unset = UNSET,
    filters_radio_id: str | Unset = UNSET,
    filters_ap_mac: str | Unset = UNSET,
    filters_switch_mac: str | Unset = UNSET,
    filters_gateway_mac: str | Unset = UNSET,
    search_key: str | Unset = UNSET,
) -> Response[Any]:
    """Get client list

     Get all clients.<br/><br/>The interface requires one of the permissions: <br/>Site Clients Manager
    View Only<br/>Site Device Manager View Only

    Args:
        omadac_id (str):
        site_id (str):
        page (int):
        page_size (int):
        sorts_name (str | Unset):
        sorts_mac (str | Unset):
        sorts_ip (str | Unset):
        filters_wireless (str | Unset):
        filters_radio_id (str | Unset):
        filters_ap_mac (str | Unset):
        filters_switch_mac (str | Unset):
        filters_gateway_mac (str | Unset):
        search_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        page=page,
        page_size=page_size,
        sorts_name=sorts_name,
        sorts_mac=sorts_mac,
        sorts_ip=sorts_ip,
        filters_wireless=filters_wireless,
        filters_radio_id=filters_radio_id,
        filters_ap_mac=filters_ap_mac,
        filters_switch_mac=filters_switch_mac,
        filters_gateway_mac=filters_gateway_mac,
        search_key=search_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    omadac_id: str,
    site_id: str,
    *,
    client: AuthenticatedClient | Client,
    page: int,
    page_size: int,
    sorts_name: str | Unset = UNSET,
    sorts_mac: str | Unset = UNSET,
    sorts_ip: str | Unset = UNSET,
    filters_wireless: str | Unset = UNSET,
    filters_radio_id: str | Unset = UNSET,
    filters_ap_mac: str | Unset = UNSET,
    filters_switch_mac: str | Unset = UNSET,
    filters_gateway_mac: str | Unset = UNSET,
    search_key: str | Unset = UNSET,
) -> Response[Any]:
    """Get client list

     Get all clients.<br/><br/>The interface requires one of the permissions: <br/>Site Clients Manager
    View Only<br/>Site Device Manager View Only

    Args:
        omadac_id (str):
        site_id (str):
        page (int):
        page_size (int):
        sorts_name (str | Unset):
        sorts_mac (str | Unset):
        sorts_ip (str | Unset):
        filters_wireless (str | Unset):
        filters_radio_id (str | Unset):
        filters_ap_mac (str | Unset):
        filters_switch_mac (str | Unset):
        filters_gateway_mac (str | Unset):
        search_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        page=page,
        page_size=page_size,
        sorts_name=sorts_name,
        sorts_mac=sorts_mac,
        sorts_ip=sorts_ip,
        filters_wireless=filters_wireless,
        filters_radio_id=filters_radio_id,
        filters_ap_mac=filters_ap_mac,
        filters_switch_mac=filters_switch_mac,
        filters_gateway_mac=filters_gateway_mac,
        search_key=search_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
