from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_ssid_dhcp_option_open_api_vo import UpdateSsidDhcpOptionOpenApiVO
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    site_template_id: str,
    wlan_id: str,
    ssid_id: str,
    *,
    body: UpdateSsidDhcpOptionOpenApiVO,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/openapi/v1/{omadac_id}/sitetemplates/{site_template_id}/wireless-network/wlans/{wlan_id}/ssids/{ssid_id}/update-dhcp-option".format(
            omadac_id=quote(str(omadac_id), safe=""),
            site_template_id=quote(str(site_template_id), safe=""),
            wlan_id=quote(str(wlan_id), safe=""),
            ssid_id=quote(str(ssid_id), safe=""),
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
    ssid_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateSsidDhcpOptionOpenApiVO,
) -> Response[Any]:
    """Update SSID template DHCP option 82 config

     Update SSID template DHCP option 82 config, Legacy note: “wlanId” is the legacy name of “apGroupId”.
    This endpoint will be deprecated in future releases. Please use Update SSID Template DHCP option 82
    config by site.<br/><br/>The interface requires one of the permissions: <br/>Global Site Template
    Manager Modify<br/><br/>The possible error code for the interface in the returned body is one of the
    following error codes (non generic error codes): <br/>-33009  -  This site template does not exist.

    Args:
        omadac_id (str):
        site_template_id (str):
        wlan_id (str):
        ssid_id (str):
        body (UpdateSsidDhcpOptionOpenApiVO):

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
        ssid_id=ssid_id,
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
    ssid_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateSsidDhcpOptionOpenApiVO,
) -> Response[Any]:
    """Update SSID template DHCP option 82 config

     Update SSID template DHCP option 82 config, Legacy note: “wlanId” is the legacy name of “apGroupId”.
    This endpoint will be deprecated in future releases. Please use Update SSID Template DHCP option 82
    config by site.<br/><br/>The interface requires one of the permissions: <br/>Global Site Template
    Manager Modify<br/><br/>The possible error code for the interface in the returned body is one of the
    following error codes (non generic error codes): <br/>-33009  -  This site template does not exist.

    Args:
        omadac_id (str):
        site_template_id (str):
        wlan_id (str):
        ssid_id (str):
        body (UpdateSsidDhcpOptionOpenApiVO):

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
        ssid_id=ssid_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
