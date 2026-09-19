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
    top_k: int | Unset = UNSET,
    query_top_ssid: bool,
    query_top_epdg: bool,
    query_clients: bool,
    query_clients_by_mac: bool,
    page: int,
    page_size: int,
    sorts_ap_name: str | Unset = UNSET,
    sorts_carrier_name: str | Unset = UNSET,
    sorts_wifi_calling_profile_name: str | Unset = UNSET,
    sorts_client_name: str | Unset = UNSET,
    sorts_ip: str | Unset = UNSET,
    sorts_domain: str | Unset = UNSET,
    sorts_traffic_down: str | Unset = UNSET,
    sorts_traffic_up: str | Unset = UNSET,
    sorts_total_traffic: str | Unset = UNSET,
    sorts_client_mac: str | Unset = UNSET,
    sorts_priority: str | Unset = UNSET,
    sorts_ssid: str | Unset = UNSET,
    sorts_start_time: str | Unset = UNSET,
    sorts_end_time: str | Unset = UNSET,
    filters_time_start: int,
    filters_time_end: int,
    search_key: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["topK"] = top_k

    params["queryTopSsid"] = query_top_ssid

    params["queryTopEPDG"] = query_top_epdg

    params["queryClients"] = query_clients

    params["queryClientsByMac"] = query_clients_by_mac

    params["page"] = page

    params["pageSize"] = page_size

    params["sorts.apName"] = sorts_ap_name

    params["sorts.carrierName"] = sorts_carrier_name

    params["sorts.wifiCallingProfileName"] = sorts_wifi_calling_profile_name

    params["sorts.clientName"] = sorts_client_name

    params["sorts.ip"] = sorts_ip

    params["sorts.domain"] = sorts_domain

    params["sorts.trafficDown"] = sorts_traffic_down

    params["sorts.trafficUp"] = sorts_traffic_up

    params["sorts.totalTraffic"] = sorts_total_traffic

    params["sorts.clientMac"] = sorts_client_mac

    params["sorts.priority"] = sorts_priority

    params["sorts.ssid"] = sorts_ssid

    params["sorts.startTime"] = sorts_start_time

    params["sorts.endTime"] = sorts_end_time

    params["filters.timeStart"] = filters_time_start

    params["filters.timeEnd"] = filters_time_end

    params["searchKey"] = search_key

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/openapi/v1/{omadac_id}/sites/{site_id}/profiles/wifi-calling/grid/summary".format(
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
    top_k: int | Unset = UNSET,
    query_top_ssid: bool,
    query_top_epdg: bool,
    query_clients: bool,
    query_clients_by_mac: bool,
    page: int,
    page_size: int,
    sorts_ap_name: str | Unset = UNSET,
    sorts_carrier_name: str | Unset = UNSET,
    sorts_wifi_calling_profile_name: str | Unset = UNSET,
    sorts_client_name: str | Unset = UNSET,
    sorts_ip: str | Unset = UNSET,
    sorts_domain: str | Unset = UNSET,
    sorts_traffic_down: str | Unset = UNSET,
    sorts_traffic_up: str | Unset = UNSET,
    sorts_total_traffic: str | Unset = UNSET,
    sorts_client_mac: str | Unset = UNSET,
    sorts_priority: str | Unset = UNSET,
    sorts_ssid: str | Unset = UNSET,
    sorts_start_time: str | Unset = UNSET,
    sorts_end_time: str | Unset = UNSET,
    filters_time_start: int,
    filters_time_end: int,
    search_key: str | Unset = UNSET,
) -> Response[Any]:
    """Get Wi-Fi Calling Summary

     Get Wi-Fi Calling Summary.<br/><br/>The interface requires one of the permissions: <br/>Site
    Settings Manager View Only<br/>Device Config Page View Only

    Args:
        omadac_id (str):
        site_id (str):
        top_k (int | Unset):
        query_top_ssid (bool):
        query_top_epdg (bool):
        query_clients (bool):
        query_clients_by_mac (bool):
        page (int):
        page_size (int):
        sorts_ap_name (str | Unset):
        sorts_carrier_name (str | Unset):
        sorts_wifi_calling_profile_name (str | Unset):
        sorts_client_name (str | Unset):
        sorts_ip (str | Unset):
        sorts_domain (str | Unset):
        sorts_traffic_down (str | Unset):
        sorts_traffic_up (str | Unset):
        sorts_total_traffic (str | Unset):
        sorts_client_mac (str | Unset):
        sorts_priority (str | Unset):
        sorts_ssid (str | Unset):
        sorts_start_time (str | Unset):
        sorts_end_time (str | Unset):
        filters_time_start (int):
        filters_time_end (int):
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
        top_k=top_k,
        query_top_ssid=query_top_ssid,
        query_top_epdg=query_top_epdg,
        query_clients=query_clients,
        query_clients_by_mac=query_clients_by_mac,
        page=page,
        page_size=page_size,
        sorts_ap_name=sorts_ap_name,
        sorts_carrier_name=sorts_carrier_name,
        sorts_wifi_calling_profile_name=sorts_wifi_calling_profile_name,
        sorts_client_name=sorts_client_name,
        sorts_ip=sorts_ip,
        sorts_domain=sorts_domain,
        sorts_traffic_down=sorts_traffic_down,
        sorts_traffic_up=sorts_traffic_up,
        sorts_total_traffic=sorts_total_traffic,
        sorts_client_mac=sorts_client_mac,
        sorts_priority=sorts_priority,
        sorts_ssid=sorts_ssid,
        sorts_start_time=sorts_start_time,
        sorts_end_time=sorts_end_time,
        filters_time_start=filters_time_start,
        filters_time_end=filters_time_end,
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
    top_k: int | Unset = UNSET,
    query_top_ssid: bool,
    query_top_epdg: bool,
    query_clients: bool,
    query_clients_by_mac: bool,
    page: int,
    page_size: int,
    sorts_ap_name: str | Unset = UNSET,
    sorts_carrier_name: str | Unset = UNSET,
    sorts_wifi_calling_profile_name: str | Unset = UNSET,
    sorts_client_name: str | Unset = UNSET,
    sorts_ip: str | Unset = UNSET,
    sorts_domain: str | Unset = UNSET,
    sorts_traffic_down: str | Unset = UNSET,
    sorts_traffic_up: str | Unset = UNSET,
    sorts_total_traffic: str | Unset = UNSET,
    sorts_client_mac: str | Unset = UNSET,
    sorts_priority: str | Unset = UNSET,
    sorts_ssid: str | Unset = UNSET,
    sorts_start_time: str | Unset = UNSET,
    sorts_end_time: str | Unset = UNSET,
    filters_time_start: int,
    filters_time_end: int,
    search_key: str | Unset = UNSET,
) -> Response[Any]:
    """Get Wi-Fi Calling Summary

     Get Wi-Fi Calling Summary.<br/><br/>The interface requires one of the permissions: <br/>Site
    Settings Manager View Only<br/>Device Config Page View Only

    Args:
        omadac_id (str):
        site_id (str):
        top_k (int | Unset):
        query_top_ssid (bool):
        query_top_epdg (bool):
        query_clients (bool):
        query_clients_by_mac (bool):
        page (int):
        page_size (int):
        sorts_ap_name (str | Unset):
        sorts_carrier_name (str | Unset):
        sorts_wifi_calling_profile_name (str | Unset):
        sorts_client_name (str | Unset):
        sorts_ip (str | Unset):
        sorts_domain (str | Unset):
        sorts_traffic_down (str | Unset):
        sorts_traffic_up (str | Unset):
        sorts_total_traffic (str | Unset):
        sorts_client_mac (str | Unset):
        sorts_priority (str | Unset):
        sorts_ssid (str | Unset):
        sorts_start_time (str | Unset):
        sorts_end_time (str | Unset):
        filters_time_start (int):
        filters_time_end (int):
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
        top_k=top_k,
        query_top_ssid=query_top_ssid,
        query_top_epdg=query_top_epdg,
        query_clients=query_clients,
        query_clients_by_mac=query_clients_by_mac,
        page=page,
        page_size=page_size,
        sorts_ap_name=sorts_ap_name,
        sorts_carrier_name=sorts_carrier_name,
        sorts_wifi_calling_profile_name=sorts_wifi_calling_profile_name,
        sorts_client_name=sorts_client_name,
        sorts_ip=sorts_ip,
        sorts_domain=sorts_domain,
        sorts_traffic_down=sorts_traffic_down,
        sorts_traffic_up=sorts_traffic_up,
        sorts_total_traffic=sorts_total_traffic,
        sorts_client_mac=sorts_client_mac,
        sorts_priority=sorts_priority,
        sorts_ssid=sorts_ssid,
        sorts_start_time=sorts_start_time,
        sorts_end_time=sorts_end_time,
        filters_time_start=filters_time_start,
        filters_time_end=filters_time_end,
        search_key=search_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
