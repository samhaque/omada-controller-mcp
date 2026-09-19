from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.vpn_user_request import VpnUserRequest
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    site_id: str,
    user_id: str,
    *,
    body: VpnUserRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/openapi/v2/{omadac_id}/sites/{site_id}/vpn/users/{user_id}".format(
            omadac_id=quote(str(omadac_id), safe=""),
            site_id=quote(str(site_id), safe=""),
            user_id=quote(str(user_id), safe=""),
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
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: VpnUserRequest,
) -> Response[Any]:
    """Modify VPN user V2

     Modify VPN user. This interface has been deprecated. Please use the following interfaces instead:
    Modify VPN user V3. This interface had been deprecated.<br/><br/>The interface requires one of the
    permissions: <br/>Site Settings Manager View Only<br/>Network Config Page View Only<br/><br/>The
    possible error code for the interface in the returned body is one of the following error codes (non
    generic error codes): <br/>-34601  -  Invalid IP address.<br/>-34602  -  This VPN policy does not
    exist.<br/>-34609  -  This VPN user already exists. Please add a VPN user with a different
    username.<br/>-34654  -  Missing parameters.<br/>-35702  -  VPN user configuration requires VPN
    server configuration.<br/>-35716  -  The device does not support configuring local IP addresses for
    VPN users.<br/>-35717  -  This device does not support configuring OpenVPN users.<br/>-35719  -  The
    device does not support configuring VPN users.

    Args:
        omadac_id (str):
        site_id (str):
        user_id (str):
        body (VpnUserRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        user_id=user_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    omadac_id: str,
    site_id: str,
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: VpnUserRequest,
) -> Response[Any]:
    """Modify VPN user V2

     Modify VPN user. This interface has been deprecated. Please use the following interfaces instead:
    Modify VPN user V3. This interface had been deprecated.<br/><br/>The interface requires one of the
    permissions: <br/>Site Settings Manager View Only<br/>Network Config Page View Only<br/><br/>The
    possible error code for the interface in the returned body is one of the following error codes (non
    generic error codes): <br/>-34601  -  Invalid IP address.<br/>-34602  -  This VPN policy does not
    exist.<br/>-34609  -  This VPN user already exists. Please add a VPN user with a different
    username.<br/>-34654  -  Missing parameters.<br/>-35702  -  VPN user configuration requires VPN
    server configuration.<br/>-35716  -  The device does not support configuring local IP addresses for
    VPN users.<br/>-35717  -  This device does not support configuring OpenVPN users.<br/>-35719  -  The
    device does not support configuring VPN users.

    Args:
        omadac_id (str):
        site_id (str):
        user_id (str):
        body (VpnUserRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        user_id=user_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
