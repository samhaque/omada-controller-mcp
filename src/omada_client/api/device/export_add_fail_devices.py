from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response


def _get_kwargs(
    omadac_id: str,
    operate_id: str,
    *,
    format_: int,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["format"] = format_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/openapi/v1/{omadac_id}/devices/add/{operate_id}/export".format(
            omadac_id=quote(str(omadac_id), safe=""),
            operate_id=quote(str(operate_id), safe=""),
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
    operate_id: str,
    *,
    client: AuthenticatedClient | Client,
    format_: int,
) -> Response[Any]:
    """Export the device file that failed to add in GLOBAL view.

     Export the device file that failed to add in GLOBAL view. Format should be a number as follows. 0
    means CSV , 1 means XLSX.<br/><br/>The interface requires one of the permissions: <br/>Site Add
    Device Manager Access

    Args:
        omadac_id (str):
        operate_id (str):
        format_ (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        operate_id=operate_id,
        format_=format_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    omadac_id: str,
    operate_id: str,
    *,
    client: AuthenticatedClient | Client,
    format_: int,
) -> Response[Any]:
    """Export the device file that failed to add in GLOBAL view.

     Export the device file that failed to add in GLOBAL view. Format should be a number as follows. 0
    means CSV , 1 means XLSX.<br/><br/>The interface requires one of the permissions: <br/>Site Add
    Device Manager Access

    Args:
        omadac_id (str):
        operate_id (str):
        format_ (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        operate_id=operate_id,
        format_=format_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
