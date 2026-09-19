from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SlaacTemplateOpenApiVO")


@_attrs_define
class SlaacTemplateOpenApiVO:
    """Lan network proto: SLAAC+Stateless DHCP mode or SLAAC+RDNSS mode

    Attributes:
        prefix (str | Unset): Address prefix
        pre_id (int | Unset): Prefix ID should be within the range of 0-127
        dnsv6 (int | Unset): DHCP Name Server, should be a value as follows: 0: "auto"; 1: "manual"
        pri_dns (str | Unset): Primary DHCP Name Server, only effective for DNSv6 "manual"
        snd_dns (str | Unset): Secondary DHCP Name Server, only effective for dnsv6 "manual"
    """

    prefix: str | Unset = UNSET
    pre_id: int | Unset = UNSET
    dnsv6: int | Unset = UNSET
    pri_dns: str | Unset = UNSET
    snd_dns: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        prefix = self.prefix

        pre_id = self.pre_id

        dnsv6 = self.dnsv6

        pri_dns = self.pri_dns

        snd_dns = self.snd_dns

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
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
        prefix = d.pop("prefix", UNSET)

        pre_id = d.pop("preId", UNSET)

        dnsv6 = d.pop("dnsv6", UNSET)

        pri_dns = d.pop("priDns", UNSET)

        snd_dns = d.pop("sndDns", UNSET)

        slaac_template_open_api_vo = cls(
            prefix=prefix,
            pre_id=pre_id,
            dnsv6=dnsv6,
            pri_dns=pri_dns,
            snd_dns=snd_dns,
        )

        slaac_template_open_api_vo.additional_properties = d
        return slaac_template_open_api_vo

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
