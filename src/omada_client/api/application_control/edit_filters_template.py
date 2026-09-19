from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.edit_filter_entity import EditFilterEntity
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    site_template_id: str,
    filter_id: str,
    *,
    body: EditFilterEntity,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/openapi/v1/{omadac_id}/sitetemplates/{site_template_id}/applicationControl/filters/{filter_id}".format(
            omadac_id=quote(str(omadac_id), safe=""),
            site_template_id=quote(str(site_template_id), safe=""),
            filter_id=quote(str(filter_id), safe=""),
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
    site_template_id: str,
    filter_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: EditFilterEntity,
) -> Response[Any]:
    """Modify an existing filter

     Modify an existing filter.<br/><br/>The interface requires one of the permissions: <br/>Global Site
    Template Manager Modify<br/><br/>The possible error code for the interface in the returned body is
    one of the following error codes (non generic error codes): <br/>-35103  -  Rules should not be
    empty.<br/>-35104  -  Filter name already exist.

    Args:
        omadac_id (str):
        site_template_id (str):
        filter_id (str):
        body (EditFilterEntity):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_template_id=site_template_id,
        filter_id=filter_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    omadac_id: str,
    site_template_id: str,
    filter_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: EditFilterEntity,
) -> Response[Any]:
    """Modify an existing filter

     Modify an existing filter.<br/><br/>The interface requires one of the permissions: <br/>Global Site
    Template Manager Modify<br/><br/>The possible error code for the interface in the returned body is
    one of the following error codes (non generic error codes): <br/>-35103  -  Rules should not be
    empty.<br/>-35104  -  Filter name already exist.

    Args:
        omadac_id (str):
        site_template_id (str):
        filter_id (str):
        body (EditFilterEntity):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_template_id=site_template_id,
        filter_id=filter_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
