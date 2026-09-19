from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ap_mgt_ssid_enterprise_setting_open_api_vo import (
        ApMgtSsidEnterpriseSettingOpenApiVO,
    )
    from ..models.ap_mgt_ssid_psk_setting_open_api_vo import (
        ApMgtSsidPskSettingOpenApiVO,
    )
    from ..models.ap_mgt_ssid_vlan_setting_open_api_vo import (
        ApMgtSsidVlanSettingOpenApiVO,
    )


T = TypeVar("T", bound="ApManagementSsidConfig")


@_attrs_define
class ApManagementSsidConfig:
    """
    Attributes:
        status (bool): SSID config status. True: enable, false: disable.
        name (str): SSID name. It should contain 1 to 32 UTF-8 characters.
        security (int): SSID security mode; Security should be a value as follows: 0: None; 2: WPA-Enterprise; 3: WPA-
            Personal.
        broadcast (bool): SSID broadcast config status. True: enable, false: disable.
        psk_setting (ApMgtSsidPskSettingOpenApiVO | Unset): WPA-Personal SSID config. This is necessary when the value
            of security is 3(WPA-Personal).
        ent_setting (ApMgtSsidEnterpriseSettingOpenApiVO | Unset): WPA-Enterprise SSID config. This is necessary when
            the value of security is 2(WPA-Enterprise).
        vlan_setting (ApMgtSsidVlanSettingOpenApiVO | Unset): SSID VLAN configuration.
    """

    status: bool
    name: str
    security: int
    broadcast: bool
    psk_setting: ApMgtSsidPskSettingOpenApiVO | Unset = UNSET
    ent_setting: ApMgtSsidEnterpriseSettingOpenApiVO | Unset = UNSET
    vlan_setting: ApMgtSsidVlanSettingOpenApiVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        name = self.name

        security = self.security

        broadcast = self.broadcast

        psk_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.psk_setting, Unset):
            psk_setting = self.psk_setting.to_dict()

        ent_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ent_setting, Unset):
            ent_setting = self.ent_setting.to_dict()

        vlan_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.vlan_setting, Unset):
            vlan_setting = self.vlan_setting.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "name": name,
                "security": security,
                "broadcast": broadcast,
            }
        )
        if psk_setting is not UNSET:
            field_dict["pskSetting"] = psk_setting
        if ent_setting is not UNSET:
            field_dict["entSetting"] = ent_setting
        if vlan_setting is not UNSET:
            field_dict["vlanSetting"] = vlan_setting

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ap_mgt_ssid_enterprise_setting_open_api_vo import (
            ApMgtSsidEnterpriseSettingOpenApiVO,
        )
        from ..models.ap_mgt_ssid_psk_setting_open_api_vo import (
            ApMgtSsidPskSettingOpenApiVO,
        )
        from ..models.ap_mgt_ssid_vlan_setting_open_api_vo import (
            ApMgtSsidVlanSettingOpenApiVO,
        )

        d = dict(src_dict)
        status = d.pop("status")

        name = d.pop("name")

        security = d.pop("security")

        broadcast = d.pop("broadcast")

        _psk_setting = d.pop("pskSetting", UNSET)
        psk_setting: ApMgtSsidPskSettingOpenApiVO | Unset
        if isinstance(_psk_setting, Unset):
            psk_setting = UNSET
        else:
            psk_setting = ApMgtSsidPskSettingOpenApiVO.from_dict(_psk_setting)

        _ent_setting = d.pop("entSetting", UNSET)
        ent_setting: ApMgtSsidEnterpriseSettingOpenApiVO | Unset
        if isinstance(_ent_setting, Unset):
            ent_setting = UNSET
        else:
            ent_setting = ApMgtSsidEnterpriseSettingOpenApiVO.from_dict(_ent_setting)

        _vlan_setting = d.pop("vlanSetting", UNSET)
        vlan_setting: ApMgtSsidVlanSettingOpenApiVO | Unset
        if isinstance(_vlan_setting, Unset):
            vlan_setting = UNSET
        else:
            vlan_setting = ApMgtSsidVlanSettingOpenApiVO.from_dict(_vlan_setting)

        ap_management_ssid_config = cls(
            status=status,
            name=name,
            security=security,
            broadcast=broadcast,
            psk_setting=psk_setting,
            ent_setting=ent_setting,
            vlan_setting=vlan_setting,
        )

        ap_management_ssid_config.additional_properties = d
        return ap_management_ssid_config

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
