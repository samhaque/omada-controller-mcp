from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="VlanNetworkVlansVO")


@_attrs_define
class VlanNetworkVlansVO:
    """
    Attributes:
        vlan_ids (list[int] | Unset): vlan list. The parameter is defined as an array of integers. However, the current
            implementation accepts non-array inputs (e.g., a single integer or a numeric string) and will treat them as a
            single-element array. For consistency and future compatibility, please provide `vlanIds` as an array
    """

    vlan_ids: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vlan_ids: list[int] | Unset = UNSET
        if not isinstance(self.vlan_ids, Unset):
            vlan_ids = self.vlan_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if vlan_ids is not UNSET:
            field_dict["vlanIds"] = vlan_ids

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        vlan_ids = cast(list[int], d.pop("vlanIds", UNSET))

        vlan_network_vlans_vo = cls(
            vlan_ids=vlan_ids,
        )

        vlan_network_vlans_vo.additional_properties = d
        return vlan_network_vlans_vo

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
