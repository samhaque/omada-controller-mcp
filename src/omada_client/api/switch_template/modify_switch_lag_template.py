from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.osw_lag_setting_vo import OswLagSettingVO
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    site_template_id: str,
    device_template_id: str,
    lag_id: str,
    *,
    body: OswLagSettingVO,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/openapi/v1/{omadac_id}/sitetemplates/{site_template_id}/switchtemplates/{device_template_id}/lags/{lag_id}".format(
            omadac_id=quote(str(omadac_id), safe=""),
            site_template_id=quote(str(site_template_id), safe=""),
            device_template_id=quote(str(device_template_id), safe=""),
            lag_id=quote(str(lag_id), safe=""),
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
    device_template_id: str,
    lag_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: OswLagSettingVO,
) -> Response[Any]:
    """Modify switch template lag

     Modify switch template lag.<br/><br/>The interface requires one of the permissions: <br/>Global Site
    Template Manager Modify<br/><br/>The possible error code for the interface in the returned body is
    one of the following error codes (non generic error codes): <br/>-39701  -  This port does not
    exist<br/>-44402  -  Device template does not exist.

    Args:
        omadac_id (str):
        site_template_id (str):
        device_template_id (str):
        lag_id (str):
        body (OswLagSettingVO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_template_id=site_template_id,
        device_template_id=device_template_id,
        lag_id=lag_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    omadac_id: str,
    site_template_id: str,
    device_template_id: str,
    lag_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: OswLagSettingVO,
) -> Response[Any]:
    """Modify switch template lag

     Modify switch template lag.<br/><br/>The interface requires one of the permissions: <br/>Global Site
    Template Manager Modify<br/><br/>The possible error code for the interface in the returned body is
    one of the following error codes (non generic error codes): <br/>-39701  -  This port does not
    exist<br/>-44402  -  Device template does not exist.

    Args:
        omadac_id (str):
        site_template_id (str):
        device_template_id (str):
        lag_id (str):
        body (OswLagSettingVO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_template_id=site_template_id,
        device_template_id=device_template_id,
        lag_id=lag_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
