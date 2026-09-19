from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.osw_stack_config_open_api_vo import OswStackConfigOpenApiVO
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    site_id: str,
    stack_id: str,
    *,
    body: OswStackConfigOpenApiVO,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/openapi/v1/{omadac_id}/sites/{site_id}/stacks/{stack_id}".format(
            omadac_id=quote(str(omadac_id), safe=""),
            site_id=quote(str(site_id), safe=""),
            stack_id=quote(str(stack_id), safe=""),
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
    stack_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: OswStackConfigOpenApiVO,
) -> Response[Any]:
    """Modify Switch Stack

     Modify Switch Stack.<br/><br/>The interface requires one of the permissions: <br/>Site Device
    Manager Modify<br/><br/>The possible error code for the interface in the returned body is one of the
    following error codes (non generic error codes): <br/>-34686  -  This service port is already in
    use, please choose another port.<br/>-39093  -  The length of the device name exceeds the
    limit.<br/>-39098  -  The number of members exceeds the maximum member limit allowed by the
    controller.<br/>-39101  -  The device has been adopted at another site. Please access the site and
    forget the device first.<br/>-39102  -  The primary device is applying configurations. Please adopt
    the member device later.<br/>-39103  -  There are stack unit conflicts.<br/>-39700  -  Switch does
    not exist<br/>-39715  -  The member port in the LAG is invalid.<br/>-40201  -  Incompatible stack
    device exists. Please check the stack compatibility.

    Args:
        omadac_id (str):
        site_id (str):
        stack_id (str):
        body (OswStackConfigOpenApiVO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        stack_id=stack_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    omadac_id: str,
    site_id: str,
    stack_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: OswStackConfigOpenApiVO,
) -> Response[Any]:
    """Modify Switch Stack

     Modify Switch Stack.<br/><br/>The interface requires one of the permissions: <br/>Site Device
    Manager Modify<br/><br/>The possible error code for the interface in the returned body is one of the
    following error codes (non generic error codes): <br/>-34686  -  This service port is already in
    use, please choose another port.<br/>-39093  -  The length of the device name exceeds the
    limit.<br/>-39098  -  The number of members exceeds the maximum member limit allowed by the
    controller.<br/>-39101  -  The device has been adopted at another site. Please access the site and
    forget the device first.<br/>-39102  -  The primary device is applying configurations. Please adopt
    the member device later.<br/>-39103  -  There are stack unit conflicts.<br/>-39700  -  Switch does
    not exist<br/>-39715  -  The member port in the LAG is invalid.<br/>-40201  -  Incompatible stack
    device exists. Please check the stack compatibility.

    Args:
        omadac_id (str):
        site_id (str):
        stack_id (str):
        body (OswStackConfigOpenApiVO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        stack_id=stack_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
