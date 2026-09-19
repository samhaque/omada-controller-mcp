from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="Ipv6DynamicOpenApiVO")


@_attrs_define
class Ipv6DynamicOpenApiVO:
    """It is required when protoType is dynamic

    Attributes:
        get_ipv_6_type (int): It should be a value as follows: 0: SLAAC; 1: DHCPv6; 2: specified; 3: auto; 4:non-
            address.
        prefix_enable (bool):
        dns_type (int): DNS Address Type, 0: dynamic, 1: static.
        prefix_size (int | Unset): It is required when [prefixEnable] is true, which ranges from 48 ~ 64.
        primary_dns (str | Unset): It is required when [dnsType] is 1.
        secondary_dns (str | Unset): It takes effect when [dnsType] is 1
    """

    get_ipv_6_type: int
    prefix_enable: bool
    dns_type: int
    prefix_size: int | Unset = UNSET
    primary_dns: str | Unset = UNSET
    secondary_dns: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        get_ipv_6_type = self.get_ipv_6_type

        prefix_enable = self.prefix_enable

        dns_type = self.dns_type

        prefix_size = self.prefix_size

        primary_dns = self.primary_dns

        secondary_dns = self.secondary_dns

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "getIpv6Type": get_ipv_6_type,
                "prefixEnable": prefix_enable,
                "dnsType": dns_type,
            }
        )
        if prefix_size is not UNSET:
            field_dict["prefixSize"] = prefix_size
        if primary_dns is not UNSET:
            field_dict["primaryDns"] = primary_dns
        if secondary_dns is not UNSET:
            field_dict["secondaryDns"] = secondary_dns

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        get_ipv_6_type = d.pop("getIpv6Type")

        prefix_enable = d.pop("prefixEnable")

        dns_type = d.pop("dnsType")

        prefix_size = d.pop("prefixSize", UNSET)

        primary_dns = d.pop("primaryDns", UNSET)

        secondary_dns = d.pop("secondaryDns", UNSET)

        ipv_6_dynamic_open_api_vo = cls(
            get_ipv_6_type=get_ipv_6_type,
            prefix_enable=prefix_enable,
            dns_type=dns_type,
            prefix_size=prefix_size,
            primary_dns=primary_dns,
            secondary_dns=secondary_dns,
        )

        ipv_6_dynamic_open_api_vo.additional_properties = d
        return ipv_6_dynamic_open_api_vo

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
