from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.wireguard_peer_open_api_vo import WireguardPeerOpenApiVO
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    site_id: str,
    id: str,
    *,
    body: WireguardPeerOpenApiVO,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/openapi/v1/{omadac_id}/sites/{site_id}/vpn/wireguard-peers/{id}".format(
            omadac_id=quote(str(omadac_id), safe=""),
            site_id=quote(str(site_id), safe=""),
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: WireguardPeerOpenApiVO,
) -> Response[Any]:
    """Modify an existing wireguard peer

     Modify an existing wireguard peer. This interface has been deprecated. Please use the following
    interfaces instead: Modify site-to-site VPN by manual.<br/><br/>The interface requires one of the
    permissions: <br/>Site Settings Manager Modify<br/>Network Config Page Modify<br/><br/>The possible
    error code for the interface in the returned body is one of the following error codes (non generic
    error codes): <br/>-33006  -  This name already exists in this site.<br/>-43202  -  The number of
    WireGuard peers has reached the limit.<br/>-43203  -  The WireGuard peer does not exist.<br/>-43205
    -  The public key of the WireGuard peer for the same interface already exists.<br/>-43206  -  The
    device does not support configuring domain for WireGuard peer.<br/>-43207  -  Endpoint and Endpoint
    Port need to be filled in at the same time or both left blank.<br/>-43208  -  The device does not
    support WireGuard VPN.

    Args:
        omadac_id (str):
        site_id (str):
        id (str):
        body (WireguardPeerOpenApiVO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    omadac_id: str,
    site_id: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: WireguardPeerOpenApiVO,
) -> Response[Any]:
    """Modify an existing wireguard peer

     Modify an existing wireguard peer. This interface has been deprecated. Please use the following
    interfaces instead: Modify site-to-site VPN by manual.<br/><br/>The interface requires one of the
    permissions: <br/>Site Settings Manager Modify<br/>Network Config Page Modify<br/><br/>The possible
    error code for the interface in the returned body is one of the following error codes (non generic
    error codes): <br/>-33006  -  This name already exists in this site.<br/>-43202  -  The number of
    WireGuard peers has reached the limit.<br/>-43203  -  The WireGuard peer does not exist.<br/>-43205
    -  The public key of the WireGuard peer for the same interface already exists.<br/>-43206  -  The
    device does not support configuring domain for WireGuard peer.<br/>-43207  -  Endpoint and Endpoint
    Port need to be filled in at the same time or both left blank.<br/>-43208  -  The device does not
    support WireGuard VPN.

    Args:
        omadac_id (str):
        site_id (str):
        id (str):
        body (WireguardPeerOpenApiVO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
