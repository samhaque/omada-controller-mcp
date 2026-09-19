from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.modify_local_user_open_api_vo import ModifyLocalUserOpenApiVO
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    site_id: str,
    id: str,
    *,
    body: ModifyLocalUserOpenApiVO,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/openapi/v1/{omadac_id}/sites/{site_id}/hotspot/localusers/{id}".format(
            omadac_id=quote(str(omadac_id), safe=""),
            site_id=quote(str(site_id), safe=""),
            id=quote(str(id), safe=""),
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
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ModifyLocalUserOpenApiVO,
) -> Response[Any]:
    """Modify an existing localuser

     Modify an existing local user with the given omadacId, siteId, localuserId.<br/><br/>The interface
    requires one of the permissions: <br/>Site Hotspot Manager Modify<br/><br/>The possible error code
    for the interface in the returned body is one of the following error codes (non generic error
    codes): <br/>-33000  -  This site does not exist.<br/>-33004  -  Operation failed because other
    operations (site copying, restoring, template synchronizing, etc.) are being performed on this site.
    Please wait and try again later.<br/>-42013  -  Local user already exists.<br/>-42020  -  The MAC
    address that is bound to the local user account is invalid.<br/>-42037  -  Please select at least
    one portal before creating local users.<br/>-42039  -  Failed to bind to the portals. Please select
    the portals with local user authentication enabled.<br/>-44111  -  The Grant Type is
    Invalid.<br/>-44112  -  The access token has expired. Please re-initiate the refreshToken process to
    obtain the access token.

    Args:
        omadac_id (str):
        site_id (str):
        id (str):
        body (ModifyLocalUserOpenApiVO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    omadac_id: str,
    site_id: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ModifyLocalUserOpenApiVO,
) -> Response[Any]:
    """Modify an existing localuser

     Modify an existing local user with the given omadacId, siteId, localuserId.<br/><br/>The interface
    requires one of the permissions: <br/>Site Hotspot Manager Modify<br/><br/>The possible error code
    for the interface in the returned body is one of the following error codes (non generic error
    codes): <br/>-33000  -  This site does not exist.<br/>-33004  -  Operation failed because other
    operations (site copying, restoring, template synchronizing, etc.) are being performed on this site.
    Please wait and try again later.<br/>-42013  -  Local user already exists.<br/>-42020  -  The MAC
    address that is bound to the local user account is invalid.<br/>-42037  -  Please select at least
    one portal before creating local users.<br/>-42039  -  Failed to bind to the portals. Please select
    the portals with local user authentication enabled.<br/>-44111  -  The Grant Type is
    Invalid.<br/>-44112  -  The access token has expired. Please re-initiate the refreshToken process to
    obtain the access token.

    Args:
        omadac_id (str):
        site_id (str):
        id (str):
        body (ModifyLocalUserOpenApiVO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
