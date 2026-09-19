from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SslVpnResourceModifyOpenApiVO")


@_attrs_define
class SslVpnResourceModifyOpenApiVO:
    """
    Attributes:
        type_ (int): Type of the SSL VPN resource should be a value as follows: 0: IP; 1: domain, and it can not be
            modified.
        ip (str | Unset): IP of the SSL VPN resource, exists when type is 0.
        mask (str | Unset): Mask of the SSL VPN resource, exists when type is 0.
        domain (str | Unset): Domain of the SSL VPN resource, exists when type is 1.
        protocol (int | Unset): Protocol of the SSL VPN resource should be a value as follows: 0:All; 1:TCP; 2:UDP;
            3:TCP/UDP; 4:ICMP; 5:Other
        src_port_start (int | Unset): Start source port of the SSL VPN resource, exists when protocol is TCP or UDP. It
            should be within the range of 0–65535
        src_port_end (int | Unset): End source port of the SSL VPN resource, exists when protocol is TCP or UDP. It
            should be within the range of 0–65535
        dst_port_start (int | Unset): Start destination port of the SSL VPN resource, exists when protocol is TCP or
            UDP. It should be within the range of 0–65535
        dst_port_end (int | Unset): End destination port of the SSL VPN resource, exists when protocol is TCP or UDP. It
            should be within the range of 0–65535
        icmp_type (int | Unset): ICMP type of the SSL VPN resource, exists when protocol is ICMP. It should be within
            the range of 0–255
        icmp_code (int | Unset): ICMP code of the SSL VPN resource, exists when protocol is ICMP. It should be within
            the range of 0–255
        other_protocol (int | Unset): Other protocol of the SSL VPN resource. It should be within the range of 1–255
    """

    type_: int
    ip: str | Unset = UNSET
    mask: str | Unset = UNSET
    domain: str | Unset = UNSET
    protocol: int | Unset = UNSET
    src_port_start: int | Unset = UNSET
    src_port_end: int | Unset = UNSET
    dst_port_start: int | Unset = UNSET
    dst_port_end: int | Unset = UNSET
    icmp_type: int | Unset = UNSET
    icmp_code: int | Unset = UNSET
    other_protocol: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        ip = self.ip

        mask = self.mask

        domain = self.domain

        protocol = self.protocol

        src_port_start = self.src_port_start

        src_port_end = self.src_port_end

        dst_port_start = self.dst_port_start

        dst_port_end = self.dst_port_end

        icmp_type = self.icmp_type

        icmp_code = self.icmp_code

        other_protocol = self.other_protocol

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if ip is not UNSET:
            field_dict["ip"] = ip
        if mask is not UNSET:
            field_dict["mask"] = mask
        if domain is not UNSET:
            field_dict["domain"] = domain
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if src_port_start is not UNSET:
            field_dict["srcPortStart"] = src_port_start
        if src_port_end is not UNSET:
            field_dict["srcPortEnd"] = src_port_end
        if dst_port_start is not UNSET:
            field_dict["dstPortStart"] = dst_port_start
        if dst_port_end is not UNSET:
            field_dict["dstPortEnd"] = dst_port_end
        if icmp_type is not UNSET:
            field_dict["icmpType"] = icmp_type
        if icmp_code is not UNSET:
            field_dict["icmpCode"] = icmp_code
        if other_protocol is not UNSET:
            field_dict["otherProtocol"] = other_protocol

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        type_ = d.pop("type")

        ip = d.pop("ip", UNSET)

        mask = d.pop("mask", UNSET)

        domain = d.pop("domain", UNSET)

        protocol = d.pop("protocol", UNSET)

        src_port_start = d.pop("srcPortStart", UNSET)

        src_port_end = d.pop("srcPortEnd", UNSET)

        dst_port_start = d.pop("dstPortStart", UNSET)

        dst_port_end = d.pop("dstPortEnd", UNSET)

        icmp_type = d.pop("icmpType", UNSET)

        icmp_code = d.pop("icmpCode", UNSET)

        other_protocol = d.pop("otherProtocol", UNSET)

        ssl_vpn_resource_modify_open_api_vo = cls(
            type_=type_,
            ip=ip,
            mask=mask,
            domain=domain,
            protocol=protocol,
            src_port_start=src_port_start,
            src_port_end=src_port_end,
            dst_port_start=dst_port_start,
            dst_port_end=dst_port_end,
            icmp_type=icmp_type,
            icmp_code=icmp_code,
            other_protocol=other_protocol,
        )

        ssl_vpn_resource_modify_open_api_vo.additional_properties = d
        return ssl_vpn_resource_modify_open_api_vo

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
