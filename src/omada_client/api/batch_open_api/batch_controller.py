from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.batch_request_entity import BatchRequestEntity
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    *,
    body: BatchRequestEntity,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/openapi/v1/{omadac_id}/batch".format(
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
    body: BatchRequestEntity,
) -> Response[Any]:
    """Batch Processing OpenAPIs

     Batch processing of multiple OpenAPIs under the same Omada controller through this
    OpenAPI.<br/><br/>The possible error code for the interface in the returned body is one of the
    following error codes (non generic error codes): <br/>-1001  -  Invalid request
    parameters.<br/>-1600  -  Unsupported request path.<br/>-1619  -  Execution has been interrupted due
    to unsuccessful execution of the pre action request.<br/>-1620  -  Error occurred while executing
    action.<br/>-44112  -  The access token has expired. Please re-initiate the refreshToken process to
    obtain the access token.<br/>-44113  -  The Access Token is Invalid.<br/>-7132  -  Our server is
    receiving too many requests now. Please try again later.

    Args:
        omadac_id (str):
        body (BatchRequestEntity):

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
    body: BatchRequestEntity,
) -> Response[Any]:
    """Batch Processing OpenAPIs

     Batch processing of multiple OpenAPIs under the same Omada controller through this
    OpenAPI.<br/><br/>The possible error code for the interface in the returned body is one of the
    following error codes (non generic error codes): <br/>-1001  -  Invalid request
    parameters.<br/>-1600  -  Unsupported request path.<br/>-1619  -  Execution has been interrupted due
    to unsuccessful execution of the pre action request.<br/>-1620  -  Error occurred while executing
    action.<br/>-44112  -  The access token has expired. Please re-initiate the refreshToken process to
    obtain the access token.<br/>-44113  -  The Access Token is Invalid.<br/>-7132  -  Our server is
    receiving too many requests now. Please try again later.

    Args:
        omadac_id (str):
        body (BatchRequestEntity):

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
