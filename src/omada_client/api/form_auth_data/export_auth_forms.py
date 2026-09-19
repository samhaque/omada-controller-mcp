from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.export_form_open_api_vo import ExportFormOpenApiVO
from ...types import UNSET, Response


def _get_kwargs(
    omadac_id: str,
    site_id: str,
    form_id: str,
    *,
    export_form_vo: ExportFormOpenApiVO,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_export_form_vo = export_form_vo.to_dict()
    params.update(json_export_form_vo)

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/openapi/v1/{omadac_id}/sites/{site_id}/files/hotspot/form-auths/{form_id}/export".format(
            omadac_id=quote(str(omadac_id), safe=""),
            site_id=quote(str(site_id), safe=""),
            form_id=quote(str(form_id), safe=""),
        ),
        "params": params,
    }

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
    site_id: str,
    form_id: str,
    *,
    client: AuthenticatedClient | Client,
    export_form_vo: ExportFormOpenApiVO,
) -> Response[Any]:
    """Export the Form Authentication Result List

     Export the Form Authentication Result List.<br/><br/>The interface requires one of the permissions:
    <br/>Site Hotspot Manager View Only

    Args:
        omadac_id (str):
        site_id (str):
        form_id (str):
        export_form_vo (ExportFormOpenApiVO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        form_id=form_id,
        export_form_vo=export_form_vo,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    omadac_id: str,
    site_id: str,
    form_id: str,
    *,
    client: AuthenticatedClient | Client,
    export_form_vo: ExportFormOpenApiVO,
) -> Response[Any]:
    """Export the Form Authentication Result List

     Export the Form Authentication Result List.<br/><br/>The interface requires one of the permissions:
    <br/>Site Hotspot Manager View Only

    Args:
        omadac_id (str):
        site_id (str):
        form_id (str):
        export_form_vo (ExportFormOpenApiVO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        form_id=form_id,
        export_form_vo=export_form_vo,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
