from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="DnsOverrideSettingOpenApiVO")


@_attrs_define
class DnsOverrideSettingOpenApiVO:
    """DNS Override setting, valid when parameter [type] is 3

    Attributes:
        primary_dns_server (str): Specify the primary upstream DNS server.
        secondary_dns_server (str | Unset): Specify the secondary upstream DNS server.
        apply_network (list[str] | Unset): Specify the effective LAN network to apply DNS Override. Available LAN
            networks can be obtained from 'Get all "single"-"multi" interface lan network'
    """

    primary_dns_server: str
    secondary_dns_server: str | Unset = UNSET
    apply_network: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        primary_dns_server = self.primary_dns_server

        secondary_dns_server = self.secondary_dns_server

        apply_network: list[str] | Unset = UNSET
        if not isinstance(self.apply_network, Unset):
            apply_network = self.apply_network

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "primaryDnsServer": primary_dns_server,
            }
        )
        if secondary_dns_server is not UNSET:
            field_dict["secondaryDnsServer"] = secondary_dns_server
        if apply_network is not UNSET:
            field_dict["applyNetwork"] = apply_network

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        primary_dns_server = d.pop("primaryDnsServer")

        secondary_dns_server = d.pop("secondaryDnsServer", UNSET)

        apply_network = cast(list[str], d.pop("applyNetwork", UNSET))

        dns_override_setting_open_api_vo = cls(
            primary_dns_server=primary_dns_server,
            secondary_dns_server=secondary_dns_server,
            apply_network=apply_network,
        )

        dns_override_setting_open_api_vo.additional_properties = d
        return dns_override_setting_open_api_vo

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
