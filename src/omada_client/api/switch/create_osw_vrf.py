from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.osw_vrf_config_open_api_vo import OswVrfConfigOpenApiVO
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    site_id: str,
    switch_mac: str,
    *,
    body: OswVrfConfigOpenApiVO,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/openapi/v1/{omadac_id}/sites/{site_id}/switches/{switch_mac}/vrfs".format(
            omadac_id=quote(str(omadac_id), safe=""),
            site_id=quote(str(site_id), safe=""),
            switch_mac=quote(str(switch_mac), safe=""),
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
    *,
    client: AuthenticatedClient | Client,
    body: OswVrfConfigOpenApiVO,
) -> Response[Any]:
    """Create new vrf

     Create new vrf.<br/><br/>The interface requires one of the permissions: <br/>Site Device Manager
    Modify<br/><br/>The possible error code for the interface in the returned body is one of the
    following error codes (non generic error codes): <br/>-39700  -  Switch does not exist<br/>-39945  -
    This switch VRF name is reserved for device management purposes, please use a different
    name.<br/>-39970  -  The number of VRF entries in this switch has reached the limit.<br/>-39971  -
    This switch VRF Name already exists.

    Args:
        omadac_id (str):
        site_id (str):
        switch_mac (str):
        body (OswVrfConfigOpenApiVO):

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
    *,
    client: AuthenticatedClient | Client,
    body: OswVrfConfigOpenApiVO,
) -> Response[Any]:
    """Create new vrf

     Create new vrf.<br/><br/>The interface requires one of the permissions: <br/>Site Device Manager
    Modify<br/><br/>The possible error code for the interface in the returned body is one of the
    following error codes (non generic error codes): <br/>-39700  -  Switch does not exist<br/>-39945  -
    This switch VRF name is reserved for device management purposes, please use a different
    name.<br/>-39970  -  The number of VRF entries in this switch has reached the limit.<br/>-39971  -
    This switch VRF Name already exists.

    Args:
        omadac_id (str):
        site_id (str):
        switch_mac (str):
        body (OswVrfConfigOpenApiVO):

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
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
