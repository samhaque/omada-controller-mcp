from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="AutoEffectDeviceForVlanVO")


@_attrs_define
class AutoEffectDeviceForVlanVO:
    """Auto effect device list.

    Attributes:
        mac (str | Unset): Device Mac
        stack_id (str | Unset): Stack Id, only valid when the device is stack.
        dhcp_mode (int | Unset): It should be a value as follows, 0:None  1:DHCP Server 2:DHCP Relay
    """

    mac: str | Unset = UNSET
    stack_id: str | Unset = UNSET
    dhcp_mode: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        stack_id = self.stack_id

        dhcp_mode = self.dhcp_mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mac is not UNSET:
            field_dict["mac"] = mac
        if stack_id is not UNSET:
            field_dict["stackId"] = stack_id
        if dhcp_mode is not UNSET:
            field_dict["dhcpMode"] = dhcp_mode

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mac = d.pop("mac", UNSET)

        stack_id = d.pop("stackId", UNSET)

        dhcp_mode = d.pop("dhcpMode", UNSET)

        auto_effect_device_for_vlan_vo = cls(
            mac=mac,
            stack_id=stack_id,
            dhcp_mode=dhcp_mode,
        )

        auto_effect_device_for_vlan_vo.additional_properties = d
        return auto_effect_device_for_vlan_vo

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
