from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.iptv_setting_open_api_vo import IptvSettingOpenApiVO
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    site_template_id: str,
    *,
    body: IptvSettingOpenApiVO,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/openapi/v1/{omadac_id}/sitetemplates/{site_template_id}/setting/service/iptv".format(
            omadac_id=quote(str(omadac_id), safe=""),
            site_template_id=quote(str(site_template_id), safe=""),
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
    *,
    client: AuthenticatedClient | Client,
    body: IptvSettingOpenApiVO,
) -> Response[Any]:
    """Modify IPTV setting template

     Modify IPTV setting template with the given omadacId and siteTemplateId. There should be a gateway
    template model preconfigured, or else you cannot modify IPTV template setting.<br/><br/>The
    interface requires one of the permissions: <br/>Global Site Template Manager Modify<br/><br/>The
    possible error code for the interface in the returned body is one of the following error codes (non
    generic error codes): <br/>-33010  -  This site template does not support current
    function.<br/>-33013  -  This name already exists in this site template.

    Args:
        omadac_id (str):
        site_template_id (str):
        body (IptvSettingOpenApiVO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_template_id=site_template_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    omadac_id: str,
    site_template_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: IptvSettingOpenApiVO,
) -> Response[Any]:
    """Modify IPTV setting template

     Modify IPTV setting template with the given omadacId and siteTemplateId. There should be a gateway
    template model preconfigured, or else you cannot modify IPTV template setting.<br/><br/>The
    interface requires one of the permissions: <br/>Global Site Template Manager Modify<br/><br/>The
    possible error code for the interface in the returned body is one of the following error codes (non
    generic error codes): <br/>-33010  -  This site template does not support current
    function.<br/>-33013  -  This name already exists in this site template.

    Args:
        omadac_id (str):
        site_template_id (str):
        body (IptvSettingOpenApiVO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_template_id=site_template_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
