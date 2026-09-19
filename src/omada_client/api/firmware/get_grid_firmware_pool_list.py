from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    omadac_id: str,
    *,
    channel: int,
    page: int,
    page_size: int,
    sorts_model_type_info: str | Unset = UNSET,
    sorts_release_time: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["channel"] = channel

    params["page"] = page

    params["pageSize"] = page_size

    params["sorts.modelTypeInfo"] = sorts_model_type_info

    params["sorts.releaseTime"] = sorts_release_time

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/openapi/v1/{omadac_id}/upgrade/overview/firmwares".format(
            omadac_id=quote(str(omadac_id), safe=""),
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
    *,
    client: AuthenticatedClient | Client,
    channel: int,
    page: int,
    page_size: int,
    sorts_model_type_info: str | Unset = UNSET,
    sorts_release_time: str | Unset = UNSET,
) -> Response[Any]:
    """Get firmware pool list

     Paging to get firmware pool list<br/><br/>The interface requires one of the permissions: <br/>Site
    Manual Firmware Upgrade View Only<br/><br/>The possible error code for the interface in the returned
    body is one of the following error codes (non generic error codes): <br/>-1501  -  Omada Cloud
    Platform error.

    Args:
        omadac_id (str):
        channel (int):
        page (int):
        page_size (int):
        sorts_model_type_info (str | Unset):
        sorts_release_time (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        channel=channel,
        page=page,
        page_size=page_size,
        sorts_model_type_info=sorts_model_type_info,
        sorts_release_time=sorts_release_time,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    omadac_id: str,
    *,
    client: AuthenticatedClient | Client,
    channel: int,
    page: int,
    page_size: int,
    sorts_model_type_info: str | Unset = UNSET,
    sorts_release_time: str | Unset = UNSET,
) -> Response[Any]:
    """Get firmware pool list

     Paging to get firmware pool list<br/><br/>The interface requires one of the permissions: <br/>Site
    Manual Firmware Upgrade View Only<br/><br/>The possible error code for the interface in the returned
    body is one of the following error codes (non generic error codes): <br/>-1501  -  Omada Cloud
    Platform error.

    Args:
        omadac_id (str):
        channel (int):
        page (int):
        page_size (int):
        sorts_model_type_info (str | Unset):
        sorts_release_time (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        channel=channel,
        page=page,
        page_size=page_size,
        sorts_model_type_info=sorts_model_type_info,
        sorts_release_time=sorts_release_time,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
