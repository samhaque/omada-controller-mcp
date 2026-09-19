from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.modify_role_vo import ModifyRoleVO
from ...types import Response


def _get_kwargs(
    msp_id: str,
    role_id: str,
    *,
    body: ModifyRoleVO,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/openapi/v1/msp/{msp_id}/roles/{role_id}".format(
            msp_id=quote(str(msp_id), safe=""),
            role_id=quote(str(role_id), safe=""),
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
    msp_id: str,
    role_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ModifyRoleVO,
) -> Response[Any]:
    """Modify an existing msp role

     Modify an existing msp role.<br/><br/>The interface requires one of the permissions: <br/>MSP Roles
    Manager Modify<br/><br/>The possible error code for the interface in the returned body is one of the
    following error codes (non generic error codes): <br/>-30102  -  This role does not
    exist.<br/>-30156  -  This role already exists.<br/>-30157  -  An error occurred while modifying the
    role.<br/>-30159  -  The default role cannot be modified.<br/>-30162  -  Cannot change the target
    account. An account with user management permission must have a role permission scope that covers
    its sub-users.

    Args:
        msp_id (str):
        role_id (str):
        body (ModifyRoleVO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        msp_id=msp_id,
        role_id=role_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    msp_id: str,
    role_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ModifyRoleVO,
) -> Response[Any]:
    """Modify an existing msp role

     Modify an existing msp role.<br/><br/>The interface requires one of the permissions: <br/>MSP Roles
    Manager Modify<br/><br/>The possible error code for the interface in the returned body is one of the
    following error codes (non generic error codes): <br/>-30102  -  This role does not
    exist.<br/>-30156  -  This role already exists.<br/>-30157  -  An error occurred while modifying the
    role.<br/>-30159  -  The default role cannot be modified.<br/>-30162  -  Cannot change the target
    account. An account with user management permission must have a role permission scope that covers
    its sub-users.

    Args:
        msp_id (str):
        role_id (str):
        body (ModifyRoleVO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        msp_id=msp_id,
        role_id=role_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
