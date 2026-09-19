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
    search_key: str | Unset = UNSET,
    filters_vpn_type: str | Unset = UNSET,
    sorts_wans: str | Unset = UNSET,
    page: int,
    page_size: int,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["searchKey"] = search_key

    params["filters.vpnType"] = filters_vpn_type

    params["sorts.wans"] = sorts_wans

    params["page"] = page

    params["pageSize"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/openapi/v2/{omadac_id}/sites/{site_id}/vpn/client-to-site-vpn-servers".format(
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
    search_key: str | Unset = UNSET,
    filters_vpn_type: str | Unset = UNSET,
    sorts_wans: str | Unset = UNSET,
    page: int,
    page_size: int,
) -> Response[Any]:
    """Get VPN Server summary list

     Get VPN Server summary list.<br/><br/>The interface requires one of the permissions: <br/>Site
    Settings Manager View Only<br/>Network Config Page View Only

    Args:
        omadac_id (str):
        site_id (str):
        search_key (str | Unset):
        filters_vpn_type (str | Unset):
        sorts_wans (str | Unset):
        page (int):
        page_size (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        search_key=search_key,
        filters_vpn_type=filters_vpn_type,
        sorts_wans=sorts_wans,
        page=page,
        page_size=page_size,
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
    search_key: str | Unset = UNSET,
    filters_vpn_type: str | Unset = UNSET,
    sorts_wans: str | Unset = UNSET,
    page: int,
    page_size: int,
) -> Response[Any]:
    """Get VPN Server summary list

     Get VPN Server summary list.<br/><br/>The interface requires one of the permissions: <br/>Site
    Settings Manager View Only<br/>Network Config Page View Only

    Args:
        omadac_id (str):
        site_id (str):
        search_key (str | Unset):
        filters_vpn_type (str | Unset):
        sorts_wans (str | Unset):
        page (int):
        page_size (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        search_key=search_key,
        filters_vpn_type=filters_vpn_type,
        sorts_wans=sorts_wans,
        page=page,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
