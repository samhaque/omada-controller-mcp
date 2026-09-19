from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.upload_local_users_body import UploadLocalUsersBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    omadac_id: str,
    site_id: str,
    *,
    body: UploadLocalUsersBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/openapi/v1/{omadac_id}/sites/{site_id}/files/hotspot/local-users".format(
            omadac_id=quote(str(omadac_id), safe=""),
            site_id=quote(str(site_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
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
    body: UploadLocalUsersBody | Unset = UNSET,
) -> Response[Any]:
    """Upload local user file (excel or csv) by localhost

     Upload local user file (excel or csv) by localhost.<br/><br/>The interface requires one of the
    permissions: <br/>Site Hotspot Manager Modify<br/><br/>The possible error code for the interface in
    the returned body is one of the following error codes (non generic error codes): <br/>-1  -
    Something went wrong. Please try again later or contact our technical support.<br/>-1001  -  Invalid
    request parameters.<br/>-1005  -  Operation forbidden.<br/>-1200  -  You have been logged out of the
    controller. This may have been caused by web application switching, data restore, reboot, session
    timeout or disabled cloud access. Please try to log in again later.<br/>-33000  -  This site does
    not exist.<br/>-33004  -  Operation failed because other operations (site copying, restoring,
    template synchronizing, etc.) are being performed on this site. Please wait and try again
    later.<br/>-33712  -  This file is empty.<br/>-42037  -  Please select at least one portal before
    creating local users.<br/>-7131  -  Controller ID not exist.

    Args:
        omadac_id (str):
        site_id (str):
        body (UploadLocalUsersBody | Unset):

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
    body: UploadLocalUsersBody | Unset = UNSET,
) -> Response[Any]:
    """Upload local user file (excel or csv) by localhost

     Upload local user file (excel or csv) by localhost.<br/><br/>The interface requires one of the
    permissions: <br/>Site Hotspot Manager Modify<br/><br/>The possible error code for the interface in
    the returned body is one of the following error codes (non generic error codes): <br/>-1  -
    Something went wrong. Please try again later or contact our technical support.<br/>-1001  -  Invalid
    request parameters.<br/>-1005  -  Operation forbidden.<br/>-1200  -  You have been logged out of the
    controller. This may have been caused by web application switching, data restore, reboot, session
    timeout or disabled cloud access. Please try to log in again later.<br/>-33000  -  This site does
    not exist.<br/>-33004  -  Operation failed because other operations (site copying, restoring,
    template synchronizing, etc.) are being performed on this site. Please wait and try again
    later.<br/>-33712  -  This file is empty.<br/>-42037  -  Please select at least one portal before
    creating local users.<br/>-7131  -  Controller ID not exist.

    Args:
        omadac_id (str):
        site_id (str):
        body (UploadLocalUsersBody | Unset):

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
