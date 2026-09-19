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
    ssid_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/openapi/v3/{omadac_id}/sites/{site_id}/topology/ssids/{ssid_id}/devices".format(
            omadac_id=quote(str(omadac_id), safe=""),
            site_id=quote(str(site_id), safe=""),
            ssid_id=quote(str(ssid_id), safe=""),
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
    ssid_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any]:
    """Filter Devices of Ssid in Topology

     Filter devices of ssid in topology with given omadacId and siteId by ssidId.<br/><br/>The interface
    requires one of the permissions: <br/>Site Settings Manager View Only<br/>Site Dashboard Manager
    View Only<br/>Site Device Manager View Only<br/><br/>The possible error code for the interface in
    the returned body is one of the following error codes (non generic error codes): <br/>-33004  -
    Operation failed because other operations (site copying, restoring, template synchronizing, etc.)
    are being performed on this site. Please wait and try again later.

    Args:
        omadac_id (str):
        site_id (str):
        ssid_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        ssid_id=ssid_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    omadac_id: str,
    site_id: str,
    ssid_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any]:
    """Filter Devices of Ssid in Topology

     Filter devices of ssid in topology with given omadacId and siteId by ssidId.<br/><br/>The interface
    requires one of the permissions: <br/>Site Settings Manager View Only<br/>Site Dashboard Manager
    View Only<br/>Site Device Manager View Only<br/><br/>The possible error code for the interface in
    the returned body is one of the following error codes (non generic error codes): <br/>-33004  -
    Operation failed because other operations (site copying, restoring, template synchronizing, etc.)
    are being performed on this site. Please wait and try again later.

    Args:
        omadac_id (str):
        site_id (str):
        ssid_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        ssid_id=ssid_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
