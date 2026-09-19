from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.speed_test_command import SpeedTestCommand
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    site_id: str,
    ap_mac: str,
    *,
    body: SpeedTestCommand,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/openapi/v1/{omadac_id}/sites/{site_id}/aps/{ap_mac}/start-speed-test".format(
            omadac_id=quote(str(omadac_id), safe=""),
            site_id=quote(str(site_id), safe=""),
            ap_mac=quote(str(ap_mac), safe=""),
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
    ap_mac: str,
    *,
    client: AuthenticatedClient | Client,
    body: SpeedTestCommand,
) -> Response[Any]:
    """Start speed test

     The speed test is initiated by device [apMac]. Different MAC addresses indicates a different speed
    test.(Only for P2P device)<br/><br/>The interface requires one of the permissions: <br/>Site Device
    Manager Modify<br/><br/>The possible error code for the interface in the returned body is one of the
    following error codes (non generic error codes): <br/>-34817  -  Failed to start speedTest, the Main
    AP is not in CONNECTED, The device connection is unstable.<br/>-34818  -  Failed to start speedTest,
    the Client AP is not in CONNECTED, The device connection is unstable.<br/>-39344  -  The Main AP
    already in speed testing.<br/>-39360  -  The current AP’s firmware does not support the link speed
    test. Please update its firmware and try again.<br/>-39362  -  Mesh configurations of the device is
    lost. Please try to forget and then adopt it again.<br/>-39365  -  The Client AP’s firmware does not
    support the link speed test.(From the Main to the Client) Please update its firmware and try
    again.<br/>-39366  -  The Main AP’s firmware does not support the link speed test.(From Client to
    Main) Please update its firmware and try again.

    Args:
        omadac_id (str):
        site_id (str):
        ap_mac (str):
        body (SpeedTestCommand):

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
        body=body,
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
    body: SpeedTestCommand,
) -> Response[Any]:
    """Start speed test

     The speed test is initiated by device [apMac]. Different MAC addresses indicates a different speed
    test.(Only for P2P device)<br/><br/>The interface requires one of the permissions: <br/>Site Device
    Manager Modify<br/><br/>The possible error code for the interface in the returned body is one of the
    following error codes (non generic error codes): <br/>-34817  -  Failed to start speedTest, the Main
    AP is not in CONNECTED, The device connection is unstable.<br/>-34818  -  Failed to start speedTest,
    the Client AP is not in CONNECTED, The device connection is unstable.<br/>-39344  -  The Main AP
    already in speed testing.<br/>-39360  -  The current AP’s firmware does not support the link speed
    test. Please update its firmware and try again.<br/>-39362  -  Mesh configurations of the device is
    lost. Please try to forget and then adopt it again.<br/>-39365  -  The Client AP’s firmware does not
    support the link speed test.(From the Main to the Client) Please update its firmware and try
    again.<br/>-39366  -  The Main AP’s firmware does not support the link speed test.(From Client to
    Main) Please update its firmware and try again.

    Args:
        omadac_id (str):
        site_id (str):
        ap_mac (str):
        body (SpeedTestCommand):

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
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
