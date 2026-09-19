from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_ap_channel_config_open_api_vo import (
    UpdateApChannelConfigOpenApiVO,
)
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    site_id: str,
    ap_mac: str,
    *,
    body: UpdateApChannelConfigOpenApiVO,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/openapi/v1/{omadac_id}/sites/{site_id}/aps/{ap_mac}/channel-config".format(
            omadac_id=quote(str(omadac_id), safe=""),
            site_id=quote(str(site_id), safe=""),
            ap_mac=quote(str(ap_mac), safe=""),
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
    ap_mac: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateApChannelConfigOpenApiVO,
) -> Response[Any]:
    """Modify AP channel config

     Modify AP channel config<br/><br/>The interface requires one of the permissions: <br/>Site Device
    Manager Modify<br/><br/>The possible error code for the interface in the returned body is one of the
    following error codes (non generic error codes): <br/>-39303  -  AP does not exist.

    Args:
        omadac_id (str):
        site_id (str):
        ap_mac (str):
        body (UpdateApChannelConfigOpenApiVO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        ap_mac=ap_mac,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    omadac_id: str,
    site_id: str,
    ap_mac: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateApChannelConfigOpenApiVO,
) -> Response[Any]:
    """Modify AP channel config

     Modify AP channel config<br/><br/>The interface requires one of the permissions: <br/>Site Device
    Manager Modify<br/><br/>The possible error code for the interface in the returned body is one of the
    following error codes (non generic error codes): <br/>-39303  -  AP does not exist.

    Args:
        omadac_id (str):
        site_id (str):
        ap_mac (str):
        body (UpdateApChannelConfigOpenApiVO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        ap_mac=ap_mac,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
