from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="LanNetworkVlansOpenApiVO")


@_attrs_define
class LanNetworkVlansOpenApiVO:
    """
    Attributes:
        vlan (int | Unset): Created vlan in site. Valid range is from 2 to 4090 in "Oui based vlan".
        lan_network_id (str | Unset): Lan network ID.
    """

    vlan: int | Unset = UNSET
    lan_network_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vlan = self.vlan

        lan_network_id = self.lan_network_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if vlan is not UNSET:
            field_dict["vlan"] = vlan
        if lan_network_id is not UNSET:
            field_dict["lanNetworkId"] = lan_network_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        vlan = d.pop("vlan", UNSET)

        lan_network_id = d.pop("lanNetworkId", UNSET)

        lan_network_vlans_open_api_vo = cls(
            vlan=vlan,
            lan_network_id=lan_network_id,
        )

        lan_network_vlans_open_api_vo.additional_properties = d
        return lan_network_vlans_open_api_vo

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
