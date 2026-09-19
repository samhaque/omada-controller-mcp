from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="LanNetworkSplitOpenApiVO")


@_attrs_define
class LanNetworkSplitOpenApiVO:
    """LanNetworkSplitOpenApiVO

    Attributes:
        name (str): LAN network name should contain 1 to 128 characters.
        id (str | Unset): LAN network ID
        vlan_type (int | Unset): When purpose is interface, VLANType should be a value as follows: 0: Single; 1:
            Multiple
        vlan (int | Unset): Vlan should be within the range of 1-4090.
        primary (bool | Unset): Primary
    """

    name: str
    id: str | Unset = UNSET
    vlan_type: int | Unset = UNSET
    vlan: int | Unset = UNSET
    primary: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        id = self.id

        vlan_type = self.vlan_type

        vlan = self.vlan

        primary = self.primary

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if vlan_type is not UNSET:
            field_dict["vlanType"] = vlan_type
        if vlan is not UNSET:
            field_dict["vlan"] = vlan
        if primary is not UNSET:
            field_dict["primary"] = primary

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        id = d.pop("id", UNSET)

        vlan_type = d.pop("vlanType", UNSET)

        vlan = d.pop("vlan", UNSET)

        primary = d.pop("primary", UNSET)

        lan_network_split_open_api_vo = cls(
            name=name,
            id=id,
            vlan_type=vlan_type,
            vlan=vlan,
            primary=primary,
        )

        lan_network_split_open_api_vo.additional_properties = d
        return lan_network_split_open_api_vo

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
