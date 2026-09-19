from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

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


T = TypeVar("T", bound="CreateSsidOpenApiVO")


@_attrs_define
class CreateSsidOpenApiVO:
    """
    Attributes:
        name (str): SSID name. It should contain 1 to 32 UTF-8 characters.
        device_type (int): SSID device type, identify which devices this SSID will take effect; The lowest bit indicates
            whether [EAP] is included, the second low bit indicates whether [Gateway] is included, 1 means included while 0
            means not included; For example, 3(11) means that EAP/Gateway is enabled, 1(01) means that EAP is enabled.
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
        hide_pwd (bool): If this field is true, the SSID password will be hidden.
        ssid_enable (bool | Unset): SSID enable status. True: enable, false: disable.
        choose_devices (int | Unset): description = select all devices or not. 0 means select all devices, 1 means not
            select all devices.
        ap_group_ids (list[str] | Unset): AP Group ID list that the SSID is associated with. Supports binding to
            multiple AP groups.
        vlan_id (int | Unset): SSID VLAN ID. This field is required when Parameter [vlanEnable] is true; It should be
            within the range of 1–4094. If the field vlanSetting is entered, this field must be null.
        psk_setting (SsidPskSettingOpenApiVO | Unset): WPA-Personal SSID config. This is necessary when the value of
            security is 3(WPA-Personal), 4(PPSK without RADIUS), 5(PPSK with RADIUS).
        ent_setting (SsidEnterpriseSettingOpenApiVO | Unset): WPA-Enterprise SSID config. This is necessary when the
            value of security is 2(WPA-Enterprise).
        ppsk_setting (SsidPpskSettingOpenApiVO | Unset): PPSK without RADIUS/PPSK without RADIUS SSID config. This is
            necessary when the value of security is 4(PPSK without RADIUS), 5(PPSK with RADIUS).
        gre_enable (bool | Unset): SSID EoGre Tunnel config status. True: enable, false: disable. This configuration can
            be enabled only when the [VPN - EoGre Tunnel] global config is enabled;(This configuration applies to the Pro
            Site of the Omada Pro Controller only).
        vlan_setting (SsidVlanSettingOpenApiVO | Unset): This field is required when Parameter [vlanEnable] is true. A
            newly added field is added to set the SSID VLAN configuration. If the field vlanId is entered, this field must
            be null.
        prohibit_wifi_share (bool | Unset): SSID prohibitWifiShare config status. True: enable, false: disable.
        wifi_calling_enable (bool | Unset): SSID Wifi Calling config status. True: enable, false: disable.
        wifi_calling_id (str | Unset): The ID of the Wi-Fi calling profile bound to the SSID. When parameter
            [wifiCallingEnable] is true, it should not be null.
        enhanced_iot_connectivity (bool | Unset): SSID Enhanced IoT Connectivity config status. True: enable, false:
            disable. This configuration can be enabled only when the 5GHz and 6GHz bands are disabled, the parameters
            [versionEnt] and [versionPsk] are not set to 4, and the following configurations are disabled:
            [hotspotV2Enable], [bandSteer], [arpCastEnable], [loadBalance], [enable11r], [gikRekeyPskEnable], [pmfMode],
            [mloEnable].
        cond_broadcast_ctrl (CondBroadcastCtrlVO | Unset): Condition Broadcast Control config.
    """

    name: str
    device_type: int
    band: int
    guest_net_enable: bool
    security: int
    broadcast: bool
    vlan_enable: bool
    mlo_enable: bool
    pmf_mode: int
    enable11r: bool
    hide_pwd: bool
    ssid_enable: bool | Unset = UNSET
    choose_devices: int | Unset = UNSET
    ap_group_ids: list[str] | Unset = UNSET
    vlan_id: int | Unset = UNSET
    psk_setting: SsidPskSettingOpenApiVO | Unset = UNSET
    ent_setting: SsidEnterpriseSettingOpenApiVO | Unset = UNSET
    ppsk_setting: SsidPpskSettingOpenApiVO | Unset = UNSET
    gre_enable: bool | Unset = UNSET
    vlan_setting: SsidVlanSettingOpenApiVO | Unset = UNSET
    prohibit_wifi_share: bool | Unset = UNSET
    wifi_calling_enable: bool | Unset = UNSET
    wifi_calling_id: str | Unset = UNSET
    enhanced_iot_connectivity: bool | Unset = UNSET
    cond_broadcast_ctrl: CondBroadcastCtrlVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        device_type = self.device_type

        band = self.band

        guest_net_enable = self.guest_net_enable

        security = self.security

        broadcast = self.broadcast

        vlan_enable = self.vlan_enable

        mlo_enable = self.mlo_enable

        pmf_mode = self.pmf_mode

        enable11r = self.enable11r

        hide_pwd = self.hide_pwd

        ssid_enable = self.ssid_enable

        choose_devices = self.choose_devices

        ap_group_ids: list[str] | Unset = UNSET
        if not isinstance(self.ap_group_ids, Unset):
            ap_group_ids = self.ap_group_ids

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

        gre_enable = self.gre_enable

        vlan_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.vlan_setting, Unset):
            vlan_setting = self.vlan_setting.to_dict()

        prohibit_wifi_share = self.prohibit_wifi_share

        wifi_calling_enable = self.wifi_calling_enable

        wifi_calling_id = self.wifi_calling_id

        enhanced_iot_connectivity = self.enhanced_iot_connectivity

        cond_broadcast_ctrl: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cond_broadcast_ctrl, Unset):
            cond_broadcast_ctrl = self.cond_broadcast_ctrl.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "deviceType": device_type,
                "band": band,
                "guestNetEnable": guest_net_enable,
                "security": security,
                "broadcast": broadcast,
                "vlanEnable": vlan_enable,
                "mloEnable": mlo_enable,
                "pmfMode": pmf_mode,
                "enable11r": enable11r,
                "hidePwd": hide_pwd,
            }
        )
        if ssid_enable is not UNSET:
            field_dict["ssidEnable"] = ssid_enable
        if choose_devices is not UNSET:
            field_dict["chooseDevices"] = choose_devices
        if ap_group_ids is not UNSET:
            field_dict["apGroupIds"] = ap_group_ids
        if vlan_id is not UNSET:
            field_dict["vlanId"] = vlan_id
        if psk_setting is not UNSET:
            field_dict["pskSetting"] = psk_setting
        if ent_setting is not UNSET:
            field_dict["entSetting"] = ent_setting
        if ppsk_setting is not UNSET:
            field_dict["ppskSetting"] = ppsk_setting
        if gre_enable is not UNSET:
            field_dict["greEnable"] = gre_enable
        if vlan_setting is not UNSET:
            field_dict["vlanSetting"] = vlan_setting
        if prohibit_wifi_share is not UNSET:
            field_dict["prohibitWifiShare"] = prohibit_wifi_share
        if wifi_calling_enable is not UNSET:
            field_dict["wifiCallingEnable"] = wifi_calling_enable
        if wifi_calling_id is not UNSET:
            field_dict["wifiCallingId"] = wifi_calling_id
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

        device_type = d.pop("deviceType")

        band = d.pop("band")

        guest_net_enable = d.pop("guestNetEnable")

        security = d.pop("security")

        broadcast = d.pop("broadcast")

        vlan_enable = d.pop("vlanEnable")

        mlo_enable = d.pop("mloEnable")

        pmf_mode = d.pop("pmfMode")

        enable11r = d.pop("enable11r")

        hide_pwd = d.pop("hidePwd")

        ssid_enable = d.pop("ssidEnable", UNSET)

        choose_devices = d.pop("chooseDevices", UNSET)

        ap_group_ids = cast(list[str], d.pop("apGroupIds", UNSET))

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

        gre_enable = d.pop("greEnable", UNSET)

        _vlan_setting = d.pop("vlanSetting", UNSET)
        vlan_setting: SsidVlanSettingOpenApiVO | Unset
        if isinstance(_vlan_setting, Unset):
            vlan_setting = UNSET
        else:
            vlan_setting = SsidVlanSettingOpenApiVO.from_dict(_vlan_setting)

        prohibit_wifi_share = d.pop("prohibitWifiShare", UNSET)

        wifi_calling_enable = d.pop("wifiCallingEnable", UNSET)

        wifi_calling_id = d.pop("wifiCallingId", UNSET)

        enhanced_iot_connectivity = d.pop("enhancedIotConnectivity", UNSET)

        _cond_broadcast_ctrl = d.pop("CondBroadcastCtrl", UNSET)
        cond_broadcast_ctrl: CondBroadcastCtrlVO | Unset
        if isinstance(_cond_broadcast_ctrl, Unset):
            cond_broadcast_ctrl = UNSET
        else:
            cond_broadcast_ctrl = CondBroadcastCtrlVO.from_dict(_cond_broadcast_ctrl)

        create_ssid_open_api_vo = cls(
            name=name,
            device_type=device_type,
            band=band,
            guest_net_enable=guest_net_enable,
            security=security,
            broadcast=broadcast,
            vlan_enable=vlan_enable,
            mlo_enable=mlo_enable,
            pmf_mode=pmf_mode,
            enable11r=enable11r,
            hide_pwd=hide_pwd,
            ssid_enable=ssid_enable,
            choose_devices=choose_devices,
            ap_group_ids=ap_group_ids,
            vlan_id=vlan_id,
            psk_setting=psk_setting,
            ent_setting=ent_setting,
            ppsk_setting=ppsk_setting,
            gre_enable=gre_enable,
            vlan_setting=vlan_setting,
            prohibit_wifi_share=prohibit_wifi_share,
            wifi_calling_enable=wifi_calling_enable,
            wifi_calling_id=wifi_calling_id,
            enhanced_iot_connectivity=enhanced_iot_connectivity,
            cond_broadcast_ctrl=cond_broadcast_ctrl,
        )

        create_ssid_open_api_vo.additional_properties = d
        return create_ssid_open_api_vo

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
