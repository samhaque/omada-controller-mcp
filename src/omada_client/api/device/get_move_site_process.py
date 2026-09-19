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
    move_site_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/openapi/v1/{omadac_id}/sites/{site_id}/devices/move/{move_site_id}/status".format(
            omadac_id=quote(str(omadac_id), safe=""),
            site_id=quote(str(site_id), safe=""),
            move_site_id=quote(str(move_site_id), safe=""),
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
    move_site_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any]:
    """Get batch move site process

     Get process of the batch move site operation. The expire time of result is 300 seconds.<br/><br/>The
    interface requires one of the permissions: <br/>Site Device Manager Modify<br/><br/>The possible
    error code for the interface in the returned body is one of the following error codes (non generic
    error codes): <br/>-1  -  Something went wrong. Please try again later or contact our technical
    support.<br/>-1001  -  Invalid request parameters.<br/>-1200  -  You have been logged out of the
    controller. This may have been caused by web application switching, data restore, reboot, session
    timeout or disabled cloud access. Please try to log in again later.<br/>-39104  -  The current
    request parameters do not exist or the request result has expired.

    Args:
        omadac_id (str):
        site_id (str):
        move_site_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        move_site_id=move_site_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    omadac_id: str,
    site_id: str,
    move_site_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any]:
    """Get batch move site process

     Get process of the batch move site operation. The expire time of result is 300 seconds.<br/><br/>The
    interface requires one of the permissions: <br/>Site Device Manager Modify<br/><br/>The possible
    error code for the interface in the returned body is one of the following error codes (non generic
    error codes): <br/>-1  -  Something went wrong. Please try again later or contact our technical
    support.<br/>-1001  -  Invalid request parameters.<br/>-1200  -  You have been logged out of the
    controller. This may have been caused by web application switching, data restore, reboot, session
    timeout or disabled cloud access. Please try to log in again later.<br/>-39104  -  The current
    request parameters do not exist or the request result has expired.

    Args:
        omadac_id (str):
        site_id (str):
        move_site_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        move_site_id=move_site_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
