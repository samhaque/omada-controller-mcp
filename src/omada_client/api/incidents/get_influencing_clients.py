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
    mac: str,
    *,
    anomaly_code: str,
    start_time: int | Unset = UNSET,
    end_time: int | Unset = UNSET,
    status: int | Unset = UNSET,
    page: int,
    page_size: int,
    sorts_name: str | Unset = UNSET,
    filters_active: str | Unset = UNSET,
    search_key: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["anomalyCode"] = anomaly_code

    params["startTime"] = start_time

    params["endTime"] = end_time

    params["status"] = status

    params["page"] = page

    params["pageSize"] = page_size

    params["sorts.name"] = sorts_name

    params["filters.active"] = filters_active

    params["searchKey"] = search_key

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/openapi/v1/{omadac_id}/sites/{site_id}/anomaly/{mac}/influencing-clients".format(
            omadac_id=quote(str(omadac_id), safe=""),
            site_id=quote(str(site_id), safe=""),
            mac=quote(str(mac), safe=""),
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
    mac: str,
    *,
    client: AuthenticatedClient | Client,
    anomaly_code: str,
    start_time: int | Unset = UNSET,
    end_time: int | Unset = UNSET,
    status: int | Unset = UNSET,
    page: int,
    page_size: int,
    sorts_name: str | Unset = UNSET,
    filters_active: str | Unset = UNSET,
    search_key: str | Unset = UNSET,
) -> Response[Any]:
    """Get Influencing Clients by an incident

     Get Influencing Clients by an incident<br/><br/>The interface requires one of the permissions:
    <br/>Incidents Page View Only

    Args:
        omadac_id (str):
        site_id (str):
        mac (str):
        anomaly_code (str):
        start_time (int | Unset):
        end_time (int | Unset):
        status (int | Unset):
        page (int):
        page_size (int):
        sorts_name (str | Unset):
        filters_active (str | Unset):
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
        mac=mac,
        anomaly_code=anomaly_code,
        start_time=start_time,
        end_time=end_time,
        status=status,
        page=page,
        page_size=page_size,
        sorts_name=sorts_name,
        filters_active=filters_active,
        search_key=search_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    omadac_id: str,
    site_id: str,
    mac: str,
    *,
    client: AuthenticatedClient | Client,
    anomaly_code: str,
    start_time: int | Unset = UNSET,
    end_time: int | Unset = UNSET,
    status: int | Unset = UNSET,
    page: int,
    page_size: int,
    sorts_name: str | Unset = UNSET,
    filters_active: str | Unset = UNSET,
    search_key: str | Unset = UNSET,
) -> Response[Any]:
    """Get Influencing Clients by an incident

     Get Influencing Clients by an incident<br/><br/>The interface requires one of the permissions:
    <br/>Incidents Page View Only

    Args:
        omadac_id (str):
        site_id (str):
        mac (str):
        anomaly_code (str):
        start_time (int | Unset):
        end_time (int | Unset):
        status (int | Unset):
        page (int):
        page_size (int):
        sorts_name (str | Unset):
        filters_active (str | Unset):
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
        mac=mac,
        anomaly_code=anomaly_code,
        start_time=start_time,
        end_time=end_time,
        status=status,
        page=page,
        page_size=page_size,
        sorts_name=sorts_name,
        filters_active=filters_active,
        search_key=search_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
