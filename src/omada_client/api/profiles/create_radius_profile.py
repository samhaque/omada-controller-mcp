from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_radius_profile_open_api_vo import CreateRadiusProfileOpenApiVO
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    site_id: str,
    *,
    body: CreateRadiusProfileOpenApiVO,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/openapi/v1/{omadac_id}/sites/{site_id}/profiles/radius".format(
            omadac_id=quote(str(omadac_id), safe=""),
            site_id=quote(str(site_id), safe=""),
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
    *,
    client: AuthenticatedClient | Client,
    body: CreateRadiusProfileOpenApiVO,
) -> Response[Any]:
    """Create a new RADIUS profile

     Create a new RADIUS profile with the given params.<br/><br/>The interface requires one of the
    permissions: <br/>Site Settings Manager Modify<br/>Network Config Page Modify<br/><br/>The possible
    error code for the interface in the returned body is one of the following error codes (non generic
    error codes): <br/>-33004  -  Operation failed because other operations (site copying, restoring,
    template synchronizing, etc.) are being performed on this site. Please wait and try again
    later.<br/>-34000  -  Interim Update Interval ranges from 60 to 86400.<br/>-34002  -  Accounting
    port number ranges from 60 to 86400.<br/>-34003  -  Enter the shared secret key of the accounting
    server using 1-128 printable ASCII characters (including the space).<br/>-34004  -  This RADIUS
    profile already exists.<br/>-34011  -  Invalid IP address of the RADIUS server.<br/>-34011  -
    Invalid IP address of the RADIUS server.<br/>-34014  -  The number of RADIUS profiles has reached
    the limit.

    Args:
        omadac_id (str):
        site_id (str):
        body (CreateRadiusProfileOpenApiVO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        body=body,
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
    body: CreateRadiusProfileOpenApiVO,
) -> Response[Any]:
    """Create a new RADIUS profile

     Create a new RADIUS profile with the given params.<br/><br/>The interface requires one of the
    permissions: <br/>Site Settings Manager Modify<br/>Network Config Page Modify<br/><br/>The possible
    error code for the interface in the returned body is one of the following error codes (non generic
    error codes): <br/>-33004  -  Operation failed because other operations (site copying, restoring,
    template synchronizing, etc.) are being performed on this site. Please wait and try again
    later.<br/>-34000  -  Interim Update Interval ranges from 60 to 86400.<br/>-34002  -  Accounting
    port number ranges from 60 to 86400.<br/>-34003  -  Enter the shared secret key of the accounting
    server using 1-128 printable ASCII characters (including the space).<br/>-34004  -  This RADIUS
    profile already exists.<br/>-34011  -  Invalid IP address of the RADIUS server.<br/>-34011  -
    Invalid IP address of the RADIUS server.<br/>-34014  -  The number of RADIUS profiles has reached
    the limit.

    Args:
        omadac_id (str):
        site_id (str):
        body (CreateRadiusProfileOpenApiVO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
