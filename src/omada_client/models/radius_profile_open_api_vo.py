from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.radius_acct_server_open_api_vo import RadiusAcctServerOpenApiVO
    from ..models.radius_auth_server_open_api_vo import RadiusAuthServerOpenApiVO


T = TypeVar("T", bound="RadiusProfileOpenApiVO")


@_attrs_define
class RadiusProfileOpenApiVO:
    """
    Attributes:
        radius_profile_id (str | Unset): Radius profile ID
        name (str | Unset): Radius profile name
        auth_server (list[RadiusAuthServerOpenApiVO] | Unset): Radius authentication server list
        radius_accounting_enable (bool | Unset): Radius accounting enable status
        interim_update_enable (bool | Unset): When radius accounting enables, interval update enable status
        interim_update_interval (int | Unset): When interval update enables, interval update duration
        acct_server (list[RadiusAcctServerOpenApiVO] | Unset): Radius accounting server list, valid when parameter
            [radiusAccountingEnable] is true
        wireless_vlan_assignment (bool | Unset): VLAN assignment for wireless network enable status
        domain_enable (bool | Unset): Domain enable status
        coa_enable (bool | Unset): Radius CoA enable status
        coa_password (str | Unset): Radius CoA password, valid when parameter [coaEnable] is true
        built_in_server (bool | Unset): Is this RADIUS server a built-in server
        server_enable (bool | Unset): Built-in RADIUS server enable status, valid when parameter [builtInServer] is true
        tunnel_reply_enable (bool | Unset): Built-in RADIUS server tunneled reply enable status, valid when parameter
            [builtInServer] is true
        built_in_server_secret (str | Unset): Built-in RADIUS server secret, valid when parameter [builtInServer] is
            true
        ip_type (int | Unset): Built-in RADIUS server IP type, 0: auto，1: custom, valid when parameter [builtInServer]
            is true
        custom_ip (str | Unset): Built-in RADIUS server custom IP, valid when parameter [builtInServer] is true and
            [ipType] is 1
        require_message_authenticator (bool | Unset): Message-Authenticator enable status
    """

    radius_profile_id: str | Unset = UNSET
    name: str | Unset = UNSET
    auth_server: list[RadiusAuthServerOpenApiVO] | Unset = UNSET
    radius_accounting_enable: bool | Unset = UNSET
    interim_update_enable: bool | Unset = UNSET
    interim_update_interval: int | Unset = UNSET
    acct_server: list[RadiusAcctServerOpenApiVO] | Unset = UNSET
    wireless_vlan_assignment: bool | Unset = UNSET
    domain_enable: bool | Unset = UNSET
    coa_enable: bool | Unset = UNSET
    coa_password: str | Unset = UNSET
    built_in_server: bool | Unset = UNSET
    server_enable: bool | Unset = UNSET
    tunnel_reply_enable: bool | Unset = UNSET
    built_in_server_secret: str | Unset = UNSET
    ip_type: int | Unset = UNSET
    custom_ip: str | Unset = UNSET
    require_message_authenticator: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        radius_profile_id = self.radius_profile_id

        name = self.name

        auth_server: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.auth_server, Unset):
            auth_server = []
            for auth_server_item_data in self.auth_server:
                auth_server_item = auth_server_item_data.to_dict()
                auth_server.append(auth_server_item)

        radius_accounting_enable = self.radius_accounting_enable

        interim_update_enable = self.interim_update_enable

        interim_update_interval = self.interim_update_interval

        acct_server: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.acct_server, Unset):
            acct_server = []
            for acct_server_item_data in self.acct_server:
                acct_server_item = acct_server_item_data.to_dict()
                acct_server.append(acct_server_item)

        wireless_vlan_assignment = self.wireless_vlan_assignment

        domain_enable = self.domain_enable

        coa_enable = self.coa_enable

        coa_password = self.coa_password

        built_in_server = self.built_in_server

        server_enable = self.server_enable

        tunnel_reply_enable = self.tunnel_reply_enable

        built_in_server_secret = self.built_in_server_secret

        ip_type = self.ip_type

        custom_ip = self.custom_ip

        require_message_authenticator = self.require_message_authenticator

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if radius_profile_id is not UNSET:
            field_dict["radiusProfileId"] = radius_profile_id
        if name is not UNSET:
            field_dict["name"] = name
        if auth_server is not UNSET:
            field_dict["authServer"] = auth_server
        if radius_accounting_enable is not UNSET:
            field_dict["radiusAccountingEnable"] = radius_accounting_enable
        if interim_update_enable is not UNSET:
            field_dict["interimUpdateEnable"] = interim_update_enable
        if interim_update_interval is not UNSET:
            field_dict["interimUpdateInterval"] = interim_update_interval
        if acct_server is not UNSET:
            field_dict["acctServer"] = acct_server
        if wireless_vlan_assignment is not UNSET:
            field_dict["wirelessVlanAssignment"] = wireless_vlan_assignment
        if domain_enable is not UNSET:
            field_dict["domainEnable"] = domain_enable
        if coa_enable is not UNSET:
            field_dict["coaEnable"] = coa_enable
        if coa_password is not UNSET:
            field_dict["coaPassword"] = coa_password
        if built_in_server is not UNSET:
            field_dict["builtInServer"] = built_in_server
        if server_enable is not UNSET:
            field_dict["serverEnable"] = server_enable
        if tunnel_reply_enable is not UNSET:
            field_dict["tunnelReplyEnable"] = tunnel_reply_enable
        if built_in_server_secret is not UNSET:
            field_dict["builtInServerSecret"] = built_in_server_secret
        if ip_type is not UNSET:
            field_dict["ipType"] = ip_type
        if custom_ip is not UNSET:
            field_dict["customIp"] = custom_ip
        if require_message_authenticator is not UNSET:
            field_dict["requireMessageAuthenticator"] = require_message_authenticator

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.radius_acct_server_open_api_vo import (
            RadiusAcctServerOpenApiVO,
        )
        from ..models.radius_auth_server_open_api_vo import (
            RadiusAuthServerOpenApiVO,
        )

        d = dict(src_dict)
        radius_profile_id = d.pop("radiusProfileId", UNSET)

        name = d.pop("name", UNSET)

        _auth_server = d.pop("authServer", UNSET)
        auth_server: list[RadiusAuthServerOpenApiVO] | Unset = UNSET
        if _auth_server is not UNSET:
            auth_server = []
            for auth_server_item_data in _auth_server:
                auth_server_item = RadiusAuthServerOpenApiVO.from_dict(
                    auth_server_item_data
                )

                auth_server.append(auth_server_item)

        radius_accounting_enable = d.pop("radiusAccountingEnable", UNSET)

        interim_update_enable = d.pop("interimUpdateEnable", UNSET)

        interim_update_interval = d.pop("interimUpdateInterval", UNSET)

        _acct_server = d.pop("acctServer", UNSET)
        acct_server: list[RadiusAcctServerOpenApiVO] | Unset = UNSET
        if _acct_server is not UNSET:
            acct_server = []
            for acct_server_item_data in _acct_server:
                acct_server_item = RadiusAcctServerOpenApiVO.from_dict(
                    acct_server_item_data
                )

                acct_server.append(acct_server_item)

        wireless_vlan_assignment = d.pop("wirelessVlanAssignment", UNSET)

        domain_enable = d.pop("domainEnable", UNSET)

        coa_enable = d.pop("coaEnable", UNSET)

        coa_password = d.pop("coaPassword", UNSET)

        built_in_server = d.pop("builtInServer", UNSET)

        server_enable = d.pop("serverEnable", UNSET)

        tunnel_reply_enable = d.pop("tunnelReplyEnable", UNSET)

        built_in_server_secret = d.pop("builtInServerSecret", UNSET)

        ip_type = d.pop("ipType", UNSET)

        custom_ip = d.pop("customIp", UNSET)

        require_message_authenticator = d.pop("requireMessageAuthenticator", UNSET)

        radius_profile_open_api_vo = cls(
            radius_profile_id=radius_profile_id,
            name=name,
            auth_server=auth_server,
            radius_accounting_enable=radius_accounting_enable,
            interim_update_enable=interim_update_enable,
            interim_update_interval=interim_update_interval,
            acct_server=acct_server,
            wireless_vlan_assignment=wireless_vlan_assignment,
            domain_enable=domain_enable,
            coa_enable=coa_enable,
            coa_password=coa_password,
            built_in_server=built_in_server,
            server_enable=server_enable,
            tunnel_reply_enable=tunnel_reply_enable,
            built_in_server_secret=built_in_server_secret,
            ip_type=ip_type,
            custom_ip=custom_ip,
            require_message_authenticator=require_message_authenticator,
        )

        radius_profile_open_api_vo.additional_properties = d
        return radius_profile_open_api_vo

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
