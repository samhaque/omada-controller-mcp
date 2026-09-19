from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SelectStacksWithVlanVO")


@_attrs_define
class SelectStacksWithVlanVO:
    """
    Attributes:
        stack_ids (list[str]): Stack ID List.
        vlan_type (int): Network type, It should be a value as follows : 0:single vlan 1:multi vlan
        vlan (int | Unset): vlan, only valid when vlanType is 0 (single vlan)
        vlans (str | Unset): vlans, only valid when vlanType is 1 (multi vlan). VLAN format: 200, 1-100.
    """

    stack_ids: list[str]
    vlan_type: int
    vlan: int | Unset = UNSET
    vlans: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stack_ids = self.stack_ids

        vlan_type = self.vlan_type

        vlan = self.vlan

        vlans = self.vlans

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stackIds": stack_ids,
                "vlanType": vlan_type,
            }
        )
        if vlan is not UNSET:
            field_dict["vlan"] = vlan
        if vlans is not UNSET:
            field_dict["vlans"] = vlans

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        stack_ids = cast(list[str], d.pop("stackIds"))

        vlan_type = d.pop("vlanType")

        vlan = d.pop("vlan", UNSET)

        vlans = d.pop("vlans", UNSET)

        select_stacks_with_vlan_vo = cls(
            stack_ids=stack_ids,
            vlan_type=vlan_type,
            vlan=vlan,
            vlans=vlans,
        )

        select_stacks_with_vlan_vo.additional_properties = d
        return select_stacks_with_vlan_vo

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
