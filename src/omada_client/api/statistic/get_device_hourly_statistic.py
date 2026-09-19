from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.stat_query_vo import StatQueryVO
from ...types import UNSET, Response


def _get_kwargs(
    omadac_id: str,
    site_id: str,
    device_mac: str,
    *,
    body: StatQueryVO,
    type_: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["type"] = type_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/openapi/v2/{omadac_id}/sites/{site_id}/stat/{device_mac}/hourly".format(
            omadac_id=quote(str(omadac_id), safe=""),
            site_id=quote(str(site_id), safe=""),
            device_mac=quote(str(device_mac), safe=""),
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
    device_mac: str,
    *,
    client: AuthenticatedClient | Client,
    body: StatQueryVO,
    type_: str,
) -> Response[Any]:
    """Get device statistic data hourly

     Get device statistic data hourly. The supported attrs and response fields depend on the type
    parameter. For details, refer to section 5.9.1 Device Statistics of the Open API Access
    Guide.<br/><br/>The interface requires one of the permissions: <br/>Site Device Manager View
    Only<br/>Site Statics Manager View Only

    Args:
        omadac_id (str):
        site_id (str):
        device_mac (str):
        type_ (str):
        body (StatQueryVO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        device_mac=device_mac,
        body=body,
        type_=type_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    omadac_id: str,
    site_id: str,
    device_mac: str,
    *,
    client: AuthenticatedClient | Client,
    body: StatQueryVO,
    type_: str,
) -> Response[Any]:
    """Get device statistic data hourly

     Get device statistic data hourly. The supported attrs and response fields depend on the type
    parameter. For details, refer to section 5.9.1 Device Statistics of the Open API Access
    Guide.<br/><br/>The interface requires one of the permissions: <br/>Site Device Manager View
    Only<br/>Site Statics Manager View Only

    Args:
        omadac_id (str):
        site_id (str):
        device_mac (str):
        type_ (str):
        body (StatQueryVO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        device_mac=device_mac,
        body=body,
        type_=type_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
