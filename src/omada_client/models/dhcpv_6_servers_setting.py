from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="Dhcpv6ServersSetting")


@_attrs_define
class Dhcpv6ServersSetting:
    """Legal DHCPv6 Server

    Attributes:
        enable (bool): The switch of DHCPv6 Guarding
        dhcpv_6_svr_1 (str | Unset): DHCPv6 Server IP1
        dhcpv_6_svr_2 (str | Unset): DHCPv6 Server IP2
    """

    enable: bool
    dhcpv_6_svr_1: str | Unset = UNSET
    dhcpv_6_svr_2: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        dhcpv_6_svr_1 = self.dhcpv_6_svr_1

        dhcpv_6_svr_2 = self.dhcpv_6_svr_2

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enable": enable,
            }
        )
        if dhcpv_6_svr_1 is not UNSET:
            field_dict["dhcpv6Svr1"] = dhcpv_6_svr_1
        if dhcpv_6_svr_2 is not UNSET:
            field_dict["dhcpv6Svr2"] = dhcpv_6_svr_2

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        enable = d.pop("enable")

        dhcpv_6_svr_1 = d.pop("dhcpv6Svr1", UNSET)

        dhcpv_6_svr_2 = d.pop("dhcpv6Svr2", UNSET)

        dhcpv_6_servers_setting = cls(
            enable=enable,
            dhcpv_6_svr_1=dhcpv_6_svr_1,
            dhcpv_6_svr_2=dhcpv_6_svr_2,
        )

        dhcpv_6_servers_setting.additional_properties = d
        return dhcpv_6_servers_setting

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
