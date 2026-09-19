from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OswIpSettingBriefOpenapiVO")


@_attrs_define
class OswIpSettingBriefOpenapiVO:
    """Network IP setting. Only valid when deviceType is 2.

    Attributes:
        mode (int): IP Setting mode. Static:0, DHCP:1
        ip (str | Unset): Static IP for mode 0, like 192.168.0.1
        netmask (str | Unset): IP Mask, like 255.255.255.0
        option12 (str | Unset): option12
    """

    mode: int
    ip: str | Unset = UNSET
    netmask: str | Unset = UNSET
    option12: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mode = self.mode

        ip = self.ip

        netmask = self.netmask

        option12 = self.option12

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mode": mode,
            }
        )
        if ip is not UNSET:
            field_dict["ip"] = ip
        if netmask is not UNSET:
            field_dict["netmask"] = netmask
        if option12 is not UNSET:
            field_dict["option12"] = option12

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mode = d.pop("mode")

        ip = d.pop("ip", UNSET)

        netmask = d.pop("netmask", UNSET)

        option12 = d.pop("option12", UNSET)

        osw_ip_setting_brief_openapi_vo = cls(
            mode=mode,
            ip=ip,
            netmask=netmask,
            option12=option12,
        )

        osw_ip_setting_brief_openapi_vo.additional_properties = d
        return osw_ip_setting_brief_openapi_vo

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
