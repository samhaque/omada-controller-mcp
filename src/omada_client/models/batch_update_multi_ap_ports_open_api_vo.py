from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.onu_port_rate_limit_vo import ONUPortRateLimitVO


T = TypeVar("T", bound="BatchUpdateMultiApPortsOpenApiVO")


@_attrs_define
class BatchUpdateMultiApPortsOpenApiVO:
    """
    Attributes:
        ap_mac_list (list[str]): AP mac list
        lan_port_list (list[str]): The list of ap ports which are configured in batches.
        name (str | Unset): Port name
        status (bool | Unset): Port status
        local_vlan_enable (bool | Unset): Specifies whether to enable the port.
        local_vlan_id (int | Unset): Local vlan ID should be within the range of 1-4094, which has a value only if
            Status is true.
        local_vlan_network_id (str | Unset): The ID of the LAN network profile selected for the port.
        poe_out_enable (bool | Unset): Whether to enable poe out.
        custom (bool | Unset): Whether to enter a tagged vlan customically. Enter the VLAN ID manually if it is true.
            and select LAN network profile if it is false.
        tagged (str | Unset): Tagged vlan list, it must be present when custom is true.
        untagged (str | Unset): Untagged vlan list, it must be present when custom is true. Two data cannot be
            duplicated.
        tagged_network_id (list[str] | Unset): The Id list of the tagged vlan network profile, it must be present when
            custom is true.
        untagged_network_id (list[str] | Unset): The Id list of the untagged vlan network profile, it must be present
            when custom is true.
        bandwidth_control_enable (bool | Unset): Whether to enable bandwidthControl.
        ingress_rate_limit (ONUPortRateLimitVO | Unset): Optical ap egress Rate Limit.
        egress_rate_limit (ONUPortRateLimitVO | Unset): Optical ap egress Rate Limit.
    """

    ap_mac_list: list[str]
    lan_port_list: list[str]
    name: str | Unset = UNSET
    status: bool | Unset = UNSET
    local_vlan_enable: bool | Unset = UNSET
    local_vlan_id: int | Unset = UNSET
    local_vlan_network_id: str | Unset = UNSET
    poe_out_enable: bool | Unset = UNSET
    custom: bool | Unset = UNSET
    tagged: str | Unset = UNSET
    untagged: str | Unset = UNSET
    tagged_network_id: list[str] | Unset = UNSET
    untagged_network_id: list[str] | Unset = UNSET
    bandwidth_control_enable: bool | Unset = UNSET
    ingress_rate_limit: ONUPortRateLimitVO | Unset = UNSET
    egress_rate_limit: ONUPortRateLimitVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ap_mac_list = self.ap_mac_list

        lan_port_list = self.lan_port_list

        name = self.name

        status = self.status

        local_vlan_enable = self.local_vlan_enable

        local_vlan_id = self.local_vlan_id

        local_vlan_network_id = self.local_vlan_network_id

        poe_out_enable = self.poe_out_enable

        custom = self.custom

        tagged = self.tagged

        untagged = self.untagged

        tagged_network_id: list[str] | Unset = UNSET
        if not isinstance(self.tagged_network_id, Unset):
            tagged_network_id = self.tagged_network_id

        untagged_network_id: list[str] | Unset = UNSET
        if not isinstance(self.untagged_network_id, Unset):
            untagged_network_id = self.untagged_network_id

        bandwidth_control_enable = self.bandwidth_control_enable

        ingress_rate_limit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ingress_rate_limit, Unset):
            ingress_rate_limit = self.ingress_rate_limit.to_dict()

        egress_rate_limit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.egress_rate_limit, Unset):
            egress_rate_limit = self.egress_rate_limit.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apMacList": ap_mac_list,
                "lanPortList": lan_port_list,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status
        if local_vlan_enable is not UNSET:
            field_dict["localVlanEnable"] = local_vlan_enable
        if local_vlan_id is not UNSET:
            field_dict["localVlanId"] = local_vlan_id
        if local_vlan_network_id is not UNSET:
            field_dict["localVlanNetworkId"] = local_vlan_network_id
        if poe_out_enable is not UNSET:
            field_dict["poeOutEnable"] = poe_out_enable
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
        if bandwidth_control_enable is not UNSET:
            field_dict["bandwidthControlEnable"] = bandwidth_control_enable
        if ingress_rate_limit is not UNSET:
            field_dict["ingressRateLimit"] = ingress_rate_limit
        if egress_rate_limit is not UNSET:
            field_dict["egressRateLimit"] = egress_rate_limit

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.onu_port_rate_limit_vo import ONUPortRateLimitVO

        d = dict(src_dict)
        ap_mac_list = cast(list[str], d.pop("apMacList"))

        lan_port_list = cast(list[str], d.pop("lanPortList"))

        name = d.pop("name", UNSET)

        status = d.pop("status", UNSET)

        local_vlan_enable = d.pop("localVlanEnable", UNSET)

        local_vlan_id = d.pop("localVlanId", UNSET)

        local_vlan_network_id = d.pop("localVlanNetworkId", UNSET)

        poe_out_enable = d.pop("poeOutEnable", UNSET)

        custom = d.pop("custom", UNSET)

        tagged = d.pop("tagged", UNSET)

        untagged = d.pop("untagged", UNSET)

        tagged_network_id = cast(list[str], d.pop("taggedNetworkId", UNSET))

        untagged_network_id = cast(list[str], d.pop("untaggedNetworkId", UNSET))

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

        batch_update_multi_ap_ports_open_api_vo = cls(
            ap_mac_list=ap_mac_list,
            lan_port_list=lan_port_list,
            name=name,
            status=status,
            local_vlan_enable=local_vlan_enable,
            local_vlan_id=local_vlan_id,
            local_vlan_network_id=local_vlan_network_id,
            poe_out_enable=poe_out_enable,
            custom=custom,
            tagged=tagged,
            untagged=untagged,
            tagged_network_id=tagged_network_id,
            untagged_network_id=untagged_network_id,
            bandwidth_control_enable=bandwidth_control_enable,
            ingress_rate_limit=ingress_rate_limit,
            egress_rate_limit=egress_rate_limit,
        )

        batch_update_multi_ap_ports_open_api_vo.additional_properties = d
        return batch_update_multi_ap_ports_open_api_vo

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
