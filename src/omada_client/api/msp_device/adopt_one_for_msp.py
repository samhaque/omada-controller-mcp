from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.adopt_device_request import AdoptDeviceRequest
from ...types import Response


def _get_kwargs(
    msp_id: str,
    customer_id: str,
    site_id: str,
    device_mac: str,
    *,
    body: AdoptDeviceRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/openapi/v1/msp/{msp_id}/customers/{customer_id}/sites/{site_id}/devices/{device_mac}/start-adopt".format(
            msp_id=quote(str(msp_id), safe=""),
            customer_id=quote(str(customer_id), safe=""),
            site_id=quote(str(site_id), safe=""),
            device_mac=quote(str(device_mac), safe=""),
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
    msp_id: str,
    customer_id: str,
    site_id: str,
    device_mac: str,
    *,
    client: AuthenticatedClient | Client,
    body: AdoptDeviceRequest,
) -> Response[Any]:
    """Start adopt device For Msp

     Start adopt device in msp view.This interface does not return the actual adoptive result, you need
    to use the interface:Get device adopt result to obtain the adoptive result<br/><br/>The interface
    requires one of the permissions: <br/>MSP Adopt Device Manager Access<br/>MSP Add Device Manager
    Access

    Args:
        msp_id (str):
        customer_id (str):
        site_id (str):
        device_mac (str):
        body (AdoptDeviceRequest):

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
        body=body,
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
    body: AdoptDeviceRequest,
) -> Response[Any]:
    """Start adopt device For Msp

     Start adopt device in msp view.This interface does not return the actual adoptive result, you need
    to use the interface:Get device adopt result to obtain the adoptive result<br/><br/>The interface
    requires one of the permissions: <br/>MSP Adopt Device Manager Access<br/>MSP Add Device Manager
    Access

    Args:
        msp_id (str):
        customer_id (str):
        site_id (str):
        device_mac (str):
        body (AdoptDeviceRequest):

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
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
