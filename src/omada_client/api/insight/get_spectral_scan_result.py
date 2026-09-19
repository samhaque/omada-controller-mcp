from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response


def _get_kwargs(
    omadac_id: str,
    site_id: str,
    ap_mac: str,
    *,
    times: int,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["times"] = times

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/openapi/v1/{omadac_id}/sites/{site_id}/spectral-scan/aps/{ap_mac}/spectral-scan-result".format(
            omadac_id=quote(str(omadac_id), safe=""),
            site_id=quote(str(site_id), safe=""),
            ap_mac=quote(str(ap_mac), safe=""),
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
    ap_mac: str,
    *,
    client: AuthenticatedClient | Client,
    times: int,
) -> Response[Any]:
    """Get current results of environment scanning

     Get current results of environment scanning. The results of the environment scan are compressed by
    the Deflate algorithm and then base64 encoded.<br/><br/>The interface requires one of the
    permissions: <br/>Site Device Manager View Only<br/><br/>The possible error code for the interface
    in the returned body is one of the following error codes (non generic error codes): <br/>-39050  -
    This device does not exist.<br/>-39303  -  AP does not exist.

    Args:
        omadac_id (str):
        site_id (str):
        ap_mac (str):
        times (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        ap_mac=ap_mac,
        times=times,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    omadac_id: str,
    site_id: str,
    ap_mac: str,
    *,
    client: AuthenticatedClient | Client,
    times: int,
) -> Response[Any]:
    """Get current results of environment scanning

     Get current results of environment scanning. The results of the environment scan are compressed by
    the Deflate algorithm and then base64 encoded.<br/><br/>The interface requires one of the
    permissions: <br/>Site Device Manager View Only<br/><br/>The possible error code for the interface
    in the returned body is one of the following error codes (non generic error codes): <br/>-39050  -
    This device does not exist.<br/>-39303  -  AP does not exist.

    Args:
        omadac_id (str):
        site_id (str):
        ap_mac (str):
        times (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        ap_mac=ap_mac,
        times=times,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
