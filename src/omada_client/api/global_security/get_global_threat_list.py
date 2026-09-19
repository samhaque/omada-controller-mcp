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
    site_list: str | Unset = UNSET,
    archived: bool,
    page: int,
    page_size: int,
    filters_start_time: int,
    filters_end_time: int,
    filters_severity: int | Unset = UNSET,
    sorts_time: str | Unset = UNSET,
    search_key: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["siteList"] = site_list

    params["archived"] = archived

    params["page"] = page

    params["pageSize"] = page_size

    params["filters.startTime"] = filters_start_time

    params["filters.endTime"] = filters_end_time

    params["filters.severity"] = filters_severity

    params["sorts.time"] = sorts_time

    params["searchKey"] = search_key

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/openapi/v1/{omadac_id}/security/threat-management".format(
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
    site_list: str | Unset = UNSET,
    archived: bool,
    page: int,
    page_size: int,
    filters_start_time: int,
    filters_end_time: int,
    filters_severity: int | Unset = UNSET,
    sorts_time: str | Unset = UNSET,
    search_key: str | Unset = UNSET,
) -> Response[Any]:
    """Get Global Threat List

     Get the global view threat management list<br/><br/>The interface requires one of the permissions:
    <br/>Global Threat Manager View Only

    Args:
        omadac_id (str):
        site_list (str | Unset):
        archived (bool):
        page (int):
        page_size (int):
        filters_start_time (int):
        filters_end_time (int):
        filters_severity (int | Unset):
        sorts_time (str | Unset):
        search_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_list=site_list,
        archived=archived,
        page=page,
        page_size=page_size,
        filters_start_time=filters_start_time,
        filters_end_time=filters_end_time,
        filters_severity=filters_severity,
        sorts_time=sorts_time,
        search_key=search_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    omadac_id: str,
    *,
    client: AuthenticatedClient | Client,
    site_list: str | Unset = UNSET,
    archived: bool,
    page: int,
    page_size: int,
    filters_start_time: int,
    filters_end_time: int,
    filters_severity: int | Unset = UNSET,
    sorts_time: str | Unset = UNSET,
    search_key: str | Unset = UNSET,
) -> Response[Any]:
    """Get Global Threat List

     Get the global view threat management list<br/><br/>The interface requires one of the permissions:
    <br/>Global Threat Manager View Only

    Args:
        omadac_id (str):
        site_list (str | Unset):
        archived (bool):
        page (int):
        page_size (int):
        filters_start_time (int):
        filters_end_time (int):
        filters_severity (int | Unset):
        sorts_time (str | Unset):
        search_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_list=site_list,
        archived=archived,
        page=page,
        page_size=page_size,
        filters_start_time=filters_start_time,
        filters_end_time=filters_end_time,
        filters_severity=filters_severity,
        sorts_time=sorts_time,
        search_key=search_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
