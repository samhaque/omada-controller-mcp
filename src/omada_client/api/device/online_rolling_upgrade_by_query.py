from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rolling_upgrade_request import RollingUpgradeRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    omadac_id: str,
    site_id: str,
    *,
    body: RollingUpgradeRequest,
    filters_ecsp_first_version: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["filters.ecspFirstVersion"] = filters_ecsp_first_version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/openapi/v1/{omadac_id}/sites/{site_id}/cmd/devices/onlineRollingUpgrade".format(
            omadac_id=quote(str(omadac_id), safe=""),
            site_id=quote(str(site_id), safe=""),
        ),
        "params": params,
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
    body: RollingUpgradeRequest,
    filters_ecsp_first_version: str | Unset = UNSET,
) -> Response[Any]:
    """Start batch rolling upgrade By Query

     Perform batch online upgrades of devices in a specific order within the site, and filter them using
    filter conditions. It is recommended to check the firmware update status before the operation,
    otherwise the firmware may not be the latest version<br/><br/>The interface requires one of the
    permissions: <br/>Site Device Manager Modify<br/><br/>The possible error code for the interface in
    the returned body is one of the following error codes (non generic error codes): <br/>-39020  -
    Failed to upgrade because no device is ready for upgrading.

    Args:
        omadac_id (str):
        site_id (str):
        filters_ecsp_first_version (str | Unset):
        body (RollingUpgradeRequest):

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
        filters_ecsp_first_version=filters_ecsp_first_version,
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
    body: RollingUpgradeRequest,
    filters_ecsp_first_version: str | Unset = UNSET,
) -> Response[Any]:
    """Start batch rolling upgrade By Query

     Perform batch online upgrades of devices in a specific order within the site, and filter them using
    filter conditions. It is recommended to check the firmware update status before the operation,
    otherwise the firmware may not be the latest version<br/><br/>The interface requires one of the
    permissions: <br/>Site Device Manager Modify<br/><br/>The possible error code for the interface in
    the returned body is one of the following error codes (non generic error codes): <br/>-39020  -
    Failed to upgrade because no device is ready for upgrading.

    Args:
        omadac_id (str):
        site_id (str):
        filters_ecsp_first_version (str | Unset):
        body (RollingUpgradeRequest):

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
        filters_ecsp_first_version=filters_ecsp_first_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
