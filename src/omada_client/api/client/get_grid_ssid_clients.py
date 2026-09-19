from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.open_api_query_data_v2vo import OpenApiQueryDataV2VO
from ...types import UNSET, Response


def _get_kwargs(
    omadac_id: str,
    site_id: str,
    ssid_id: str,
    *,
    arg5: OpenApiQueryDataV2VO,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_arg5 = arg5.to_dict()
    params.update(json_arg5)

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/openapi/v1/{omadac_id}/sites/{site_id}/clientList/{ssid_id}".format(
            omadac_id=quote(str(omadac_id), safe=""),
            site_id=quote(str(site_id), safe=""),
            ssid_id=quote(str(ssid_id), safe=""),
        ),
        "params": params,
    }

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
    ssid_id: str,
    *,
    client: AuthenticatedClient | Client,
    arg5: OpenApiQueryDataV2VO,
) -> Response[Any]:
    """Get clients list of ssid.

     Get clients list of ssid.<br/><br/>The interface requires one of the permissions: <br/>Network
    Config Page View Only

    Args:
        omadac_id (str):
        site_id (str):
        ssid_id (str):
        arg5 (OpenApiQueryDataV2VO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        ssid_id=ssid_id,
        arg5=arg5,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    omadac_id: str,
    site_id: str,
    ssid_id: str,
    *,
    client: AuthenticatedClient | Client,
    arg5: OpenApiQueryDataV2VO,
) -> Response[Any]:
    """Get clients list of ssid.

     Get clients list of ssid.<br/><br/>The interface requires one of the permissions: <br/>Network
    Config Page View Only

    Args:
        omadac_id (str):
        site_id (str):
        ssid_id (str):
        arg5 (OpenApiQueryDataV2VO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        ssid_id=ssid_id,
        arg5=arg5,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
