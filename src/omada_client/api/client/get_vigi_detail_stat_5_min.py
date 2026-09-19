from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.client_stat_query import ClientStatQuery
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    site_id: str,
    vigi_mac: str,
    *,
    body: ClientStatQuery,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/openapi/v1/{omadac_id}/sites/{site_id}/vigi-stat-detail/{vigi_mac}/5Min".format(
            omadac_id=quote(str(omadac_id), safe=""),
            site_id=quote(str(site_id), safe=""),
            vigi_mac=quote(str(vigi_mac), safe=""),
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
    vigi_mac: str,
    *,
    client: AuthenticatedClient | Client,
    body: ClientStatQuery,
) -> Response[Any]:
    """Get VIGI device statistical data details at a 5-minute interval.

     Get VIGI device statistical data details at a 5-minute interval.<br/><br/>The interface requires one
    of the permissions: <br/>Site Device Manager View Only

    Args:
        omadac_id (str):
        site_id (str):
        vigi_mac (str):
        body (ClientStatQuery):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        vigi_mac=vigi_mac,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    omadac_id: str,
    site_id: str,
    vigi_mac: str,
    *,
    client: AuthenticatedClient | Client,
    body: ClientStatQuery,
) -> Response[Any]:
    """Get VIGI device statistical data details at a 5-minute interval.

     Get VIGI device statistical data details at a 5-minute interval.<br/><br/>The interface requires one
    of the permissions: <br/>Site Device Manager View Only

    Args:
        omadac_id (str):
        site_id (str):
        vigi_mac (str):
        body (ClientStatQuery):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        vigi_mac=vigi_mac,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
