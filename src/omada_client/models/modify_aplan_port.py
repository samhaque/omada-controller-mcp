from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.onu_port_rate_limit_vo import ONUPortRateLimitVO


T = TypeVar("T", bound="ModifyAPLANPort")


@_attrs_define
class ModifyAPLANPort:
    """
    Attributes:
        lan_port (str | Unset): lanPort
        name (str | Unset): port name
        status (bool | Unset): port status, true: enable; false: disable
        local_vlan_enable (bool | Unset): vlan status, true: enable; false: disable
        local_vlan_id (int | Unset): port vlan id
        local_vlan_network_id (str | Unset): local vlan network Id
        poe_out_enable (bool | Unset): poe out status, true: enable; false: disable
        custom (bool | Unset): custom
        tagged (str | Unset): tagged
        untagged (str | Unset): untagged
        tagged_network_id (list[str] | Unset): vlan tagged NetworkId
        untagged_network_id (list[str] | Unset): vlan untagged NetworkId
        bandwidth_control_enable (bool | Unset): bandwidth Control status
        ingress_rate_limit (ONUPortRateLimitVO | Unset): Optical ap egress Rate Limit.
        egress_rate_limit (ONUPortRateLimitVO | Unset): Optical ap egress Rate Limit.
    """

    lan_port: str | Unset = UNSET
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
        lan_port = self.lan_port

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
        field_dict.update({})
        if lan_port is not UNSET:
            field_dict["lanPort"] = lan_port
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
        lan_port = d.pop("lanPort", UNSET)

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

        modify_aplan_port = cls(
            lan_port=lan_port,
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

        modify_aplan_port.additional_properties = d
        return modify_aplan_port

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
