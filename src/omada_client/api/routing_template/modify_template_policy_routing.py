from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.policy_routing_config import PolicyRoutingConfig
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    site_template_id: str,
    policy_routing_id: str,
    *,
    body: PolicyRoutingConfig,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/openapi/v1/{omadac_id}/sitetemplates/{site_template_id}/routing/policy-routings/{policy_routing_id}".format(
            omadac_id=quote(str(omadac_id), safe=""),
            site_template_id=quote(str(site_template_id), safe=""),
            policy_routing_id=quote(str(policy_routing_id), safe=""),
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
    policy_routing_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PolicyRoutingConfig,
) -> Response[Any]:
    """Modify site template's policy routing

     Modify site template's policy routing.<br/><br/>The interface requires one of the permissions:
    <br/>Global Site Template Manager Modify<br/><br/>The possible error code for the interface in the
    returned body is one of the following error codes (non generic error codes): <br/>-33006  -  This
    name already exists in this site.<br/>-33600  -  Invalid Source Type.<br/>-33601  -  Invalid
    Destination Type.<br/>-33603  -  Source or Destination entry does not exist.<br/>-33608  -  Invalid
    protocols.<br/>-34267  -  Only one WAN interface can be configured for Policy Routing.<br/>-34268  -
    Unable to select a virtual WAN as the WAN interface for Policy Routing.<br/>-34269  -  Unable to
    select Location Group as the Destination for Policy Routing.<br/>-34270  -  Unable to select Domain
    Group as the Destination for Policy Routing.<br/>-34602  -  This VPN policy does not exist.

    Args:
        omadac_id (str):
        site_template_id (str):
        policy_routing_id (str):
        body (PolicyRoutingConfig):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_template_id=site_template_id,
        policy_routing_id=policy_routing_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    omadac_id: str,
    site_template_id: str,
    policy_routing_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PolicyRoutingConfig,
) -> Response[Any]:
    """Modify site template's policy routing

     Modify site template's policy routing.<br/><br/>The interface requires one of the permissions:
    <br/>Global Site Template Manager Modify<br/><br/>The possible error code for the interface in the
    returned body is one of the following error codes (non generic error codes): <br/>-33006  -  This
    name already exists in this site.<br/>-33600  -  Invalid Source Type.<br/>-33601  -  Invalid
    Destination Type.<br/>-33603  -  Source or Destination entry does not exist.<br/>-33608  -  Invalid
    protocols.<br/>-34267  -  Only one WAN interface can be configured for Policy Routing.<br/>-34268  -
    Unable to select a virtual WAN as the WAN interface for Policy Routing.<br/>-34269  -  Unable to
    select Location Group as the Destination for Policy Routing.<br/>-34270  -  Unable to select Domain
    Group as the Destination for Policy Routing.<br/>-34602  -  This VPN policy does not exist.

    Args:
        omadac_id (str):
        site_template_id (str):
        policy_routing_id (str):
        body (PolicyRoutingConfig):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_template_id=site_template_id,
        policy_routing_id=policy_routing_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
