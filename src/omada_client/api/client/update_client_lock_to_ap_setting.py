from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.client_lock_to_ap_setting import ClientLockToAPSetting
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    site_id: str,
    client_mac: str,
    *,
    body: ClientLockToAPSetting,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/openapi/v1/{omadac_id}/sites/{site_id}/clients/{client_mac}/lock-to-ap".format(
            omadac_id=quote(str(omadac_id), safe=""),
            site_id=quote(str(site_id), safe=""),
            client_mac=quote(str(client_mac), safe=""),
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
    client_mac: str,
    *,
    client: AuthenticatedClient | Client,
    body: ClientLockToAPSetting,
) -> Response[Any]:
    """Lock the given client to aps

     Lock the given client to aps.<br/><br/>The interface requires one of the permissions: <br/>Site
    Clients Manager Modify<br/><br/>The possible error code for the interface in the returned body is
    one of the following error codes (non generic error codes): <br/>-41011  -  This client does not
    exist.<br/>-41020  -  Only wireless clients support Lock to wireless device.<br/>-41021  -  The
    number of Lock to wireless device entries has reached the upper limit.<br/>-41022  -  Blocked
    clients cannot be locked to wireless device.

    Args:
        omadac_id (str):
        site_id (str):
        client_mac (str):
        body (ClientLockToAPSetting):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        client_mac=client_mac,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    omadac_id: str,
    site_id: str,
    client_mac: str,
    *,
    client: AuthenticatedClient | Client,
    body: ClientLockToAPSetting,
) -> Response[Any]:
    """Lock the given client to aps

     Lock the given client to aps.<br/><br/>The interface requires one of the permissions: <br/>Site
    Clients Manager Modify<br/><br/>The possible error code for the interface in the returned body is
    one of the following error codes (non generic error codes): <br/>-41011  -  This client does not
    exist.<br/>-41020  -  Only wireless clients support Lock to wireless device.<br/>-41021  -  The
    number of Lock to wireless device entries has reached the upper limit.<br/>-41022  -  Blocked
    clients cannot be locked to wireless device.

    Args:
        omadac_id (str):
        site_id (str):
        client_mac (str):
        body (ClientLockToAPSetting):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        client_mac=client_mac,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
