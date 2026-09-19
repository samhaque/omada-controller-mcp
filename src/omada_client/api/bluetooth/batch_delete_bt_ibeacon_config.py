from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.batch_delete_common_open_api_vo import BatchDeleteCommonOpenApiVO
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    site_id: str,
    *,
    body: BatchDeleteCommonOpenApiVO,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/openapi/v1/{omadac_id}/sites/{site_id}/setting/iot/devices/config/batch".format(
            omadac_id=quote(str(omadac_id), safe=""),
            site_id=quote(str(site_id), safe=""),
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
    *,
    client: AuthenticatedClient | Client,
    body: BatchDeleteCommonOpenApiVO,
) -> Response[Any]:
    """Batch delete Bluetooth Advertising

     Batch delete Bluetooth Advertising. Note:The parameter [transmitPower] is deprecated, all devices
    with transmit power configured via this v1 interface will have their transmit power configuration
    set to override on the new radio setting page. If you want to configure Transmit Power in Bluetooth
    -> Radio Setting, configure Bluetooth Advertising using v2 interface.<br/><br/>The interface
    requires one of the permissions: <br/>Site Settings Manager Modify<br/>Device Config Page Modify

    Args:
        omadac_id (str):
        site_id (str):
        body (BatchDeleteCommonOpenApiVO):

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
    body: BatchDeleteCommonOpenApiVO,
) -> Response[Any]:
    """Batch delete Bluetooth Advertising

     Batch delete Bluetooth Advertising. Note:The parameter [transmitPower] is deprecated, all devices
    with transmit power configured via this v1 interface will have their transmit power configuration
    set to override on the new radio setting page. If you want to configure Transmit Power in Bluetooth
    -> Radio Setting, configure Bluetooth Advertising using v2 interface.<br/><br/>The interface
    requires one of the permissions: <br/>Site Settings Manager Modify<br/>Device Config Page Modify

    Args:
        omadac_id (str):
        site_id (str):
        body (BatchDeleteCommonOpenApiVO):

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
