from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.osw_network_open_api import OswNetworkOpenApi
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    site_id: str,
    switch_mac: str,
    network_id: str,
    *,
    body: OswNetworkOpenApi,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/openapi/v1/{omadac_id}/sites/{site_id}/switches/{switch_mac}/networks/{network_id}".format(
            omadac_id=quote(str(omadac_id), safe=""),
            site_id=quote(str(site_id), safe=""),
            switch_mac=quote(str(switch_mac), safe=""),
            network_id=quote(str(network_id), safe=""),
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
    switch_mac: str,
    network_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: OswNetworkOpenApi,
) -> Response[Any]:
    """Modify switch network config.

     Modify switch network config.<br/><br/>The interface requires one of the permissions: <br/>Site
    Device Manager Modify<br/><br/>The possible error code for the interface in the returned body is one
    of the following error codes (non generic error codes): <br/>-33529  -  The network cannot be
    disabled because it has been configured as the Management VLAN.<br/>-33538  -  The number of VLAN
    Interface entries has reached the limit.<br/>-33549  -  Only one VLAN interface can be enabled for
    the switches in a LAN network whose VLAN Type is Multiple.<br/>-33555  -  The IP range you set for
    the VLAN Interface conflicts with the IP range of another VLAN Interface.<br/>-35207  -  IP address
    is null or invalid.<br/>-39700  -  Switch does not exist<br/>-39710  -  Management VLAN does not
    exist.

    Args:
        omadac_id (str):
        site_id (str):
        switch_mac (str):
        network_id (str):
        body (OswNetworkOpenApi):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        switch_mac=switch_mac,
        network_id=network_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    omadac_id: str,
    site_id: str,
    switch_mac: str,
    network_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: OswNetworkOpenApi,
) -> Response[Any]:
    """Modify switch network config.

     Modify switch network config.<br/><br/>The interface requires one of the permissions: <br/>Site
    Device Manager Modify<br/><br/>The possible error code for the interface in the returned body is one
    of the following error codes (non generic error codes): <br/>-33529  -  The network cannot be
    disabled because it has been configured as the Management VLAN.<br/>-33538  -  The number of VLAN
    Interface entries has reached the limit.<br/>-33549  -  Only one VLAN interface can be enabled for
    the switches in a LAN network whose VLAN Type is Multiple.<br/>-33555  -  The IP range you set for
    the VLAN Interface conflicts with the IP range of another VLAN Interface.<br/>-35207  -  IP address
    is null or invalid.<br/>-39700  -  Switch does not exist<br/>-39710  -  Management VLAN does not
    exist.

    Args:
        omadac_id (str):
        site_id (str):
        switch_mac (str):
        network_id (str):
        body (OswNetworkOpenApi):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        switch_mac=switch_mac,
        network_id=network_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
