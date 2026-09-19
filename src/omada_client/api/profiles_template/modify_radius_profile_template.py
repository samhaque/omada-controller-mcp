from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_radius_profile_open_api_vo import CreateRadiusProfileOpenApiVO
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    site_template_id: str,
    radius_profile_id: str,
    *,
    body: CreateRadiusProfileOpenApiVO,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/openapi/v1/{omadac_id}/sitetemplates/{site_template_id}/profiles/radius/{radius_profile_id}".format(
            omadac_id=quote(str(omadac_id), safe=""),
            site_template_id=quote(str(site_template_id), safe=""),
            radius_profile_id=quote(str(radius_profile_id), safe=""),
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
    radius_profile_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateRadiusProfileOpenApiVO,
) -> Response[Any]:
    """Modify an exist RADIUS profile template

     Modify an exist RADIUS profile template with the given params.<br/><br/>The interface requires one
    of the permissions: <br/>Global Site Template Manager Modify<br/><br/>The possible error code for
    the interface in the returned body is one of the following error codes (non generic error codes):
    <br/>-33011  -  Operation failed because other operations are being performed on this site template.
    Please wait and try again later.<br/>-34000  -  Interim Update Interval ranges from 60 to
    86400.<br/>-34002  -  Accounting port number ranges from 60 to 86400.<br/>-34003  -  Enter the
    shared secret key of the accounting server using 1-128 printable ASCII characters (including the
    space).<br/>-34004  -  This RADIUS profile already exists.<br/>-34005  -  This RADIUS profile does
    not exist.<br/>-34011  -  Invalid IP address of the RADIUS server.<br/>-34011  -  Invalid IP address
    of the RADIUS server.<br/>-34016  -  Unable to set the authentication server URL because the profile
    is applied in authentications that do not support authentication server URL.<br/>-34018  -  Failed
    to modify this RADIUS profile because it has been used in 802.1X authentication.<br/>-34022  -
    Failed to modify built-in RADIUS profile.<br/>-34027  -  The built-in server is being used, failed
    to stop built-in RADIUS server.<br/>-43006  -  The RADIUS profile cannot add more than 2 RADIUS
    servers because it is used by SSL VPN.<br/>-43012  -  The number of Accounting Servers in the RADIUS
    profile should not be greater than the number of Authentication Servers because the RADIUS profile
    is used by the SSL VPN server.

    Args:
        omadac_id (str):
        site_template_id (str):
        radius_profile_id (str):
        body (CreateRadiusProfileOpenApiVO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_template_id=site_template_id,
        radius_profile_id=radius_profile_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    omadac_id: str,
    site_template_id: str,
    radius_profile_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateRadiusProfileOpenApiVO,
) -> Response[Any]:
    """Modify an exist RADIUS profile template

     Modify an exist RADIUS profile template with the given params.<br/><br/>The interface requires one
    of the permissions: <br/>Global Site Template Manager Modify<br/><br/>The possible error code for
    the interface in the returned body is one of the following error codes (non generic error codes):
    <br/>-33011  -  Operation failed because other operations are being performed on this site template.
    Please wait and try again later.<br/>-34000  -  Interim Update Interval ranges from 60 to
    86400.<br/>-34002  -  Accounting port number ranges from 60 to 86400.<br/>-34003  -  Enter the
    shared secret key of the accounting server using 1-128 printable ASCII characters (including the
    space).<br/>-34004  -  This RADIUS profile already exists.<br/>-34005  -  This RADIUS profile does
    not exist.<br/>-34011  -  Invalid IP address of the RADIUS server.<br/>-34011  -  Invalid IP address
    of the RADIUS server.<br/>-34016  -  Unable to set the authentication server URL because the profile
    is applied in authentications that do not support authentication server URL.<br/>-34018  -  Failed
    to modify this RADIUS profile because it has been used in 802.1X authentication.<br/>-34022  -
    Failed to modify built-in RADIUS profile.<br/>-34027  -  The built-in server is being used, failed
    to stop built-in RADIUS server.<br/>-43006  -  The RADIUS profile cannot add more than 2 RADIUS
    servers because it is used by SSL VPN.<br/>-43012  -  The number of Accounting Servers in the RADIUS
    profile should not be greater than the number of Authentication Servers because the RADIUS profile
    is used by the SSL VPN server.

    Args:
        omadac_id (str):
        site_template_id (str):
        radius_profile_id (str):
        body (CreateRadiusProfileOpenApiVO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_template_id=site_template_id,
        radius_profile_id=radius_profile_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
