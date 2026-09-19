from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.band_steer_open_api_vo import BandSteerOpenApiVO
    from ..models.hotspot_v2_setting_open_api_vo import HotspotV2SettingOpenApiVO
    from ..models.rate_limit_setting_open_api_vo import RateLimitSettingOpenApiVO
    from ..models.ssid_dhcp_option_open_api_vo import SsidDhcpOptionOpenApiVO
    from ..models.ssid_enterprise_setting_open_api_vo import (
        SsidEnterpriseSettingOpenApiVO,
    )
    from ..models.ssid_mac_filter_open_api_vo import SsidMacFilterOpenApiVO
    from ..models.ssid_multi_cast_open_api_vo import SsidMultiCastOpenApiVO
    from ..models.ssid_ppsk_setting_open_api_vo import SsidPpskSettingOpenApiVO
    from ..models.ssid_psk_setting_open_api_vo import SsidPskSettingOpenApiVO
    from ..models.ssid_rate_control_open_api_vo import SsidRateControlOpenApiVO
    from ..models.ssid_vlan_setting_open_api_vo import SsidVlanSettingOpenApiVO
    from ..models.ssid_wlan_schedule_open_api_vo import SsidWlanScheduleOpenApiVO


T = TypeVar("T", bound="SsidDetailOpenApiVO")


