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
    gateway_mac: str,
    sim_card: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/openapi/v1/{omadac_id}/sites/{site_id}/gateways/{gateway_mac}/sim/quota/{sim_card}".format(
            omadac_id=quote(str(omadac_id), safe=""),
            site_id=quote(str(site_id), safe=""),
            gateway_mac=quote(str(gateway_mac), safe=""),
            sim_card=quote(str(sim_card), safe=""),
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
    gateway_mac: str,
    sim_card: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any]:
    """Get one of Dual-SIM card's SIM data setting by mac

     Get SIM data setting by mac.<br/><br/>The interface requires one of the permissions: <br/>Site
    Settings Manager View Only<br/>Site Device Manager View Only<br/><br/>The possible error code for
    the interface in the returned body is one of the following error codes (non generic error codes):
    <br/>-35400  -  The adopted gateway does not support SIM configurations.

    Args:
        omadac_id (str):
        site_id (str):
        gateway_mac (str):
        sim_card (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        gateway_mac=gateway_mac,
        sim_card=sim_card,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    omadac_id: str,
    site_id: str,
    gateway_mac: str,
    sim_card: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any]:
    """Get one of Dual-SIM card's SIM data setting by mac

     Get SIM data setting by mac.<br/><br/>The interface requires one of the permissions: <br/>Site
    Settings Manager View Only<br/>Site Device Manager View Only<br/><br/>The possible error code for
    the interface in the returned body is one of the following error codes (non generic error codes):
    <br/>-35400  -  The adopted gateway does not support SIM configurations.

    Args:
        omadac_id (str):
        site_id (str):
        gateway_mac (str):
        sim_card (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        gateway_mac=gateway_mac,
        sim_card=sim_card,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
