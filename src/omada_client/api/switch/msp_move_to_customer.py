from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.move_to_customer_open_api_vo import MoveToCustomerOpenApiVO
from ...types import Response


def _get_kwargs(
    msp_id: str,
    customer_id: str,
    site_id: str,
    *,
    body: MoveToCustomerOpenApiVO,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/openapi/v1/msp/{msp_id}/customers/{customer_id}/sites/{site_id}/cmd/switches/move".format(
            msp_id=quote(str(msp_id), safe=""),
            customer_id=quote(str(customer_id), safe=""),
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
    msp_id: str,
    customer_id: str,
    site_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: MoveToCustomerOpenApiVO,
) -> Response[Any]:
    """Move site to target customer

     Move site to target customer<br/><br/>The interface requires one of the permissions: <br/>Site
    Device Manager Modify<br/><br/>The possible error code for the interface in the returned body is one
    of the following error codes (non generic error codes): <br/>-33421  -  The gateway model in the
    target site is different from the gateway model configured in the WAN Settings Overrides in the
    original site.<br/>-39034  -  Failed to move this site because the devices are upgrading.<br/>-39035
    -  Failed to move this site because the devices are rebooting.<br/>-39036  -  Failed to move this
    site because the devices are synchronizing configurations.<br/>-39037  -  Failed to move this site
    because the devices are provisioning.<br/>-39050  -  This device does not exist.<br/>-44261  -  The
    device does not support cluster and can only be adopted to its own site.

    Args:
        msp_id (str):
        customer_id (str):
        site_id (str):
        body (MoveToCustomerOpenApiVO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        msp_id=msp_id,
        customer_id=customer_id,
        site_id=site_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    msp_id: str,
    customer_id: str,
    site_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: MoveToCustomerOpenApiVO,
) -> Response[Any]:
    """Move site to target customer

     Move site to target customer<br/><br/>The interface requires one of the permissions: <br/>Site
    Device Manager Modify<br/><br/>The possible error code for the interface in the returned body is one
    of the following error codes (non generic error codes): <br/>-33421  -  The gateway model in the
    target site is different from the gateway model configured in the WAN Settings Overrides in the
    original site.<br/>-39034  -  Failed to move this site because the devices are upgrading.<br/>-39035
    -  Failed to move this site because the devices are rebooting.<br/>-39036  -  Failed to move this
    site because the devices are synchronizing configurations.<br/>-39037  -  Failed to move this site
    because the devices are provisioning.<br/>-39050  -  This device does not exist.<br/>-44261  -  The
    device does not support cluster and can only be adopted to its own site.

    Args:
        msp_id (str):
        customer_id (str):
        site_id (str):
        body (MoveToCustomerOpenApiVO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        msp_id=msp_id,
        customer_id=customer_id,
        site_id=site_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
