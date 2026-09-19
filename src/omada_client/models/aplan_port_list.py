from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ap_port_status_vo import ApPortStatusVO
    from ..models.onu_port_rate_limit_vo import ONUPortRateLimitVO


T = TypeVar("T", bound="APLANPortList")


@_attrs_define
class APLANPortList:
    """
    Attributes:
        id (str | Unset): Port Id
        onu_id (str | Unset): Onu Id
        port (int | Unset): Port Number
        port_type (int | Unset): Port Type
        lan_port (str | Unset): Lan Port
        name (str | Unset): Port Name. It should contain 1 ~ 64 ASCII characters. If it is NULL, LanPort is displayed.
        link_status (int | Unset): Link status; It should be a value as follows:  1:link up;  0: link down.
        link_speed (int | Unset): Real-time link speed;It should be a value as follows: 1: 10Mbps; 2: 100Mbps; 3:
            1000Mbps; 4: 10Gbps.
        duplex (int | Unset): Real-time duplex mode;It should be a value as follows: 1: Half; 2: Full.
        support_vlan (bool | Unset): Whether the port supports VLANs.
        local_vlan_enable (bool | Unset): Whether the port enable VLANs.
        local_vlan_id (int | Unset): Local vlan id.
        local_vlan_network_id (str | Unset): Local Vlan Network Id, used to enter the LAN field.
        status (bool | Unset): Whether to disable the port, defaults to true.
        support_poe (bool | Unset): Whether poe is supported.
        poe_out_enable (bool | Unset): Whether to enable poe out.
        poe_state (int | Unset): This value is only available when supportPoe is true.It should be a value as follows:
            0：In the power supply; 1：Not in the power supply.
        voip_state (int | Unset): This field has a value for the voice port.It should be a value as follows: 0：Off-hook;
            1：On-hook.
        support_vlan_option (bool | Unset): Whether configure a VLAN in profile is supported
        support_vlan_tagged (bool | Unset): Whether vlan tagged is supported
        support_status_enable (bool | Unset): Whether the port disabling is supported.
        support_status_inform (bool | Unset): Whether report the status of port links through inform is supported.
        custom (bool | Unset): Whether to enter a tagged vlan customically. Enter the VLAN ID manually if it is true
        tagged (str | Unset): Tagged vlan list, it must be present when custom is true.
        untagged (str | Unset): Untagged vlan list, it must be present when custom is true. Two data cannot be
            duplicated.
        tagged_network_id (list[str] | Unset): The Id list of the tagged vlan network profile, it must be present when
            custom is true.
        untagged_network_id (list[str] | Unset): The Id list of the untagged vlan network profile, it must be present
            when custom is true.
        uplink_port (bool | Unset): Whether it is an actual uplink port in topology.
        logic_uplink_port (bool | Unset): Whether it is a logical uplink port of device.
        support_bandwidth_control (bool | Unset): Whether band width control is supported
        bandwidth_control_enable (bool | Unset): Whether to enable band width control.
        ingress_rate_limit (ONUPortRateLimitVO | Unset): Optical ap egress Rate Limit.
        egress_rate_limit (ONUPortRateLimitVO | Unset): Optical ap egress Rate Limit.
        port_status (ApPortStatusVO | Unset): Port Status
        poe_input_mode (int | Unset): Poe Input Mode. It should be a value as follows: 0: OFF, 1: BT, 2: AT, 3: AF.
    """

    id: str | Unset = UNSET
    onu_id: str | Unset = UNSET
    port: int | Unset = UNSET
    port_type: int | Unset = UNSET
    lan_port: str | Unset = UNSET
    name: str | Unset = UNSET
    link_status: int | Unset = UNSET
    link_speed: int | Unset = UNSET
    duplex: int | Unset = UNSET
    support_vlan: bool | Unset = UNSET
    local_vlan_enable: bool | Unset = UNSET
    local_vlan_id: int | Unset = UNSET
    local_vlan_network_id: str | Unset = UNSET
    status: bool | Unset = UNSET
    support_poe: bool | Unset = UNSET
    poe_out_enable: bool | Unset = UNSET
    poe_state: int | Unset = UNSET
    voip_state: int | Unset = UNSET
    support_vlan_option: bool | Unset = UNSET
    support_vlan_tagged: bool | Unset = UNSET
    support_status_enable: bool | Unset = UNSET
    support_status_inform: bool | Unset = UNSET
    custom: bool | Unset = UNSET
    tagged: str | Unset = UNSET
    untagged: str | Unset = UNSET
    tagged_network_id: list[str] | Unset = UNSET
    untagged_network_id: list[str] | Unset = UNSET
    uplink_port: bool | Unset = UNSET
    logic_uplink_port: bool | Unset = UNSET
    support_bandwidth_control: bool | Unset = UNSET
    bandwidth_control_enable: bool | Unset = UNSET
    ingress_rate_limit: ONUPortRateLimitVO | Unset = UNSET
    egress_rate_limit: ONUPortRateLimitVO | Unset = UNSET
    port_status: ApPortStatusVO | Unset = UNSET
    poe_input_mode: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        onu_id = self.onu_id

        port = self.port

        port_type = self.port_type

        lan_port = self.lan_port

        name = self.name

        link_status = self.link_status

        link_speed = self.link_speed

        duplex = self.duplex

        support_vlan = self.support_vlan

        local_vlan_enable = self.local_vlan_enable

        local_vlan_id = self.local_vlan_id

        local_vlan_network_id = self.local_vlan_network_id

        status = self.status

        support_poe = self.support_poe

        poe_out_enable = self.poe_out_enable

        poe_state = self.poe_state

        voip_state = self.voip_state

        support_vlan_option = self.support_vlan_option

        support_vlan_tagged = self.support_vlan_tagged

        support_status_enable = self.support_status_enable

        support_status_inform = self.support_status_inform

        custom = self.custom

        tagged = self.tagged

        untagged = self.untagged

        tagged_network_id: list[str] | Unset = UNSET
        if not isinstance(self.tagged_network_id, Unset):
            tagged_network_id = self.tagged_network_id

        untagged_network_id: list[str] | Unset = UNSET
        if not isinstance(self.untagged_network_id, Unset):
            untagged_network_id = self.untagged_network_id

        uplink_port = self.uplink_port

        logic_uplink_port = self.logic_uplink_port

        support_bandwidth_control = self.support_bandwidth_control

        bandwidth_control_enable = self.bandwidth_control_enable

        ingress_rate_limit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ingress_rate_limit, Unset):
            ingress_rate_limit = self.ingress_rate_limit.to_dict()

        egress_rate_limit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.egress_rate_limit, Unset):
            egress_rate_limit = self.egress_rate_limit.to_dict()

        port_status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.port_status, Unset):
            port_status = self.port_status.to_dict()

        poe_input_mode = self.poe_input_mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if onu_id is not UNSET:
            field_dict["onuId"] = onu_id
        if port is not UNSET:
            field_dict["port"] = port
        if port_type is not UNSET:
            field_dict["portType"] = port_type
        if lan_port is not UNSET:
            field_dict["lanPort"] = lan_port
        if name is not UNSET:
            field_dict["name"] = name
        if link_status is not UNSET:
            field_dict["linkStatus"] = link_status
        if link_speed is not UNSET:
            field_dict["linkSpeed"] = link_speed
        if duplex is not UNSET:
            field_dict["duplex"] = duplex
        if support_vlan is not UNSET:
            field_dict["supportVlan"] = support_vlan
        if local_vlan_enable is not UNSET:
            field_dict["localVlanEnable"] = local_vlan_enable
        if local_vlan_id is not UNSET:
            field_dict["localVlanId"] = local_vlan_id
        if local_vlan_network_id is not UNSET:
            field_dict["localVlanNetworkId"] = local_vlan_network_id
        if status is not UNSET:
            field_dict["status"] = status
        if support_poe is not UNSET:
            field_dict["supportPoe"] = support_poe
        if poe_out_enable is not UNSET:
            field_dict["poeOutEnable"] = poe_out_enable
        if poe_state is not UNSET:
            field_dict["poeState"] = poe_state
        if voip_state is not UNSET:
            field_dict["voipState"] = voip_state
        if support_vlan_option is not UNSET:
            field_dict["supportVlanOption"] = support_vlan_option
        if support_vlan_tagged is not UNSET:
            field_dict["supportVlanTagged"] = support_vlan_tagged
        if support_status_enable is not UNSET:
            field_dict["supportStatusEnable"] = support_status_enable
        if support_status_inform is not UNSET:
            field_dict["supportStatusInform"] = support_status_inform
        if custom is not UNSET:
            field_dict["custom"] = custom
        if tagged is not UNSET:
            field_dict["tagged"] = tagged
        if untagged is not UNSET:
            field_dict["untagged"] = untagged
        if tagged_network_id is not UNSET:
            field_dict["taggedNetworkId"] = tagged_network_id
        if untagged_network_id is not UNSET:
            field_dict["untaggedNetworkId"] = untagged_network_id
        if uplink_port is not UNSET:
            field_dict["uplinkPort"] = uplink_port
        if logic_uplink_port is not UNSET:
            field_dict["logicUplinkPort"] = logic_uplink_port
        if support_bandwidth_control is not UNSET:
            field_dict["supportBandwidthControl"] = support_bandwidth_control
        if bandwidth_control_enable is not UNSET:
            field_dict["bandwidthControlEnable"] = bandwidth_control_enable
        if ingress_rate_limit is not UNSET:
            field_dict["ingressRateLimit"] = ingress_rate_limit
        if egress_rate_limit is not UNSET:
            field_dict["egressRateLimit"] = egress_rate_limit
        if port_status is not UNSET:
            field_dict["portStatus"] = port_status
        if poe_input_mode is not UNSET:
            field_dict["poeInputMode"] = poe_input_mode

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ap_port_status_vo import ApPortStatusVO
        from ..models.onu_port_rate_limit_vo import ONUPortRateLimitVO

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        onu_id = d.pop("onuId", UNSET)

        port = d.pop("port", UNSET)

        port_type = d.pop("portType", UNSET)

        lan_port = d.pop("lanPort", UNSET)

        name = d.pop("name", UNSET)

        link_status = d.pop("linkStatus", UNSET)

        link_speed = d.pop("linkSpeed", UNSET)

        duplex = d.pop("duplex", UNSET)

        support_vlan = d.pop("supportVlan", UNSET)

        local_vlan_enable = d.pop("localVlanEnable", UNSET)

        local_vlan_id = d.pop("localVlanId", UNSET)

        local_vlan_network_id = d.pop("localVlanNetworkId", UNSET)

        status = d.pop("status", UNSET)

        support_poe = d.pop("supportPoe", UNSET)

        poe_out_enable = d.pop("poeOutEnable", UNSET)

        poe_state = d.pop("poeState", UNSET)

        voip_state = d.pop("voipState", UNSET)

        support_vlan_option = d.pop("supportVlanOption", UNSET)

        support_vlan_tagged = d.pop("supportVlanTagged", UNSET)

        support_status_enable = d.pop("supportStatusEnable", UNSET)

        support_status_inform = d.pop("supportStatusInform", UNSET)

        custom = d.pop("custom", UNSET)

        tagged = d.pop("tagged", UNSET)

        untagged = d.pop("untagged", UNSET)

        tagged_network_id = cast(list[str], d.pop("taggedNetworkId", UNSET))

        untagged_network_id = cast(list[str], d.pop("untaggedNetworkId", UNSET))

        uplink_port = d.pop("uplinkPort", UNSET)

        logic_uplink_port = d.pop("logicUplinkPort", UNSET)

        support_bandwidth_control = d.pop("supportBandwidthControl", UNSET)

        bandwidth_control_enable = d.pop("bandwidthControlEnable", UNSET)

        _ingress_rate_limit = d.pop("ingressRateLimit", UNSET)
        ingress_rate_limit: ONUPortRateLimitVO | Unset
        if isinstance(_ingress_rate_limit, Unset):
            ingress_rate_limit = UNSET
        else:
            ingress_rate_limit = ONUPortRateLimitVO.from_dict(_ingress_rate_limit)

        _egress_rate_limit = d.pop("egressRateLimit", UNSET)
        egress_rate_limit: ONUPortRateLimitVO | Unset
        if isinstance(_egress_rate_limit, Unset):
            egress_rate_limit = UNSET
        else:
            egress_rate_limit = ONUPortRateLimitVO.from_dict(_egress_rate_limit)

        _port_status = d.pop("portStatus", UNSET)
        port_status: ApPortStatusVO | Unset
        if isinstance(_port_status, Unset):
            port_status = UNSET
        else:
            port_status = ApPortStatusVO.from_dict(_port_status)

        poe_input_mode = d.pop("poeInputMode", UNSET)

        aplan_port_list = cls(
            id=id,
            onu_id=onu_id,
            port=port,
            port_type=port_type,
            lan_port=lan_port,
            name=name,
            link_status=link_status,
            link_speed=link_speed,
            duplex=duplex,
            support_vlan=support_vlan,
            local_vlan_enable=local_vlan_enable,
            local_vlan_id=local_vlan_id,
            local_vlan_network_id=local_vlan_network_id,
            status=status,
            support_poe=support_poe,
            poe_out_enable=poe_out_enable,
            poe_state=poe_state,
            voip_state=voip_state,
            support_vlan_option=support_vlan_option,
            support_vlan_tagged=support_vlan_tagged,
            support_status_enable=support_status_enable,
            support_status_inform=support_status_inform,
            custom=custom,
            tagged=tagged,
            untagged=untagged,
            tagged_network_id=tagged_network_id,
            untagged_network_id=untagged_network_id,
            uplink_port=uplink_port,
            logic_uplink_port=logic_uplink_port,
            support_bandwidth_control=support_bandwidth_control,
            bandwidth_control_enable=bandwidth_control_enable,
            ingress_rate_limit=ingress_rate_limit,
            egress_rate_limit=egress_rate_limit,
            port_status=port_status,
            poe_input_mode=poe_input_mode,
        )

        aplan_port_list.additional_properties = d
        return aplan_port_list

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
