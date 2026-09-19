from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    site_template_id: str,
    type_: str,
    port_schedule_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/openapi/v1/{omadac_id}/sitetemplates/{site_template_id}/setting/service/port-schedules/{type_}/{port_schedule_id}".format(
            omadac_id=quote(str(omadac_id), safe=""),
            site_template_id=quote(str(site_template_id), safe=""),
            type_=quote(str(type_), safe=""),
            port_schedule_id=quote(str(port_schedule_id), safe=""),
        ),
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
    type_: str,
    port_schedule_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any]:
    """Delete Port Schedule Template

     Delete Port Schedule Template with the given params.<br/><br/>The interface requires one of the
    permissions: <br/>Global Site Template Manager Modify<br/><br/>The possible error code for the
    interface in the returned body is one of the following error codes (non generic error codes):
    <br/>-33009  -  This site template does not exist.<br/>-33011  -  Operation failed because other
    operations are being performed on this site template. Please wait and try again later.

    Args:
        omadac_id (str):
        site_template_id (str):
        type_ (str):
        port_schedule_id (str):

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
        port_schedule_id=port_schedule_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    omadac_id: str,
    site_template_id: str,
    type_: str,
    port_schedule_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any]:
    """Delete Port Schedule Template

     Delete Port Schedule Template with the given params.<br/><br/>The interface requires one of the
    permissions: <br/>Global Site Template Manager Modify<br/><br/>The possible error code for the
    interface in the returned body is one of the following error codes (non generic error codes):
    <br/>-33009  -  This site template does not exist.<br/>-33011  -  Operation failed because other
    operations are being performed on this site template. Please wait and try again later.

    Args:
        omadac_id (str):
        site_template_id (str):
        type_ (str):
        port_schedule_id (str):

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
        port_schedule_id=port_schedule_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
