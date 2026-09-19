from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    site_id: str,
    vpn_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/openapi/v1/{omadac_id}/sites/{site_id}/vpn/client-to-site-vpn-clients/{vpn_id}".format(
            omadac_id=quote(str(omadac_id), safe=""),
            site_id=quote(str(site_id), safe=""),
            vpn_id=quote(str(vpn_id), safe=""),
        ),
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
    vpn_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any]:
    """Delete client-to-site VPN client

     Delete client-to-site VPN client. This interface has been deprecated. Please use the following
    interfaces instead: Delete VPN V2. This interface had been deprecated.<br/><br/>The interface
    requires one of the permissions: <br/>Site Settings Manager Modify<br/>Network Config Page
    Modify<br/><br/>The possible error code for the interface in the returned body is one of the
    following error codes (non generic error codes): <br/>-34682  -  This VPN entry has been used by
    Static Route, and thus it cannot be deleted.<br/>-34683  -  This VPN entry has been used by Policy
    Routing, and thus it cannot be deleted.<br/>-34684  -  This VPN entry has been used by Static Route
    and Policy Routing, and thus it cannot be deleted.<br/>-35706  -  This VPN entry has been used by
    Gateway ACL, and thus it cannot be deleted.

    Args:
        omadac_id (str):
        site_id (str):
        vpn_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        vpn_id=vpn_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    omadac_id: str,
    site_id: str,
    vpn_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any]:
    """Delete client-to-site VPN client

     Delete client-to-site VPN client. This interface has been deprecated. Please use the following
    interfaces instead: Delete VPN V2. This interface had been deprecated.<br/><br/>The interface
    requires one of the permissions: <br/>Site Settings Manager Modify<br/>Network Config Page
    Modify<br/><br/>The possible error code for the interface in the returned body is one of the
    following error codes (non generic error codes): <br/>-34682  -  This VPN entry has been used by
    Static Route, and thus it cannot be deleted.<br/>-34683  -  This VPN entry has been used by Policy
    Routing, and thus it cannot be deleted.<br/>-34684  -  This VPN entry has been used by Static Route
    and Policy Routing, and thus it cannot be deleted.<br/>-35706  -  This VPN entry has been used by
    Gateway ACL, and thus it cannot be deleted.

    Args:
        omadac_id (str):
        site_id (str):
        vpn_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        vpn_id=vpn_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
