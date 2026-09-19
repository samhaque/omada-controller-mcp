from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dhcp_ip_vo import DhcpIpVO
    from ..models.dhcp_servers_setting import DhcpServersSetting
    from ..models.dhcp_setting_info import DhcpSettingInfo
    from ..models.dhcpv_6_servers_setting import Dhcpv6ServersSetting
    from ..models.lan_network_ipv6_config import LanNetworkIPV6Config
    from ..models.osw_dhcp_relay_vo import OswDhcpRelayVO
    from ..models.osw_dhcp_server_vo import OswDhcpServerVO
    from ..models.osw_ip_setting_vo import OswIpSettingVO


T = TypeVar("T", bound="LanNetworkVO")


@_attrs_define
class LanNetworkVO:
    """LANNetworkVO

    Attributes:
        name (str): LAN network name should contain 1 to 128 characters.
        purpose (str): LAN network purpose should be as follows: vlan or interface
        igmp_snoop_enable (bool): Enable IGMP snooping
        id (str | Unset): LAN network ID
        site (str | Unset): Site ID
        interface_ids (list[str] | Unset): Gateway LAN port IDs (acquired from "Check WAN/LAN status")
        vlan_type (int | Unset): When purpose is interface, VLANType should be a value as follows: 0: Single; 1:
            Multiple
        vlans (str | Unset): When purpose is interface and VLANType is 1, batch create VLANs. VLAN format: 200, 1-100.
        application (int | Unset): Effective device type should be a value as follows: 0: Gateway and Switch; 1: Switch
        isolation (bool | Unset): Whether network isolated.
        vlan (int | Unset): Only Valid when vlanType is 0. Vlan should be within the range of 1-4094.
        gateway_subnet (str | Unset): When purpose is interface, gateway subnet is needed. Format: IP/Mask
        dhcp_settings (DhcpSettingInfo | Unset): Configure DHCP settings
        domain (str | Unset): The domain of this network
        fast_leave_enable (bool | Unset): IGMP Snooping fast leave enable status
        mld_snoop_enable (bool | Unset): Enable MLD snooping
        dhcpv_6_guard (Dhcpv6ServersSetting | Unset): Legal DHCPv6 Server
        dhcp_l2_relay_enable (bool | Unset): The switch of DHCP L2 relay
        dhcp_guard (DhcpServersSetting | Unset): Legal DHCP Server
        portal (bool | Unset): Show portal is enabled or not
        portal_id (str | Unset): Show portal ID
        portal_name (str | Unset): Show related portal name
        access_control_rule (bool | Unset): Show AccessControlRule is enabled or not
        rate_limit (bool | Unset): Show RateLimit is enabled or not
        lan_nework_ipv_6_config (LanNetworkIPV6Config | Unset): LAN network IPv6 config
        all_lan (bool | Unset): When Internet pre-config is closed or Internet pre-config is Universal, allLAN is
            "true"; after adopting gateway, allLAN is "false".
        resource (int | Unset): Resource is a value as follows: 0: new created; 1: from template; 2: override
        orig_name (str | Unset): Original name
        arp_detection_enable (bool | Unset): Enable arp detection. Only valid when deviceType is 1 and gateway supports
            this feature.
        qos_queue_enable (bool | Unset): The switch of QoS queue.
        queue_id (int | Unset): QoS queue Id.
        exist_multi_vlan (bool | Unset): Whether VLAN Type is Multiple.
        exist_ra (bool | Unset): Whether RA has been configured.
        exist_custom_dhcp_option (bool | Unset): Whether custom DHCP Options has been configured.
        exist_dhcp_next_server (bool | Unset): Whether DHCP Next Server has been configured.
        exist_arp_detection (bool | Unset): Whether Arp Detection is configured.
        exist_network_isolation (bool | Unset): Whether Network Isolation is configured.
        device_type (int | Unset): DHCP Server Device type. It should be a value as follows: 0:External Device 1:gateway
            2:switch 3:none
        device_mac (str | Unset): DHCP Server Device mac. Only valid when deviceType is 1 or 2. When deviceType is 1,
            deviceMac can be empty when there is no gateway in the site.
        stack_id (str | Unset): DHCP Server Device stackId. Only valid when deviceType is 2 and the selected device is
            stack
        vrf_id (str | Unset): VRF ID
        ip (OswIpSettingVO | Unset): Network IP setting.
        mode (int | Unset): DHCP mode. 0: None 1: DHCP Server 2: DHCP Relay. Only valid when deviceType is 2.
        dhcp_server (OswDhcpServerVO | Unset): Network DHCP server settings.
        dhcp_relay (OswDhcpRelayVO | Unset): Network DHCP relay settings.
        state (int | Unset): Network delivering state. It should be a value as follows: 0: not in delivering
            1:delivering 2. deliver done
        total_ip_num (int | Unset): Total ip num
        dhcp_server_num (int | Unset): The number of dhcp server devices in effect, Only valid when vlanType is 0.
        dhcp_ip (DhcpIpVO | Unset): The dhcp ip and mask info obtained from device.
        subnet_override_enable (bool | Unset): Subnet override enable status
        subnet_override (bool | Unset): Subnet override
        interface (bool | Unset):
        primary (bool | Unset): Primary
    """

    name: str
    purpose: str
    igmp_snoop_enable: bool
    id: str | Unset = UNSET
    site: str | Unset = UNSET
    interface_ids: list[str] | Unset = UNSET
    vlan_type: int | Unset = UNSET
    vlans: str | Unset = UNSET
    application: int | Unset = UNSET
    isolation: bool | Unset = UNSET
    vlan: int | Unset = UNSET
    gateway_subnet: str | Unset = UNSET
    dhcp_settings: DhcpSettingInfo | Unset = UNSET
    domain: str | Unset = UNSET
    fast_leave_enable: bool | Unset = UNSET
    mld_snoop_enable: bool | Unset = UNSET
    dhcpv_6_guard: Dhcpv6ServersSetting | Unset = UNSET
    dhcp_l2_relay_enable: bool | Unset = UNSET
    dhcp_guard: DhcpServersSetting | Unset = UNSET
    portal: bool | Unset = UNSET
    portal_id: str | Unset = UNSET
    portal_name: str | Unset = UNSET
    access_control_rule: bool | Unset = UNSET
    rate_limit: bool | Unset = UNSET
    lan_nework_ipv_6_config: LanNetworkIPV6Config | Unset = UNSET
    all_lan: bool | Unset = UNSET
    resource: int | Unset = UNSET
    orig_name: str | Unset = UNSET
    arp_detection_enable: bool | Unset = UNSET
    qos_queue_enable: bool | Unset = UNSET
    queue_id: int | Unset = UNSET
    exist_multi_vlan: bool | Unset = UNSET
    exist_ra: bool | Unset = UNSET
    exist_custom_dhcp_option: bool | Unset = UNSET
    exist_dhcp_next_server: bool | Unset = UNSET
    exist_arp_detection: bool | Unset = UNSET
    exist_network_isolation: bool | Unset = UNSET
    device_type: int | Unset = UNSET
    device_mac: str | Unset = UNSET
    stack_id: str | Unset = UNSET
    vrf_id: str | Unset = UNSET
    ip: OswIpSettingVO | Unset = UNSET
    mode: int | Unset = UNSET
    dhcp_server: OswDhcpServerVO | Unset = UNSET
    dhcp_relay: OswDhcpRelayVO | Unset = UNSET
    state: int | Unset = UNSET
    total_ip_num: int | Unset = UNSET
    dhcp_server_num: int | Unset = UNSET
    dhcp_ip: DhcpIpVO | Unset = UNSET
    subnet_override_enable: bool | Unset = UNSET
    subnet_override: bool | Unset = UNSET
    interface: bool | Unset = UNSET
    primary: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        purpose = self.purpose

        igmp_snoop_enable = self.igmp_snoop_enable

        id = self.id

        site = self.site

        interface_ids: list[str] | Unset = UNSET
        if not isinstance(self.interface_ids, Unset):
            interface_ids = self.interface_ids

        vlan_type = self.vlan_type

        vlans = self.vlans

        application = self.application

        isolation = self.isolation

        vlan = self.vlan

        gateway_subnet = self.gateway_subnet

        dhcp_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dhcp_settings, Unset):
            dhcp_settings = self.dhcp_settings.to_dict()

        domain = self.domain

        fast_leave_enable = self.fast_leave_enable

        mld_snoop_enable = self.mld_snoop_enable

        dhcpv_6_guard: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dhcpv_6_guard, Unset):
            dhcpv_6_guard = self.dhcpv_6_guard.to_dict()

        dhcp_l2_relay_enable = self.dhcp_l2_relay_enable

        dhcp_guard: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dhcp_guard, Unset):
            dhcp_guard = self.dhcp_guard.to_dict()

        portal = self.portal

        portal_id = self.portal_id

        portal_name = self.portal_name

        access_control_rule = self.access_control_rule

        rate_limit = self.rate_limit

        lan_nework_ipv_6_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lan_nework_ipv_6_config, Unset):
            lan_nework_ipv_6_config = self.lan_nework_ipv_6_config.to_dict()

        all_lan = self.all_lan

        resource = self.resource

        orig_name = self.orig_name

        arp_detection_enable = self.arp_detection_enable

        qos_queue_enable = self.qos_queue_enable

        queue_id = self.queue_id

        exist_multi_vlan = self.exist_multi_vlan

        exist_ra = self.exist_ra

        exist_custom_dhcp_option = self.exist_custom_dhcp_option

        exist_dhcp_next_server = self.exist_dhcp_next_server

        exist_arp_detection = self.exist_arp_detection

        exist_network_isolation = self.exist_network_isolation

        device_type = self.device_type

        device_mac = self.device_mac

        stack_id = self.stack_id

        vrf_id = self.vrf_id

        ip: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ip, Unset):
            ip = self.ip.to_dict()

        mode = self.mode

        dhcp_server: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dhcp_server, Unset):
            dhcp_server = self.dhcp_server.to_dict()

        dhcp_relay: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dhcp_relay, Unset):
            dhcp_relay = self.dhcp_relay.to_dict()

        state = self.state

        total_ip_num = self.total_ip_num

        dhcp_server_num = self.dhcp_server_num

        dhcp_ip: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dhcp_ip, Unset):
            dhcp_ip = self.dhcp_ip.to_dict()

        subnet_override_enable = self.subnet_override_enable

        subnet_override = self.subnet_override

        interface = self.interface

        primary = self.primary

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "purpose": purpose,
                "igmpSnoopEnable": igmp_snoop_enable,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if site is not UNSET:
            field_dict["site"] = site
        if interface_ids is not UNSET:
            field_dict["interfaceIds"] = interface_ids
        if vlan_type is not UNSET:
            field_dict["vlanType"] = vlan_type
        if vlans is not UNSET:
            field_dict["vlans"] = vlans
        if application is not UNSET:
            field_dict["application"] = application
        if isolation is not UNSET:
            field_dict["isolation"] = isolation
        if vlan is not UNSET:
            field_dict["vlan"] = vlan
        if gateway_subnet is not UNSET:
            field_dict["gatewaySubnet"] = gateway_subnet
        if dhcp_settings is not UNSET:
            field_dict["dhcpSettings"] = dhcp_settings
        if domain is not UNSET:
            field_dict["domain"] = domain
        if fast_leave_enable is not UNSET:
            field_dict["fastLeaveEnable"] = fast_leave_enable
        if mld_snoop_enable is not UNSET:
            field_dict["mldSnoopEnable"] = mld_snoop_enable
        if dhcpv_6_guard is not UNSET:
            field_dict["dhcpv6Guard"] = dhcpv_6_guard
        if dhcp_l2_relay_enable is not UNSET:
            field_dict["dhcpL2RelayEnable"] = dhcp_l2_relay_enable
        if dhcp_guard is not UNSET:
            field_dict["dhcpGuard"] = dhcp_guard
        if portal is not UNSET:
            field_dict["portal"] = portal
        if portal_id is not UNSET:
            field_dict["portalId"] = portal_id
        if portal_name is not UNSET:
            field_dict["portalName"] = portal_name
        if access_control_rule is not UNSET:
            field_dict["accessControlRule"] = access_control_rule
        if rate_limit is not UNSET:
            field_dict["rateLimit"] = rate_limit
        if lan_nework_ipv_6_config is not UNSET:
            field_dict["lanNeworkIpv6Config"] = lan_nework_ipv_6_config
        if all_lan is not UNSET:
            field_dict["allLan"] = all_lan
        if resource is not UNSET:
            field_dict["resource"] = resource
        if orig_name is not UNSET:
            field_dict["origName"] = orig_name
        if arp_detection_enable is not UNSET:
            field_dict["arpDetectionEnable"] = arp_detection_enable
        if qos_queue_enable is not UNSET:
            field_dict["qosQueueEnable"] = qos_queue_enable
        if queue_id is not UNSET:
            field_dict["queueId"] = queue_id
        if exist_multi_vlan is not UNSET:
            field_dict["existMultiVlan"] = exist_multi_vlan
        if exist_ra is not UNSET:
            field_dict["existRA"] = exist_ra
        if exist_custom_dhcp_option is not UNSET:
            field_dict["existCustomDhcpOption"] = exist_custom_dhcp_option
        if exist_dhcp_next_server is not UNSET:
            field_dict["existDhcpNextServer"] = exist_dhcp_next_server
        if exist_arp_detection is not UNSET:
            field_dict["existArpDetection"] = exist_arp_detection
        if exist_network_isolation is not UNSET:
            field_dict["existNetworkIsolation"] = exist_network_isolation
        if device_type is not UNSET:
            field_dict["deviceType"] = device_type
        if device_mac is not UNSET:
            field_dict["deviceMac"] = device_mac
        if stack_id is not UNSET:
            field_dict["stackId"] = stack_id
        if vrf_id is not UNSET:
            field_dict["vrfId"] = vrf_id
        if ip is not UNSET:
            field_dict["ip"] = ip
        if mode is not UNSET:
            field_dict["mode"] = mode
        if dhcp_server is not UNSET:
            field_dict["dhcpServer"] = dhcp_server
        if dhcp_relay is not UNSET:
            field_dict["dhcpRelay"] = dhcp_relay
        if state is not UNSET:
            field_dict["state"] = state
        if total_ip_num is not UNSET:
            field_dict["totalIpNum"] = total_ip_num
        if dhcp_server_num is not UNSET:
            field_dict["dhcpServerNum"] = dhcp_server_num
        if dhcp_ip is not UNSET:
            field_dict["dhcpIp"] = dhcp_ip
        if subnet_override_enable is not UNSET:
            field_dict["subnetOverrideEnable"] = subnet_override_enable
        if subnet_override is not UNSET:
            field_dict["subnetOverride"] = subnet_override
        if interface is not UNSET:
            field_dict["interface"] = interface
        if primary is not UNSET:
            field_dict["primary"] = primary

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.dhcp_ip_vo import DhcpIpVO
        from ..models.dhcp_servers_setting import DhcpServersSetting
        from ..models.dhcp_setting_info import DhcpSettingInfo
        from ..models.dhcpv_6_servers_setting import (
            Dhcpv6ServersSetting,
        )
        from ..models.lan_network_ipv6_config import (
            LanNetworkIPV6Config,
        )
        from ..models.osw_dhcp_relay_vo import OswDhcpRelayVO
        from ..models.osw_dhcp_server_vo import OswDhcpServerVO
        from ..models.osw_ip_setting_vo import OswIpSettingVO

        d = dict(src_dict)
        name = d.pop("name")

        purpose = d.pop("purpose")

        igmp_snoop_enable = d.pop("igmpSnoopEnable")

        id = d.pop("id", UNSET)

        site = d.pop("site", UNSET)

        interface_ids = cast(list[str], d.pop("interfaceIds", UNSET))

        vlan_type = d.pop("vlanType", UNSET)

        vlans = d.pop("vlans", UNSET)

        application = d.pop("application", UNSET)

        isolation = d.pop("isolation", UNSET)

        vlan = d.pop("vlan", UNSET)

        gateway_subnet = d.pop("gatewaySubnet", UNSET)

        _dhcp_settings = d.pop("dhcpSettings", UNSET)
        dhcp_settings: DhcpSettingInfo | Unset
        if isinstance(_dhcp_settings, Unset):
            dhcp_settings = UNSET
        else:
            dhcp_settings = DhcpSettingInfo.from_dict(_dhcp_settings)

        domain = d.pop("domain", UNSET)

        fast_leave_enable = d.pop("fastLeaveEnable", UNSET)

        mld_snoop_enable = d.pop("mldSnoopEnable", UNSET)

        _dhcpv_6_guard = d.pop("dhcpv6Guard", UNSET)
        dhcpv_6_guard: Dhcpv6ServersSetting | Unset
        if isinstance(_dhcpv_6_guard, Unset):
            dhcpv_6_guard = UNSET
        else:
            dhcpv_6_guard = Dhcpv6ServersSetting.from_dict(_dhcpv_6_guard)

        dhcp_l2_relay_enable = d.pop("dhcpL2RelayEnable", UNSET)

        _dhcp_guard = d.pop("dhcpGuard", UNSET)
        dhcp_guard: DhcpServersSetting | Unset
        if isinstance(_dhcp_guard, Unset):
            dhcp_guard = UNSET
        else:
            dhcp_guard = DhcpServersSetting.from_dict(_dhcp_guard)

        portal = d.pop("portal", UNSET)

        portal_id = d.pop("portalId", UNSET)

        portal_name = d.pop("portalName", UNSET)

        access_control_rule = d.pop("accessControlRule", UNSET)

        rate_limit = d.pop("rateLimit", UNSET)

        _lan_nework_ipv_6_config = d.pop("lanNeworkIpv6Config", UNSET)
        lan_nework_ipv_6_config: LanNetworkIPV6Config | Unset
        if isinstance(_lan_nework_ipv_6_config, Unset):
            lan_nework_ipv_6_config = UNSET
        else:
            lan_nework_ipv_6_config = LanNetworkIPV6Config.from_dict(
                _lan_nework_ipv_6_config
            )

        all_lan = d.pop("allLan", UNSET)

        resource = d.pop("resource", UNSET)

        orig_name = d.pop("origName", UNSET)

        arp_detection_enable = d.pop("arpDetectionEnable", UNSET)

        qos_queue_enable = d.pop("qosQueueEnable", UNSET)

        queue_id = d.pop("queueId", UNSET)

        exist_multi_vlan = d.pop("existMultiVlan", UNSET)

        exist_ra = d.pop("existRA", UNSET)

        exist_custom_dhcp_option = d.pop("existCustomDhcpOption", UNSET)

        exist_dhcp_next_server = d.pop("existDhcpNextServer", UNSET)

        exist_arp_detection = d.pop("existArpDetection", UNSET)

        exist_network_isolation = d.pop("existNetworkIsolation", UNSET)

        device_type = d.pop("deviceType", UNSET)

        device_mac = d.pop("deviceMac", UNSET)

        stack_id = d.pop("stackId", UNSET)

        vrf_id = d.pop("vrfId", UNSET)

        _ip = d.pop("ip", UNSET)
        ip: OswIpSettingVO | Unset
        if isinstance(_ip, Unset):
            ip = UNSET
        else:
            ip = OswIpSettingVO.from_dict(_ip)

        mode = d.pop("mode", UNSET)

        _dhcp_server = d.pop("dhcpServer", UNSET)
        dhcp_server: OswDhcpServerVO | Unset
        if isinstance(_dhcp_server, Unset):
            dhcp_server = UNSET
        else:
            dhcp_server = OswDhcpServerVO.from_dict(_dhcp_server)

        _dhcp_relay = d.pop("dhcpRelay", UNSET)
        dhcp_relay: OswDhcpRelayVO | Unset
        if isinstance(_dhcp_relay, Unset):
            dhcp_relay = UNSET
        else:
            dhcp_relay = OswDhcpRelayVO.from_dict(_dhcp_relay)

        state = d.pop("state", UNSET)

        total_ip_num = d.pop("totalIpNum", UNSET)

        dhcp_server_num = d.pop("dhcpServerNum", UNSET)

        _dhcp_ip = d.pop("dhcpIp", UNSET)
        dhcp_ip: DhcpIpVO | Unset
        if isinstance(_dhcp_ip, Unset):
            dhcp_ip = UNSET
        else:
            dhcp_ip = DhcpIpVO.from_dict(_dhcp_ip)

        subnet_override_enable = d.pop("subnetOverrideEnable", UNSET)

        subnet_override = d.pop("subnetOverride", UNSET)

        interface = d.pop("interface", UNSET)

        primary = d.pop("primary", UNSET)

        lan_network_vo = cls(
            name=name,
            purpose=purpose,
            igmp_snoop_enable=igmp_snoop_enable,
            id=id,
            site=site,
            interface_ids=interface_ids,
            vlan_type=vlan_type,
            vlans=vlans,
            application=application,
            isolation=isolation,
            vlan=vlan,
            gateway_subnet=gateway_subnet,
            dhcp_settings=dhcp_settings,
            domain=domain,
            fast_leave_enable=fast_leave_enable,
            mld_snoop_enable=mld_snoop_enable,
            dhcpv_6_guard=dhcpv_6_guard,
            dhcp_l2_relay_enable=dhcp_l2_relay_enable,
            dhcp_guard=dhcp_guard,
            portal=portal,
            portal_id=portal_id,
            portal_name=portal_name,
            access_control_rule=access_control_rule,
            rate_limit=rate_limit,
            lan_nework_ipv_6_config=lan_nework_ipv_6_config,
            all_lan=all_lan,
            resource=resource,
            orig_name=orig_name,
            arp_detection_enable=arp_detection_enable,
            qos_queue_enable=qos_queue_enable,
            queue_id=queue_id,
            exist_multi_vlan=exist_multi_vlan,
            exist_ra=exist_ra,
            exist_custom_dhcp_option=exist_custom_dhcp_option,
            exist_dhcp_next_server=exist_dhcp_next_server,
            exist_arp_detection=exist_arp_detection,
            exist_network_isolation=exist_network_isolation,
            device_type=device_type,
            device_mac=device_mac,
            stack_id=stack_id,
            vrf_id=vrf_id,
            ip=ip,
            mode=mode,
            dhcp_server=dhcp_server,
            dhcp_relay=dhcp_relay,
            state=state,
            total_ip_num=total_ip_num,
            dhcp_server_num=dhcp_server_num,
            dhcp_ip=dhcp_ip,
            subnet_override_enable=subnet_override_enable,
            subnet_override=subnet_override,
            interface=interface,
            primary=primary,
        )

        lan_network_vo.additional_properties = d
        return lan_network_vo

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
