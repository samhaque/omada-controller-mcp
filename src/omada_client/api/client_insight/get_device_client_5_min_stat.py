from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.device_client_stat_query_open_api_vo import (
    DeviceClientStatQueryOpenApiVO,
)
from ...types import UNSET, Response


def _get_kwargs(
    omadac_id: str,
    site_id: str,
    device_mac: str,
    *,
    body: DeviceClientStatQueryOpenApiVO,
    device_type: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["deviceType"] = device_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/openapi/v1/{omadac_id}/sites/{site_id}/stat/{device_mac}/client-stat-5min".format(
            omadac_id=quote(str(omadac_id), safe=""),
            site_id=quote(str(site_id), safe=""),
            device_mac=quote(str(device_mac), safe=""),
        ),
        "params": params,
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
    device_mac: str,
    *,
    client: AuthenticatedClient | Client,
    body: DeviceClientStatQueryOpenApiVO,
    device_type: str,
) -> Response[Any]:
    """Get device client 5 min stat.

     Obtain the 5-minute sampling statistics of the clients.<br/><br/>The interface requires one of the
    permissions: <br/>Site Statics Manager View Only<br/><br/>The possible error code for the interface
    in the returned body is one of the following error codes (non generic error codes): <br/>-1001  -
    Invalid request parameters.

    Args:
        omadac_id (str):
        site_id (str):
        device_mac (str):
        device_type (str):
        body (DeviceClientStatQueryOpenApiVO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        device_mac=device_mac,
        body=body,
        device_type=device_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    omadac_id: str,
    site_id: str,
    device_mac: str,
    *,
    client: AuthenticatedClient | Client,
    body: DeviceClientStatQueryOpenApiVO,
    device_type: str,
) -> Response[Any]:
    """Get device client 5 min stat.

     Obtain the 5-minute sampling statistics of the clients.<br/><br/>The interface requires one of the
    permissions: <br/>Site Statics Manager View Only<br/><br/>The possible error code for the interface
    in the returned body is one of the following error codes (non generic error codes): <br/>-1001  -
    Invalid request parameters.

    Args:
        omadac_id (str):
        site_id (str):
        device_mac (str):
        device_type (str):
        body (DeviceClientStatQueryOpenApiVO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        device_mac=device_mac,
        body=body,
        device_type=device_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
