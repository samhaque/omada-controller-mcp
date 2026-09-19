from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.oui_based_vlan_template_open_api_vo import OuiBasedVlanTemplateOpenApiVO
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    site_template_id: str,
    *,
    body: OuiBasedVlanTemplateOpenApiVO,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/openapi/v1/{omadac_id}/sitetemplates/{site_template_id}/switch-oui-rules".format(
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
    body: OuiBasedVlanTemplateOpenApiVO,
) -> Response[Any]:
    """Create Switch oui based vlan template

     Create Switch oui based vlan template.<br/><br/>The interface requires one of the permissions:
    <br/>Global Site Template Manager Modify<br/><br/>The possible error code for the interface in the
    returned body is one of the following error codes (non generic error codes): <br/>-33009  -  This
    site template does not exist.<br/>-33779  -  This OUI profile does not exist.<br/>-34219  -  The
    rule for all device ports has been created in Rules.<br/>-34220  -  The rule for all device ports
    and the rule for custom device ports should not be enabled simultaneously.<br/>-34223  -  When the
    rule enabled, the same VLAN should not be bound with the same device port/LAG in different rules.
    Please check the settings.<br/>-34224  -  When the rule is enabled, the same device should not
    configure OUI-VLAN combination greater than 16.<br/>-34227  -  When the rule is enabled, the same
    OUI on the same device should not be configured in multiple rules.<br/>-34229  -  The OUI based VLAN
    rule name already exists.<br/>-34230  -  When the rule for all device ports is created, devices with
    old firmware should not be configured in rules for custom device ports.

    Args:
        omadac_id (str):
        site_template_id (str):
        body (OuiBasedVlanTemplateOpenApiVO):

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
    body: OuiBasedVlanTemplateOpenApiVO,
) -> Response[Any]:
    """Create Switch oui based vlan template

     Create Switch oui based vlan template.<br/><br/>The interface requires one of the permissions:
    <br/>Global Site Template Manager Modify<br/><br/>The possible error code for the interface in the
    returned body is one of the following error codes (non generic error codes): <br/>-33009  -  This
    site template does not exist.<br/>-33779  -  This OUI profile does not exist.<br/>-34219  -  The
    rule for all device ports has been created in Rules.<br/>-34220  -  The rule for all device ports
    and the rule for custom device ports should not be enabled simultaneously.<br/>-34223  -  When the
    rule enabled, the same VLAN should not be bound with the same device port/LAG in different rules.
    Please check the settings.<br/>-34224  -  When the rule is enabled, the same device should not
    configure OUI-VLAN combination greater than 16.<br/>-34227  -  When the rule is enabled, the same
    OUI on the same device should not be configured in multiple rules.<br/>-34229  -  The OUI based VLAN
    rule name already exists.<br/>-34230  -  When the rule for all device ports is created, devices with
    old firmware should not be configured in rules for custom device ports.

    Args:
        omadac_id (str):
        site_template_id (str):
        body (OuiBasedVlanTemplateOpenApiVO):

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
