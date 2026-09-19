from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_group_open_api_vo import CreateGroupOpenApiVO
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    site_id: str,
    *,
    body: CreateGroupOpenApiVO,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/openapi/v1/{omadac_id}/sites/{site_id}/profiles/groups".format(
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
    body: CreateGroupOpenApiVO,
) -> Response[Any]:
    """Create a new group profile

     Create a new group profile with the given params.<br/><br/>The interface requires one of the
    permissions: <br/>Site Settings Manager Modify<br/>Network Config Page Modify<br/>Site Device
    Manager Modify<br/>Device Config Page Modify<br/><br/>The possible error code for the interface in
    the returned body is one of the following error codes (non generic error codes): <br/>-33004  -
    Operation failed because other operations (site copying, restoring, template synchronizing, etc.)
    are being performed on this site. Please wait and try again later.<br/>-33702  -  This group name
    already exists.<br/>-33706  -  The number of rules has reached the limit.<br/>-33707  -  This MAC
    List already exists.<br/>-33708  -  The number of addresses has reached the limit.<br/>-33724  -
    The number of IpGroups has reached the limit.<br/>-33725  -  The number of IpPortGroups has reached
    the limit.<br/>-33726  -  The number of Ips has reached the limit of IpGroup.<br/>-33727  -  The
    number of Ips has reached the limit of IpPortGroup.<br/>-33728  -  The number of Ports has reached
    the limit of IpPortGroup.<br/>-33749  -  Duplicate MAC addresses exist in the MAC address list of
    the MAC group.<br/>-33760  -  The number of IP addresses in the IPv6 group has reached the
    limit.<br/>-33761  -  The number of IPv6 groups has reached the limit.<br/>-33765  -  The number of
    IP addresses in the IPv6 Port group has reached the limit.<br/>-33766  -  The number of Ports has
    reached the limit of Ipv6PortGroup.<br/>-33767  -  The number of IPv6 port groups has reached the
    limit.<br/>-33770  -  The number of Country groups has reached the limit.<br/>-33815  -  The number
    of domain groups has reached the limit.<br/>-33817  -  The number of domain names has reached the
    limit of domain group.<br/>-33819  -  This domain group has wrong type of domain.<br/>-33822  -
    This domain group has wrong domain or invalid format port.

    Args:
        omadac_id (str):
        site_id (str):
        body (CreateGroupOpenApiVO):

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
    body: CreateGroupOpenApiVO,
) -> Response[Any]:
    """Create a new group profile

     Create a new group profile with the given params.<br/><br/>The interface requires one of the
    permissions: <br/>Site Settings Manager Modify<br/>Network Config Page Modify<br/>Site Device
    Manager Modify<br/>Device Config Page Modify<br/><br/>The possible error code for the interface in
    the returned body is one of the following error codes (non generic error codes): <br/>-33004  -
    Operation failed because other operations (site copying, restoring, template synchronizing, etc.)
    are being performed on this site. Please wait and try again later.<br/>-33702  -  This group name
    already exists.<br/>-33706  -  The number of rules has reached the limit.<br/>-33707  -  This MAC
    List already exists.<br/>-33708  -  The number of addresses has reached the limit.<br/>-33724  -
    The number of IpGroups has reached the limit.<br/>-33725  -  The number of IpPortGroups has reached
    the limit.<br/>-33726  -  The number of Ips has reached the limit of IpGroup.<br/>-33727  -  The
    number of Ips has reached the limit of IpPortGroup.<br/>-33728  -  The number of Ports has reached
    the limit of IpPortGroup.<br/>-33749  -  Duplicate MAC addresses exist in the MAC address list of
    the MAC group.<br/>-33760  -  The number of IP addresses in the IPv6 group has reached the
    limit.<br/>-33761  -  The number of IPv6 groups has reached the limit.<br/>-33765  -  The number of
    IP addresses in the IPv6 Port group has reached the limit.<br/>-33766  -  The number of Ports has
    reached the limit of Ipv6PortGroup.<br/>-33767  -  The number of IPv6 port groups has reached the
    limit.<br/>-33770  -  The number of Country groups has reached the limit.<br/>-33815  -  The number
    of domain groups has reached the limit.<br/>-33817  -  The number of domain names has reached the
    limit of domain group.<br/>-33819  -  This domain group has wrong type of domain.<br/>-33822  -
    This domain group has wrong domain or invalid format port.

    Args:
        omadac_id (str):
        site_id (str):
        body (CreateGroupOpenApiVO):

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
