from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ssl_vpn_server_config_open_api_vo import SslVpnServerConfigOpenApiVO
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    site_id: str,
    *,
    body: SslVpnServerConfigOpenApiVO,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/openapi/v1/{omadac_id}/sites/{site_id}/vpn/ssl-vpn-server/setting".format(
            omadac_id=quote(str(omadac_id), safe=""),
            site_id=quote(str(site_id), safe=""),
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
    *,
    client: AuthenticatedClient | Client,
    body: SslVpnServerConfigOpenApiVO,
) -> Response[Any]:
    """Modify SSL VPN server setting

     Get SSL VPN server setting. This interface has been deprecated. Please use the following interfaces
    instead: Create client-to-site VPN server V2 or Modify client-to-site VPN server V2.<br/><br/>The
    interface requires one of the permissions: <br/>Site Settings Manager Modify<br/>Network Config Page
    Modify<br/><br/>The possible error code for the interface in the returned body is one of the
    following error codes (non generic error codes): <br/>-33474  -  This feature is not supported for
    the DS-Lite or Map-E WAN connection types.<br/>-34032  -  Built-in RADIUS server not
    started.<br/>-43008  -  The current gateway model or firmware version does not support SSL VPN
    configuration.<br/>-43008  -  The current gateway model or firmware version does not support SSL VPN
    configuration.<br/>-43010  -  The IP addresses in SSL VPN IP pool cannot overlap with other VPN IP
    pools on the same site.<br/>-43011  -  The service port cannot be the same as that of the OpenVPN
    server.<br/>-43017  -  The device does not support configuring RADIUS type.<br/>-43018  -  The
    device does not support configuring LDAP type.

    Args:
        omadac_id (str):
        site_id (str):
        body (SslVpnServerConfigOpenApiVO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        body=body,
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
    body: SslVpnServerConfigOpenApiVO,
) -> Response[Any]:
    """Modify SSL VPN server setting

     Get SSL VPN server setting. This interface has been deprecated. Please use the following interfaces
    instead: Create client-to-site VPN server V2 or Modify client-to-site VPN server V2.<br/><br/>The
    interface requires one of the permissions: <br/>Site Settings Manager Modify<br/>Network Config Page
    Modify<br/><br/>The possible error code for the interface in the returned body is one of the
    following error codes (non generic error codes): <br/>-33474  -  This feature is not supported for
    the DS-Lite or Map-E WAN connection types.<br/>-34032  -  Built-in RADIUS server not
    started.<br/>-43008  -  The current gateway model or firmware version does not support SSL VPN
    configuration.<br/>-43008  -  The current gateway model or firmware version does not support SSL VPN
    configuration.<br/>-43010  -  The IP addresses in SSL VPN IP pool cannot overlap with other VPN IP
    pools on the same site.<br/>-43011  -  The service port cannot be the same as that of the OpenVPN
    server.<br/>-43017  -  The device does not support configuring RADIUS type.<br/>-43018  -  The
    device does not support configuring LDAP type.

    Args:
        omadac_id (str):
        site_id (str):
        body (SslVpnServerConfigOpenApiVO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
