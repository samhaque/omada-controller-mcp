from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    omadac_id: str,
    site_template_id: str,
    group_type: str,
    group_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/openapi/v1/{omadac_id}/sitetemplates/{site_template_id}/profiles/groups/{group_type}/{group_id}".format(
            omadac_id=quote(str(omadac_id), safe=""),
            site_template_id=quote(str(site_template_id), safe=""),
            group_type=quote(str(group_type), safe=""),
            group_id=quote(str(group_id), safe=""),
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
    site_template_id: str,
    group_type: str,
    group_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any]:
    """Delete an exist group profile template

     Delete an exist group profile template with the given params.<br/><br/>The interface requires one of
    the permissions: <br/>Global Site Template Manager Modify<br/><br/>The possible error code for the
    interface in the returned body is one of the following error codes (non generic error codes):
    <br/>-33009  -  This site template does not exist.<br/>-33011  -  Operation failed because other
    operations are being performed on this site template. Please wait and try again later.<br/>-33703  -
    This group does not exist.<br/>-33704  -  This group does not exist.<br/>-33705  -  Failed to delete
    this group because it is used in wireless network settings.<br/>-33717  -  This IP group has been
    used in the ACL rule.<br/>-33718  -  This IP-Port group has been used in the ACL rule.<br/>-33719  -
    This MAC group has been used in the ACL rule.<br/>-33720  -  This IP group has been used in URL
    filtering rule.<br/>-33721  -  This IP group has been used in Transmission settings.<br/>-33729  -
    Default IpGroup not allowed to be edited.<br/>-33741  -  This IP-Port group has been used in Policy
    Routing.<br/>-33762  -  This IPv6 group has been used in QoS class rule.<br/>-33764  -  This IP
    group has been used in QoS class rule.<br/>-33768  -  This IPv6 group has been used in the ACL
    rule.<br/>-33769  -  This IPv6 port group has been used in the ACL rule.<br/>-33771  -  This Country
    group has been used in the ACL rule.<br/>-33775  -  Cannot delete the MAC group because it is used
    in the MAC Filtering.<br/>-33816  -  Default domain group not allowed to be edited.<br/>-33818  -
    This domain group has been used in the ACL rule.

    Args:
        omadac_id (str):
        site_template_id (str):
        group_type (str):
        group_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_template_id=site_template_id,
        group_type=group_type,
        group_id=group_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    omadac_id: str,
    site_template_id: str,
    group_type: str,
    group_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any]:
    """Delete an exist group profile template

     Delete an exist group profile template with the given params.<br/><br/>The interface requires one of
    the permissions: <br/>Global Site Template Manager Modify<br/><br/>The possible error code for the
    interface in the returned body is one of the following error codes (non generic error codes):
    <br/>-33009  -  This site template does not exist.<br/>-33011  -  Operation failed because other
    operations are being performed on this site template. Please wait and try again later.<br/>-33703  -
    This group does not exist.<br/>-33704  -  This group does not exist.<br/>-33705  -  Failed to delete
    this group because it is used in wireless network settings.<br/>-33717  -  This IP group has been
    used in the ACL rule.<br/>-33718  -  This IP-Port group has been used in the ACL rule.<br/>-33719  -
    This MAC group has been used in the ACL rule.<br/>-33720  -  This IP group has been used in URL
    filtering rule.<br/>-33721  -  This IP group has been used in Transmission settings.<br/>-33729  -
    Default IpGroup not allowed to be edited.<br/>-33741  -  This IP-Port group has been used in Policy
    Routing.<br/>-33762  -  This IPv6 group has been used in QoS class rule.<br/>-33764  -  This IP
    group has been used in QoS class rule.<br/>-33768  -  This IPv6 group has been used in the ACL
    rule.<br/>-33769  -  This IPv6 port group has been used in the ACL rule.<br/>-33771  -  This Country
    group has been used in the ACL rule.<br/>-33775  -  Cannot delete the MAC group because it is used
    in the MAC Filtering.<br/>-33816  -  Default domain group not allowed to be edited.<br/>-33818  -
    This domain group has been used in the ACL rule.

    Args:
        omadac_id (str):
        site_template_id (str):
        group_type (str):
        group_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        omadac_id=omadac_id,
        site_template_id=site_template_id,
        group_type=group_type,
        group_id=group_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
