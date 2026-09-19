from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dhcp_servers_setting import DhcpServersSetting
    from ..models.dhcp_setting_config import DhcpSettingConfig
    from ..models.dhcpv_6_servers_setting import Dhcpv6ServersSetting
    from ..models.lan_network_ipv6_config import LanNetworkIPV6Config
    from ..models.osw_dhcp_relay_open_api_vo import OswDhcpRelayOpenApiVO
    from ..models.osw_dhcp_server_open_api_vo import OswDhcpServerOpenApiVO
    from ..models.osw_ip_setting_brief_openapi_vo import OswIpSettingBriefOpenapiVO


T = TypeVar("T", bound="LanNetworkOpenApiV3VO")


@_attrs_define
class LanNetworkOpenApiV3VO:
    """LANNetworkOpenApiVO

    Attributes:
        name (str): LAN network name should contain 1 to 128 characters.
        igmp_snoop_enable (bool): Enable IGMP snooping
        device_type (int): DHCP Server Device type. It should be a value as follows: 0:External Device 1:gateway
            2:switch 3:none
        vlan_type (int | Unset): VLANType should be a value as follows: 0: Single; 1: Multiple
        vlans (str | Unset): Only valid when vlanType is 1 and device type is 0 , 1 or 3. When device type is 0 or 3,
            batch create single vlan, when deviceType is 1 , create bridge vlan. VLAN format: 200, 1-100.
        vlan (int | Unset): Only Valid when vlanType is 0. Vlan should be within the range of 1-4094.
        gateway_subnet (str | Unset): When deviceType is 1, gateway subnet is needed. Format: IP/Mask
        dhcp_settings (DhcpSettingConfig | Unset): Configure DHCP settings
        domain (str | Unset): The domain of this network
        mld_snoop_enable (bool | Unset): Enable MLD snooping
        dhcp_l2_relay_enable (bool | Unset): The switch of DHCP L2 relay
        dhcp_guard (DhcpServersSetting | Unset): Legal DHCP Server
        dhcpv_6_guard (Dhcpv6ServersSetting | Unset): Legal DHCPv6 Server
        lan_network_ipv_6_config (LanNetworkIPV6Config | Unset): LAN network IPv6 config
        arp_detection_enable (bool | Unset): Enable arp detection. Only valid when deviceType is 1 and gateway supports
            this feature.
        isolation (bool | Unset): Whether network isolated.
        qos_queue_enable (bool | Unset): The switch of QoS queue.
        queue_id (int | Unset): QoS queue Id.
        device_mac (str | Unset): DHCP Server Device mac. Only valid when deviceType is 1 or 2. When deviceType is 1,
            deviceMac can be empty when there is no gateway in the site.
        stack_id (str | Unset): DHCP Server Device stackId. Only valid when deviceType is 2 and the selected device is
            stack
        ip (OswIpSettingBriefOpenapiVO | Unset): Network IP setting. Only valid when deviceType is 2.
        mode (int | Unset): DHCP mode. 0: None 1: DHCP Server 2: DHCP Relay. Only valid when deviceType is 2.
        vrf_id (str | Unset): VRF ID
        dhcp_server (OswDhcpServerOpenApiVO | Unset): Network DHCP server settings. Only valid when deviceType is 2 and
            mode is 1.
        dhcp_relay (OswDhcpRelayOpenApiVO | Unset): Network DHCP relay settings. Only valid when deviceType is 2 and
            mode is 2
        subnet_override_enable (bool | Unset): The switch status of DHCP Settings Overrides.
    """

    name: str
    igmp_snoop_enable: bool
    device_type: int
    vlan_type: int | Unset = UNSET
    vlans: str | Unset = UNSET
    vlan: int | Unset = UNSET
    gateway_subnet: str | Unset = UNSET
    dhcp_settings: DhcpSettingConfig | Unset = UNSET
    domain: str | Unset = UNSET
    mld_snoop_enable: bool | Unset = UNSET
    dhcp_l2_relay_enable: bool | Unset = UNSET
    dhcp_guard: DhcpServersSetting | Unset = UNSET
    dhcpv_6_guard: Dhcpv6ServersSetting | Unset = UNSET
    lan_network_ipv_6_config: LanNetworkIPV6Config | Unset = UNSET
    arp_detection_enable: bool | Unset = UNSET
    isolation: bool | Unset = UNSET
    qos_queue_enable: bool | Unset = UNSET
    queue_id: int | Unset = UNSET
    device_mac: str | Unset = UNSET
    stack_id: str | Unset = UNSET
    ip: OswIpSettingBriefOpenapiVO | Unset = UNSET
    mode: int | Unset = UNSET
    vrf_id: str | Unset = UNSET
    dhcp_server: OswDhcpServerOpenApiVO | Unset = UNSET
    dhcp_relay: OswDhcpRelayOpenApiVO | Unset = UNSET
    subnet_override_enable: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        igmp_snoop_enable = self.igmp_snoop_enable

        device_type = self.device_type

        vlan_type = self.vlan_type

        vlans = self.vlans

        vlan = self.vlan

        gateway_subnet = self.gateway_subnet

        dhcp_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dhcp_settings, Unset):
            dhcp_settings = self.dhcp_settings.to_dict()

        domain = self.domain

        mld_snoop_enable = self.mld_snoop_enable

        dhcp_l2_relay_enable = self.dhcp_l2_relay_enable

        dhcp_guard: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dhcp_guard, Unset):
            dhcp_guard = self.dhcp_guard.to_dict()

        dhcpv_6_guard: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dhcpv_6_guard, Unset):
            dhcpv_6_guard = self.dhcpv_6_guard.to_dict()

        lan_network_ipv_6_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lan_network_ipv_6_config, Unset):
            lan_network_ipv_6_config = self.lan_network_ipv_6_config.to_dict()

        arp_detection_enable = self.arp_detection_enable

        isolation = self.isolation

        qos_queue_enable = self.qos_queue_enable

        queue_id = self.queue_id

        device_mac = self.device_mac

        stack_id = self.stack_id

        ip: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ip, Unset):
            ip = self.ip.to_dict()

        mode = self.mode

        vrf_id = self.vrf_id

        dhcp_server: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dhcp_server, Unset):
            dhcp_server = self.dhcp_server.to_dict()

        dhcp_relay: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dhcp_relay, Unset):
            dhcp_relay = self.dhcp_relay.to_dict()

        subnet_override_enable = self.subnet_override_enable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "igmpSnoopEnable": igmp_snoop_enable,
                "deviceType": device_type,
            }
        )
        if vlan_type is not UNSET:
            field_dict["vlanType"] = vlan_type
        if vlans is not UNSET:
            field_dict["vlans"] = vlans
        if vlan is not UNSET:
            field_dict["vlan"] = vlan
        if gateway_subnet is not UNSET:
            field_dict["gatewaySubnet"] = gateway_subnet
        if dhcp_settings is not UNSET:
            field_dict["dhcpSettings"] = dhcp_settings
        if domain is not UNSET:
            field_dict["domain"] = domain
        if mld_snoop_enable is not UNSET:
            field_dict["mldSnoopEnable"] = mld_snoop_enable
        if dhcp_l2_relay_enable is not UNSET:
            field_dict["dhcpL2RelayEnable"] = dhcp_l2_relay_enable
        if dhcp_guard is not UNSET:
            field_dict["dhcpGuard"] = dhcp_guard
        if dhcpv_6_guard is not UNSET:
            field_dict["dhcpv6Guard"] = dhcpv_6_guard
        if lan_network_ipv_6_config is not UNSET:
            field_dict["lanNetworkIpv6Config"] = lan_network_ipv_6_config
        if arp_detection_enable is not UNSET:
            field_dict["arpDetectionEnable"] = arp_detection_enable
        if isolation is not UNSET:
            field_dict["isolation"] = isolation
        if qos_queue_enable is not UNSET:
            field_dict["qosQueueEnable"] = qos_queue_enable
        if queue_id is not UNSET:
            field_dict["queueId"] = queue_id
        if device_mac is not UNSET:
            field_dict["deviceMac"] = device_mac
        if stack_id is not UNSET:
            field_dict["stackId"] = stack_id
        if ip is not UNSET:
            field_dict["ip"] = ip
        if mode is not UNSET:
            field_dict["mode"] = mode
        if vrf_id is not UNSET:
            field_dict["vrfId"] = vrf_id
        if dhcp_server is not UNSET:
            field_dict["dhcpServer"] = dhcp_server
        if dhcp_relay is not UNSET:
            field_dict["dhcpRelay"] = dhcp_relay
        if subnet_override_enable is not UNSET:
            field_dict["subnetOverrideEnable"] = subnet_override_enable

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.dhcp_servers_setting import DhcpServersSetting
        from ..models.dhcp_setting_config import DhcpSettingConfig
        from ..models.dhcpv_6_servers_setting import (
            Dhcpv6ServersSetting,
        )
        from ..models.lan_network_ipv6_config import (
            LanNetworkIPV6Config,
        )
        from ..models.osw_dhcp_relay_open_api_vo import (
            OswDhcpRelayOpenApiVO,
        )
        from ..models.osw_dhcp_server_open_api_vo import (
            OswDhcpServerOpenApiVO,
        )
        from ..models.osw_ip_setting_brief_openapi_vo import (
            OswIpSettingBriefOpenapiVO,
        )

        d = dict(src_dict)
        name = d.pop("name")

        igmp_snoop_enable = d.pop("igmpSnoopEnable")

        device_type = d.pop("deviceType")

        vlan_type = d.pop("vlanType", UNSET)

        vlans = d.pop("vlans", UNSET)

        vlan = d.pop("vlan", UNSET)

        gateway_subnet = d.pop("gatewaySubnet", UNSET)

        _dhcp_settings = d.pop("dhcpSettings", UNSET)
        dhcp_settings: DhcpSettingConfig | Unset
        if isinstance(_dhcp_settings, Unset):
            dhcp_settings = UNSET
        else:
            dhcp_settings = DhcpSettingConfig.from_dict(_dhcp_settings)

        domain = d.pop("domain", UNSET)

        mld_snoop_enable = d.pop("mldSnoopEnable", UNSET)

        dhcp_l2_relay_enable = d.pop("dhcpL2RelayEnable", UNSET)

        _dhcp_guard = d.pop("dhcpGuard", UNSET)
        dhcp_guard: DhcpServersSetting | Unset
        if isinstance(_dhcp_guard, Unset):
            dhcp_guard = UNSET
        else:
            dhcp_guard = DhcpServersSetting.from_dict(_dhcp_guard)

        _dhcpv_6_guard = d.pop("dhcpv6Guard", UNSET)
        dhcpv_6_guard: Dhcpv6ServersSetting | Unset
        if isinstance(_dhcpv_6_guard, Unset):
            dhcpv_6_guard = UNSET
        else:
            dhcpv_6_guard = Dhcpv6ServersSetting.from_dict(_dhcpv_6_guard)

        _lan_network_ipv_6_config = d.pop("lanNetworkIpv6Config", UNSET)
        lan_network_ipv_6_config: LanNetworkIPV6Config | Unset
        if isinstance(_lan_network_ipv_6_config, Unset):
            lan_network_ipv_6_config = UNSET
        else:
            lan_network_ipv_6_config = LanNetworkIPV6Config.from_dict(
                _lan_network_ipv_6_config
            )

        arp_detection_enable = d.pop("arpDetectionEnable", UNSET)

        isolation = d.pop("isolation", UNSET)

        qos_queue_enable = d.pop("qosQueueEnable", UNSET)

        queue_id = d.pop("queueId", UNSET)

        device_mac = d.pop("deviceMac", UNSET)

        stack_id = d.pop("stackId", UNSET)

        _ip = d.pop("ip", UNSET)
        ip: OswIpSettingBriefOpenapiVO | Unset
        if isinstance(_ip, Unset):
            ip = UNSET
        else:
            ip = OswIpSettingBriefOpenapiVO.from_dict(_ip)

        mode = d.pop("mode", UNSET)

        vrf_id = d.pop("vrfId", UNSET)

        _dhcp_server = d.pop("dhcpServer", UNSET)
        dhcp_server: OswDhcpServerOpenApiVO | Unset
        if isinstance(_dhcp_server, Unset):
            dhcp_server = UNSET
        else:
            dhcp_server = OswDhcpServerOpenApiVO.from_dict(_dhcp_server)

        _dhcp_relay = d.pop("dhcpRelay", UNSET)
        dhcp_relay: OswDhcpRelayOpenApiVO | Unset
        if isinstance(_dhcp_relay, Unset):
            dhcp_relay = UNSET
        else:
            dhcp_relay = OswDhcpRelayOpenApiVO.from_dict(_dhcp_relay)

        subnet_override_enable = d.pop("subnetOverrideEnable", UNSET)

        lan_network_open_api_v3vo = cls(
            name=name,
            igmp_snoop_enable=igmp_snoop_enable,
            device_type=device_type,
            vlan_type=vlan_type,
            vlans=vlans,
            vlan=vlan,
            gateway_subnet=gateway_subnet,
            dhcp_settings=dhcp_settings,
            domain=domain,
            mld_snoop_enable=mld_snoop_enable,
            dhcp_l2_relay_enable=dhcp_l2_relay_enable,
            dhcp_guard=dhcp_guard,
            dhcpv_6_guard=dhcpv_6_guard,
            lan_network_ipv_6_config=lan_network_ipv_6_config,
            arp_detection_enable=arp_detection_enable,
            isolation=isolation,
            qos_queue_enable=qos_queue_enable,
            queue_id=queue_id,
            device_mac=device_mac,
            stack_id=stack_id,
            ip=ip,
            mode=mode,
            vrf_id=vrf_id,
            dhcp_server=dhcp_server,
            dhcp_relay=dhcp_relay,
            subnet_override_enable=subnet_override_enable,
        )

        lan_network_open_api_v3vo.additional_properties = d
        return lan_network_open_api_v3vo

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
