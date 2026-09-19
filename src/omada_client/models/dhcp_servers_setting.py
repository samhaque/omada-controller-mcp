from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="DhcpServersSetting")


@_attrs_define
class DhcpServersSetting:
    """Legal DHCP Server

    Attributes:
        enable (bool): The switch of DHCP Guarding. When the switch is off, any configuration of DHCP Guarding will not
            be saved.
        mode (int | Unset): The fill mode of DHCP Guarding, 1：follow Server 2：custom
        dhcp_svr_1 (str | Unset): Primary DHCP Guarding IP
        dhcp_svr_2 (str | Unset): Secondary DHCP Guarding IP
    """

    enable: bool
    mode: int | Unset = UNSET
    dhcp_svr_1: str | Unset = UNSET
    dhcp_svr_2: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        mode = self.mode

        dhcp_svr_1 = self.dhcp_svr_1

        dhcp_svr_2 = self.dhcp_svr_2

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enable": enable,
            }
        )
        if mode is not UNSET:
            field_dict["mode"] = mode
        if dhcp_svr_1 is not UNSET:
            field_dict["dhcpSvr1"] = dhcp_svr_1
        if dhcp_svr_2 is not UNSET:
            field_dict["dhcpSvr2"] = dhcp_svr_2

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        enable = d.pop("enable")

        mode = d.pop("mode", UNSET)

        dhcp_svr_1 = d.pop("dhcpSvr1", UNSET)

        dhcp_svr_2 = d.pop("dhcpSvr2", UNSET)

        dhcp_servers_setting = cls(
            enable=enable,
            mode=mode,
            dhcp_svr_1=dhcp_svr_1,
            dhcp_svr_2=dhcp_svr_2,
        )

        dhcp_servers_setting.additional_properties = d
        return dhcp_servers_setting

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
