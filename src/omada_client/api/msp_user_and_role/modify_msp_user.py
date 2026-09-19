from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.modify_msp_user_vo import ModifyMspUserVO
from ...types import Response


def _get_kwargs(
    msp_id: str,
    user_id: str,
    *,
    body: ModifyMspUserVO,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/openapi/v1/msp/{msp_id}/users/{user_id}".format(
            msp_id=quote(str(msp_id), safe=""),
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
    msp_id: str,
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ModifyMspUserVO,
) -> Response[Any]:
    """Modify an existing msp user

     Modify an existing msp user. This interface only supports the authorization code mode, not the
    client mode. Please call this interface in authorization code mode.<br/><br/>The interface requires
    one of the permissions: <br/>MSP Users Manager Modify<br/><br/>The possible error code for the
    interface in the returned body is one of the following error codes (non generic error codes):
    <br/>-30103  -  Invalid email address.<br/>-30104  -  Invalid username.<br/>-30105  -  Invalid
    password.<br/>-30106  -  This username is already registered.<br/>-30108  -  This username does not
    exist.<br/>-30133  -  The account should not have privileges to fewer sites than its sub-
    users.<br/>-30134  -  Failed to add Site. Sub-users should not have privileges to more sites than
    their parent account.<br/>-30135  -  Are you sure you want to change the role of %Username% from
    Administrator to Viewer?If its role is changed, the viewer accounts it has created will be moved to
    your account.<br/>-30136  -  Failed to save. If the editing is saved, the viewer account will have
    privileges to more sites than that of its immediate superior account.<br/>-44118  -  This interface
    only supports the authorization code mode, not the client mode. Please call this interface in
    authorization code mode.

    Args:
        msp_id (str):
        user_id (str):
        body (ModifyMspUserVO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        msp_id=msp_id,
        user_id=user_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    msp_id: str,
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ModifyMspUserVO,
) -> Response[Any]:
    """Modify an existing msp user

     Modify an existing msp user. This interface only supports the authorization code mode, not the
    client mode. Please call this interface in authorization code mode.<br/><br/>The interface requires
    one of the permissions: <br/>MSP Users Manager Modify<br/><br/>The possible error code for the
    interface in the returned body is one of the following error codes (non generic error codes):
    <br/>-30103  -  Invalid email address.<br/>-30104  -  Invalid username.<br/>-30105  -  Invalid
    password.<br/>-30106  -  This username is already registered.<br/>-30108  -  This username does not
    exist.<br/>-30133  -  The account should not have privileges to fewer sites than its sub-
    users.<br/>-30134  -  Failed to add Site. Sub-users should not have privileges to more sites than
    their parent account.<br/>-30135  -  Are you sure you want to change the role of %Username% from
    Administrator to Viewer?If its role is changed, the viewer accounts it has created will be moved to
    your account.<br/>-30136  -  Failed to save. If the editing is saved, the viewer account will have
    privileges to more sites than that of its immediate superior account.<br/>-44118  -  This interface
    only supports the authorization code mode, not the client mode. Please call this interface in
    authorization code mode.

    Args:
        msp_id (str):
        user_id (str):
        body (ModifyMspUserVO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        msp_id=msp_id,
        user_id=user_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
