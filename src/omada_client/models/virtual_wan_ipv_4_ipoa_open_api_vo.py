from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.virtual_wan_multiple_ip_vo import VirtualWanMultipleIpVO


T = TypeVar("T", bound="VirtualWanIpv4IpoaOpenApiVO")


@_attrs_define
class VirtualWanIpv4IpoaOpenApiVO:
    """VirtualWanIpv4IpoaOpenApiVO

    Attributes:
        ipaddr (str): IP address.
        netmask (str): Subnet mask.
        gateway (str): Gateway IP.
        mtu (int): Parameter [mtu] should be a value between 576 and 1500.
        dns1 (str | Unset): Primary DNS server.
        dns2 (str | Unset): Secondary DNS server.
        wan_multiple_ips (list[VirtualWanMultipleIpVO] | Unset):
    """

    ipaddr: str
    netmask: str
    gateway: str
    mtu: int
    dns1: str | Unset = UNSET
    dns2: str | Unset = UNSET
    wan_multiple_ips: list[VirtualWanMultipleIpVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ipaddr = self.ipaddr

        netmask = self.netmask

        gateway = self.gateway

        mtu = self.mtu

        dns1 = self.dns1

        dns2 = self.dns2

        wan_multiple_ips: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.wan_multiple_ips, Unset):
            wan_multiple_ips = []
            for wan_multiple_ips_item_data in self.wan_multiple_ips:
                wan_multiple_ips_item = wan_multiple_ips_item_data.to_dict()
                wan_multiple_ips.append(wan_multiple_ips_item)

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
        if wan_multiple_ips is not UNSET:
            field_dict["wanMultipleIps"] = wan_multiple_ips

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.virtual_wan_multiple_ip_vo import (
            VirtualWanMultipleIpVO,
        )

        d = dict(src_dict)
        ipaddr = d.pop("ipaddr")

        netmask = d.pop("netmask")

        gateway = d.pop("gateway")

        mtu = d.pop("mtu")

        dns1 = d.pop("dns1", UNSET)

        dns2 = d.pop("dns2", UNSET)

        _wan_multiple_ips = d.pop("wanMultipleIps", UNSET)
        wan_multiple_ips: list[VirtualWanMultipleIpVO] | Unset = UNSET
        if _wan_multiple_ips is not UNSET:
            wan_multiple_ips = []
            for wan_multiple_ips_item_data in _wan_multiple_ips:
                wan_multiple_ips_item = VirtualWanMultipleIpVO.from_dict(
                    wan_multiple_ips_item_data
                )

                wan_multiple_ips.append(wan_multiple_ips_item)

        virtual_wan_ipv_4_ipoa_open_api_vo = cls(
            ipaddr=ipaddr,
            netmask=netmask,
            gateway=gateway,
            mtu=mtu,
            dns1=dns1,
            dns2=dns2,
            wan_multiple_ips=wan_multiple_ips,
        )

        virtual_wan_ipv_4_ipoa_open_api_vo.additional_properties = d
        return virtual_wan_ipv_4_ipoa_open_api_vo

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
