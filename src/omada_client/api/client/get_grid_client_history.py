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
    client_mac: str,
    *,
    page: int,
    page_size: int,
    sorts_name: str | Unset = UNSET,
    sorts_mac: str | Unset = UNSET,
    sorts_ip: str | Unset = UNSET,
    sorts_auth_type: str | Unset = UNSET,
    sorts_ssid_or_network: str | Unset = UNSET,
    sorts_download: str | Unset = UNSET,
    sorts_upload: str | Unset = UNSET,
    sorts_status: str | Unset = UNSET,
    sorts_start: str | Unset = UNSET,
    sorts_end: str | Unset = UNSET,
    sorts_duration: str | Unset = UNSET,
    search_key: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["pageSize"] = page_size

    params["sorts.name"] = sorts_name

    params["sorts.mac"] = sorts_mac

    params["sorts.ip"] = sorts_ip

    params["sorts.authType"] = sorts_auth_type

    params["sorts.ssidOrNetwork"] = sorts_ssid_or_network

    params["sorts.download"] = sorts_download

    params["sorts.upload"] = sorts_upload

    params["sorts.status"] = sorts_status

    params["sorts.start"] = sorts_start

    params["sorts.end"] = sorts_end

    params["sorts.duration"] = sorts_duration

    params["searchKey"] = search_key

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/openapi/v1/{omadac_id}/sites/{site_id}/clients/{client_mac}/client-history".format(
            omadac_id=quote(str(omadac_id), safe=""),
            site_id=quote(str(site_id), safe=""),
            client_mac=quote(str(client_mac), safe=""),
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
    client_mac: str,
    *,
    client: AuthenticatedClient | Client,
    page: int,
    page_size: int,
    sorts_name: str | Unset = UNSET,
    sorts_mac: str | Unset = UNSET,
    sorts_ip: str | Unset = UNSET,
    sorts_auth_type: str | Unset = UNSET,
    sorts_ssid_or_network: str | Unset = UNSET,
    sorts_download: str | Unset = UNSET,
    sorts_upload: str | Unset = UNSET,
    sorts_status: str | Unset = UNSET,
    sorts_start: str | Unset = UNSET,
    sorts_end: str | Unset = UNSET,
    sorts_duration: str | Unset = UNSET,
    search_key: str | Unset = UNSET,
) -> Response[Any]:
    """Get Client history.

     Get Client history.<br/><br/>The interface requires one of the permissions: <br/>Site Clients
    Manager View Only

    Args:
        omadac_id (str):
        site_id (str):
        client_mac (str):
        page (int):
        page_size (int):
        sorts_name (str | Unset):
        sorts_mac (str | Unset):
        sorts_ip (str | Unset):
        sorts_auth_type (str | Unset):
        sorts_ssid_or_network (str | Unset):
        sorts_download (str | Unset):
        sorts_upload (str | Unset):
        sorts_status (str | Unset):
        sorts_start (str | Unset):
        sorts_end (str | Unset):
        sorts_duration (str | Unset):
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
        client_mac=client_mac,
        page=page,
        page_size=page_size,
        sorts_name=sorts_name,
        sorts_mac=sorts_mac,
        sorts_ip=sorts_ip,
        sorts_auth_type=sorts_auth_type,
        sorts_ssid_or_network=sorts_ssid_or_network,
        sorts_download=sorts_download,
        sorts_upload=sorts_upload,
        sorts_status=sorts_status,
        sorts_start=sorts_start,
        sorts_end=sorts_end,
        sorts_duration=sorts_duration,
        search_key=search_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    omadac_id: str,
    site_id: str,
    client_mac: str,
    *,
    client: AuthenticatedClient | Client,
    page: int,
    page_size: int,
    sorts_name: str | Unset = UNSET,
    sorts_mac: str | Unset = UNSET,
    sorts_ip: str | Unset = UNSET,
    sorts_auth_type: str | Unset = UNSET,
    sorts_ssid_or_network: str | Unset = UNSET,
    sorts_download: str | Unset = UNSET,
    sorts_upload: str | Unset = UNSET,
    sorts_status: str | Unset = UNSET,
    sorts_start: str | Unset = UNSET,
    sorts_end: str | Unset = UNSET,
    sorts_duration: str | Unset = UNSET,
    search_key: str | Unset = UNSET,
) -> Response[Any]:
    """Get Client history.

     Get Client history.<br/><br/>The interface requires one of the permissions: <br/>Site Clients
    Manager View Only

    Args:
        omadac_id (str):
        site_id (str):
        client_mac (str):
        page (int):
        page_size (int):
        sorts_name (str | Unset):
        sorts_mac (str | Unset):
        sorts_ip (str | Unset):
        sorts_auth_type (str | Unset):
        sorts_ssid_or_network (str | Unset):
        sorts_download (str | Unset):
        sorts_upload (str | Unset):
        sorts_status (str | Unset):
        sorts_start (str | Unset):
        sorts_end (str | Unset):
        sorts_duration (str | Unset):
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
        client_mac=client_mac,
        page=page,
        page_size=page_size,
        sorts_name=sorts_name,
        sorts_mac=sorts_mac,
        sorts_ip=sorts_ip,
        sorts_auth_type=sorts_auth_type,
        sorts_ssid_or_network=sorts_ssid_or_network,
        sorts_download=sorts_download,
        sorts_upload=sorts_upload,
        sorts_status=sorts_status,
        sorts_start=sorts_start,
        sorts_end=sorts_end,
        sorts_duration=sorts_duration,
        search_key=search_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
