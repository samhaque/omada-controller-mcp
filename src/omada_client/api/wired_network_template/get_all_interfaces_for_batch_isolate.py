from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    omadac_id: str,
    site_template_id: str,
    *,
    search_key: str | Unset = UNSET,
    isolation_filter: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["searchKey"] = search_key

    params["isolation_filter"] = isolation_filter

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/openapi/v2/{omadac_id}/sitetemplates/{site_template_id}/lan-networks/isolate/interfaces".format(
            omadac_id=quote(str(omadac_id), safe=""),
            site_template_id=quote(str(site_template_id), safe=""),
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
    site_template_id: str,
    *,
    client: AuthenticatedClient | Client,
    search_key: str | Unset = UNSET,
    isolation_filter: int | Unset = UNSET,
) -> Response[Any]:
    """Get interface Grid

     Get interface Grid.<br/><br/>The interface requires one of the permissions: <br/>Global Site
    Template Manager View Only

    Args:
        omadac_id (str):
        site_template_id (str):
        search_key (str | Unset):
        isolation_filter (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_template_id=site_template_id,
        search_key=search_key,
        isolation_filter=isolation_filter,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    omadac_id: str,
    site_template_id: str,
    *,
    client: AuthenticatedClient | Client,
    search_key: str | Unset = UNSET,
    isolation_filter: int | Unset = UNSET,
) -> Response[Any]:
    """Get interface Grid

     Get interface Grid.<br/><br/>The interface requires one of the permissions: <br/>Global Site
    Template Manager View Only

    Args:
        omadac_id (str):
        site_template_id (str):
        search_key (str | Unset):
        isolation_filter (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_template_id=site_template_id,
        search_key=search_key,
        isolation_filter=isolation_filter,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
