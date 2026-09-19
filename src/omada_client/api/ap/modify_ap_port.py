from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.modify_aplan_port import ModifyAPLANPort
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    site_id: str,
    ap_mac: str,
    port: str,
    *,
    body: ModifyAPLANPort,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/openapi/v1/{omadac_id}/sites/{site_id}/aps/{ap_mac}/ports/{port}".format(
            omadac_id=quote(str(omadac_id), safe=""),
            site_id=quote(str(site_id), safe=""),
            ap_mac=quote(str(ap_mac), safe=""),
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
    ap_mac: str,
    port: str,
    *,
    client: AuthenticatedClient | Client,
    body: ModifyAPLANPort,
) -> Response[Any]:
    """Modify AP port config

     Modify AP port config<br/><br/>The interface requires one of the permissions: <br/>Site Device
    Manager Modify<br/><br/>The possible error code for the interface in the returned body is one of the
    following error codes (non generic error codes): <br/>-39050  -  This device does not
    exist.<br/>-39051  -  Operation failed. Please try again later.<br/>-39303  -  AP does not
    exist.<br/>-39348  -  This AP port vlanId can not be same as the exist default LanNetwork profile.

    Args:
        omadac_id (str):
        site_id (str):
        ap_mac (str):
        port (str):
        body (ModifyAPLANPort):

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
    ap_mac: str,
    port: str,
    *,
    client: AuthenticatedClient | Client,
    body: ModifyAPLANPort,
) -> Response[Any]:
    """Modify AP port config

     Modify AP port config<br/><br/>The interface requires one of the permissions: <br/>Site Device
    Manager Modify<br/><br/>The possible error code for the interface in the returned body is one of the
    following error codes (non generic error codes): <br/>-39050  -  This device does not
    exist.<br/>-39051  -  Operation failed. Please try again later.<br/>-39303  -  AP does not
    exist.<br/>-39348  -  This AP port vlanId can not be same as the exist default LanNetwork profile.

    Args:
        omadac_id (str):
        site_id (str):
        ap_mac (str):
        port (str):
        body (ModifyAPLANPort):

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
        port=port,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
