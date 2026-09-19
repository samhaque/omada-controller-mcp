from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="VirtualWanIpv4StaticOpenApiVO")


@_attrs_define
class VirtualWanIpv4StaticOpenApiVO:
    """VirtualWanIpv4StaticOpenApiVO

    Attributes:
        ipaddr (str): IP address.
        netmask (str): Subnet mask.
        gateway (str): Gateway IP.
        mtu (int): Parameter [mtu] should be a value between 576 and 1500.
        dns1 (str | Unset): Primary DNS.
        dns2 (str | Unset): Secondary DNS.
    """

    ipaddr: str
    netmask: str
    gateway: str
    mtu: int
    dns1: str | Unset = UNSET
    dns2: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ipaddr = self.ipaddr

        netmask = self.netmask

        gateway = self.gateway

        mtu = self.mtu

        dns1 = self.dns1

        dns2 = self.dns2

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ipaddr": ipaddr,
                "netmask": netmask,
                "gateway": gateway,
                "mtu": mtu,
            }
        )
        if dns1 is not UNSET:
            field_dict["dns1"] = dns1
        if dns2 is not UNSET:
            field_dict["dns2"] = dns2

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        ipaddr = d.pop("ipaddr")

        netmask = d.pop("netmask")

        gateway = d.pop("gateway")

        mtu = d.pop("mtu")

        dns1 = d.pop("dns1", UNSET)

        dns2 = d.pop("dns2", UNSET)

        virtual_wan_ipv_4_static_open_api_vo = cls(
            ipaddr=ipaddr,
            netmask=netmask,
            gateway=gateway,
            mtu=mtu,
            dns1=dns1,
            dns2=dns2,
        )

        virtual_wan_ipv_4_static_open_api_vo.additional_properties = d
        return virtual_wan_ipv_4_static_open_api_vo

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
