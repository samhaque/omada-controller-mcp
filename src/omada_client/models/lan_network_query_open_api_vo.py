from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dhcp_servers_setting import DhcpServersSetting
    from ..models.dhcp_settings import DhcpSettings
    from ..models.dhcpv_6_servers_setting import Dhcpv6ServersSetting
    from ..models.lan_network_ipv6_config import LanNetworkIPV6Config


T = TypeVar("T", bound="LanNetworkQueryOpenApiVO")


@_attrs_define
class LanNetworkQueryOpenApiVO:
    """LANNetworkQueryOpenApiVO

    Attributes:
        name (str): LAN network name should contain 1 to 128 characters.
        purpose (int): LAN network purpose, 0: VLAN, 1: interface
        igmp_snoop_enable (bool): Enable IGMP snooping
        id (str | Unset): LAN network ID
        interface_ids (list[str] | Unset): Gateway LAN port IDs (acquired from "Check WAN/LAN status")
        vlan_type (int | Unset): When purpose is interface, VLANType is valid. 0: Single; 1: Multiple
        vlans (str | Unset): When purpose is interface and VLANType is 1, batch create VLANs. VLAN format: 200, 1-100.
        vlan (int | Unset): When purpose is "VLAN" or purpose is "interface" and VLANType is 0, create VLAN. VLAN range
            1 to 4090.
        application (int | Unset): Effective device type. 0: Gateway, Switch; 1: Switch
        gateway_subnet (str | Unset): When purpose is interface, gateway subnet is needed. Format: IP/Mask
        dhcp_settings_vo (DhcpSettings | Unset): Configure DHCP settings
        domain (str | Unset): The domain of this network
        mld_snoop_enable (bool | Unset): Enable MLD snooping
        dhcp_l2_relay_enable (bool | Unset): The switch of DHCP L2 relay
        dhcp_guard (DhcpServersSetting | Unset): Legal DHCP Server
        dhcpv_6_guard (Dhcpv6ServersSetting | Unset): Legal DHCPv6 Server
        portal (bool | Unset): Show portal is enabled or not
        portal_id (str | Unset): Show portal ID
        portal_name (str | Unset): Show related portal name
        access_control_rule (bool | Unset): Show AccessControlRule is enabled or not
        rate_limit (bool | Unset): Show RateLimit is enabled or not
        lan_nework_ipv_6_config (LanNetworkIPV6Config | Unset): LAN network IPv6 config
        all_lan (bool | Unset): When Internet pre-config is closed or Internet pre-config is Universal, allLAN is
            "true"; after adopting gateway, allLAN is "false".
        qos_queue_enable (bool | Unset): The switch of QoS(Quality of Service).
        queue_id (int | Unset): The queue Id of QoS.
        primary (bool | Unset): Primary
    """

    name: str
    purpose: int
    igmp_snoop_enable: bool
    id: str | Unset = UNSET
    interface_ids: list[str] | Unset = UNSET
    vlan_type: int | Unset = UNSET
    vlans: str | Unset = UNSET
    vlan: int | Unset = UNSET
    application: int | Unset = UNSET
    gateway_subnet: str | Unset = UNSET
    dhcp_settings_vo: DhcpSettings | Unset = UNSET
    domain: str | Unset = UNSET
    mld_snoop_enable: bool | Unset = UNSET
    dhcp_l2_relay_enable: bool | Unset = UNSET
    dhcp_guard: DhcpServersSetting | Unset = UNSET
    dhcpv_6_guard: Dhcpv6ServersSetting | Unset = UNSET
    portal: bool | Unset = UNSET
    portal_id: str | Unset = UNSET
    portal_name: str | Unset = UNSET
    access_control_rule: bool | Unset = UNSET
    rate_limit: bool | Unset = UNSET
    lan_nework_ipv_6_config: LanNetworkIPV6Config | Unset = UNSET
    all_lan: bool | Unset = UNSET
    qos_queue_enable: bool | Unset = UNSET
    queue_id: int | Unset = UNSET
    primary: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        purpose = self.purpose

        igmp_snoop_enable = self.igmp_snoop_enable

        id = self.id

        interface_ids: list[str] | Unset = UNSET
        if not isinstance(self.interface_ids, Unset):
            interface_ids = self.interface_ids

        vlan_type = self.vlan_type

        vlans = self.vlans

        vlan = self.vlan

        application = self.application

        gateway_subnet = self.gateway_subnet

        dhcp_settings_vo: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dhcp_settings_vo, Unset):
            dhcp_settings_vo = self.dhcp_settings_vo.to_dict()

        domain = self.domain

        mld_snoop_enable = self.mld_snoop_enable

        dhcp_l2_relay_enable = self.dhcp_l2_relay_enable

        dhcp_guard: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dhcp_guard, Unset):
            dhcp_guard = self.dhcp_guard.to_dict()

        dhcpv_6_guard: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dhcpv_6_guard, Unset):
            dhcpv_6_guard = self.dhcpv_6_guard.to_dict()

        portal = self.portal

        portal_id = self.portal_id

        portal_name = self.portal_name

        access_control_rule = self.access_control_rule

        rate_limit = self.rate_limit

        lan_nework_ipv_6_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lan_nework_ipv_6_config, Unset):
            lan_nework_ipv_6_config = self.lan_nework_ipv_6_config.to_dict()

        all_lan = self.all_lan

        qos_queue_enable = self.qos_queue_enable

        queue_id = self.queue_id

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
        if interface_ids is not UNSET:
            field_dict["interfaceIds"] = interface_ids
        if vlan_type is not UNSET:
            field_dict["vlanType"] = vlan_type
        if vlans is not UNSET:
            field_dict["vlans"] = vlans
        if vlan is not UNSET:
            field_dict["vlan"] = vlan
        if application is not UNSET:
            field_dict["application"] = application
        if gateway_subnet is not UNSET:
            field_dict["gatewaySubnet"] = gateway_subnet
        if dhcp_settings_vo is not UNSET:
            field_dict["dhcpSettingsVO"] = dhcp_settings_vo
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
        if qos_queue_enable is not UNSET:
            field_dict["qosQueueEnable"] = qos_queue_enable
        if queue_id is not UNSET:
            field_dict["queueId"] = queue_id
        if primary is not UNSET:
            field_dict["primary"] = primary

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.dhcp_servers_setting import DhcpServersSetting
        from ..models.dhcp_settings import DhcpSettings
        from ..models.dhcpv_6_servers_setting import (
            Dhcpv6ServersSetting,
        )
        from ..models.lan_network_ipv6_config import (
            LanNetworkIPV6Config,
        )

        d = dict(src_dict)
        name = d.pop("name")

        purpose = d.pop("purpose")

        igmp_snoop_enable = d.pop("igmpSnoopEnable")

        id = d.pop("id", UNSET)

        interface_ids = cast(list[str], d.pop("interfaceIds", UNSET))

        vlan_type = d.pop("vlanType", UNSET)

        vlans = d.pop("vlans", UNSET)

        vlan = d.pop("vlan", UNSET)

        application = d.pop("application", UNSET)

        gateway_subnet = d.pop("gatewaySubnet", UNSET)

        _dhcp_settings_vo = d.pop("dhcpSettingsVO", UNSET)
        dhcp_settings_vo: DhcpSettings | Unset
        if isinstance(_dhcp_settings_vo, Unset):
            dhcp_settings_vo = UNSET
        else:
            dhcp_settings_vo = DhcpSettings.from_dict(_dhcp_settings_vo)

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

        qos_queue_enable = d.pop("qosQueueEnable", UNSET)

        queue_id = d.pop("queueId", UNSET)

        primary = d.pop("primary", UNSET)

        lan_network_query_open_api_vo = cls(
            name=name,
            purpose=purpose,
            igmp_snoop_enable=igmp_snoop_enable,
            id=id,
            interface_ids=interface_ids,
            vlan_type=vlan_type,
            vlans=vlans,
            vlan=vlan,
            application=application,
            gateway_subnet=gateway_subnet,
            dhcp_settings_vo=dhcp_settings_vo,
            domain=domain,
            mld_snoop_enable=mld_snoop_enable,
            dhcp_l2_relay_enable=dhcp_l2_relay_enable,
            dhcp_guard=dhcp_guard,
            dhcpv_6_guard=dhcpv_6_guard,
            portal=portal,
            portal_id=portal_id,
            portal_name=portal_name,
            access_control_rule=access_control_rule,
            rate_limit=rate_limit,
            lan_nework_ipv_6_config=lan_nework_ipv_6_config,
            all_lan=all_lan,
            qos_queue_enable=qos_queue_enable,
            queue_id=queue_id,
            primary=primary,
        )

        lan_network_query_open_api_vo.additional_properties = d
        return lan_network_query_open_api_vo

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
