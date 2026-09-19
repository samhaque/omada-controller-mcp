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
    site_template_id: str,
    device_template_id: str,
    *,
    body: OsgConfigWlansOpenApiVO,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/openapi/v1/{omadac_id}/sitetemplates/{site_template_id}/gatewaytemplates/{device_template_id}/config/wlans".format(
            omadac_id=quote(str(omadac_id), safe=""),
            site_template_id=quote(str(site_template_id), safe=""),
            device_template_id=quote(str(device_template_id), safe=""),
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
    device_template_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: OsgConfigWlansOpenApiVO,
) -> Response[Any]:
    """Modify gateway template wlans config

     Modify gateway template wlans config<br/><br/>The interface requires one of the permissions:
    <br/>Global Site Template Manager Modify<br/><br/>The possible error code for the interface in the
    returned body is one of the following error codes (non generic error codes): <br/>-33221  -  The
    SSID to be edited does not exist.<br/>-33222  -  The SSID should contain 1-32 characters.<br/>-33223
    -  The security key can only contain 8-63 printable ASCII characters or 8-63 hexadecimal
    digits.<br/>-33231  -  The ssid' s name should not be the same with emergency ssid.<br/>-39306  -
    This WLAN group does not exist.<br/>-39307  -  Failed to add this AP to the WLAN group because this
    AP is not in the site of the WLAN group.<br/>-39501  -  This gateway does not exist.<br/>-44434  -
    The device template does not contain this configuration option and can not be modified.

    Args:
        omadac_id (str):
        site_template_id (str):
        device_template_id (str):
        body (OsgConfigWlansOpenApiVO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_template_id=site_template_id,
        device_template_id=device_template_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    omadac_id: str,
    site_template_id: str,
    device_template_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: OsgConfigWlansOpenApiVO,
) -> Response[Any]:
    """Modify gateway template wlans config

     Modify gateway template wlans config<br/><br/>The interface requires one of the permissions:
    <br/>Global Site Template Manager Modify<br/><br/>The possible error code for the interface in the
    returned body is one of the following error codes (non generic error codes): <br/>-33221  -  The
    SSID to be edited does not exist.<br/>-33222  -  The SSID should contain 1-32 characters.<br/>-33223
    -  The security key can only contain 8-63 printable ASCII characters or 8-63 hexadecimal
    digits.<br/>-33231  -  The ssid' s name should not be the same with emergency ssid.<br/>-39306  -
    This WLAN group does not exist.<br/>-39307  -  Failed to add this AP to the WLAN group because this
    AP is not in the site of the WLAN group.<br/>-39501  -  This gateway does not exist.<br/>-44434  -
    The device template does not contain this configuration option and can not be modified.

    Args:
        omadac_id (str):
        site_template_id (str):
        device_template_id (str):
        body (OsgConfigWlansOpenApiVO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_template_id=site_template_id,
        device_template_id=device_template_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
