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
    group_id: str,
    *,
    page: int,
    page_size: int,
    sorts_code: str | Unset = UNSET,
    filters_status: int | Unset = UNSET,
    search_key: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["pageSize"] = page_size

    params["sorts.code"] = sorts_code

    params["filters.status"] = filters_status

    params["searchKey"] = search_key

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/openapi/v1/{omadac_id}/sites/{site_id}/hotspot/voucher-groups/{group_id}".format(
            omadac_id=quote(str(omadac_id), safe=""),
            site_id=quote(str(site_id), safe=""),
            group_id=quote(str(group_id), safe=""),
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
    group_id: str,
    *,
    client: AuthenticatedClient | Client,
    page: int,
    page_size: int,
    sorts_code: str | Unset = UNSET,
    filters_status: int | Unset = UNSET,
    search_key: str | Unset = UNSET,
) -> Response[Any]:
    """Get Voucher Group Detail

     Get Voucher Group Detail with the given params.<br/><br/>The interface requires one of the
    permissions: <br/>Site Hotspot Manager View Only<br/><br/>The possible error code for the interface
    in the returned body is one of the following error codes (non generic error codes): <br/>-33000  -
    This site does not exist.<br/>-33004  -  Operation failed because other operations (site copying,
    restoring, template synchronizing, etc.) are being performed on this site. Please wait and try again
    later.<br/>-44111  -  The Grant Type is Invalid.<br/>-44112  -  The access token has expired. Please
    re-initiate the refreshToken process to obtain the access token.

    Args:
        omadac_id (str):
        site_id (str):
        group_id (str):
        page (int):
        page_size (int):
        sorts_code (str | Unset):
        filters_status (int | Unset):
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
        group_id=group_id,
        page=page,
        page_size=page_size,
        sorts_code=sorts_code,
        filters_status=filters_status,
        search_key=search_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    omadac_id: str,
    site_id: str,
    group_id: str,
    *,
    client: AuthenticatedClient | Client,
    page: int,
    page_size: int,
    sorts_code: str | Unset = UNSET,
    filters_status: int | Unset = UNSET,
    search_key: str | Unset = UNSET,
) -> Response[Any]:
    """Get Voucher Group Detail

     Get Voucher Group Detail with the given params.<br/><br/>The interface requires one of the
    permissions: <br/>Site Hotspot Manager View Only<br/><br/>The possible error code for the interface
    in the returned body is one of the following error codes (non generic error codes): <br/>-33000  -
    This site does not exist.<br/>-33004  -  Operation failed because other operations (site copying,
    restoring, template synchronizing, etc.) are being performed on this site. Please wait and try again
    later.<br/>-44111  -  The Grant Type is Invalid.<br/>-44112  -  The access token has expired. Please
    re-initiate the refreshToken process to obtain the access token.

    Args:
        omadac_id (str):
        site_id (str):
        group_id (str):
        page (int):
        page_size (int):
        sorts_code (str | Unset):
        filters_status (int | Unset):
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
        group_id=group_id,
        page=page,
        page_size=page_size,
        sorts_code=sorts_code,
        filters_status=filters_status,
        search_key=search_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
