from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cond_broadcast_ctrl_vo import CondBroadcastCtrlVO
    from ..models.ssid_enterprise_setting_open_api_vo import (
        SsidEnterpriseSettingOpenApiVO,
    )
    from ..models.ssid_ppsk_setting_open_api_vo import SsidPpskSettingOpenApiVO
    from ..models.ssid_psk_setting_open_api_vo import SsidPskSettingOpenApiVO
    from ..models.ssid_vlan_setting_open_api_vo import SsidVlanSettingOpenApiVO


T = TypeVar("T", bound="UpdateSsidBasicConfigOpenApiVO")


@_attrs_define
class UpdateSsidBasicConfigOpenApiVO:
    """
    Attributes:
        name (str): SSID name. It should contain 1 to 32 UTF-8 characters.
        band (int): SSID band. The lowest bit indicates whether 2.4G is included; the second lowest bit indicates
            whether 5G is included; the third lowest bit indicates whether 6G is included; 1 means included while 0 means
            not included. For example, 7(111) means that 2G/5G/6G are enabled; 1(001) means that 2G is enabled. (When 5G is
            included，it means 5G/5G1/5G2 are enabled.)
        guest_net_enable (bool): SSID guest network config status. True: enable, false: disable.
        security (int): SSID security mode; Security should be a value as follows: 0: None; 2: WPA-Enterprise; 3: WPA-
            Personal; 4: PPSK without RADIUS; 5: PPSK with RADIUS.
        broadcast (bool): SSID broadcast config status. True: enable, false: disable.
        vlan_enable (bool): SSID VLAN config status. True: enable, false: disable.
        mlo_enable (bool): SSID MLO config status. True: enable, false: disable.
        pmf_mode (int): SSID PMF mode. It should be a value as follows: 1: Mandatory; 2: Capable; 3: Disable.
        enable11r (bool): SSID 802.11r config status. True: enable, false: disable.
        auto_wan_access (bool | Unset): Whether to enable auto wan access. True: enable, false: disable.
        owe_enable (bool | Unset): Opportunistic Wireless Encryption, also known as Enhanced Open, is a certification
            provided by the Wi-Fi Alliance as part of the WPA3 wireless security standard. OWE will enable two wireless VAPs
            per radio, one for access of OWE-supported stations, and one for access of other stations. An SSID with OWE
            enabled will be counted as two SSID entries for 2G and 5G. Only for security is None and band contains 2.4G or
            5G.
        vlan_id (int | Unset): SSID VLAN ID. This field is required when Parameter [vlanEnable] is true; It should be
            within the range of 1–4094.
        psk_setting (SsidPskSettingOpenApiVO | Unset): WPA-Personal SSID config. This is necessary when the value of
            security is 3(WPA-Personal), 4(PPSK without RADIUS), 5(PPSK with RADIUS).
        ent_setting (SsidEnterpriseSettingOpenApiVO | Unset): WPA-Enterprise SSID config. This is necessary when the
            value of security is 2(WPA-Enterprise).
        ppsk_setting (SsidPpskSettingOpenApiVO | Unset): PPSK without RADIUS/PPSK without RADIUS SSID config. This is
            necessary when the value of security is 4(PPSK without RADIUS), 5(PPSK with RADIUS).
        hide_pwd (bool | Unset): If this field is true, the SSID password will be hidden.
        gre_enable (bool | Unset): SSID EoGre Tunnel config status. True: enable, false: disable; This configuration can
            be enabled only when the [VPN - EoGre Tunnel] global config is enabled.
        vlan_setting (SsidVlanSettingOpenApiVO | Unset): This field is required when Parameter [vlanEnable] is true. A
            newly added field is added to set the SSID VLAN configuration. If the field vlanId is entered, this field must
            be null.
        prohibit_wifi_share (bool | Unset): SSID prohibitWifiShare config status. True: enable, false: disable.
        enhanced_iot_connectivity (bool | Unset): SSID Enhanced IoT Connectivity config status. True: enable, false:
            disable. This configuration can be enabled only when the 5GHz and 6GHz bands are disabled, the parameters
            [versionEnt] and [versionPsk] are not set to 4, and the following configurations are disabled:
            [hotspotV2Enable], [bandSteer], [arpCastEnable], [loadBalance], [enable11r], [gikRekeyPskEnable], [pmfMode],
            [mloEnable].
        cond_broadcast_ctrl (CondBroadcastCtrlVO | Unset): Condition Broadcast Control config.
    """

    name: str
    band: int
    guest_net_enable: bool
    security: int
    broadcast: bool
    vlan_enable: bool
    mlo_enable: bool
    pmf_mode: int
    enable11r: bool
    auto_wan_access: bool | Unset = UNSET
    owe_enable: bool | Unset = UNSET
    vlan_id: int | Unset = UNSET
    psk_setting: SsidPskSettingOpenApiVO | Unset = UNSET
    ent_setting: SsidEnterpriseSettingOpenApiVO | Unset = UNSET
    ppsk_setting: SsidPpskSettingOpenApiVO | Unset = UNSET
    hide_pwd: bool | Unset = UNSET
    gre_enable: bool | Unset = UNSET
    vlan_setting: SsidVlanSettingOpenApiVO | Unset = UNSET
    prohibit_wifi_share: bool | Unset = UNSET
    enhanced_iot_connectivity: bool | Unset = UNSET
    cond_broadcast_ctrl: CondBroadcastCtrlVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        band = self.band

        guest_net_enable = self.guest_net_enable

        security = self.security

        broadcast = self.broadcast

        vlan_enable = self.vlan_enable

        mlo_enable = self.mlo_enable

        pmf_mode = self.pmf_mode

        enable11r = self.enable11r

        auto_wan_access = self.auto_wan_access

        owe_enable = self.owe_enable

        vlan_id = self.vlan_id

        psk_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.psk_setting, Unset):
            psk_setting = self.psk_setting.to_dict()

        ent_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ent_setting, Unset):
            ent_setting = self.ent_setting.to_dict()

        ppsk_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ppsk_setting, Unset):
            ppsk_setting = self.ppsk_setting.to_dict()

        hide_pwd = self.hide_pwd

        gre_enable = self.gre_enable

        vlan_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.vlan_setting, Unset):
            vlan_setting = self.vlan_setting.to_dict()

        prohibit_wifi_share = self.prohibit_wifi_share

        enhanced_iot_connectivity = self.enhanced_iot_connectivity

        cond_broadcast_ctrl: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cond_broadcast_ctrl, Unset):
            cond_broadcast_ctrl = self.cond_broadcast_ctrl.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "band": band,
                "guestNetEnable": guest_net_enable,
                "security": security,
                "broadcast": broadcast,
                "vlanEnable": vlan_enable,
                "mloEnable": mlo_enable,
                "pmfMode": pmf_mode,
                "enable11r": enable11r,
            }
        )
        if auto_wan_access is not UNSET:
            field_dict["autoWanAccess"] = auto_wan_access
        if owe_enable is not UNSET:
            field_dict["oweEnable"] = owe_enable
        if vlan_id is not UNSET:
            field_dict["vlanId"] = vlan_id
        if psk_setting is not UNSET:
            field_dict["pskSetting"] = psk_setting
        if ent_setting is not UNSET:
            field_dict["entSetting"] = ent_setting
        if ppsk_setting is not UNSET:
            field_dict["ppskSetting"] = ppsk_setting
        if hide_pwd is not UNSET:
            field_dict["hidePwd"] = hide_pwd
        if gre_enable is not UNSET:
            field_dict["greEnable"] = gre_enable
        if vlan_setting is not UNSET:
            field_dict["vlanSetting"] = vlan_setting
        if prohibit_wifi_share is not UNSET:
            field_dict["prohibitWifiShare"] = prohibit_wifi_share
        if enhanced_iot_connectivity is not UNSET:
            field_dict["enhancedIotConnectivity"] = enhanced_iot_connectivity
        if cond_broadcast_ctrl is not UNSET:
            field_dict["CondBroadcastCtrl"] = cond_broadcast_ctrl

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.cond_broadcast_ctrl_vo import CondBroadcastCtrlVO
        from ..models.ssid_enterprise_setting_open_api_vo import (
            SsidEnterpriseSettingOpenApiVO,
        )
        from ..models.ssid_ppsk_setting_open_api_vo import (
            SsidPpskSettingOpenApiVO,
        )
        from ..models.ssid_psk_setting_open_api_vo import (
            SsidPskSettingOpenApiVO,
        )
        from ..models.ssid_vlan_setting_open_api_vo import (
            SsidVlanSettingOpenApiVO,
        )

        d = dict(src_dict)
        name = d.pop("name")

        band = d.pop("band")

        guest_net_enable = d.pop("guestNetEnable")

        security = d.pop("security")

        broadcast = d.pop("broadcast")

        vlan_enable = d.pop("vlanEnable")

        mlo_enable = d.pop("mloEnable")

        pmf_mode = d.pop("pmfMode")

        enable11r = d.pop("enable11r")

        auto_wan_access = d.pop("autoWanAccess", UNSET)

        owe_enable = d.pop("oweEnable", UNSET)

        vlan_id = d.pop("vlanId", UNSET)

        _psk_setting = d.pop("pskSetting", UNSET)
        psk_setting: SsidPskSettingOpenApiVO | Unset
        if isinstance(_psk_setting, Unset):
            psk_setting = UNSET
        else:
            psk_setting = SsidPskSettingOpenApiVO.from_dict(_psk_setting)

        _ent_setting = d.pop("entSetting", UNSET)
        ent_setting: SsidEnterpriseSettingOpenApiVO | Unset
        if isinstance(_ent_setting, Unset):
            ent_setting = UNSET
        else:
            ent_setting = SsidEnterpriseSettingOpenApiVO.from_dict(_ent_setting)

        _ppsk_setting = d.pop("ppskSetting", UNSET)
        ppsk_setting: SsidPpskSettingOpenApiVO | Unset
        if isinstance(_ppsk_setting, Unset):
            ppsk_setting = UNSET
        else:
            ppsk_setting = SsidPpskSettingOpenApiVO.from_dict(_ppsk_setting)

        hide_pwd = d.pop("hidePwd", UNSET)

        gre_enable = d.pop("greEnable", UNSET)

        _vlan_setting = d.pop("vlanSetting", UNSET)
        vlan_setting: SsidVlanSettingOpenApiVO | Unset
        if isinstance(_vlan_setting, Unset):
            vlan_setting = UNSET
        else:
            vlan_setting = SsidVlanSettingOpenApiVO.from_dict(_vlan_setting)

        prohibit_wifi_share = d.pop("prohibitWifiShare", UNSET)

        enhanced_iot_connectivity = d.pop("enhancedIotConnectivity", UNSET)

        _cond_broadcast_ctrl = d.pop("CondBroadcastCtrl", UNSET)
        cond_broadcast_ctrl: CondBroadcastCtrlVO | Unset
        if isinstance(_cond_broadcast_ctrl, Unset):
            cond_broadcast_ctrl = UNSET
        else:
            cond_broadcast_ctrl = CondBroadcastCtrlVO.from_dict(_cond_broadcast_ctrl)

        update_ssid_basic_config_open_api_vo = cls(
            name=name,
            band=band,
            guest_net_enable=guest_net_enable,
            security=security,
            broadcast=broadcast,
            vlan_enable=vlan_enable,
            mlo_enable=mlo_enable,
            pmf_mode=pmf_mode,
            enable11r=enable11r,
            auto_wan_access=auto_wan_access,
            owe_enable=owe_enable,
            vlan_id=vlan_id,
            psk_setting=psk_setting,
            ent_setting=ent_setting,
            ppsk_setting=ppsk_setting,
            hide_pwd=hide_pwd,
            gre_enable=gre_enable,
            vlan_setting=vlan_setting,
            prohibit_wifi_share=prohibit_wifi_share,
            enhanced_iot_connectivity=enhanced_iot_connectivity,
            cond_broadcast_ctrl=cond_broadcast_ctrl,
        )

        update_ssid_basic_config_open_api_vo.additional_properties = d
        return update_ssid_basic_config_open_api_vo

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
