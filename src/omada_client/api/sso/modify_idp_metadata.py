from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.idp_metadata_open_api_vo import IdpMetadataOpenApiVO
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    idp_id: str,
    *,
    body: IdpMetadataOpenApiVO,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/openapi/v1/{omadac_id}/sso/saml-idps/{idp_id}".format(
            omadac_id=quote(str(omadac_id), safe=""),
            idp_id=quote(str(idp_id), safe=""),
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
    idp_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: IdpMetadataOpenApiVO,
) -> Response[Any]:
    """Modify an existing idp

     Modify an existing idp.<br/><br/>The interface requires one of the permissions: <br/>Global Saml SSO
    Manager Modify<br/><br/>The possible error code for the interface in the returned body is one of the
    following error codes (non generic error codes): <br/>-30170  -  The SAML sso metadata entityId
    already exists.<br/>-30171  -  The SAML sso metadata name already exist.

    Args:
        omadac_id (str):
        idp_id (str):
        body (IdpMetadataOpenApiVO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        idp_id=idp_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    omadac_id: str,
    idp_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: IdpMetadataOpenApiVO,
) -> Response[Any]:
    """Modify an existing idp

     Modify an existing idp.<br/><br/>The interface requires one of the permissions: <br/>Global Saml SSO
    Manager Modify<br/><br/>The possible error code for the interface in the returned body is one of the
    following error codes (non generic error codes): <br/>-30170  -  The SAML sso metadata entityId
    already exists.<br/>-30171  -  The SAML sso metadata name already exist.

    Args:
        omadac_id (str):
        idp_id (str):
        body (IdpMetadataOpenApiVO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        idp_id=idp_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
