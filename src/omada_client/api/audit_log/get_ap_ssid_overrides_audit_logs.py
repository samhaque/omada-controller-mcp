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
    ap_mac: str,
    *,
    page: int,
    page_size: int,
    sorts_time: str | Unset = UNSET,
    filters_times: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["pageSize"] = page_size

    params["sorts.time"] = sorts_time

    params["filters.times"] = filters_times

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/openapi/v1/{omadac_id}/sites/{site_id}/audit-logs/{ap_mac}/ssid-overrides".format(
            omadac_id=quote(str(omadac_id), safe=""),
            site_id=quote(str(site_id), safe=""),
            ap_mac=quote(str(ap_mac), safe=""),
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
    ap_mac: str,
    *,
    client: AuthenticatedClient | Client,
    page: int,
    page_size: int,
    sorts_time: str | Unset = UNSET,
    filters_times: str | Unset = UNSET,
) -> Response[Any]:
    """Get ap ssidoverride audit log list

     Get ap ssidoverride audit logs in site audit page.<br/><br/>The interface requires one of the
    permissions: <br/>Site Log & Audit Log Manager View Only

    Args:
        omadac_id (str):
        site_id (str):
        ap_mac (str):
        page (int):
        page_size (int):
        sorts_time (str | Unset):
        filters_times (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        ap_mac=ap_mac,
        page=page,
        page_size=page_size,
        sorts_time=sorts_time,
        filters_times=filters_times,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    omadac_id: str,
    site_id: str,
    ap_mac: str,
    *,
    client: AuthenticatedClient | Client,
    page: int,
    page_size: int,
    sorts_time: str | Unset = UNSET,
    filters_times: str | Unset = UNSET,
) -> Response[Any]:
    """Get ap ssidoverride audit log list

     Get ap ssidoverride audit logs in site audit page.<br/><br/>The interface requires one of the
    permissions: <br/>Site Log & Audit Log Manager View Only

    Args:
        omadac_id (str):
        site_id (str):
        ap_mac (str):
        page (int):
        page_size (int):
        sorts_time (str | Unset):
        filters_times (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        ap_mac=ap_mac,
        page=page,
        page_size=page_size,
        sorts_time=sorts_time,
        filters_times=filters_times,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
