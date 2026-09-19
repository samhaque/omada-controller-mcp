from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="VlanNetworkAffectingDeviceVO")


@_attrs_define
class VlanNetworkAffectingDeviceVO:
    """
    Attributes:
        name (str | Unset): Device Name.
        mac (str | Unset): Device Mac.
        type_ (int | Unset): Device type, 1: gateway  2: switch  3: ap
        stack_id (str | Unset): StackId
        dhcp_mode (int | Unset): DHCP Mode, Only type is switch will return.
    """

    name: str | Unset = UNSET
    mac: str | Unset = UNSET
    type_: int | Unset = UNSET
    stack_id: str | Unset = UNSET
    dhcp_mode: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        mac = self.mac

        type_ = self.type_

        stack_id = self.stack_id

        dhcp_mode = self.dhcp_mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if mac is not UNSET:
            field_dict["mac"] = mac
        if type_ is not UNSET:
            field_dict["type"] = type_
        if stack_id is not UNSET:
            field_dict["stackId"] = stack_id
        if dhcp_mode is not UNSET:
            field_dict["dhcpMode"] = dhcp_mode

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        mac = d.pop("mac", UNSET)

        type_ = d.pop("type", UNSET)

        stack_id = d.pop("stackId", UNSET)

        dhcp_mode = d.pop("dhcpMode", UNSET)

        vlan_network_affecting_device_vo = cls(
            name=name,
            mac=mac,
            type_=type_,
            stack_id=stack_id,
            dhcp_mode=dhcp_mode,
        )

        vlan_network_affecting_device_vo.additional_properties = d
        return vlan_network_affecting_device_vo

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
