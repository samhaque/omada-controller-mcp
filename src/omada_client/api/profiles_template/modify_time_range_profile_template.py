from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_time_range_profile_open_api_vo import (
    UpdateTimeRangeProfileOpenApiVO,
)
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    site_template_id: str,
    profile_id: str,
    *,
    body: UpdateTimeRangeProfileOpenApiVO,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/openapi/v1/{omadac_id}/sitetemplates/{site_template_id}/time-range-profile/{profile_id}".format(
            omadac_id=quote(str(omadac_id), safe=""),
            site_template_id=quote(str(site_template_id), safe=""),
            profile_id=quote(str(profile_id), safe=""),
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
    site_template_id: str,
    profile_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateTimeRangeProfileOpenApiVO,
) -> Response[Any]:
    """Modify time range profile template

     Modify time range profile template<br/><br/>The interface requires one of the permissions:
    <br/>Global Site Template Manager Modify<br/><br/>The possible error code for the interface in the
    returned body is one of the following error codes (non generic error codes): <br/>-33709  -  This
    profile already exists.<br/>-33716  -  End time should be later than start time.<br/>-33731  -  Time
    range is not allowed to be empty.<br/>-33748  -  The number of time range per entry has reached the
    limit.<br/>-33799  -  Invalid schedule time param of time range profile

    Args:
        omadac_id (str):
        site_template_id (str):
        profile_id (str):
        body (UpdateTimeRangeProfileOpenApiVO):

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
        body=body,
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
    body: UpdateTimeRangeProfileOpenApiVO,
) -> Response[Any]:
    """Modify time range profile template

     Modify time range profile template<br/><br/>The interface requires one of the permissions:
    <br/>Global Site Template Manager Modify<br/><br/>The possible error code for the interface in the
    returned body is one of the following error codes (non generic error codes): <br/>-33709  -  This
    profile already exists.<br/>-33716  -  End time should be later than start time.<br/>-33731  -  Time
    range is not allowed to be empty.<br/>-33748  -  The number of time range per entry has reached the
    limit.<br/>-33799  -  Invalid schedule time param of time range profile

    Args:
        omadac_id (str):
        site_template_id (str):
        profile_id (str):
        body (UpdateTimeRangeProfileOpenApiVO):

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
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
