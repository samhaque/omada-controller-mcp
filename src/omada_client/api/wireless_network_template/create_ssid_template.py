from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_ssid_open_api_vo import CreateSsidOpenApiVO
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    site_template_id: str,
    wlan_id: str,
    *,
    body: CreateSsidOpenApiVO,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/openapi/v1/{omadac_id}/sitetemplates/{site_template_id}/wireless-network/wlans/{wlan_id}/ssids".format(
            omadac_id=quote(str(omadac_id), safe=""),
            site_template_id=quote(str(site_template_id), safe=""),
            wlan_id=quote(str(wlan_id), safe=""),
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
    site_template_id: str,
    wlan_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateSsidOpenApiVO,
) -> Response[Any]:
    """Create new SSID template

     Create new SSID template, Legacy note: “wlanId” is the legacy name of “apGroupId”. This endpoint
    will be deprecated in future releases. Please use Create new SSID template v2.<br/><br/>The
    interface requires one of the permissions: <br/>Global Site Template Manager Modify<br/><br/>The
    possible error code for the interface in the returned body is one of the following error codes (non
    generic error codes): <br/>-33009  -  This site template does not exist.<br/>-33217  -  Invalid SSID
    security mode.<br/>-33219  -  This SSID already exists.<br/>-33220  -  Enter a different SSID to
    override the current SSID.<br/>-33231  -  The ssid' s name should not be the same with emergency
    ssid.<br/>-33240  -  The SSID name should be between 1 and 32 bytes.<br/>-33788  -  PPSK and OUI
    Based VLAN are mutually exclusive. Please make sure the SSID is not enabled in OUI Based
    VLAN.<br/>-33807  -  Invalid VLAN ID. Enter a number from 1 to 4094.<br/>-34017  -  Only the EKMS
    authentication method in PPSK with RADIUS supports domain name.

    Args:
        omadac_id (str):
        site_template_id (str):
        wlan_id (str):
        body (CreateSsidOpenApiVO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_template_id=site_template_id,
        wlan_id=wlan_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    omadac_id: str,
    site_template_id: str,
    wlan_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateSsidOpenApiVO,
) -> Response[Any]:
    """Create new SSID template

     Create new SSID template, Legacy note: “wlanId” is the legacy name of “apGroupId”. This endpoint
    will be deprecated in future releases. Please use Create new SSID template v2.<br/><br/>The
    interface requires one of the permissions: <br/>Global Site Template Manager Modify<br/><br/>The
    possible error code for the interface in the returned body is one of the following error codes (non
    generic error codes): <br/>-33009  -  This site template does not exist.<br/>-33217  -  Invalid SSID
    security mode.<br/>-33219  -  This SSID already exists.<br/>-33220  -  Enter a different SSID to
    override the current SSID.<br/>-33231  -  The ssid' s name should not be the same with emergency
    ssid.<br/>-33240  -  The SSID name should be between 1 and 32 bytes.<br/>-33788  -  PPSK and OUI
    Based VLAN are mutually exclusive. Please make sure the SSID is not enabled in OUI Based
    VLAN.<br/>-33807  -  Invalid VLAN ID. Enter a number from 1 to 4094.<br/>-34017  -  Only the EKMS
    authentication method in PPSK with RADIUS supports domain name.

    Args:
        omadac_id (str):
        site_template_id (str):
        wlan_id (str):
        body (CreateSsidOpenApiVO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_template_id=site_template_id,
        wlan_id=wlan_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
