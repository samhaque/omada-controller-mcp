from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response


def _get_kwargs(
    omadac_id: str,
    site_id: str,
    *,
    wan_ip: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["wanIp"] = wan_ip

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/openapi/v1/{omadac_id}/sites/{site_id}/vpn/ssl-vpn-server/certificate".format(
            omadac_id=quote(str(omadac_id), safe=""),
            site_id=quote(str(site_id), safe=""),
        ),
        "params": params,
    }

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
    wan_ip: str,
) -> Response[Any]:
    """Download SSL VPN certificate.

     Download SSL VPN certificate. Filename is a UTF-8 string encoded by URL Encoder. This interface has
    been deprecated. Please use the following interfaces instead: Download Open VPN or SSL VPN
    certificate.<br/><br/>The interface requires one of the permissions: <br/>Site Settings Manager View
    Only<br/>Network Config Page View Only<br/><br/>The possible error code for the interface in the
    returned body is one of the following error codes (non generic error codes): <br/>-34606  -  No
    gateway in this site.<br/>-34607  -  Failed to get the VPN certificate.<br/>-34624  -  Failed to get
    any response from the gateway.<br/>-34685  -  It takes about 5 minutes to generate the file, please
    export it later.

    Args:
        omadac_id (str):
        site_id (str):
        wan_ip (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        wan_ip=wan_ip,
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
    wan_ip: str,
) -> Response[Any]:
    """Download SSL VPN certificate.

     Download SSL VPN certificate. Filename is a UTF-8 string encoded by URL Encoder. This interface has
    been deprecated. Please use the following interfaces instead: Download Open VPN or SSL VPN
    certificate.<br/><br/>The interface requires one of the permissions: <br/>Site Settings Manager View
    Only<br/>Network Config Page View Only<br/><br/>The possible error code for the interface in the
    returned body is one of the following error codes (non generic error codes): <br/>-34606  -  No
    gateway in this site.<br/>-34607  -  Failed to get the VPN certificate.<br/>-34624  -  Failed to get
    any response from the gateway.<br/>-34685  -  It takes about 5 minutes to generate the file, please
    export it later.

    Args:
        omadac_id (str):
        site_id (str):
        wan_ip (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        wan_ip=wan_ip,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
