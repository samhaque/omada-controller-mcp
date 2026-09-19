from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.lan_dns_open_api_vo import LanDnsOpenApiVO
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    site_id: str,
    dns_id: str,
    *,
    body: LanDnsOpenApiVO,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/openapi/v1/{omadac_id}/sites/{site_id}/setting/lan/dns/{dns_id}".format(
            omadac_id=quote(str(omadac_id), safe=""),
            site_id=quote(str(site_id), safe=""),
            dns_id=quote(str(dns_id), safe=""),
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
    dns_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: LanDnsOpenApiVO,
) -> Response[Any]:
    """Modify an existing LAN DNS rule

     Modify an existing LAN DNS rule.<br/><br/>The interface requires one of the permissions: <br/>Site
    Settings Manager Modify<br/>Network Config Page Modify<br/><br/>The possible error code for the
    interface in the returned body is one of the following error codes (non generic error codes):
    <br/>-35300  -  The LAN DNS does not exist.<br/>-35301  -  The number of LAN DNS entries has reached
    the limit.<br/>-35302  -  The configured IP addresses has reached the limit.<br/>-35305  -  IP
    address cannot be empty.<br/>-35306  -  There are duplicate IPv4 addresses.<br/>-35307  -  There are
    duplicate IPv6 addresses.<br/>-35308  -  CNAME cannot be empty.<br/>-35309  -  DNS server cannot be
    empty.<br/>-35310  -  There are duplicate DNS servers.<br/>-35311  -  Domain name and alias are
    duplicate.<br/>-35312  -  The gateway does not support LAN DNS.<br/>-35313  -  The gateway does not
    support configuring TTL in LAN DNS.

    Args:
        omadac_id (str):
        site_id (str):
        dns_id (str):
        body (LanDnsOpenApiVO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        dns_id=dns_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    omadac_id: str,
    site_id: str,
    dns_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: LanDnsOpenApiVO,
) -> Response[Any]:
    """Modify an existing LAN DNS rule

     Modify an existing LAN DNS rule.<br/><br/>The interface requires one of the permissions: <br/>Site
    Settings Manager Modify<br/>Network Config Page Modify<br/><br/>The possible error code for the
    interface in the returned body is one of the following error codes (non generic error codes):
    <br/>-35300  -  The LAN DNS does not exist.<br/>-35301  -  The number of LAN DNS entries has reached
    the limit.<br/>-35302  -  The configured IP addresses has reached the limit.<br/>-35305  -  IP
    address cannot be empty.<br/>-35306  -  There are duplicate IPv4 addresses.<br/>-35307  -  There are
    duplicate IPv6 addresses.<br/>-35308  -  CNAME cannot be empty.<br/>-35309  -  DNS server cannot be
    empty.<br/>-35310  -  There are duplicate DNS servers.<br/>-35311  -  Domain name and alias are
    duplicate.<br/>-35312  -  The gateway does not support LAN DNS.<br/>-35313  -  The gateway does not
    support configuring TTL in LAN DNS.

    Args:
        omadac_id (str):
        site_id (str):
        dns_id (str):
        body (LanDnsOpenApiVO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        dns_id=dns_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
