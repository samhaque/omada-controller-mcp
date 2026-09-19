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


T = TypeVar("T", bound="CreateRadiusProfileOpenApiVO")


@_attrs_define
class CreateRadiusProfileOpenApiVO:
    """
    Attributes:
        name (str): Radius profile name should contain 1 to 64 characters
        auth_server (list[RadiusAuthServerOpenApiVO]): Radius authentication server list
        radius_accounting_enable (bool): Radius accounting enable status
        wireless_vlan_assignment (bool): VLAN assignment for wireless network enable status
        interim_update_enable (bool | Unset): When radius accounting enables, interval update enable status
        interim_update_interval (int | Unset): When interval update enables, interval update duration, unit: second.
            InterimUpdateInterval should be within the range of 60-86400
        acct_server (list[RadiusAcctServerOpenApiVO] | Unset): Radius accounting server list, valid when parameter
            [radiusAccountingEnable] is true
        coa_enable (bool | Unset): Radius CoA enable status
        coa_password (str | Unset): Radius CoA password, required when parameter [coaEnable] is true. CoaPassword should
            contain 1 to 128 characters. The question mark (?), double quote ("), percent sign (%), and backslash (\\) may
            cause the RADIUS function to fail and are not recommended.
        require_message_authenticator (bool | Unset): Message-Authenticator enable status
    """

    name: str
    auth_server: list[RadiusAuthServerOpenApiVO]
    radius_accounting_enable: bool
    wireless_vlan_assignment: bool
    interim_update_enable: bool | Unset = UNSET
    interim_update_interval: int | Unset = UNSET
    acct_server: list[RadiusAcctServerOpenApiVO] | Unset = UNSET
    coa_enable: bool | Unset = UNSET
    coa_password: str | Unset = UNSET
    require_message_authenticator: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        auth_server = []
        for auth_server_item_data in self.auth_server:
            auth_server_item = auth_server_item_data.to_dict()
            auth_server.append(auth_server_item)

        radius_accounting_enable = self.radius_accounting_enable

        wireless_vlan_assignment = self.wireless_vlan_assignment

        interim_update_enable = self.interim_update_enable

        interim_update_interval = self.interim_update_interval

        acct_server: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.acct_server, Unset):
            acct_server = []
            for acct_server_item_data in self.acct_server:
                acct_server_item = acct_server_item_data.to_dict()
                acct_server.append(acct_server_item)

        coa_enable = self.coa_enable

        coa_password = self.coa_password

        require_message_authenticator = self.require_message_authenticator

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "authServer": auth_server,
                "radiusAccountingEnable": radius_accounting_enable,
                "wirelessVlanAssignment": wireless_vlan_assignment,
            }
        )
        if interim_update_enable is not UNSET:
            field_dict["interimUpdateEnable"] = interim_update_enable
        if interim_update_interval is not UNSET:
            field_dict["interimUpdateInterval"] = interim_update_interval
        if acct_server is not UNSET:
            field_dict["acctServer"] = acct_server
        if coa_enable is not UNSET:
            field_dict["coaEnable"] = coa_enable
        if coa_password is not UNSET:
            field_dict["coaPassword"] = coa_password
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
        name = d.pop("name")

        auth_server = []
        _auth_server = d.pop("authServer")
        for auth_server_item_data in _auth_server:
            auth_server_item = RadiusAuthServerOpenApiVO.from_dict(
                auth_server_item_data
            )

            auth_server.append(auth_server_item)

        radius_accounting_enable = d.pop("radiusAccountingEnable")

        wireless_vlan_assignment = d.pop("wirelessVlanAssignment")

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

        coa_enable = d.pop("coaEnable", UNSET)

        coa_password = d.pop("coaPassword", UNSET)

        require_message_authenticator = d.pop("requireMessageAuthenticator", UNSET)

        create_radius_profile_open_api_vo = cls(
            name=name,
            auth_server=auth_server,
            radius_accounting_enable=radius_accounting_enable,
            wireless_vlan_assignment=wireless_vlan_assignment,
            interim_update_enable=interim_update_enable,
            interim_update_interval=interim_update_interval,
            acct_server=acct_server,
            coa_enable=coa_enable,
            coa_password=coa_password,
            require_message_authenticator=require_message_authenticator,
        )

        create_radius_profile_open_api_vo.additional_properties = d
        return create_radius_profile_open_api_vo

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
