from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="DnsSecSettingOpenApiVO")


@_attrs_define
class DnsSecSettingOpenApiVO:
    """DNS proxy DNSSEC setting, valid when parameter [type] is 0

    Attributes:
        servers (list[str]): DNS Server IP list, Up to 2 entries are allowed for the server list
        reply_policy (int): Bogus DNS reply policy type. ReplyPolicy should be a value as follows: 0: Pass, 1: Drop
    """

    servers: list[str]
    reply_policy: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        servers = self.servers

        reply_policy = self.reply_policy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "servers": servers,
                "replyPolicy": reply_policy,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        servers = cast(list[str], d.pop("servers"))

        reply_policy = d.pop("replyPolicy")

        dns_sec_setting_open_api_vo = cls(
            servers=servers,
            reply_policy=reply_policy,
        )

        dns_sec_setting_open_api_vo.additional_properties = d
        return dns_sec_setting_open_api_vo

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
