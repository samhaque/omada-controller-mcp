from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    site_id: str,
    survey_result_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/openapi/v1/{omadac_id}/sites/{site_id}/hotspot/surveys/auth-results/{survey_result_id}".format(
            omadac_id=quote(str(omadac_id), safe=""),
            site_id=quote(str(site_id), safe=""),
            survey_result_id=quote(str(survey_result_id), safe=""),
        ),
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
    survey_result_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any]:
    """Delete an authentication survey result for given surveyResultId

     Delete an authentication survey result in a site with given omadacId, siteId,
    surveyResultId.<br/><br/>The interface requires one of the permissions: <br/>Site Hotspot Manager
    Modify

    Args:
        omadac_id (str):
        site_id (str):
        survey_result_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        survey_result_id=survey_result_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    omadac_id: str,
    site_id: str,
    survey_result_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any]:
    """Delete an authentication survey result for given surveyResultId

     Delete an authentication survey result in a site with given omadacId, siteId,
    surveyResultId.<br/><br/>The interface requires one of the permissions: <br/>Site Hotspot Manager
    Modify

    Args:
        omadac_id (str):
        site_id (str):
        survey_result_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_id=site_id,
        survey_result_id=survey_result_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
