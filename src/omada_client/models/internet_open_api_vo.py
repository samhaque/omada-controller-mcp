from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lte_wan_port_setting_open_api_vo import LteWanPortSettingOpenApiVO
    from ..models.osg_port_info_open_api_vo import OsgPortInfoOpenApiVO
    from ..models.port_online_status_open_api_vo import PortOnlineStatusOpenApiVO
    from ..models.usb_lte_setting_open_api_vo import UsbLteSettingOpenApiVO
    from ..models.wan_load_balance_open_api_vo import WanLoadBalanceOpenApiVO
    from ..models.wan_port_setting_open_api_vo import WanPortSettingOpenApiVO


T = TypeVar("T", bound="InternetOpenApiVO")


@_attrs_define
class InternetOpenApiVO:
    """
    Attributes:
        site_id (str): Site ID.
        omadac_id (str | Unset): Omadac ID.
        enable (bool | Unset): Is Internet enable.
        osg_port_info (OsgPortInfoOpenApiVO | Unset): Gateway port info.
        port_uuids (list[str] | Unset): The list of wan port UUID.
        interval (int | Unset): Time taken to check the connection of wan port.
        unit (int | Unset): Unit.
        support_custom_interval (bool | Unset): Whether the device supports Custom Interval.
        support_discrete_wan (bool | Unset): Whether the device supports Discrete Wan.
        support_reduce_usb_rfi (bool | Unset): Whether the device supports Reduce USB 3.0 Interference Reduction.
        support_all_wan (bool | Unset): Whether the device supports all wan.
        support_max_wan_num (int | Unset): The maximum number of wans supported.
        support_ipv_6_non_address (bool | Unset): Whether the IPv6 configuration supports Non-Address.
        support_mss_clamping (bool | Unset): Whether MSS clamping is supported for PPPoE, L2TP, and PPTP.
        support_pppoe_mru (bool | Unset): Whether to configure PPPoE MRUs.
        support_wan_multiple_ip (bool | Unset): Whether to configure multiple IP addresses for wan ports.
        support_lte (bool | Unset): Whether to configure LTE Wan.
        support_dual_sim (int | Unset): Whether it supports dual SIM single standby: 0: not support, 1: support.
        support_dsl (bool | Unset): Whether it supports DSL.
        support_virtual_wan (bool | Unset): Whether it supports virtual wan.
        support_network_isolation (bool | Unset): Whether it supports isolate network.
        support_dhcp_options (bool | Unset): Whether WAN port dhcpOptions can be customized.
        support_usb_dhcp_options (bool | Unset): Whether USB port dhcpOptions can be customized.
        support_ds_lite (bool | Unset): Whether the WAN port supports configuring DS-Lite.
        support_map_e (bool | Unset): Whether the WAN port supports configuring MAP-E.
        support_timing_mode (bool | Unset): Whether the Load Balance Failover supports Timing mode.
        wan_port_settings (list[WanPortSettingOpenApiVO] | Unset): A list of wan port setting.
        usb_lte_settings (list[UsbLteSettingOpenApiVO] | Unset): A list of USB LTE setting.
        lte_wan_settings (list[LteWanPortSettingOpenApiVO] | Unset): A list of LTE wan setting.
        wan_load_balance (WanLoadBalanceOpenApiVO | Unset):
        network_names (list[str] | Unset): A list of the name of the LanNetwork entry that was invalidated on the
            frontend.
        unmatched_wans (list[str] | Unset): A list of the name of the WAN port that was invalidated on the frontend.
        gateway_mac (str | Unset): Gateway MAC.
        enable_modified (bool | Unset): Whether it enable modified.
        lte_interval_tips (bool | Unset): Whether to display the interval prompt for LTE ports.
        port_online_status (PortOnlineStatusOpenApiVO | Unset): Port online status.
        resource (int | Unset): Resource of data.
    """

    site_id: str
    omadac_id: str | Unset = UNSET
    enable: bool | Unset = UNSET
    osg_port_info: OsgPortInfoOpenApiVO | Unset = UNSET
    port_uuids: list[str] | Unset = UNSET
    interval: int | Unset = UNSET
    unit: int | Unset = UNSET
    support_custom_interval: bool | Unset = UNSET
    support_discrete_wan: bool | Unset = UNSET
    support_reduce_usb_rfi: bool | Unset = UNSET
    support_all_wan: bool | Unset = UNSET
    support_max_wan_num: int | Unset = UNSET
    support_ipv_6_non_address: bool | Unset = UNSET
    support_mss_clamping: bool | Unset = UNSET
    support_pppoe_mru: bool | Unset = UNSET
    support_wan_multiple_ip: bool | Unset = UNSET
    support_lte: bool | Unset = UNSET
    support_dual_sim: int | Unset = UNSET
    support_dsl: bool | Unset = UNSET
    support_virtual_wan: bool | Unset = UNSET
    support_network_isolation: bool | Unset = UNSET
    support_dhcp_options: bool | Unset = UNSET
    support_usb_dhcp_options: bool | Unset = UNSET
    support_ds_lite: bool | Unset = UNSET
    support_map_e: bool | Unset = UNSET
    support_timing_mode: bool | Unset = UNSET
    wan_port_settings: list[WanPortSettingOpenApiVO] | Unset = UNSET
    usb_lte_settings: list[UsbLteSettingOpenApiVO] | Unset = UNSET
    lte_wan_settings: list[LteWanPortSettingOpenApiVO] | Unset = UNSET
    wan_load_balance: WanLoadBalanceOpenApiVO | Unset = UNSET
    network_names: list[str] | Unset = UNSET
    unmatched_wans: list[str] | Unset = UNSET
    gateway_mac: str | Unset = UNSET
    enable_modified: bool | Unset = UNSET
    lte_interval_tips: bool | Unset = UNSET
    port_online_status: PortOnlineStatusOpenApiVO | Unset = UNSET
    resource: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        site_id = self.site_id

        omadac_id = self.omadac_id

        enable = self.enable

        osg_port_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.osg_port_info, Unset):
            osg_port_info = self.osg_port_info.to_dict()

        port_uuids: list[str] | Unset = UNSET
        if not isinstance(self.port_uuids, Unset):
            port_uuids = self.port_uuids

        interval = self.interval

        unit = self.unit

        support_custom_interval = self.support_custom_interval

        support_discrete_wan = self.support_discrete_wan

        support_reduce_usb_rfi = self.support_reduce_usb_rfi

        support_all_wan = self.support_all_wan

        support_max_wan_num = self.support_max_wan_num

        support_ipv_6_non_address = self.support_ipv_6_non_address

        support_mss_clamping = self.support_mss_clamping

        support_pppoe_mru = self.support_pppoe_mru

        support_wan_multiple_ip = self.support_wan_multiple_ip

        support_lte = self.support_lte

        support_dual_sim = self.support_dual_sim

        support_dsl = self.support_dsl

        support_virtual_wan = self.support_virtual_wan

        support_network_isolation = self.support_network_isolation

        support_dhcp_options = self.support_dhcp_options

        support_usb_dhcp_options = self.support_usb_dhcp_options

        support_ds_lite = self.support_ds_lite

        support_map_e = self.support_map_e

        support_timing_mode = self.support_timing_mode

        wan_port_settings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.wan_port_settings, Unset):
            wan_port_settings = []
            for wan_port_settings_item_data in self.wan_port_settings:
                wan_port_settings_item = wan_port_settings_item_data.to_dict()
                wan_port_settings.append(wan_port_settings_item)

        usb_lte_settings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.usb_lte_settings, Unset):
            usb_lte_settings = []
            for usb_lte_settings_item_data in self.usb_lte_settings:
                usb_lte_settings_item = usb_lte_settings_item_data.to_dict()
                usb_lte_settings.append(usb_lte_settings_item)

        lte_wan_settings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.lte_wan_settings, Unset):
            lte_wan_settings = []
            for lte_wan_settings_item_data in self.lte_wan_settings:
                lte_wan_settings_item = lte_wan_settings_item_data.to_dict()
                lte_wan_settings.append(lte_wan_settings_item)

        wan_load_balance: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wan_load_balance, Unset):
            wan_load_balance = self.wan_load_balance.to_dict()

        network_names: list[str] | Unset = UNSET
        if not isinstance(self.network_names, Unset):
            network_names = self.network_names

        unmatched_wans: list[str] | Unset = UNSET
        if not isinstance(self.unmatched_wans, Unset):
            unmatched_wans = self.unmatched_wans

        gateway_mac = self.gateway_mac

        enable_modified = self.enable_modified

        lte_interval_tips = self.lte_interval_tips

        port_online_status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.port_online_status, Unset):
            port_online_status = self.port_online_status.to_dict()

        resource = self.resource

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "siteId": site_id,
            }
        )
        if omadac_id is not UNSET:
            field_dict["omadacId"] = omadac_id
        if enable is not UNSET:
            field_dict["enable"] = enable
        if osg_port_info is not UNSET:
            field_dict["osgPortInfo"] = osg_port_info
        if port_uuids is not UNSET:
            field_dict["portUuids"] = port_uuids
        if interval is not UNSET:
            field_dict["interval"] = interval
        if unit is not UNSET:
            field_dict["unit"] = unit
        if support_custom_interval is not UNSET:
            field_dict["supportCustomInterval"] = support_custom_interval
        if support_discrete_wan is not UNSET:
            field_dict["supportDiscreteWan"] = support_discrete_wan
        if support_reduce_usb_rfi is not UNSET:
            field_dict["supportReduceUsbRfi"] = support_reduce_usb_rfi
        if support_all_wan is not UNSET:
            field_dict["supportAllWan"] = support_all_wan
        if support_max_wan_num is not UNSET:
            field_dict["supportMaxWanNum"] = support_max_wan_num
        if support_ipv_6_non_address is not UNSET:
            field_dict["supportIpv6NonAddress"] = support_ipv_6_non_address
        if support_mss_clamping is not UNSET:
            field_dict["supportMssClamping"] = support_mss_clamping
        if support_pppoe_mru is not UNSET:
            field_dict["supportPppoeMru"] = support_pppoe_mru
        if support_wan_multiple_ip is not UNSET:
            field_dict["supportWanMultipleIp"] = support_wan_multiple_ip
        if support_lte is not UNSET:
            field_dict["supportLte"] = support_lte
        if support_dual_sim is not UNSET:
            field_dict["supportDualSim"] = support_dual_sim
        if support_dsl is not UNSET:
            field_dict["supportDsl"] = support_dsl
        if support_virtual_wan is not UNSET:
            field_dict["supportVirtualWan"] = support_virtual_wan
        if support_network_isolation is not UNSET:
            field_dict["supportNetworkIsolation"] = support_network_isolation
        if support_dhcp_options is not UNSET:
            field_dict["supportDhcpOptions"] = support_dhcp_options
        if support_usb_dhcp_options is not UNSET:
            field_dict["supportUsbDhcpOptions"] = support_usb_dhcp_options
        if support_ds_lite is not UNSET:
            field_dict["supportDsLite"] = support_ds_lite
        if support_map_e is not UNSET:
            field_dict["supportMapE"] = support_map_e
        if support_timing_mode is not UNSET:
            field_dict["supportTimingMode"] = support_timing_mode
        if wan_port_settings is not UNSET:
            field_dict["wanPortSettings"] = wan_port_settings
        if usb_lte_settings is not UNSET:
            field_dict["usbLteSettings"] = usb_lte_settings
        if lte_wan_settings is not UNSET:
            field_dict["lteWanSettings"] = lte_wan_settings
        if wan_load_balance is not UNSET:
            field_dict["wanLoadBalance"] = wan_load_balance
        if network_names is not UNSET:
            field_dict["networkNames"] = network_names
        if unmatched_wans is not UNSET:
            field_dict["unmatchedWans"] = unmatched_wans
        if gateway_mac is not UNSET:
            field_dict["gatewayMac"] = gateway_mac
        if enable_modified is not UNSET:
            field_dict["enableModified"] = enable_modified
        if lte_interval_tips is not UNSET:
            field_dict["lteIntervalTips"] = lte_interval_tips
        if port_online_status is not UNSET:
            field_dict["portOnlineStatus"] = port_online_status
        if resource is not UNSET:
            field_dict["resource"] = resource

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.lte_wan_port_setting_open_api_vo import (
            LteWanPortSettingOpenApiVO,
        )
        from ..models.osg_port_info_open_api_vo import (
            OsgPortInfoOpenApiVO,
        )
        from ..models.port_online_status_open_api_vo import (
            PortOnlineStatusOpenApiVO,
        )
        from ..models.usb_lte_setting_open_api_vo import (
            UsbLteSettingOpenApiVO,
        )
        from ..models.wan_load_balance_open_api_vo import (
            WanLoadBalanceOpenApiVO,
        )
        from ..models.wan_port_setting_open_api_vo import (
            WanPortSettingOpenApiVO,
        )

        d = dict(src_dict)
        site_id = d.pop("siteId")

        omadac_id = d.pop("omadacId", UNSET)

        enable = d.pop("enable", UNSET)

        _osg_port_info = d.pop("osgPortInfo", UNSET)
        osg_port_info: OsgPortInfoOpenApiVO | Unset
        if isinstance(_osg_port_info, Unset):
            osg_port_info = UNSET
        else:
            osg_port_info = OsgPortInfoOpenApiVO.from_dict(_osg_port_info)

        port_uuids = cast(list[str], d.pop("portUuids", UNSET))

        interval = d.pop("interval", UNSET)

        unit = d.pop("unit", UNSET)

        support_custom_interval = d.pop("supportCustomInterval", UNSET)

        support_discrete_wan = d.pop("supportDiscreteWan", UNSET)

        support_reduce_usb_rfi = d.pop("supportReduceUsbRfi", UNSET)

        support_all_wan = d.pop("supportAllWan", UNSET)

        support_max_wan_num = d.pop("supportMaxWanNum", UNSET)

        support_ipv_6_non_address = d.pop("supportIpv6NonAddress", UNSET)

        support_mss_clamping = d.pop("supportMssClamping", UNSET)

        support_pppoe_mru = d.pop("supportPppoeMru", UNSET)

        support_wan_multiple_ip = d.pop("supportWanMultipleIp", UNSET)

        support_lte = d.pop("supportLte", UNSET)

        support_dual_sim = d.pop("supportDualSim", UNSET)

        support_dsl = d.pop("supportDsl", UNSET)

        support_virtual_wan = d.pop("supportVirtualWan", UNSET)

        support_network_isolation = d.pop("supportNetworkIsolation", UNSET)

        support_dhcp_options = d.pop("supportDhcpOptions", UNSET)

        support_usb_dhcp_options = d.pop("supportUsbDhcpOptions", UNSET)

        support_ds_lite = d.pop("supportDsLite", UNSET)

        support_map_e = d.pop("supportMapE", UNSET)

        support_timing_mode = d.pop("supportTimingMode", UNSET)

        _wan_port_settings = d.pop("wanPortSettings", UNSET)
        wan_port_settings: list[WanPortSettingOpenApiVO] | Unset = UNSET
        if _wan_port_settings is not UNSET:
            wan_port_settings = []
            for wan_port_settings_item_data in _wan_port_settings:
                wan_port_settings_item = WanPortSettingOpenApiVO.from_dict(
                    wan_port_settings_item_data
                )

                wan_port_settings.append(wan_port_settings_item)

        _usb_lte_settings = d.pop("usbLteSettings", UNSET)
        usb_lte_settings: list[UsbLteSettingOpenApiVO] | Unset = UNSET
        if _usb_lte_settings is not UNSET:
            usb_lte_settings = []
            for usb_lte_settings_item_data in _usb_lte_settings:
                usb_lte_settings_item = UsbLteSettingOpenApiVO.from_dict(
                    usb_lte_settings_item_data
                )

                usb_lte_settings.append(usb_lte_settings_item)

        _lte_wan_settings = d.pop("lteWanSettings", UNSET)
        lte_wan_settings: list[LteWanPortSettingOpenApiVO] | Unset = UNSET
        if _lte_wan_settings is not UNSET:
            lte_wan_settings = []
            for lte_wan_settings_item_data in _lte_wan_settings:
                lte_wan_settings_item = LteWanPortSettingOpenApiVO.from_dict(
                    lte_wan_settings_item_data
                )

                lte_wan_settings.append(lte_wan_settings_item)

        _wan_load_balance = d.pop("wanLoadBalance", UNSET)
        wan_load_balance: WanLoadBalanceOpenApiVO | Unset
        if isinstance(_wan_load_balance, Unset):
            wan_load_balance = UNSET
        else:
            wan_load_balance = WanLoadBalanceOpenApiVO.from_dict(_wan_load_balance)

        network_names = cast(list[str], d.pop("networkNames", UNSET))

        unmatched_wans = cast(list[str], d.pop("unmatchedWans", UNSET))

        gateway_mac = d.pop("gatewayMac", UNSET)

        enable_modified = d.pop("enableModified", UNSET)

        lte_interval_tips = d.pop("lteIntervalTips", UNSET)

        _port_online_status = d.pop("portOnlineStatus", UNSET)
        port_online_status: PortOnlineStatusOpenApiVO | Unset
        if isinstance(_port_online_status, Unset):
            port_online_status = UNSET
        else:
            port_online_status = PortOnlineStatusOpenApiVO.from_dict(
                _port_online_status
            )

        resource = d.pop("resource", UNSET)

        internet_open_api_vo = cls(
            site_id=site_id,
            omadac_id=omadac_id,
            enable=enable,
            osg_port_info=osg_port_info,
            port_uuids=port_uuids,
            interval=interval,
            unit=unit,
            support_custom_interval=support_custom_interval,
            support_discrete_wan=support_discrete_wan,
            support_reduce_usb_rfi=support_reduce_usb_rfi,
            support_all_wan=support_all_wan,
            support_max_wan_num=support_max_wan_num,
            support_ipv_6_non_address=support_ipv_6_non_address,
            support_mss_clamping=support_mss_clamping,
            support_pppoe_mru=support_pppoe_mru,
            support_wan_multiple_ip=support_wan_multiple_ip,
            support_lte=support_lte,
            support_dual_sim=support_dual_sim,
            support_dsl=support_dsl,
            support_virtual_wan=support_virtual_wan,
            support_network_isolation=support_network_isolation,
            support_dhcp_options=support_dhcp_options,
            support_usb_dhcp_options=support_usb_dhcp_options,
            support_ds_lite=support_ds_lite,
            support_map_e=support_map_e,
            support_timing_mode=support_timing_mode,
            wan_port_settings=wan_port_settings,
            usb_lte_settings=usb_lte_settings,
            lte_wan_settings=lte_wan_settings,
            wan_load_balance=wan_load_balance,
            network_names=network_names,
            unmatched_wans=unmatched_wans,
            gateway_mac=gateway_mac,
            enable_modified=enable_modified,
            lte_interval_tips=lte_interval_tips,
            port_online_status=port_online_status,
            resource=resource,
        )

        internet_open_api_vo.additional_properties = d
        return internet_open_api_vo

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
