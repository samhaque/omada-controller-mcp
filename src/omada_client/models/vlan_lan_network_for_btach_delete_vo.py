from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="VlanLanNetworkForBtachDeleteVO")


@_attrs_define
class VlanLanNetworkForBtachDeleteVO:
    """
    Attributes:
        purpose (str): LAN network purpose, 0: VLAN, 1: interface
        name (str | Unset): network name
        id (str | Unset): network id
        vlan (int | Unset): vlan id
    """

    purpose: str
    name: str | Unset = UNSET
    id: str | Unset = UNSET
    vlan: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        purpose = self.purpose

        name = self.name

        id = self.id

        vlan = self.vlan

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "purpose": purpose,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if id is not UNSET:
            field_dict["id"] = id
        if vlan is not UNSET:
            field_dict["vlan"] = vlan

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        purpose = d.pop("purpose")

        name = d.pop("name", UNSET)

        id = d.pop("id", UNSET)

        vlan = d.pop("vlan", UNSET)

        vlan_lan_network_for_btach_delete_vo = cls(
            purpose=purpose,
            name=name,
            id=id,
            vlan=vlan,
        )

        vlan_lan_network_for_btach_delete_vo.additional_properties = d
        return vlan_lan_network_for_btach_delete_vo

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
