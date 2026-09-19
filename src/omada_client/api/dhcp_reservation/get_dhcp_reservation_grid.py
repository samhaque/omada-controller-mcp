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
    sorts_mac: str | Unset = UNSET,
    sorts_ip: str | Unset = UNSET,
    sorts_net_name: str | Unset = UNSET,
    sorts_description: str | Unset = UNSET,
    sorts_status: str | Unset = UNSET,
    search_key: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["pageSize"] = page_size

    params["sorts.mac"] = sorts_mac

    params["sorts.ip"] = sorts_ip

    params["sorts.netName"] = sorts_net_name

    params["sorts.description"] = sorts_description

    params["sorts.status"] = sorts_status

    params["searchKey"] = search_key

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/openapi/v1/{omadac_id}/sites/{site_id}/setting/service/dhcp".format(
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
    sorts_mac: str | Unset = UNSET,
    sorts_ip: str | Unset = UNSET,
    sorts_net_name: str | Unset = UNSET,
    sorts_description: str | Unset = UNSET,
    sorts_status: str | Unset = UNSET,
    search_key: str | Unset = UNSET,
) -> Response[Any]:
    """Get DHCP reservation list

     Get DHCP reservation list of the site with the given omadacId and siteId.<br/><br/>The interface
    requires one of the permissions: <br/>Site Settings Manager View Only<br/>Network Config Page View
    Only<br/>Site Device Manager View Only<br/><br/>The possible error code for the interface in the
    returned body is one of the following error codes (non generic error codes): <br/>-33000  -  This
    site does not exist.<br/>-33004  -  Operation failed because other operations (site copying,
    restoring, template synchronizing, etc.) are being performed on this site. Please wait and try again
    later.

    Args:
        omadac_id (str):
        site_id (str):
        page (int):
        page_size (int):
        sorts_mac (str | Unset):
        sorts_ip (str | Unset):
        sorts_net_name (str | Unset):
        sorts_description (str | Unset):
        sorts_status (str | Unset):
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
        sorts_mac=sorts_mac,
        sorts_ip=sorts_ip,
        sorts_net_name=sorts_net_name,
        sorts_description=sorts_description,
        sorts_status=sorts_status,
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
    sorts_mac: str | Unset = UNSET,
    sorts_ip: str | Unset = UNSET,
    sorts_net_name: str | Unset = UNSET,
    sorts_description: str | Unset = UNSET,
    sorts_status: str | Unset = UNSET,
    search_key: str | Unset = UNSET,
) -> Response[Any]:
    """Get DHCP reservation list

     Get DHCP reservation list of the site with the given omadacId and siteId.<br/><br/>The interface
    requires one of the permissions: <br/>Site Settings Manager View Only<br/>Network Config Page View
    Only<br/>Site Device Manager View Only<br/><br/>The possible error code for the interface in the
    returned body is one of the following error codes (non generic error codes): <br/>-33000  -  This
    site does not exist.<br/>-33004  -  Operation failed because other operations (site copying,
    restoring, template synchronizing, etc.) are being performed on this site. Please wait and try again
    later.

    Args:
        omadac_id (str):
        site_id (str):
        page (int):
        page_size (int):
        sorts_mac (str | Unset):
        sorts_ip (str | Unset):
        sorts_net_name (str | Unset):
        sorts_description (str | Unset):
        sorts_status (str | Unset):
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
        sorts_mac=sorts_mac,
        sorts_ip=sorts_ip,
        sorts_net_name=sorts_net_name,
        sorts_description=sorts_description,
        sorts_status=sorts_status,
        search_key=search_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
