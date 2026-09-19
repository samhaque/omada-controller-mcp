from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.class_rule_open_api_vo import ClassRuleOpenApiVO
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    site_id: str,
    id: str,
    *,
    body: ClassRuleOpenApiVO,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/openapi/v1/{omadac_id}/sites/{site_id}/qos/gateway/class-rules/{id}".format(
            omadac_id=quote(str(omadac_id), safe=""),
            site_id=quote(str(site_id), safe=""),
            id=quote(str(id), safe=""),
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
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ClassRuleOpenApiVO,
) -> Response[Any]:
    """Modify an existing class rule

     Modify an existing class rule.<br/><br/>The interface requires one of the permissions: <br/>Site
    Settings Manager Modify<br/>Network Config Page Modify<br/>Site Device Manager Modify<br/><br/>The
    possible error code for the interface in the returned body is one of the following error codes (non
    generic error codes): <br/>-34265  -  The adopted or preconfigured gateway does not support
    QoS.<br/>-43301  -  The service type does not exist.<br/>-43306  -  The class rule does not
    exist.<br/>-43307  -  The IP group does not exist.<br/>-43308  -  The value of DSCP is invalid.

    Args:
        omadac_id (str):
        site_id (str):
        id (str):
        body (ClassRuleOpenApiVO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    omadac_id: str,
    site_id: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ClassRuleOpenApiVO,
) -> Response[Any]:
    """Modify an existing class rule

     Modify an existing class rule.<br/><br/>The interface requires one of the permissions: <br/>Site
    Settings Manager Modify<br/>Network Config Page Modify<br/>Site Device Manager Modify<br/><br/>The
    possible error code for the interface in the returned body is one of the following error codes (non
    generic error codes): <br/>-34265  -  The adopted or preconfigured gateway does not support
    QoS.<br/>-43301  -  The service type does not exist.<br/>-43306  -  The class rule does not
    exist.<br/>-43307  -  The IP group does not exist.<br/>-43308  -  The value of DSCP is invalid.

    Args:
        omadac_id (str):
        site_id (str):
        id (str):
        body (ClassRuleOpenApiVO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
