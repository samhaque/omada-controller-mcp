from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.oui_based_vlan_ap_open_api_vo import OuiBasedVlanApOpenApiVO
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    site_id: str,
    *,
    body: OuiBasedVlanApOpenApiVO,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/openapi/v1/{omadac_id}/sites/{site_id}/ap-oui-rules".format(
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
    body: OuiBasedVlanApOpenApiVO,
) -> Response[Any]:
    """Create Ap oui based vlan

     Create Ap oui based vlan.<br/><br/>The interface requires one of the permissions: <br/>Site Settings
    Manager Modify<br/>Network Config Page Modify<br/><br/>The possible error code for the interface in
    the returned body is one of the following error codes (non generic error codes): <br/>-33779  -
    This OUI profile does not exist.<br/>-33789  -  PPSK and OUI Based VLAN are mutually exclusive.
    Please make sure the SSID does not select PPSK.<br/>-34224  -  When the rule is enabled, the same
    device should not configure OUI-VLAN combination greater than 16.<br/>-34225  -  When the rule is
    enabled, the same SSID should not be configured in multiple rules.<br/>-34229  -  The OUI based VLAN
    rule name already exists.

    Args:
        omadac_id (str):
        site_id (str):
        body (OuiBasedVlanApOpenApiVO):

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
    body: OuiBasedVlanApOpenApiVO,
) -> Response[Any]:
    """Create Ap oui based vlan

     Create Ap oui based vlan.<br/><br/>The interface requires one of the permissions: <br/>Site Settings
    Manager Modify<br/>Network Config Page Modify<br/><br/>The possible error code for the interface in
    the returned body is one of the following error codes (non generic error codes): <br/>-33779  -
    This OUI profile does not exist.<br/>-33789  -  PPSK and OUI Based VLAN are mutually exclusive.
    Please make sure the SSID does not select PPSK.<br/>-34224  -  When the rule is enabled, the same
    device should not configure OUI-VLAN combination greater than 16.<br/>-34225  -  When the rule is
    enabled, the same SSID should not be configured in multiple rules.<br/>-34229  -  The OUI based VLAN
    rule name already exists.

    Args:
        omadac_id (str):
        site_id (str):
        body (OuiBasedVlanApOpenApiVO):

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
