from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.sd_wan_nat_info_config import SdWanNatInfoConfig
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    group_id: str,
    *,
    body: SdWanNatInfoConfig,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/openapi/v1/{omadac_id}/sdwan/sdwan-group/map/{group_id}".format(
            omadac_id=quote(str(omadac_id), safe=""),
            group_id=quote(str(group_id), safe=""),
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
    group_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SdWanNatInfoConfig,
) -> Response[Any]:
    """Modify SD-WAN Group NAT info.

     Modify SD-WAN Group NAT info.<br/><br/>The interface requires one of the permissions: <br/>SD WAN
    Modify

    Args:
        omadac_id (str):
        group_id (str):
        body (SdWanNatInfoConfig): The NAT info of the SD-WAN group

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        group_id=group_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    omadac_id: str,
    group_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SdWanNatInfoConfig,
) -> Response[Any]:
    """Modify SD-WAN Group NAT info.

     Modify SD-WAN Group NAT info.<br/><br/>The interface requires one of the permissions: <br/>SD WAN
    Modify

    Args:
        omadac_id (str):
        group_id (str):
        body (SdWanNatInfoConfig): The NAT info of the SD-WAN group

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        group_id=group_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