@_attrs_define
class SsidDetailOpenApiVO:
    """
    Attributes:
        ssid_id (str | Unset): SSID ID, kept for backward compatibility and equivalent to id. This field will be removed
            in a future release; use id instead.
        id (str | Unset): SSID ID
        name (str | Unset): SSID name. It should contain 1 to 32 UTF-8 characters.
        band (int | Unset): SSID band. The lowest bit indicates whether 2.4G is included; the second lowest bit
            indicates whether 5G is included; the third lowest bit indicates whether 6G is included; 1 means included while
            0 means not included. For example, 7(111) means that 2G/5G/6G are enabled; 1(001) means that 2G is enabled.
            (When 5G is included，it means 5G/5G1/5G2 are enabled.)
        auto_wan_access (bool | Unset): Whether to enable auto wan access. True: enable, false: disable.
        guest_net_enable (bool | Unset): SSID guest network config status. True: enable, false: disable.
        security (int | Unset): SSID security mode; Security should be a value as follows: 0: None; 2: WPA-Enterprise;
            3: WPA-Personal; 4: PPSK without RADIUS; 5: PPSK with RADIUS.
        owe_enable (bool | Unset): Opportunistic Wireless Encryption, also known as Enhanced Open, is a certification
            provided by the Wi-Fi Alliance as part of the WPA3 wireless security standard. OWE will enable two wireless VAPs
            per radio, one for access of OWE-supported stations, and one for access of other stations. An SSID with OWE
            enabled will be counted as two SSID entries for 2G and 5G.
        broadcast (bool | Unset): SSID broadcast config status. True: enable, false: disable.
        vlan_enable (bool | Unset): SSID VLAN config status. True: enable, false: disable.
        vlan_id (int | Unset): SSID VLAN ID. This field is required when Parameter [vlanEnable] is true; It should be
            within the range of 1–4094.
        hide_pwd (bool | Unset): If this field is true, the SSID password will be hidden.
        vlan_setting (SsidVlanSettingOpenApiVO | Unset): This field is required when Parameter [vlanEnable] is true. A
            newly added field is added to set the SSID VLAN configuration. If the field vlanId is entered, this field must
            be null.
        psk_setting (SsidPskSettingOpenApiVO | Unset): WPA-Personal SSID config. This is necessary when the value of
            security is 3(WPA-Personal), 4(PPSK without RADIUS), 5(PPSK with RADIUS).
        ent_setting (SsidEnterpriseSettingOpenApiVO | Unset): WPA-Enterprise SSID config. This is necessary when the
            value of security is 2(WPA-Enterprise).
        ppsk_setting (SsidPpskSettingOpenApiVO | Unset): PPSK without RADIUS/PPSK without RADIUS SSID config. This is
            necessary when the value of security is 4(PPSK without RADIUS), 5(PPSK with RADIUS).
        mlo_enable (bool | Unset): SSID MLO config status. True: enable, false: disable.
        pmf_mode (int | Unset): SSID PMF mode. It should be a value as follows: 1: Mandatory; 2: Capable; 3: Disable.
        enable11r (bool | Unset): SSID 802.11r config status. True: enable, false: disable.
        client_rate_limit (RateLimitSettingOpenApiVO | Unset): SSID rate limit config.
        ssid_rate_limit (RateLimitSettingOpenApiVO | Unset): SSID rate limit config.
        wlan_schedule (SsidWlanScheduleOpenApiVO | Unset): SSID WLAN schedule config.
        rate_control (SsidRateControlOpenApiVO | Unset): SSID 802.11 Rate Control config.
        mac_filter (SsidMacFilterOpenApiVO | Unset): SSID MAC Filter config.
        multi_cast (SsidMultiCastOpenApiVO | Unset): SSID Multicast/Broadcast Management config.
        dhcp_option_82 (SsidDhcpOptionOpenApiVO | Unset): SSID DHCP Option 82 config.
        device_type (int | Unset): SSID device type, identify which devices this SSID will take effect. The lowest bit
            indicates whether [EAP] is included, the second low bit indicates whether [Gateway] is included, 1 means
            included while 0 means not included; For example, 3(11) means that EAP/Gateway is enabled, 1(01) means that EAP
            is enabled.
        ssid_enable (bool | Unset): SSID enable status. True: enable, false: disable.
        choose_devices (int | Unset): description = select all devices or not. 0 means select all devices, 1 means not
            select all devices.
        prohibit_wifi_share (bool | Unset): SSID prohibitWifiShare config status. True: enable, false: disable.
        hotspot_v2_setting (HotspotV2SettingOpenApiVO | Unset): Hotspot 2.0 is a WFA (Wi-Fi Alliance) technical
            specification based on IEEE 802.11u protocol.<br />It provides a simplified mechanism for wireless clients to
            discover and connect to suitable networks and switch seamlessly between mobile networks and wireless networks.
        wifi_calling_enable (bool | Unset): SSID Wifi Calling config status. True: enable, false: disable.
        wifi_calling_id (str | Unset): The ID of the Wi-Fi calling profile bound to the SSID. When parameter
            [wifiCallingEnable] is true, it should not be null.
        ssid_dhcp_option (BandSteerOpenApiVO | Unset): SSID Band Steer config.
        ap_group_ids (list[str] | Unset): List of AP Group IDs associated with this SSID
        enhanced_iot_connectivity (bool | Unset): SSID Enhanced IoT Connectivity config status. True: enable, false:
            disable. This configuration can be enabled only when the 5GHz and 6GHz bands are disabled, the parameters
            [versionEnt] and [versionPsk] are not set to 4, and the following configurations are disabled:
            [hotspotV2Enable], [bandSteer], [arpCastEnable], [loadBalance], [enable11r], [gikRekeyPskEnable], [pmfMode],
            [mloEnable].
    """

    ssid_id: str | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    band: int | Unset = UNSET
    auto_wan_access: bool | Unset = UNSET
    guest_net_enable: bool | Unset = UNSET
    security: int | Unset = UNSET
    owe_enable: bool | Unset = UNSET
    broadcast: bool | Unset = UNSET
    vlan_enable: bool | Unset = UNSET
    vlan_id: int | Unset = UNSET
    hide_pwd: bool | Unset = UNSET
    vlan_setting: SsidVlanSettingOpenApiVO | Unset = UNSET
    psk_setting: SsidPskSettingOpenApiVO | Unset = UNSET
    ent_setting: SsidEnterpriseSettingOpenApiVO | Unset = UNSET
    ppsk_setting: SsidPpskSettingOpenApiVO | Unset = UNSET
    mlo_enable: bool | Unset = UNSET
    pmf_mode: int | Unset = UNSET
    enable11r: bool | Unset = UNSET
    client_rate_limit: RateLimitSettingOpenApiVO | Unset = UNSET
    ssid_rate_limit: RateLimitSettingOpenApiVO | Unset = UNSET
    wlan_schedule: SsidWlanScheduleOpenApiVO | Unset = UNSET
    rate_control: SsidRateControlOpenApiVO | Unset = UNSET
    mac_filter: SsidMacFilterOpenApiVO | Unset = UNSET
    multi_cast: SsidMultiCastOpenApiVO | Unset = UNSET
    dhcp_option_82: SsidDhcpOptionOpenApiVO | Unset = UNSET
    device_type: int | Unset = UNSET
    ssid_enable: bool | Unset = UNSET
    choose_devices: int | Unset = UNSET
    prohibit_wifi_share: bool | Unset = UNSET
    hotspot_v2_setting: HotspotV2SettingOpenApiVO | Unset = UNSET
    wifi_calling_enable: bool | Unset = UNSET
    wifi_calling_id: str | Unset = UNSET
    ssid_dhcp_option: BandSteerOpenApiVO | Unset = UNSET
    ap_group_ids: list[str] | Unset = UNSET
    enhanced_iot_connectivity: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ssid_id = self.ssid_id

        id = self.id

        name = self.name

        band = self.band

        auto_wan_access = self.auto_wan_access

        guest_net_enable = self.guest_net_enable

        security = self.security

        owe_enable = self.owe_enable

        broadcast = self.broadcast

        vlan_enable = self.vlan_enable

        vlan_id = self.vlan_id

        hide_pwd = self.hide_pwd

        vlan_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.vlan_setting, Unset):
            vlan_setting = self.vlan_setting.to_dict()

        psk_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.psk_setting, Unset):
            psk_setting = self.psk_setting.to_dict()

        ent_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ent_setting, Unset):
            ent_setting = self.ent_setting.to_dict()

        ppsk_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ppsk_setting, Unset):
            ppsk_setting = self.ppsk_setting.to_dict()

        mlo_enable = self.mlo_enable

        pmf_mode = self.pmf_mode

        enable11r = self.enable11r

        client_rate_limit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.client_rate_limit, Unset):
            client_rate_limit = self.client_rate_limit.to_dict()

        ssid_rate_limit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ssid_rate_limit, Unset):
            ssid_rate_limit = self.ssid_rate_limit.to_dict()

        wlan_schedule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wlan_schedule, Unset):
            wlan_schedule = self.wlan_schedule.to_dict()

        rate_control: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rate_control, Unset):
            rate_control = self.rate_control.to_dict()

        mac_filter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mac_filter, Unset):
            mac_filter = self.mac_filter.to_dict()

        multi_cast: dict[str, Any] | Unset = UNSET
        if not isinstance(self.multi_cast, Unset):
            multi_cast = self.multi_cast.to_dict()

        dhcp_option_82: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dhcp_option_82, Unset):
            dhcp_option_82 = self.dhcp_option_82.to_dict()

        device_type = self.device_type

        ssid_enable = self.ssid_enable

        choose_devices = self.choose_devices

        prohibit_wifi_share = self.prohibit_wifi_share

        hotspot_v2_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.hotspot_v2_setting, Unset):
            hotspot_v2_setting = self.hotspot_v2_setting.to_dict()

        wifi_calling_enable = self.wifi_calling_enable

        wifi_calling_id = self.wifi_calling_id

        ssid_dhcp_option: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ssid_dhcp_option, Unset):
            ssid_dhcp_option = self.ssid_dhcp_option.to_dict()

        ap_group_ids: list[str] | Unset = UNSET
        if not isinstance(self.ap_group_ids, Unset):
            ap_group_ids = self.ap_group_ids

        enhanced_iot_connectivity = self.enhanced_iot_connectivity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ssid_id is not UNSET:
            field_dict["ssidId"] = ssid_id
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if band is not UNSET:
            field_dict["band"] = band
        if auto_wan_access is not UNSET:
            field_dict["autoWanAccess"] = auto_wan_access
        if guest_net_enable is not UNSET:
            field_dict["guestNetEnable"] = guest_net_enable
        if security is not UNSET:
            field_dict["security"] = security
        if owe_enable is not UNSET:
            field_dict["oweEnable"] = owe_enable
        if broadcast is not UNSET:
            field_dict["broadcast"] = broadcast
        if vlan_enable is not UNSET:
            field_dict["vlanEnable"] = vlan_enable
        if vlan_id is not UNSET:
            field_dict["vlanId"] = vlan_id
        if hide_pwd is not UNSET:
            field_dict["hidePwd"] = hide_pwd
        if vlan_setting is not UNSET:
            field_dict["vlanSetting"] = vlan_setting
        if psk_setting is not UNSET:
            field_dict["pskSetting"] = psk_setting
        if ent_setting is not UNSET:
            field_dict["entSetting"] = ent_setting
        if ppsk_setting is not UNSET:
            field_dict["ppskSetting"] = ppsk_setting
        if mlo_enable is not UNSET:
            field_dict["mloEnable"] = mlo_enable
        if pmf_mode is not UNSET:
            field_dict["pmfMode"] = pmf_mode
        if enable11r is not UNSET:
            field_dict["enable11r"] = enable11r
        if client_rate_limit is not UNSET:
            field_dict["clientRateLimit"] = client_rate_limit
        if ssid_rate_limit is not UNSET:
            field_dict["ssidRateLimit"] = ssid_rate_limit
        if wlan_schedule is not UNSET:
            field_dict["wlanSchedule"] = wlan_schedule
        if rate_control is not UNSET:
            field_dict["rateControl"] = rate_control
        if mac_filter is not UNSET:
            field_dict["macFilter"] = mac_filter
        if multi_cast is not UNSET:
            field_dict["multiCast"] = multi_cast
        if dhcp_option_82 is not UNSET:
            field_dict["dhcpOption82"] = dhcp_option_82
        if device_type is not UNSET:
            field_dict["deviceType"] = device_type
        if ssid_enable is not UNSET:
            field_dict["ssidEnable"] = ssid_enable
        if choose_devices is not UNSET:
            field_dict["chooseDevices"] = choose_devices
        if prohibit_wifi_share is not UNSET:
            field_dict["prohibitWifiShare"] = prohibit_wifi_share
        if hotspot_v2_setting is not UNSET:
            field_dict["hotspotV2Setting"] = hotspot_v2_setting
        if wifi_calling_enable is not UNSET:
            field_dict["wifiCallingEnable"] = wifi_calling_enable
        if wifi_calling_id is not UNSET:
            field_dict["wifiCallingId"] = wifi_calling_id
        if ssid_dhcp_option is not UNSET:
            field_dict["ssidDhcpOption"] = ssid_dhcp_option
        if ap_group_ids is not UNSET:
            field_dict["apGroupIds"] = ap_group_ids
        if enhanced_iot_connectivity is not UNSET:
            field_dict["enhancedIotConnectivity"] = enhanced_iot_connectivity

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.band_steer_open_api_vo import BandSteerOpenApiVO
        from ..models.hotspot_v2_setting_open_api_vo import (
            HotspotV2SettingOpenApiVO,
        )
        from ..models.rate_limit_setting_open_api_vo import (
            RateLimitSettingOpenApiVO,
        )
        from ..models.ssid_dhcp_option_open_api_vo import (
            SsidDhcpOptionOpenApiVO,
        )
        from ..models.ssid_enterprise_setting_open_api_vo import (
            SsidEnterpriseSettingOpenApiVO,
        )
        from ..models.ssid_mac_filter_open_api_vo import (
            SsidMacFilterOpenApiVO,
        )
        from ..models.ssid_multi_cast_open_api_vo import (
            SsidMultiCastOpenApiVO,
        )
        from ..models.ssid_ppsk_setting_open_api_vo import (
            SsidPpskSettingOpenApiVO,
        )
        from ..models.ssid_psk_setting_open_api_vo import (
            SsidPskSettingOpenApiVO,
        )
        from ..models.ssid_rate_control_open_api_vo import (
            SsidRateControlOpenApiVO,
        )
        from ..models.ssid_vlan_setting_open_api_vo import (
            SsidVlanSettingOpenApiVO,
        )
        from ..models.ssid_wlan_schedule_open_api_vo import (
            SsidWlanScheduleOpenApiVO,
        )

        d = dict(src_dict)
        ssid_id = d.pop("ssidId", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        band = d.pop("band", UNSET)

        auto_wan_access = d.pop("autoWanAccess", UNSET)

        guest_net_enable = d.pop("guestNetEnable", UNSET)

        security = d.pop("security", UNSET)

        owe_enable = d.pop("oweEnable", UNSET)

        broadcast = d.pop("broadcast", UNSET)

        vlan_enable = d.pop("vlanEnable", UNSET)

        vlan_id = d.pop("vlanId", UNSET)

        hide_pwd = d.pop("hidePwd", UNSET)

        _vlan_setting = d.pop("vlanSetting", UNSET)
        vlan_setting: SsidVlanSettingOpenApiVO | Unset
        if isinstance(_vlan_setting, Unset):
            vlan_setting = UNSET
        else:
            vlan_setting = SsidVlanSettingOpenApiVO.from_dict(_vlan_setting)

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

        mlo_enable = d.pop("mloEnable", UNSET)

        pmf_mode = d.pop("pmfMode", UNSET)

        enable11r = d.pop("enable11r", UNSET)

        _client_rate_limit = d.pop("clientRateLimit", UNSET)
        client_rate_limit: RateLimitSettingOpenApiVO | Unset
        if isinstance(_client_rate_limit, Unset):
            client_rate_limit = UNSET
        else:
            client_rate_limit = RateLimitSettingOpenApiVO.from_dict(_client_rate_limit)

        _ssid_rate_limit = d.pop("ssidRateLimit", UNSET)
        ssid_rate_limit: RateLimitSettingOpenApiVO | Unset
        if isinstance(_ssid_rate_limit, Unset):
            ssid_rate_limit = UNSET
        else:
            ssid_rate_limit = RateLimitSettingOpenApiVO.from_dict(_ssid_rate_limit)

        _wlan_schedule = d.pop("wlanSchedule", UNSET)
        wlan_schedule: SsidWlanScheduleOpenApiVO | Unset
        if isinstance(_wlan_schedule, Unset):
            wlan_schedule = UNSET
        else:
            wlan_schedule = SsidWlanScheduleOpenApiVO.from_dict(_wlan_schedule)

        _rate_control = d.pop("rateControl", UNSET)
        rate_control: SsidRateControlOpenApiVO | Unset
        if isinstance(_rate_control, Unset):
            rate_control = UNSET
        else:
            rate_control = SsidRateControlOpenApiVO.from_dict(_rate_control)

        _mac_filter = d.pop("macFilter", UNSET)
        mac_filter: SsidMacFilterOpenApiVO | Unset
        if isinstance(_mac_filter, Unset):
            mac_filter = UNSET
        else:
            mac_filter = SsidMacFilterOpenApiVO.from_dict(_mac_filter)

        _multi_cast = d.pop("multiCast", UNSET)
        multi_cast: SsidMultiCastOpenApiVO | Unset
        if isinstance(_multi_cast, Unset):
            multi_cast = UNSET
        else:
            multi_cast = SsidMultiCastOpenApiVO.from_dict(_multi_cast)

        _dhcp_option_82 = d.pop("dhcpOption82", UNSET)
        dhcp_option_82: SsidDhcpOptionOpenApiVO | Unset
        if isinstance(_dhcp_option_82, Unset):
            dhcp_option_82 = UNSET
        else:
            dhcp_option_82 = SsidDhcpOptionOpenApiVO.from_dict(_dhcp_option_82)

        device_type = d.pop("deviceType", UNSET)

        ssid_enable = d.pop("ssidEnable", UNSET)

        choose_devices = d.pop("chooseDevices", UNSET)

        prohibit_wifi_share = d.pop("prohibitWifiShare", UNSET)

        _hotspot_v2_setting = d.pop("hotspotV2Setting", UNSET)
        hotspot_v2_setting: HotspotV2SettingOpenApiVO | Unset
        if isinstance(_hotspot_v2_setting, Unset):
            hotspot_v2_setting = UNSET
        else:
            hotspot_v2_setting = HotspotV2SettingOpenApiVO.from_dict(
                _hotspot_v2_setting
            )

        wifi_calling_enable = d.pop("wifiCallingEnable", UNSET)

        wifi_calling_id = d.pop("wifiCallingId", UNSET)

        _ssid_dhcp_option = d.pop("ssidDhcpOption", UNSET)
        ssid_dhcp_option: BandSteerOpenApiVO | Unset
        if isinstance(_ssid_dhcp_option, Unset):
            ssid_dhcp_option = UNSET
        else:
            ssid_dhcp_option = BandSteerOpenApiVO.from_dict(_ssid_dhcp_option)

        ap_group_ids = cast(list[str], d.pop("apGroupIds", UNSET))

        enhanced_iot_connectivity = d.pop("enhancedIotConnectivity", UNSET)

        ssid_detail_open_api_vo = cls(
            ssid_id=ssid_id,
            id=id,
            name=name,
            band=band,
            auto_wan_access=auto_wan_access,
            guest_net_enable=guest_net_enable,
            security=security,
            owe_enable=owe_enable,
            broadcast=broadcast,
            vlan_enable=vlan_enable,
            vlan_id=vlan_id,
            hide_pwd=hide_pwd,
            vlan_setting=vlan_setting,
            psk_setting=psk_setting,
            ent_setting=ent_setting,
            ppsk_setting=ppsk_setting,
            mlo_enable=mlo_enable,
            pmf_mode=pmf_mode,
            enable11r=enable11r,
            client_rate_limit=client_rate_limit,
            ssid_rate_limit=ssid_rate_limit,
            wlan_schedule=wlan_schedule,
            rate_control=rate_control,
            mac_filter=mac_filter,
            multi_cast=multi_cast,
            dhcp_option_82=dhcp_option_82,
            device_type=device_type,
            ssid_enable=ssid_enable,
            choose_devices=choose_devices,
            prohibit_wifi_share=prohibit_wifi_share,
            hotspot_v2_setting=hotspot_v2_setting,
            wifi_calling_enable=wifi_calling_enable,
            wifi_calling_id=wifi_calling_id,
            ssid_dhcp_option=ssid_dhcp_option,
            ap_group_ids=ap_group_ids,
            enhanced_iot_connectivity=enhanced_iot_connectivity,
        )

        ssid_detail_open_api_vo.additional_properties = d
        return ssid_detail_open_api_vo

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
