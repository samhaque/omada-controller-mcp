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
    profile_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/openapi/v2/{omadac_id}/sites/{site_id}/lan-profiles/{profile_id}".format(
            omadac_id=quote(str(omadac_id), safe=""),
            site_id=quote(str(site_id), safe=""),
            profile_id=quote(str(profile_id), safe=""),
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
    profile_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any]:
    """Delete an existing switch profile

     Delete an existing switch profile. If returns -33560, use "Query Agile Series switch that used the
    profile" to query these Agile Series witches.<br/><br/>The interface requires one of the
    permissions: <br/>Site Settings Manager Modify<br/>Device Config Page Modify<br/><br/>The possible
    error code for the interface in the returned body is one of the following error codes (non generic
    error codes): <br/>0  -  Success.<br/>-1001  -  Invalid request parameters.<br/>-33004  -  Operation
    failed because other operations (site copying, restoring, template synchronizing, etc.) are being
    performed on this site. Please wait and try again later.<br/>-33507  -  This profile does not
    exist.<br/>-33560  -  The Agile Series Switch has been configured with this profile. Cannot delete
    the profile or turn off the option "Agile Series Switch Enabled".

    Args:
        omadac_id (str):
        site_id (str):
        profile_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        profile_id=profile_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    omadac_id: str,
    site_id: str,
    profile_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any]:
    """Delete an existing switch profile

     Delete an existing switch profile. If returns -33560, use "Query Agile Series switch that used the
    profile" to query these Agile Series witches.<br/><br/>The interface requires one of the
    permissions: <br/>Site Settings Manager Modify<br/>Device Config Page Modify<br/><br/>The possible
    error code for the interface in the returned body is one of the following error codes (non generic
    error codes): <br/>0  -  Success.<br/>-1001  -  Invalid request parameters.<br/>-33004  -  Operation
    failed because other operations (site copying, restoring, template synchronizing, etc.) are being
    performed on this site. Please wait and try again later.<br/>-33507  -  This profile does not
    exist.<br/>-33560  -  The Agile Series Switch has been configured with this profile. Cannot delete
    the profile or turn off the option "Agile Series Switch Enabled".

    Args:
        omadac_id (str):
        site_id (str):
        profile_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        profile_id=profile_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
