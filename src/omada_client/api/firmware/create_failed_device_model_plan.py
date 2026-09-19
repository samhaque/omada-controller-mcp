from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.failed_create_model_plan_upgrade_info import (
    FailedCreateModelPlanUpgradeInfo,
)
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    upgrade_log_id: str,
    *,
    body: FailedCreateModelPlanUpgradeInfo,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/openapi/v1/{omadac_id}/logs/{upgrade_log_id}/upgrade/overview/failed-model-plan".format(
            omadac_id=quote(str(omadac_id), safe=""),
            upgrade_log_id=quote(str(upgrade_log_id), safe=""),
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
    upgrade_log_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: FailedCreateModelPlanUpgradeInfo,
) -> Response[Any]:
    """Create Upgrade Plan for Failed Device

     Create Upgrade Plan for Failed Device<br/><br/>The interface requires one of the permissions:
    <br/>Site Manual Firmware Upgrade Modify<br/><br/>The possible error code for the interface in the
    returned body is one of the following error codes (non generic error codes): <br/>-1001  -  Invalid
    request parameters.<br/>-1005  -  Operation forbidden.<br/>-30028  -  Operation failed because other
    operations (backuping, site copying, customer copying, etc.) are being performed on this
    organization. Please wait and try again later.<br/>-39061  -  The target firmware has been
    removed/deleted. Please reset the rule.

    Args:
        omadac_id (str):
        upgrade_log_id (str):
        body (FailedCreateModelPlanUpgradeInfo):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        upgrade_log_id=upgrade_log_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    omadac_id: str,
    upgrade_log_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: FailedCreateModelPlanUpgradeInfo,
) -> Response[Any]:
    """Create Upgrade Plan for Failed Device

     Create Upgrade Plan for Failed Device<br/><br/>The interface requires one of the permissions:
    <br/>Site Manual Firmware Upgrade Modify<br/><br/>The possible error code for the interface in the
    returned body is one of the following error codes (non generic error codes): <br/>-1001  -  Invalid
    request parameters.<br/>-1005  -  Operation forbidden.<br/>-30028  -  Operation failed because other
    operations (backuping, site copying, customer copying, etc.) are being performed on this
    organization. Please wait and try again later.<br/>-39061  -  The target firmware has been
    removed/deleted. Please reset the rule.

    Args:
        omadac_id (str):
        upgrade_log_id (str):
        body (FailedCreateModelPlanUpgradeInfo):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        upgrade_log_id=upgrade_log_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
