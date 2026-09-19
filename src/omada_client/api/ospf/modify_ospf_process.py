from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ospf_process_config_open_api_vo import OspfProcessConfigOpenApiVO
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    site_id: str,
    ospf_process_id: str,
    *,
    body: OspfProcessConfigOpenApiVO,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/openapi/v1/{omadac_id}/sites/{site_id}/ospf/process/{ospf_process_id}".format(
            omadac_id=quote(str(omadac_id), safe=""),
            site_id=quote(str(site_id), safe=""),
            ospf_process_id=quote(str(ospf_process_id), safe=""),
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
    ospf_process_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: OspfProcessConfigOpenApiVO,
) -> Response[Any]:
    """Modify Ospf Process

     Modify Ospf Process.<br/><br/>The interface requires one of the permissions: <br/>Site Settings
    Manager Modify<br/>Site Device Manager Modify<br/><br/>The possible error code for the interface in
    the returned body is one of the following error codes (non generic error codes): <br/>-39700  -
    Switch does not exist<br/>-43902  -  OSPF Process does not exist.<br/>-43912  -  The OSPF process
    has duplicate networks.<br/>-43913  -  The OSPF process router ID is invalid.<br/>-43914  -  The
    device name cannot be changed.<br/>-43915  -  The OSPF process has invalid network IP.<br/>-43916  -
    The device does not support OSPF.<br/>-43918  -  The OSPF process area type is invalid.<br/>-43919
    -  The process ID cannot be modified.<br/>-43920  -  The area ID cannot be duplicated.

    Args:
        omadac_id (str):
        site_id (str):
        ospf_process_id (str):
        body (OspfProcessConfigOpenApiVO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        ospf_process_id=ospf_process_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    omadac_id: str,
    site_id: str,
    ospf_process_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: OspfProcessConfigOpenApiVO,
) -> Response[Any]:
    """Modify Ospf Process

     Modify Ospf Process.<br/><br/>The interface requires one of the permissions: <br/>Site Settings
    Manager Modify<br/>Site Device Manager Modify<br/><br/>The possible error code for the interface in
    the returned body is one of the following error codes (non generic error codes): <br/>-39700  -
    Switch does not exist<br/>-43902  -  OSPF Process does not exist.<br/>-43912  -  The OSPF process
    has duplicate networks.<br/>-43913  -  The OSPF process router ID is invalid.<br/>-43914  -  The
    device name cannot be changed.<br/>-43915  -  The OSPF process has invalid network IP.<br/>-43916  -
    The device does not support OSPF.<br/>-43918  -  The OSPF process area type is invalid.<br/>-43919
    -  The process ID cannot be modified.<br/>-43920  -  The area ID cannot be duplicated.

    Args:
        omadac_id (str):
        site_id (str):
        ospf_process_id (str):
        body (OspfProcessConfigOpenApiVO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        ospf_process_id=ospf_process_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
