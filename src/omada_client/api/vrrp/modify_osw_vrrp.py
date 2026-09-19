from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.osw_vrrp_config_open_api_vo import OswVrrpConfigOpenApiVO
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    site_id: str,
    osw_vrrp_id: str,
    *,
    body: OswVrrpConfigOpenApiVO,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/openapi/v1/{omadac_id}/sites/{site_id}/osw-vrrp/{osw_vrrp_id}".format(
            omadac_id=quote(str(omadac_id), safe=""),
            site_id=quote(str(site_id), safe=""),
            osw_vrrp_id=quote(str(osw_vrrp_id), safe=""),
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
    osw_vrrp_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: OswVrrpConfigOpenApiVO,
) -> Response[Any]:
    """Modify Switch Vrrp

     Modify Switch Vrrp.<br/><br/>The interface requires one of the permissions: <br/>Site Settings
    Manager Modify<br/>Device Config Page Modify<br/><br/>The possible error code for the interface in
    the returned body is one of the following error codes (non generic error codes): <br/>-40100  -
    This switch VRRP Name already exists.<br/>-40101  -  Virtual IP cannot be duplicated.<br/>-40102  -
    Invalid Virtual IP address.<br/>-40104  -  Virtual IP cannot be empty.<br/>-40107  -  The
    combination of VRID and VLAN interface for switch already exists<br/>-40109  -  The target VRRP does
    not exist.<br/>-40112  -  VRRP key cannot be empty when authentication type is MD5 or
    simple.<br/>-40113  -  VRRP key should be empty when authentication type is none.<br/>-40116  -  The
    IPv6 link-local address is invalid.

    Args:
        omadac_id (str):
        site_id (str):
        osw_vrrp_id (str):
        body (OswVrrpConfigOpenApiVO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        osw_vrrp_id=osw_vrrp_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    omadac_id: str,
    site_id: str,
    osw_vrrp_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: OswVrrpConfigOpenApiVO,
) -> Response[Any]:
    """Modify Switch Vrrp

     Modify Switch Vrrp.<br/><br/>The interface requires one of the permissions: <br/>Site Settings
    Manager Modify<br/>Device Config Page Modify<br/><br/>The possible error code for the interface in
    the returned body is one of the following error codes (non generic error codes): <br/>-40100  -
    This switch VRRP Name already exists.<br/>-40101  -  Virtual IP cannot be duplicated.<br/>-40102  -
    Invalid Virtual IP address.<br/>-40104  -  Virtual IP cannot be empty.<br/>-40107  -  The
    combination of VRID and VLAN interface for switch already exists<br/>-40109  -  The target VRRP does
    not exist.<br/>-40112  -  VRRP key cannot be empty when authentication type is MD5 or
    simple.<br/>-40113  -  VRRP key should be empty when authentication type is none.<br/>-40116  -  The
    IPv6 link-local address is invalid.

    Args:
        omadac_id (str):
        site_id (str):
        osw_vrrp_id (str):
        body (OswVrrpConfigOpenApiVO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        osw_vrrp_id=osw_vrrp_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
