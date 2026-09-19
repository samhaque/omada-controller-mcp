from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.client_active_timeout import ClientActiveTimeout
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    *,
    body: ClientActiveTimeout,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/openapi/v1/{omadac_id}/controller/setting/active-timeout".format(
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
    body: ClientActiveTimeout,
) -> Response[Any]:
    """Modify an existing client active timeout

     Modify an existing client active timeout.<br/><br/>The interface requires one of the permissions:
    <br/>Global Other Setting Modify

    Args:
        omadac_id (str):
        body (ClientActiveTimeout):

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
    body: ClientActiveTimeout,
) -> Response[Any]:
    """Modify an existing client active timeout

     Modify an existing client active timeout.<br/><br/>The interface requires one of the permissions:
    <br/>Global Other Setting Modify

    Args:
        omadac_id (str):
        body (ClientActiveTimeout):

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
