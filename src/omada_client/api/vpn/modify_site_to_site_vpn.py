from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.site_to_site_vpn import SiteToSiteVpn
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    site_id: str,
    vpn_id: str,
    *,
    body: SiteToSiteVpn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/openapi/v1/{omadac_id}/sites/{site_id}/vpn/site-to-site-vpns/{vpn_id}".format(
            omadac_id=quote(str(omadac_id), safe=""),
            site_id=quote(str(site_id), safe=""),
            vpn_id=quote(str(vpn_id), safe=""),
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
    vpn_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SiteToSiteVpn,
) -> Response[Any]:
    """Modify site-to-site VPN

     Modify site-to-site VPN. This interface has been deprecated. Please use the following interfaces
    instead: Modify site-to-site VPN by auto or Modify site-to-site VPN by manual.<br/><br/>The
    interface requires one of the permissions: <br/>Site Settings Manager Modify<br/>Network Config Page
    Modify<br/><br/>The possible error code for the interface in the returned body is one of the
    following error codes (non generic error codes): <br/>-33474  -  This feature is not supported for
    the DS-Lite or Map-E WAN connection types.

    Args:
        omadac_id (str):
        site_id (str):
        vpn_id (str):
        body (SiteToSiteVpn):

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
        body=body,
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
    body: SiteToSiteVpn,
) -> Response[Any]:
    """Modify site-to-site VPN

     Modify site-to-site VPN. This interface has been deprecated. Please use the following interfaces
    instead: Modify site-to-site VPN by auto or Modify site-to-site VPN by manual.<br/><br/>The
    interface requires one of the permissions: <br/>Site Settings Manager Modify<br/>Network Config Page
    Modify<br/><br/>The possible error code for the interface in the returned body is one of the
    following error codes (non generic error codes): <br/>-33474  -  This feature is not supported for
    the DS-Lite or Map-E WAN connection types.

    Args:
        omadac_id (str):
        site_id (str):
        vpn_id (str):
        body (SiteToSiteVpn):

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
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
