from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="LanNetworkProtoSLAACStatelessDHCPModeOrSLAACRDNSSMode")


@_attrs_define
class LanNetworkProtoSLAACStatelessDHCPModeOrSLAACRDNSSMode:
    """Lan network proto: SLAAC+Stateless DHCP mode or SLAAC+RDNSS mode

    Attributes:
        pre_type (int | Unset): Prefix type should be a value as follows:  0: "manual"; 1: "get from PD"
        prefix (str | Unset): Address prefix
        port_uuid (str | Unset): The port UUID of WAN
        pre_id (int | Unset): Prefix ID should be within the range of 0-127
        dnsv6 (int | Unset): DHCP Name Server, should be a value as follows: 0: "auto"; 1: "manual"
        pri_dns (str | Unset): Primary DHCP Name Server, only effective for DNSv6 "manual"
        snd_dns (str | Unset): Secondary DHCP Name Server, only effective for dnsv6 "manual"
    """

    pre_type: int | Unset = UNSET
    prefix: str | Unset = UNSET
    port_uuid: str | Unset = UNSET
    pre_id: int | Unset = UNSET
    dnsv6: int | Unset = UNSET
    pri_dns: str | Unset = UNSET
    snd_dns: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pre_type = self.pre_type

        prefix = self.prefix

        port_uuid = self.port_uuid

        pre_id = self.pre_id

        dnsv6 = self.dnsv6

        pri_dns = self.pri_dns

        snd_dns = self.snd_dns

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pre_type is not UNSET:
            field_dict["preType"] = pre_type
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if port_uuid is not UNSET:
            field_dict["portUuid"] = port_uuid
        if pre_id is not UNSET:
            field_dict["preId"] = pre_id
        if dnsv6 is not UNSET:
            field_dict["dnsv6"] = dnsv6
        if pri_dns is not UNSET:
            field_dict["priDns"] = pri_dns
        if snd_dns is not UNSET:
            field_dict["sndDns"] = snd_dns

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        pre_type = d.pop("preType", UNSET)

        prefix = d.pop("prefix", UNSET)

        port_uuid = d.pop("portUuid", UNSET)

        pre_id = d.pop("preId", UNSET)

        dnsv6 = d.pop("dnsv6", UNSET)

        pri_dns = d.pop("priDns", UNSET)

        snd_dns = d.pop("sndDns", UNSET)

        lan_network_proto_slaac_stateless_dhcp_mode_or_slaacrdnss_mode = cls(
            pre_type=pre_type,
            prefix=prefix,
            port_uuid=port_uuid,
            pre_id=pre_id,
            dnsv6=dnsv6,
            pri_dns=pri_dns,
            snd_dns=snd_dns,
        )

        lan_network_proto_slaac_stateless_dhcp_mode_or_slaacrdnss_mode.additional_properties = d
        return lan_network_proto_slaac_stateless_dhcp_mode_or_slaacrdnss_mode

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
