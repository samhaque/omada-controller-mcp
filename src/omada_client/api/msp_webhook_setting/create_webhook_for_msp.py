from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.open_api_webhook_setting_add_vo import OpenApiWebhookSettingAddVO
from ...types import Response


def _get_kwargs(
    msp_id: str,
    *,
    body: OpenApiWebhookSettingAddVO,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/openapi/v1/msp/{msp_id}/webhook/settings".format(
            msp_id=quote(str(msp_id), safe=""),
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
    *,
    client: AuthenticatedClient | Client,
    body: OpenApiWebhookSettingAddVO,
) -> Response[Any]:
    """Create MSP webhook setting

     Create MSP webhook setting.<br/><br/>The interface requires one of the permissions: <br/>MSP Webhook
    Manager Modify<br/><br/>The possible error code for the interface in the returned body is one of the
    following error codes (non generic error codes): <br/>-44200  -  The number of webhooks has reached
    the limit.<br/>-44201  -  This webhook name already exists.<br/>-44203  -  Webhook URL List should
    contain 1 to 3 URL entries. URL entries cannot be duplicated.

    Args:
        msp_id (str):
        body (OpenApiWebhookSettingAddVO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        msp_id=msp_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    msp_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: OpenApiWebhookSettingAddVO,
) -> Response[Any]:
    """Create MSP webhook setting

     Create MSP webhook setting.<br/><br/>The interface requires one of the permissions: <br/>MSP Webhook
    Manager Modify<br/><br/>The possible error code for the interface in the returned body is one of the
    following error codes (non generic error codes): <br/>-44200  -  The number of webhooks has reached
    the limit.<br/>-44201  -  This webhook name already exists.<br/>-44203  -  Webhook URL List should
    contain 1 to 3 URL entries. URL entries cannot be duplicated.

    Args:
        msp_id (str):
        body (OpenApiWebhookSettingAddVO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        msp_id=msp_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
