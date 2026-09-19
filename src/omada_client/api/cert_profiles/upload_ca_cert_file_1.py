from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.upload_ca_cert_file_1_body import UploadCaCertFile1Body
from ...types import UNSET, Response, Unset


def _get_kwargs(
    omadac_id: str,
    site_id: str,
    *,
    body: UploadCaCertFile1Body | Unset = UNSET,
    data: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["data"] = data

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/openapi/v1/{omadac_id}/files/sites/{site_id}/setting/profiles/cert-profiles/ca-cert".format(
            omadac_id=quote(str(omadac_id), safe=""),
            site_id=quote(str(site_id), safe=""),
        ),
        "params": params,
    }

    if not isinstance(body, Unset):
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
    site_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UploadCaCertFile1Body | Unset = UNSET,
    data: str,
) -> Response[Any]:
    """Upload CA profile file

     Upload CA profile file of the omadac with the given omadacId.<br/><br/>The interface requires one of
    the permissions: <br/>Network Config Page Modify<br/>Site Settings Manager Modify<br/><br/>The
    possible error code for the interface in the returned body is one of the following error codes (non
    generic error codes): <br/>-30025  -  Failed to import the certificate.<br/>-30028  -  Operation
    failed because other operations (backuping, site copying, customer copying, etc.) are being
    performed on this organization. Please wait and try again later.<br/>-33796  -  The size of the
    certificate file has exceeded the limit. It should be less than 10KB.<br/>-33797  -  The certificate
    file cannot be parsed, please check the file or try uploading another file

    Args:
        omadac_id (str):
        site_id (str):
        data (str):
        body (UploadCaCertFile1Body | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        body=body,
        data=data,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    omadac_id: str,
    site_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UploadCaCertFile1Body | Unset = UNSET,
    data: str,
) -> Response[Any]:
    """Upload CA profile file

     Upload CA profile file of the omadac with the given omadacId.<br/><br/>The interface requires one of
    the permissions: <br/>Network Config Page Modify<br/>Site Settings Manager Modify<br/><br/>The
    possible error code for the interface in the returned body is one of the following error codes (non
    generic error codes): <br/>-30025  -  Failed to import the certificate.<br/>-30028  -  Operation
    failed because other operations (backuping, site copying, customer copying, etc.) are being
    performed on this organization. Please wait and try again later.<br/>-33796  -  The size of the
    certificate file has exceeded the limit. It should be less than 10KB.<br/>-33797  -  The certificate
    file cannot be parsed, please check the file or try uploading another file

    Args:
        omadac_id (str):
        site_id (str):
        data (str):
        body (UploadCaCertFile1Body | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        body=body,
        data=data,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
