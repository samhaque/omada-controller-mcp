from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    site_id: str,
    ap_mac: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/openapi/v1/{omadac_id}/sites/{site_id}/aps/{ap_mac}/start-rf-scan".format(
            omadac_id=quote(str(omadac_id), safe=""),
            site_id=quote(str(site_id), safe=""),
            ap_mac=quote(str(ap_mac), safe=""),
        ),
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
    ap_mac: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any]:
    """Start rf scan

     Wi-Fi connection will lost for several minutes during the scanning. Please select a spare time of
    network to start scanning. This interface has been deprecated. Please use the following interface
    instead: Start rf scan v2.<br/><br/>The interface requires one of the permissions: <br/>Site Device
    Manager Modify<br/><br/>The possible error code for the interface in the returned body is one of the
    following error codes (non generic error codes): <br/>-34800  -  No SSIDs are configured on the
    corresponding radio band.<br/>-34802  -  RF scan failed. Please turn on the radio.<br/>-34803  -
    The AP is performing WLAN optimization. Please try again later.<br/>-34808  -  This AP is not
    connected.<br/>-34809  -  This AP does not support RF Scanning.<br/>-34810  -  Mesh APs do not
    support RF Scanning.

    Args:
        omadac_id (str):
        site_id (str):
        ap_mac (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        ap_mac=ap_mac,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    omadac_id: str,
    site_id: str,
    ap_mac: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any]:
    """Start rf scan

     Wi-Fi connection will lost for several minutes during the scanning. Please select a spare time of
    network to start scanning. This interface has been deprecated. Please use the following interface
    instead: Start rf scan v2.<br/><br/>The interface requires one of the permissions: <br/>Site Device
    Manager Modify<br/><br/>The possible error code for the interface in the returned body is one of the
    following error codes (non generic error codes): <br/>-34800  -  No SSIDs are configured on the
    corresponding radio band.<br/>-34802  -  RF scan failed. Please turn on the radio.<br/>-34803  -
    The AP is performing WLAN optimization. Please try again later.<br/>-34808  -  This AP is not
    connected.<br/>-34809  -  This AP does not support RF Scanning.<br/>-34810  -  Mesh APs do not
    support RF Scanning.

    Args:
        omadac_id (str):
        site_id (str):
        ap_mac (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        ap_mac=ap_mac,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
