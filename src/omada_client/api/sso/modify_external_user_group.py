from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.external_user_group_open_api_vo import ExternalUserGroupOpenApiVO
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    external_user_group_id: str,
    *,
    body: ExternalUserGroupOpenApiVO,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/openapi/v1/{omadac_id}/sso/external-user-groups/{external_user_group_id}".format(
            omadac_id=quote(str(omadac_id), safe=""),
            external_user_group_id=quote(str(external_user_group_id), safe=""),
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
    external_user_group_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ExternalUserGroupOpenApiVO,
) -> Response[Any]:
    """Modify an existing external user group

     Modify an existing external user group.<br/><br/>The interface requires one of the permissions:
    <br/>Global Saml Roles Manager Modify<br/><br/>The possible error code for the interface in the
    returned body is one of the following error codes (non generic error codes): <br/>-30102  -  This
    role does not exist.<br/>-30172  -  The SAML User Group name already exists.

    Args:
        omadac_id (str):
        external_user_group_id (str):
        body (ExternalUserGroupOpenApiVO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        external_user_group_id=external_user_group_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    omadac_id: str,
    external_user_group_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ExternalUserGroupOpenApiVO,
) -> Response[Any]:
    """Modify an existing external user group

     Modify an existing external user group.<br/><br/>The interface requires one of the permissions:
    <br/>Global Saml Roles Manager Modify<br/><br/>The possible error code for the interface in the
    returned body is one of the following error codes (non generic error codes): <br/>-30102  -  This
    role does not exist.<br/>-30172  -  The SAML User Group name already exists.

    Args:
        omadac_id (str):
        external_user_group_id (str):
        body (ExternalUserGroupOpenApiVO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        external_user_group_id=external_user_group_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
