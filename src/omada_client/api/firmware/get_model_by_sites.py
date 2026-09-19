from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.upgrade_site_model_req_info import UpgradeSiteModelReqInfo
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    *,
    body: UpgradeSiteModelReqInfo,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/openapi/v1/{omadac_id}/upgrade/models".format(
            omadac_id=quote(str(omadac_id), safe=""),
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
    *,
    client: AuthenticatedClient | Client,
    body: UpgradeSiteModelReqInfo,
) -> Response[Any]:
    """Get the model of the specified site

     Get the model of the specified site. If no site is specified, it defaults to all authorized
    sites<br/><br/>The interface requires one of the permissions: <br/>Site Manual Firmware Upgrade View
    Only

    Args:
        omadac_id (str):
        body (UpgradeSiteModelReqInfo):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    omadac_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpgradeSiteModelReqInfo,
) -> Response[Any]:
    """Get the model of the specified site

     Get the model of the specified site. If no site is specified, it defaults to all authorized
    sites<br/><br/>The interface requires one of the permissions: <br/>Site Manual Firmware Upgrade View
    Only

    Args:
        omadac_id (str):
        body (UpgradeSiteModelReqInfo):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
