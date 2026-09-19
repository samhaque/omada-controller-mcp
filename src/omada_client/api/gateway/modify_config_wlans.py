from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.osg_config_wlans_open_api_vo import OsgConfigWlansOpenApiVO
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    site_id: str,
    gateway_mac: str,
    *,
    body: OsgConfigWlansOpenApiVO,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/openapi/v1/{omadac_id}/sites/{site_id}/gateways/{gateway_mac}/config/wlans".format(
            omadac_id=quote(str(omadac_id), safe=""),
            site_id=quote(str(site_id), safe=""),
            gateway_mac=quote(str(gateway_mac), safe=""),
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
    gateway_mac: str,
    *,
    client: AuthenticatedClient | Client,
    body: OsgConfigWlansOpenApiVO,
) -> Response[Any]:
    """Modify gateway wlans config

     Modify gateway wlans config<br/><br/>The interface requires one of the permissions: <br/>Site Device
    Manager Modify<br/><br/>The possible error code for the interface in the returned body is one of the
    following error codes (non generic error codes): <br/>-33221  -  The SSID to be edited does not
    exist.<br/>-33222  -  The SSID should contain 1-32 characters.<br/>-33223  -  The security key can
    only contain 8-63 printable ASCII characters or 8-63 hexadecimal digits.<br/>-33231  -  The ssid' s
    name should not be the same with emergency ssid.<br/>-33242  -  This SSID VLAN ID cannot be same as
    the exist default LanNetwork profile.<br/>-33807  -  Invalid VLAN ID. Enter a number from 1 to
    4094.<br/>-39093  -  The length of the device name exceeds the limit.<br/>-39306  -  This WLAN group
    does not exist.<br/>-39307  -  Failed to add this AP to the WLAN group because this AP is not in the
    site of the WLAN group.<br/>-39350  -  The SSID of the AP group is used in Gateway ACL. Please
    delete the related ACL rule first.<br/>-39501  -  This gateway does not exist.<br/>-44405  -  The
    configuration has been overridden.

    Args:
        omadac_id (str):
        site_id (str):
        gateway_mac (str):
        body (OsgConfigWlansOpenApiVO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        gateway_mac=gateway_mac,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    omadac_id: str,
    site_id: str,
    gateway_mac: str,
    *,
    client: AuthenticatedClient | Client,
    body: OsgConfigWlansOpenApiVO,
) -> Response[Any]:
    """Modify gateway wlans config

     Modify gateway wlans config<br/><br/>The interface requires one of the permissions: <br/>Site Device
    Manager Modify<br/><br/>The possible error code for the interface in the returned body is one of the
    following error codes (non generic error codes): <br/>-33221  -  The SSID to be edited does not
    exist.<br/>-33222  -  The SSID should contain 1-32 characters.<br/>-33223  -  The security key can
    only contain 8-63 printable ASCII characters or 8-63 hexadecimal digits.<br/>-33231  -  The ssid' s
    name should not be the same with emergency ssid.<br/>-33242  -  This SSID VLAN ID cannot be same as
    the exist default LanNetwork profile.<br/>-33807  -  Invalid VLAN ID. Enter a number from 1 to
    4094.<br/>-39093  -  The length of the device name exceeds the limit.<br/>-39306  -  This WLAN group
    does not exist.<br/>-39307  -  Failed to add this AP to the WLAN group because this AP is not in the
    site of the WLAN group.<br/>-39350  -  The SSID of the AP group is used in Gateway ACL. Please
    delete the related ACL rule first.<br/>-39501  -  This gateway does not exist.<br/>-44405  -  The
    configuration has been overridden.

    Args:
        omadac_id (str):
        site_id (str):
        gateway_mac (str):
        body (OsgConfigWlansOpenApiVO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        gateway_mac=gateway_mac,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
