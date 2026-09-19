from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="VirtualWanMacSettingOpenApiVO")


@_attrs_define
class VirtualWanMacSettingOpenApiVO:
    """VirtualWanMacSettingOpenApiVO

    Attributes:
        method (str): Parameter [method] should be set or recover. Set: Customize MAC address; Recover: Use default MAC
            address.
        mac (str | Unset): Device MAC. When [method] is set, parameter [mac] should not be empty.
    """

    method: str
    mac: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        method = self.method

        mac = self.mac

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "method": method,
            }
        )
        if mac is not UNSET:
            field_dict["mac"] = mac

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        method = d.pop("method")

        mac = d.pop("mac", UNSET)

        virtual_wan_mac_setting_open_api_vo = cls(
            method=method,
            mac=mac,
        )

        virtual_wan_mac_setting_open_api_vo.additional_properties = d
        return virtual_wan_mac_setting_open_api_vo

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
