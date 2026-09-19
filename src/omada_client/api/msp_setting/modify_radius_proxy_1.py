from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.radius_proxy_server_setting_request_body import (
    RadiusProxyServerSettingRequestBody,
)
from ...types import Response


def _get_kwargs(
    msp_id: str,
    *,
    body: RadiusProxyServerSettingRequestBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/openapi/v1/msp/{msp_id}/settings/network/radius-proxy".format(
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
    body: RadiusProxyServerSettingRequestBody,
) -> Response[Any]:
    """Modify Msp RADIUS proxy server setting

     Modify Msp RADIUS proxy server setting<br/><br/>The interface requires one of the permissions:
    <br/>MSP Other Settings Modify

    Args:
        msp_id (str):
        body (RadiusProxyServerSettingRequestBody):

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
    body: RadiusProxyServerSettingRequestBody,
) -> Response[Any]:
    """Modify Msp RADIUS proxy server setting

     Modify Msp RADIUS proxy server setting<br/><br/>The interface requires one of the permissions:
    <br/>MSP Other Settings Modify

    Args:
        msp_id (str):
        body (RadiusProxyServerSettingRequestBody):

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
