from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.wan_setting_config_open_api_vo import WanSettingConfigOpenApiVO
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    site_id: str,
    *,
    body: WanSettingConfigOpenApiVO,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/openapi/v1/{omadac_id}/sites/{site_id}/internet/ports-config".format(
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
    body: WanSettingConfigOpenApiVO,
) -> Response[Any]:
    """Modify internet ports config

     Modify internet ports config. Make sure the parameter[preConfiguration] is true and all wan ports
    config is include, so the port configuration can take effect after you adopt a gateway.<br/><br/>The
    interface requires one of the permissions: <br/>Site Settings Manager Modify<br/>Network Config Page
    Modify<br/><br/>The possible error code for the interface in the returned body is one of the
    following error codes (non generic error codes): <br/>-33400  -  Current site has no WAN.<br/>-33413
    -  The IP range you set for the WAN port conflicts with the IP range of LAN networks.<br/>-33414  -
    The MAC address is not available because it has been used for another port.<br/>-33416  -  The IP
    range you set for the WAN port conflicts with the IP range of the other WAN port.<br/>-33426  -  The
    Secondary DNS cannot be the same as the Primary DNS. Please enter another IP address.<br/>-33427  -
    The IP you set for DNS Server conflicts with the IP range of the LAN network.<br/>-33429  -  There
    are duplicate IPs in the WAN alias IPs and static IPs.<br/>-33431  -  VLAN ID ranges from 1 to
    4094.<br/>-33501  -  This VLAN ID is already used by the WAN interface.<br/>-33531  -  This WAN port
    has been used by other networks.<br/>-34212  -  The WAN port is used for one-to-one NAT and can only
    use the Static IP type.

    Args:
        omadac_id (str):
        site_id (str):
        body (WanSettingConfigOpenApiVO):

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
    body: WanSettingConfigOpenApiVO,
) -> Response[Any]:
    """Modify internet ports config

     Modify internet ports config. Make sure the parameter[preConfiguration] is true and all wan ports
    config is include, so the port configuration can take effect after you adopt a gateway.<br/><br/>The
    interface requires one of the permissions: <br/>Site Settings Manager Modify<br/>Network Config Page
    Modify<br/><br/>The possible error code for the interface in the returned body is one of the
    following error codes (non generic error codes): <br/>-33400  -  Current site has no WAN.<br/>-33413
    -  The IP range you set for the WAN port conflicts with the IP range of LAN networks.<br/>-33414  -
    The MAC address is not available because it has been used for another port.<br/>-33416  -  The IP
    range you set for the WAN port conflicts with the IP range of the other WAN port.<br/>-33426  -  The
    Secondary DNS cannot be the same as the Primary DNS. Please enter another IP address.<br/>-33427  -
    The IP you set for DNS Server conflicts with the IP range of the LAN network.<br/>-33429  -  There
    are duplicate IPs in the WAN alias IPs and static IPs.<br/>-33431  -  VLAN ID ranges from 1 to
    4094.<br/>-33501  -  This VLAN ID is already used by the WAN interface.<br/>-33531  -  This WAN port
    has been used by other networks.<br/>-34212  -  The WAN port is used for one-to-one NAT and can only
    use the Static IP type.

    Args:
        omadac_id (str):
        site_id (str):
        body (WanSettingConfigOpenApiVO):

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
