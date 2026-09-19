from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="AvailableWanPortOpenApiVO")


@_attrs_define
class AvailableWanPortOpenApiVO:
    """available wan ports

    Attributes:
        port_name (str | Unset): port name
        port_uuid (str | Unset): port id
        type_ (int | Unset): wan type
        configured (bool | Unset): qos configured
        support_iptv (bool | Unset): support iptv?
        virtual_wan_num (int | Unset): How many virtual wan does this wan port support
        proto (str | Unset): WAN IPv4 connection type, it supports Static IP, DHCP, PPPoE, L2TP, PPTP, DS-Lite, and
            MAP-E.
        ipv6 (bool | Unset): IPv6 enable.
        ipv_6_proto (str | Unset): IPv6 connection type: 0: static; 1: dynamic; 2: PPPoE; 3: 6to4Tunnel; 4: bridge.
        recommended_wan (bool | Unset): Recommended WAN port.
        ip (str | Unset): IPv4 address.
    """

    port_name: str | Unset = UNSET
    port_uuid: str | Unset = UNSET
    type_: int | Unset = UNSET
    configured: bool | Unset = UNSET
    support_iptv: bool | Unset = UNSET
    virtual_wan_num: int | Unset = UNSET
    proto: str | Unset = UNSET
    ipv6: bool | Unset = UNSET
    ipv_6_proto: str | Unset = UNSET
    recommended_wan: bool | Unset = UNSET
    ip: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port_name = self.port_name

        port_uuid = self.port_uuid

        type_ = self.type_

        configured = self.configured

        support_iptv = self.support_iptv

        virtual_wan_num = self.virtual_wan_num

        proto = self.proto

        ipv6 = self.ipv6

        ipv_6_proto = self.ipv_6_proto

        recommended_wan = self.recommended_wan

        ip = self.ip

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if port_name is not UNSET:
            field_dict["portName"] = port_name
        if port_uuid is not UNSET:
            field_dict["portUuid"] = port_uuid
        if type_ is not UNSET:
            field_dict["type"] = type_
        if configured is not UNSET:
            field_dict["configured"] = configured
        if support_iptv is not UNSET:
            field_dict["supportIptv"] = support_iptv
        if virtual_wan_num is not UNSET:
            field_dict["virtualWanNum"] = virtual_wan_num
        if proto is not UNSET:
            field_dict["proto"] = proto
        if ipv6 is not UNSET:
            field_dict["ipv6"] = ipv6
        if ipv_6_proto is not UNSET:
            field_dict["ipv6Proto"] = ipv_6_proto
        if recommended_wan is not UNSET:
            field_dict["recommendedWan"] = recommended_wan
        if ip is not UNSET:
            field_dict["ip"] = ip

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        port_name = d.pop("portName", UNSET)

        port_uuid = d.pop("portUuid", UNSET)

        type_ = d.pop("type", UNSET)

        configured = d.pop("configured", UNSET)

        support_iptv = d.pop("supportIptv", UNSET)

        virtual_wan_num = d.pop("virtualWanNum", UNSET)

        proto = d.pop("proto", UNSET)

        ipv6 = d.pop("ipv6", UNSET)

        ipv_6_proto = d.pop("ipv6Proto", UNSET)

        recommended_wan = d.pop("recommendedWan", UNSET)

        ip = d.pop("ip", UNSET)

        available_wan_port_open_api_vo = cls(
            port_name=port_name,
            port_uuid=port_uuid,
            type_=type_,
            configured=configured,
            support_iptv=support_iptv,
            virtual_wan_num=virtual_wan_num,
            proto=proto,
            ipv6=ipv6,
            ipv_6_proto=ipv_6_proto,
            recommended_wan=recommended_wan,
            ip=ip,
        )

        available_wan_port_open_api_vo.additional_properties = d
        return available_wan_port_open_api_vo

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
