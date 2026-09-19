from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    site_template_id: str,
    profile_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/openapi/v1/{omadac_id}/sitetemplates/{site_template_id}/time-range-profile/{profile_id}".format(
            omadac_id=quote(str(omadac_id), safe=""),
            site_template_id=quote(str(site_template_id), safe=""),
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
    site_template_id: str,
    profile_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any]:
    """Delete time range profile template

     Delete time range profile template<br/><br/>The interface requires one of the permissions:
    <br/>Global Site Template Manager Modify<br/><br/>The possible error code for the interface in the
    returned body is one of the following error codes (non generic error codes): <br/>-33701  -  Failed
    to delete this time range profile because it is applied in wireless networks.<br/>-33710  -  This
    profile does not exist.<br/>-33722  -  Cannot delete the time range. It is being used in PoE
    Schedule.<br/>-33754  -  Failed to delete this time range profile because it is applied in
    ACL.<br/>-33776  -  Failed to delete this time range profile because it is applied in
    IPS.<br/>-33853  -  Failed to delete this time range profile because it is applied in RRM
    settings.<br/>-34555  -  Cannot delete the time range. It is being used in Port Schedule.<br/>-35106
    -  Failed to delete this time range profile because it is applied in DPI.

    Args:
        omadac_id (str):
        site_template_id (str):
        profile_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_template_id=site_template_id,
        profile_id=profile_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    omadac_id: str,
    site_template_id: str,
    profile_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any]:
    """Delete time range profile template

     Delete time range profile template<br/><br/>The interface requires one of the permissions:
    <br/>Global Site Template Manager Modify<br/><br/>The possible error code for the interface in the
    returned body is one of the following error codes (non generic error codes): <br/>-33701  -  Failed
    to delete this time range profile because it is applied in wireless networks.<br/>-33710  -  This
    profile does not exist.<br/>-33722  -  Cannot delete the time range. It is being used in PoE
    Schedule.<br/>-33754  -  Failed to delete this time range profile because it is applied in
    ACL.<br/>-33776  -  Failed to delete this time range profile because it is applied in
    IPS.<br/>-33853  -  Failed to delete this time range profile because it is applied in RRM
    settings.<br/>-34555  -  Cannot delete the time range. It is being used in Port Schedule.<br/>-35106
    -  Failed to delete this time range profile because it is applied in DPI.

    Args:
        omadac_id (str):
        site_template_id (str):
        profile_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_template_id=site_template_id,
        profile_id=profile_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
