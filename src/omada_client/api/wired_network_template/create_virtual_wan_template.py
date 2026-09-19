from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.virtual_wan_config_open_api_vo import VirtualWanConfigOpenApiVO
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    site_template_id: str,
    *,
    body: VirtualWanConfigOpenApiVO,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/openapi/v1/{omadac_id}/sitetemplates/{site_template_id}/setting/virtual-wans".format(
            omadac_id=quote(str(omadac_id), safe=""),
            site_template_id=quote(str(site_template_id), safe=""),
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
    *,
    client: AuthenticatedClient | Client,
    body: VirtualWanConfigOpenApiVO,
) -> Response[Any]:
    """Create virtual WAN template

     Create virtual WAN template.<br/><br/>The interface requires one of the permissions: <br/>Global
    Site Template Manager Modify<br/><br/>The possible error code for the interface in the returned body
    is one of the following error codes (non generic error codes): <br/>-44701  -  This VLAN ID is
    already used by the Virtual WAN interface.<br/>-44702  -  Duplicate names of the virtual
    WAN.<br/>-44703  -  When no gateway is adopted, at most 3 virtual WAN ports can be added.<br/>-44704
    -  The number of enabled WAN ports and virtual WAN ports cannot exceed the number of WAN ports plus
    3.<br/>-44705  -  At most 3 virtual WAN ports can be mapped to each WAN port.<br/>-44706  -  DSL
    setting cannot be null when DSL WAN is selected.<br/>-44707  -  The gateway does not support
    MssClamping in Virtual WAN.<br/>-44708  -  The gateway does not support DHCP Options in Virtual
    WAN.<br/>-44709  -  The gateway does not support PppoeMru in Virtual WAN.<br/>-44710  -  The gateway
    does not support DslMer in Virtual WAN.<br/>-44711  -  The gateway does not support Virtual
    WAN.<br/>-44712  -  The gateway only support DSL WAN.

    Args:
        omadac_id (str):
        site_template_id (str):
        body (VirtualWanConfigOpenApiVO): VirtualWanConfig

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_template_id=site_template_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    omadac_id: str,
    site_template_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: VirtualWanConfigOpenApiVO,
) -> Response[Any]:
    """Create virtual WAN template

     Create virtual WAN template.<br/><br/>The interface requires one of the permissions: <br/>Global
    Site Template Manager Modify<br/><br/>The possible error code for the interface in the returned body
    is one of the following error codes (non generic error codes): <br/>-44701  -  This VLAN ID is
    already used by the Virtual WAN interface.<br/>-44702  -  Duplicate names of the virtual
    WAN.<br/>-44703  -  When no gateway is adopted, at most 3 virtual WAN ports can be added.<br/>-44704
    -  The number of enabled WAN ports and virtual WAN ports cannot exceed the number of WAN ports plus
    3.<br/>-44705  -  At most 3 virtual WAN ports can be mapped to each WAN port.<br/>-44706  -  DSL
    setting cannot be null when DSL WAN is selected.<br/>-44707  -  The gateway does not support
    MssClamping in Virtual WAN.<br/>-44708  -  The gateway does not support DHCP Options in Virtual
    WAN.<br/>-44709  -  The gateway does not support PppoeMru in Virtual WAN.<br/>-44710  -  The gateway
    does not support DslMer in Virtual WAN.<br/>-44711  -  The gateway does not support Virtual
    WAN.<br/>-44712  -  The gateway only support DSL WAN.

    Args:
        omadac_id (str):
        site_template_id (str):
        body (VirtualWanConfigOpenApiVO): VirtualWanConfig

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_template_id=site_template_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
