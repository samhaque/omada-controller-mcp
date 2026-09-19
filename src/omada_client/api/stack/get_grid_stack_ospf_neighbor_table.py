from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    omadac_id: str,
    site_id: str,
    stack_id: str,
    *,
    page: int,
    page_size: int,
    sorts_neighbor_interface: str | Unset = UNSET,
    filters_neighbor_interface: list[str] | Unset = UNSET,
    filters_process_id: str | Unset = UNSET,
    search_key: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["pageSize"] = page_size

    params["sorts.neighborInterface"] = sorts_neighbor_interface

    json_filters_neighbor_interface: list[str] | Unset = UNSET
    if not isinstance(filters_neighbor_interface, Unset):
        json_filters_neighbor_interface = filters_neighbor_interface

    params["filters.neighborInterface"] = json_filters_neighbor_interface

    params["filters.processId"] = filters_process_id

    params["searchKey"] = search_key

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/openapi/v1/{omadac_id}/sites/{site_id}/stack/{stack_id}/ospf-neighbors".format(
            omadac_id=quote(str(omadac_id), safe=""),
            site_id=quote(str(site_id), safe=""),
            stack_id=quote(str(stack_id), safe=""),
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
    stack_id: str,
    *,
    client: AuthenticatedClient | Client,
    page: int,
    page_size: int,
    sorts_neighbor_interface: str | Unset = UNSET,
    filters_neighbor_interface: list[str] | Unset = UNSET,
    filters_process_id: str | Unset = UNSET,
    search_key: str | Unset = UNSET,
) -> Response[Any]:
    """Get stack ospf neighbor table

     Get stack ospf neighbor table.<br/><br/>The interface requires one of the permissions: <br/>Site
    Device Manager View Only

    Args:
        omadac_id (str):
        site_id (str):
        stack_id (str):
        page (int):
        page_size (int):
        sorts_neighbor_interface (str | Unset):
        filters_neighbor_interface (list[str] | Unset):
        filters_process_id (str | Unset):
        search_key (str | Unset):

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
        page=page,
        page_size=page_size,
        sorts_neighbor_interface=sorts_neighbor_interface,
        filters_neighbor_interface=filters_neighbor_interface,
        filters_process_id=filters_process_id,
        search_key=search_key,
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
    page: int,
    page_size: int,
    sorts_neighbor_interface: str | Unset = UNSET,
    filters_neighbor_interface: list[str] | Unset = UNSET,
    filters_process_id: str | Unset = UNSET,
    search_key: str | Unset = UNSET,
) -> Response[Any]:
    """Get stack ospf neighbor table

     Get stack ospf neighbor table.<br/><br/>The interface requires one of the permissions: <br/>Site
    Device Manager View Only

    Args:
        omadac_id (str):
        site_id (str):
        stack_id (str):
        page (int):
        page_size (int):
        sorts_neighbor_interface (str | Unset):
        filters_neighbor_interface (list[str] | Unset):
        filters_process_id (str | Unset):
        search_key (str | Unset):

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
        page=page,
        page_size=page_size,
        sorts_neighbor_interface=sorts_neighbor_interface,
        filters_neighbor_interface=filters_neighbor_interface,
        filters_process_id=filters_process_id,
        search_key=search_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
