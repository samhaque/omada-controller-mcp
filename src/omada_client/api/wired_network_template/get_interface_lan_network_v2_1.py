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
    type_: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["type"] = type_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/openapi/v1/{omadac_id}/sitetemplates/{site_template_id}/lan-networks/interface".format(
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
    type_: int | Unset = UNSET,
) -> Response[Any]:
    """Get all "single"/"multi" interface lan network template

     Get all "single"/"multi" interface lan network template<br/><br/>The interface requires one of the
    permissions: <br/>Global Site Template Manager View Only

    Args:
        omadac_id (str):
        site_template_id (str):
        type_ (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_template_id=site_template_id,
        type_=type_,
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
    type_: int | Unset = UNSET,
) -> Response[Any]:
    """Get all "single"/"multi" interface lan network template

     Get all "single"/"multi" interface lan network template<br/><br/>The interface requires one of the
    permissions: <br/>Global Site Template Manager View Only

    Args:
        omadac_id (str):
        site_template_id (str):
        type_ (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_template_id=site_template_id,
        type_=type_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
