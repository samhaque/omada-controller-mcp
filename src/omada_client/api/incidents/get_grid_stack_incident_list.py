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
    filters_status: int | Unset = UNSET,
    page: int,
    page_size: int,
    filters_start_time: int | Unset = UNSET,
    filters_end_time: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["filters.status"] = filters_status

    params["page"] = page

    params["pageSize"] = page_size

    params["filters.startTime"] = filters_start_time

    params["filters.endTime"] = filters_end_time

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/openapi/v1/{omadac_id}/sites/{site_id}/incident/stack/{stack_id}".format(
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
    filters_status: int | Unset = UNSET,
    page: int,
    page_size: int,
    filters_start_time: int | Unset = UNSET,
    filters_end_time: int | Unset = UNSET,
) -> Response[Any]:
    """Get grid stack incident list

     Get incident list for a stack detail page.<br/><br/>The interface requires one of the permissions:
    <br/>Incidents Page View Only

    Args:
        omadac_id (str):
        site_id (str):
        stack_id (str):
        filters_status (int | Unset):
        page (int):
        page_size (int):
        filters_start_time (int | Unset):
        filters_end_time (int | Unset):

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
        filters_status=filters_status,
        page=page,
        page_size=page_size,
        filters_start_time=filters_start_time,
        filters_end_time=filters_end_time,
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
    filters_status: int | Unset = UNSET,
    page: int,
    page_size: int,
    filters_start_time: int | Unset = UNSET,
    filters_end_time: int | Unset = UNSET,
) -> Response[Any]:
    """Get grid stack incident list

     Get incident list for a stack detail page.<br/><br/>The interface requires one of the permissions:
    <br/>Incidents Page View Only

    Args:
        omadac_id (str):
        site_id (str):
        stack_id (str):
        filters_status (int | Unset):
        page (int):
        page_size (int):
        filters_start_time (int | Unset):
        filters_end_time (int | Unset):

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
        filters_status=filters_status,
        page=page,
        page_size=page_size,
        filters_start_time=filters_start_time,
        filters_end_time=filters_end_time,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
