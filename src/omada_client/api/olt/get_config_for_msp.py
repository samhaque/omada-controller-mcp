from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    msp_id: str,
    customer_id: str,
    site_id: str,
    device_mac: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/openapi/v1/msp/{msp_id}/customers/{customer_id}/sites/{site_id}/olts/{device_mac}/system/system-info/configs".format(
            msp_id=quote(str(msp_id), safe=""),
            customer_id=quote(str(customer_id), safe=""),
            site_id=quote(str(site_id), safe=""),
            device_mac=quote(str(device_mac), safe=""),
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
    msp_id: str,
    customer_id: str,
    site_id: str,
    device_mac: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any]:
    """Get OLT description info(MSP mode)

     Get OLT description info(MSP mode)<br/><br/>The interface requires one of the permissions: <br/>MSP
    Device Manager View Only<br/><br/>The possible error code for the interface in the returned body is
    one of the following error codes (non generic error codes): <br/>-45000  -  This OLT does not
    exist.<br/>-45001  -  The OLT is offline. Please reconnect<br/>-45002  -  OLT upgrading... Cannot
    manage the device now.<br/>-45003  -  OLT rebooting... Cannot manage the device now.

    Args:
        msp_id (str):
        customer_id (str):
        site_id (str):
        device_mac (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        msp_id=msp_id,
        customer_id=customer_id,
        site_id=site_id,
        device_mac=device_mac,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    msp_id: str,
    customer_id: str,
    site_id: str,
    device_mac: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any]:
    """Get OLT description info(MSP mode)

     Get OLT description info(MSP mode)<br/><br/>The interface requires one of the permissions: <br/>MSP
    Device Manager View Only<br/><br/>The possible error code for the interface in the returned body is
    one of the following error codes (non generic error codes): <br/>-45000  -  This OLT does not
    exist.<br/>-45001  -  The OLT is offline. Please reconnect<br/>-45002  -  OLT upgrading... Cannot
    manage the device now.<br/>-45003  -  OLT rebooting... Cannot manage the device now.

    Args:
        msp_id (str):
        customer_id (str):
        site_id (str):
        device_mac (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        msp_id=msp_id,
        customer_id=customer_id,
        site_id=site_id,
        device_mac=device_mac,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
