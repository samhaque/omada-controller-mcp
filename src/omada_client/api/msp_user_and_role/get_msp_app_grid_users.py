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
    sorts_name: str | Unset = UNSET,
    sorts_role_id: str | Unset = UNSET,
    sorts_email: str | Unset = UNSET,
    sorts_customer_role_id: str | Unset = UNSET,
    search_key: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["pageSize"] = page_size

    params["sorts.name"] = sorts_name

    params["sorts.roleId"] = sorts_role_id

    params["sorts.email"] = sorts_email

    params["sorts.customerRoleId"] = sorts_customer_role_id

    params["searchKey"] = search_key

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/openapi/v1/msp/{msp_id}/all-users".format(
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
    sorts_name: str | Unset = UNSET,
    sorts_role_id: str | Unset = UNSET,
    sorts_email: str | Unset = UNSET,
    sorts_customer_role_id: str | Unset = UNSET,
    search_key: str | Unset = UNSET,
) -> Response[Any]:
    """Get msp user list for app

     Get msp user list. This interface only supports the authorization code mode, not the client mode.
    Please call this interface in authorization code mode.<br/><br/>The interface requires one of the
    permissions: <br/>MSP Users Manager View Only<br/><br/>The possible error code for the interface in
    the returned body is one of the following error codes (non generic error codes): <br/>-44118  -
    This interface only supports the authorization code mode, not the client mode. Please call this
    interface in authorization code mode.

    Args:
        msp_id (str):
        page (int):
        page_size (int):
        sorts_name (str | Unset):
        sorts_role_id (str | Unset):
        sorts_email (str | Unset):
        sorts_customer_role_id (str | Unset):
        search_key (str | Unset):

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
        sorts_name=sorts_name,
        sorts_role_id=sorts_role_id,
        sorts_email=sorts_email,
        sorts_customer_role_id=sorts_customer_role_id,
        search_key=search_key,
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
    sorts_name: str | Unset = UNSET,
    sorts_role_id: str | Unset = UNSET,
    sorts_email: str | Unset = UNSET,
    sorts_customer_role_id: str | Unset = UNSET,
    search_key: str | Unset = UNSET,
) -> Response[Any]:
    """Get msp user list for app

     Get msp user list. This interface only supports the authorization code mode, not the client mode.
    Please call this interface in authorization code mode.<br/><br/>The interface requires one of the
    permissions: <br/>MSP Users Manager View Only<br/><br/>The possible error code for the interface in
    the returned body is one of the following error codes (non generic error codes): <br/>-44118  -
    This interface only supports the authorization code mode, not the client mode. Please call this
    interface in authorization code mode.

    Args:
        msp_id (str):
        page (int):
        page_size (int):
        sorts_name (str | Unset):
        sorts_role_id (str | Unset):
        sorts_email (str | Unset):
        sorts_customer_role_id (str | Unset):
        search_key (str | Unset):

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
        sorts_name=sorts_name,
        sorts_role_id=sorts_role_id,
        sorts_email=sorts_email,
        sorts_customer_role_id=sorts_customer_role_id,
        search_key=search_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
