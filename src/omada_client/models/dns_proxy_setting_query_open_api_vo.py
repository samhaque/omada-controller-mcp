from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dns_override_setting_open_api_vo import DnsOverrideSettingOpenApiVO
    from ..models.dns_sec_setting_open_api_vo import DnsSecSettingOpenApiVO
    from ..models.doh_setting_open_api_vo import DohSettingOpenApiVO
    from ..models.dot_setting_open_api_vo import DotSettingOpenApiVO


T = TypeVar("T", bound="DnsProxySettingQueryOpenApiVO")


@_attrs_define
class DnsProxySettingQueryOpenApiVO:
    """
    Attributes:
        enable (bool | Unset): DNS proxy setting enable status.
        type_ (int | Unset): DNS proxy setting type. Type should be a value as follows: 0: DNSSEC, 1: DoH, 2: DoT, 3:
            DNS Override
        dns_sec_setting (DnsSecSettingOpenApiVO | Unset): DNS proxy DNSSEC setting, valid when parameter [type] is 0
        doh_setting (DohSettingOpenApiVO | Unset): DNS proxy DoH setting, valid when parameter [type] is 1
        dot_setting (DotSettingOpenApiVO | Unset): DNS proxy DoT setting, valid when parameter [type] is 2
        dns_override_setting (DnsOverrideSettingOpenApiVO | Unset): DNS Override setting, valid when parameter [type] is
            3
        support_dns_override (bool | Unset): Whether DNS Override setting is supported in DNS Proxy.
        exist_dns_override (bool | Unset): Whether DNS Override has been configured in DNS Proxy.
    """

    enable: bool | Unset = UNSET
    type_: int | Unset = UNSET
    dns_sec_setting: DnsSecSettingOpenApiVO | Unset = UNSET
    doh_setting: DohSettingOpenApiVO | Unset = UNSET
    dot_setting: DotSettingOpenApiVO | Unset = UNSET
    dns_override_setting: DnsOverrideSettingOpenApiVO | Unset = UNSET
    support_dns_override: bool | Unset = UNSET
    exist_dns_override: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        type_ = self.type_

        dns_sec_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dns_sec_setting, Unset):
            dns_sec_setting = self.dns_sec_setting.to_dict()

        doh_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.doh_setting, Unset):
            doh_setting = self.doh_setting.to_dict()

        dot_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dot_setting, Unset):
            dot_setting = self.dot_setting.to_dict()

        dns_override_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dns_override_setting, Unset):
            dns_override_setting = self.dns_override_setting.to_dict()

        support_dns_override = self.support_dns_override

        exist_dns_override = self.exist_dns_override

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable is not UNSET:
            field_dict["enable"] = enable
        if type_ is not UNSET:
            field_dict["type"] = type_
        if dns_sec_setting is not UNSET:
            field_dict["dnsSecSetting"] = dns_sec_setting
        if doh_setting is not UNSET:
            field_dict["dohSetting"] = doh_setting
        if dot_setting is not UNSET:
            field_dict["dotSetting"] = dot_setting
        if dns_override_setting is not UNSET:
            field_dict["dnsOverrideSetting"] = dns_override_setting
        if support_dns_override is not UNSET:
            field_dict["supportDnsOverride"] = support_dns_override
        if exist_dns_override is not UNSET:
            field_dict["existDnsOverride"] = exist_dns_override

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.dns_override_setting_open_api_vo import (
            DnsOverrideSettingOpenApiVO,
        )
        from ..models.dns_sec_setting_open_api_vo import (
            DnsSecSettingOpenApiVO,
        )
        from ..models.doh_setting_open_api_vo import (
            DohSettingOpenApiVO,
        )
        from ..models.dot_setting_open_api_vo import (
            DotSettingOpenApiVO,
        )

        d = dict(src_dict)
        enable = d.pop("enable", UNSET)

        type_ = d.pop("type", UNSET)

        _dns_sec_setting = d.pop("dnsSecSetting", UNSET)
        dns_sec_setting: DnsSecSettingOpenApiVO | Unset
        if isinstance(_dns_sec_setting, Unset):
            dns_sec_setting = UNSET
        else:
            dns_sec_setting = DnsSecSettingOpenApiVO.from_dict(_dns_sec_setting)

        _doh_setting = d.pop("dohSetting", UNSET)
        doh_setting: DohSettingOpenApiVO | Unset
        if isinstance(_doh_setting, Unset):
            doh_setting = UNSET
        else:
            doh_setting = DohSettingOpenApiVO.from_dict(_doh_setting)

        _dot_setting = d.pop("dotSetting", UNSET)
        dot_setting: DotSettingOpenApiVO | Unset
        if isinstance(_dot_setting, Unset):
            dot_setting = UNSET
        else:
            dot_setting = DotSettingOpenApiVO.from_dict(_dot_setting)

        _dns_override_setting = d.pop("dnsOverrideSetting", UNSET)
        dns_override_setting: DnsOverrideSettingOpenApiVO | Unset
        if isinstance(_dns_override_setting, Unset):
            dns_override_setting = UNSET
        else:
            dns_override_setting = DnsOverrideSettingOpenApiVO.from_dict(
                _dns_override_setting
            )

        support_dns_override = d.pop("supportDnsOverride", UNSET)

        exist_dns_override = d.pop("existDnsOverride", UNSET)

        dns_proxy_setting_query_open_api_vo = cls(
            enable=enable,
            type_=type_,
            dns_sec_setting=dns_sec_setting,
            doh_setting=doh_setting,
            dot_setting=dot_setting,
            dns_override_setting=dns_override_setting,
            support_dns_override=support_dns_override,
            exist_dns_override=exist_dns_override,
        )

        dns_proxy_setting_query_open_api_vo.additional_properties = d
        return dns_proxy_setting_query_open_api_vo

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
