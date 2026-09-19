from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.switch_profile_id import SwitchProfileID
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    site_id: str,
    switch_mac: str,
    port: str,
    *,
    body: SwitchProfileID,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/openapi/v1/{omadac_id}/sites/{site_id}/switches/{switch_mac}/ports/{port}/profile".format(
            omadac_id=quote(str(omadac_id), safe=""),
            site_id=quote(str(site_id), safe=""),
            switch_mac=quote(str(switch_mac), safe=""),
            port=quote(str(port), safe=""),
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
    switch_mac: str,
    port: str,
    *,
    client: AuthenticatedClient | Client,
    body: SwitchProfileID,
) -> Response[Any]:
    """Set profile for given port

     Set profile for given port.<br/><br/>The interface requires one of the permissions: <br/>Site Device
    Manager Modify<br/><br/>The possible error code for the interface in the returned body is one of the
    following error codes (non generic error codes): <br/>-33507  -  This profile does not
    exist.<br/>-33558  -  The profile does not support the Agile Series Switch.<br/>-33564  -  The
    number of VLANs has reached the limit of the Agile Series Switch.<br/>-39050  -  This device does
    not exist.<br/>-39701  -  This port does not exist<br/>-40205  -  The device has been added to the
    stack group and related configurations cannot be modified.

    Args:
        omadac_id (str):
        site_id (str):
        switch_mac (str):
        port (str):
        body (SwitchProfileID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        switch_mac=switch_mac,
        port=port,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    omadac_id: str,
    site_id: str,
    switch_mac: str,
    port: str,
    *,
    client: AuthenticatedClient | Client,
    body: SwitchProfileID,
) -> Response[Any]:
    """Set profile for given port

     Set profile for given port.<br/><br/>The interface requires one of the permissions: <br/>Site Device
    Manager Modify<br/><br/>The possible error code for the interface in the returned body is one of the
    following error codes (non generic error codes): <br/>-33507  -  This profile does not
    exist.<br/>-33558  -  The profile does not support the Agile Series Switch.<br/>-33564  -  The
    number of VLANs has reached the limit of the Agile Series Switch.<br/>-39050  -  This device does
    not exist.<br/>-39701  -  This port does not exist<br/>-40205  -  The device has been added to the
    stack group and related configurations cannot be modified.

    Args:
        omadac_id (str):
        site_id (str):
        switch_mac (str):
        port (str):
        body (SwitchProfileID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        switch_mac=switch_mac,
        port=port,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
