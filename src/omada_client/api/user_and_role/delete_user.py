from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_user_vo import DeleteUserVO
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    user_id: str,
    *,
    body: DeleteUserVO,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/openapi/v1/{omadac_id}/users/{user_id}".format(
            omadac_id=quote(str(omadac_id), safe=""),
            user_id=quote(str(user_id), safe=""),
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
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DeleteUserVO,
) -> Response[Any]:
    """Delete an existing user

     Delete an existing user. This interface only supports the authorization code mode, not the client
    mode. Please call this interface in authorization code mode.<br/><br/>The interface requires one of
    the permissions: <br/>Global Users Manager Modify<br/><br/>The possible error code for the interface
    in the returned body is one of the following error codes (non generic error codes): <br/>-30112  -
    This user does not exist.<br/>-30114  -  An error occurred while deleting the user.<br/>-30132  -
    Are you sure you want to delete the account %Username%? Once deleted, all sub-users created by this
    account will be transferred to your account.<br/>-44118  -  This interface only supports the
    authorization code mode, not the client mode. Please call this interface in authorization code mode.

    Args:
        omadac_id (str):
        user_id (str):
        body (DeleteUserVO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        user_id=user_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    omadac_id: str,
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DeleteUserVO,
) -> Response[Any]:
    """Delete an existing user

     Delete an existing user. This interface only supports the authorization code mode, not the client
    mode. Please call this interface in authorization code mode.<br/><br/>The interface requires one of
    the permissions: <br/>Global Users Manager Modify<br/><br/>The possible error code for the interface
    in the returned body is one of the following error codes (non generic error codes): <br/>-30112  -
    This user does not exist.<br/>-30114  -  An error occurred while deleting the user.<br/>-30132  -
    Are you sure you want to delete the account %Username%? Once deleted, all sub-users created by this
    account will be transferred to your account.<br/>-44118  -  This interface only supports the
    authorization code mode, not the client mode. Please call this interface in authorization code mode.

    Args:
        omadac_id (str):
        user_id (str):
        body (DeleteUserVO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        user_id=user_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
