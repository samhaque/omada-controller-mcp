from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    msp_id: str,
    *,
    page: int,
    page_size: int,
    filters_time_start: int,
    filters_time_end: int,
    filters_module: str | Unset = UNSET,
    filters_resolved: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["pageSize"] = page_size

    params["filters.timeStart"] = filters_time_start

    params["filters.timeEnd"] = filters_time_end

    params["filters.module"] = filters_module

    params["filters.resolved"] = filters_resolved

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/openapi/v1/msp/{msp_id}/logs/alerts".format(
            msp_id=quote(str(msp_id), safe=""),
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
    msp_id: str,
    *,
    client: AuthenticatedClient | Client,
    page: int,
    page_size: int,
    filters_time_start: int,
    filters_time_end: int,
    filters_module: str | Unset = UNSET,
    filters_resolved: bool | Unset = UNSET,
) -> Response[Any]:
    """Get MSP alert log list

     Get logs in MSP alert log page.<br/><br/>The interface requires one of the permissions: <br/>MSP Log
    Manager View Only

    Args:
        msp_id (str):
        page (int):
        page_size (int):
        filters_time_start (int):
        filters_time_end (int):
        filters_module (str | Unset):
        filters_resolved (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        msp_id=msp_id,
        page=page,
        page_size=page_size,
        filters_time_start=filters_time_start,
        filters_time_end=filters_time_end,
        filters_module=filters_module,
        filters_resolved=filters_resolved,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    msp_id: str,
    *,
    client: AuthenticatedClient | Client,
    page: int,
    page_size: int,
    filters_time_start: int,
    filters_time_end: int,
    filters_module: str | Unset = UNSET,
    filters_resolved: bool | Unset = UNSET,
) -> Response[Any]:
    """Get MSP alert log list

     Get logs in MSP alert log page.<br/><br/>The interface requires one of the permissions: <br/>MSP Log
    Manager View Only

    Args:
        msp_id (str):
        page (int):
        page_size (int):
        filters_time_start (int):
        filters_time_end (int):
        filters_module (str | Unset):
        filters_resolved (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        msp_id=msp_id,
        page=page,
        page_size=page_size,
        filters_time_start=filters_time_start,
        filters_time_end=filters_time_end,
        filters_module=filters_module,
        filters_resolved=filters_resolved,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
