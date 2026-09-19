from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.device_move_site_open_api_vo import DeviceMoveSiteOpenApiVO
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    site_id: str,
    device_mac: str,
    *,
    body: DeviceMoveSiteOpenApiVO,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/openapi/v1/{omadac_id}/sites/{site_id}/devices/{device_mac}/site-move".format(
            omadac_id=quote(str(omadac_id), safe=""),
            site_id=quote(str(site_id), safe=""),
            device_mac=quote(str(device_mac), safe=""),
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
    device_mac: str,
    *,
    client: AuthenticatedClient | Client,
    body: DeviceMoveSiteOpenApiVO,
) -> Response[Any]:
    """Move site

     Move the device to another site. If you want to move a networked bridge AP, use the "batch move ap
    site" interface to move all APs in the bridge network at the same time.<br/><br/>The interface
    requires one of the permissions: <br/>Site Device Manager Modify<br/><br/>The possible error code
    for the interface in the returned body is one of the following error codes (non generic error
    codes): <br/>-33000  -  This site does not exist.<br/>-33421  -  The gateway model in the target
    site is different from the gateway model configured in the WAN Settings Overrides in the original
    site.<br/>-39050  -  This device does not exist.<br/>-39081  -  The device is already in the target
    site.<br/>-39094  -  The site type does not match the device series, pro site can only manage Omada
    Pro device.<br/>-39095  -  The site type does not match the device series, basic site can only
    manage Omada device.<br/>-39363  -  Cannot move the bridge AP(s). Please ensure all the APs in the
    bridge network are in movable state and move them at the same time.<br/>-39502  -  Failed to move
    the gateway. The target site already has a gateway.<br/>-44261  -  The device does not support
    cluster and can only be adopted to its own site.

    Args:
        omadac_id (str):
        site_id (str):
        device_mac (str):
        body (DeviceMoveSiteOpenApiVO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        device_mac=device_mac,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    omadac_id: str,
    site_id: str,
    device_mac: str,
    *,
    client: AuthenticatedClient | Client,
    body: DeviceMoveSiteOpenApiVO,
) -> Response[Any]:
    """Move site

     Move the device to another site. If you want to move a networked bridge AP, use the "batch move ap
    site" interface to move all APs in the bridge network at the same time.<br/><br/>The interface
    requires one of the permissions: <br/>Site Device Manager Modify<br/><br/>The possible error code
    for the interface in the returned body is one of the following error codes (non generic error
    codes): <br/>-33000  -  This site does not exist.<br/>-33421  -  The gateway model in the target
    site is different from the gateway model configured in the WAN Settings Overrides in the original
    site.<br/>-39050  -  This device does not exist.<br/>-39081  -  The device is already in the target
    site.<br/>-39094  -  The site type does not match the device series, pro site can only manage Omada
    Pro device.<br/>-39095  -  The site type does not match the device series, basic site can only
    manage Omada device.<br/>-39363  -  Cannot move the bridge AP(s). Please ensure all the APs in the
    bridge network are in movable state and move them at the same time.<br/>-39502  -  Failed to move
    the gateway. The target site already has a gateway.<br/>-44261  -  The device does not support
    cluster and can only be adopted to its own site.

    Args:
        omadac_id (str):
        site_id (str):
        device_mac (str):
        body (DeviceMoveSiteOpenApiVO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        device_mac=device_mac,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
