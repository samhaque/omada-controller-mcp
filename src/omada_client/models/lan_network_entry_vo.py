from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="LanNetworkEntryVO")


@_attrs_define
class LanNetworkEntryVO:
    """It can be issued when the type is either "Network" or "Custom". For the "Network" type, multiple options are
    available; for the "Custom" type, a single option is required.

        Attributes:
            network_id (str | Unset): The LAN Network ID
            vlan_id (int | Unset): The VLAN ID
    """

    network_id: str | Unset = UNSET
    vlan_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        network_id = self.network_id

        vlan_id = self.vlan_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if network_id is not UNSET:
            field_dict["networkId"] = network_id
        if vlan_id is not UNSET:
            field_dict["vlanId"] = vlan_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        network_id = d.pop("networkId", UNSET)

        vlan_id = d.pop("vlanId", UNSET)

        lan_network_entry_vo = cls(
            network_id=network_id,
            vlan_id=vlan_id,
        )

        lan_network_entry_vo.additional_properties = d
        return lan_network_entry_vo

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
