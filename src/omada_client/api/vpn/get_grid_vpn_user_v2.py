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
    search_key: str | Unset = UNSET,
    filters_protocol: str | Unset = UNSET,
    filters_client_mode: str | Unset = UNSET,
    sorts_max_connections: str | Unset = UNSET,
    sorts_validity: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["pageSize"] = page_size

    params["searchKey"] = search_key

    params["filters.protocol"] = filters_protocol

    params["filters.clientMode"] = filters_client_mode

    params["sorts.maxConnections"] = sorts_max_connections

    params["sorts.validity"] = sorts_validity

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/openapi/v2/{omadac_id}/sites/{site_id}/vpn/users".format(
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
    search_key: str | Unset = UNSET,
    filters_protocol: str | Unset = UNSET,
    filters_client_mode: str | Unset = UNSET,
    sorts_max_connections: str | Unset = UNSET,
    sorts_validity: str | Unset = UNSET,
) -> Response[Any]:
    """Get VPN user list V2

     Get VPN user list V2.<br/><br/>The interface requires one of the permissions: <br/>Site Settings
    Manager View Only<br/>Network Config Page View Only

    Args:
        omadac_id (str):
        site_id (str):
        page (int):
        page_size (int):
        search_key (str | Unset):
        filters_protocol (str | Unset):
        filters_client_mode (str | Unset):
        sorts_max_connections (str | Unset):
        sorts_validity (str | Unset):

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
        search_key=search_key,
        filters_protocol=filters_protocol,
        filters_client_mode=filters_client_mode,
        sorts_max_connections=sorts_max_connections,
        sorts_validity=sorts_validity,
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
    search_key: str | Unset = UNSET,
    filters_protocol: str | Unset = UNSET,
    filters_client_mode: str | Unset = UNSET,
    sorts_max_connections: str | Unset = UNSET,
    sorts_validity: str | Unset = UNSET,
) -> Response[Any]:
    """Get VPN user list V2

     Get VPN user list V2.<br/><br/>The interface requires one of the permissions: <br/>Site Settings
    Manager View Only<br/>Network Config Page View Only

    Args:
        omadac_id (str):
        site_id (str):
        page (int):
        page_size (int):
        search_key (str | Unset):
        filters_protocol (str | Unset):
        filters_client_mode (str | Unset):
        sorts_max_connections (str | Unset):
        sorts_validity (str | Unset):

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
        search_key=search_key,
        filters_protocol=filters_protocol,
        filters_client_mode=filters_client_mode,
        sorts_max_connections=sorts_max_connections,
        sorts_validity=sorts_validity,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
