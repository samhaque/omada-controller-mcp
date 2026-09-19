from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.batch_edit_tabs import BatchEditTabs
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    site_id: str,
    *,
    body: BatchEditTabs,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/openapi/v1/{omadac_id}/sites/{site_id}/dashboard/multi-tabs/config".format(
            omadac_id=quote(str(omadac_id), safe=""),
            site_id=quote(str(site_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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
    *,
    client: AuthenticatedClient | Client,
    body: BatchEditTabs,
) -> Response[Any]:
    """Batch set tab config

     Batch set tab configurations, add or delete tabs.<br/><br/>The interface requires one of the
    permissions: <br/>Site Dashboard Manager Modify<br/><br/>The possible error code for the interface
    in the returned body is one of the following error codes (non generic error codes): <br/>-34700  -
    The dashboard page does not exist in current site.<br/>-34701  -  This tab does not exist in the
    dashboard.<br/>-34702  -  This tab name already exists.<br/>-34704  -  Non-overall tabs do not allow
    editing system cards.

    Args:
        omadac_id (str):
        site_id (str):
        body (BatchEditTabs):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    omadac_id: str,
    site_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: BatchEditTabs,
) -> Response[Any]:
    """Batch set tab config

     Batch set tab configurations, add or delete tabs.<br/><br/>The interface requires one of the
    permissions: <br/>Site Dashboard Manager Modify<br/><br/>The possible error code for the interface
    in the returned body is one of the following error codes (non generic error codes): <br/>-34700  -
    The dashboard page does not exist in current site.<br/>-34701  -  This tab does not exist in the
    dashboard.<br/>-34702  -  This tab name already exists.<br/>-34704  -  Non-overall tabs do not allow
    editing system cards.

    Args:
        omadac_id (str):
        site_id (str):
        body (BatchEditTabs):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
