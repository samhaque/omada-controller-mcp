from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="GatewayDirectionEntity")


@_attrs_define
class GatewayDirectionEntity:
    """Only for Gateway.

    Attributes:
        lan_to_wan (bool | Unset): Whether select LAN->WAN direction
        lan_to_lan (bool | Unset): Whether select LAN->LAN direction, which conflicts with other directions
        wan_in_ids (list[str] | Unset): Selected WAN port IDs
        vpn_in_ids (list[str] | Unset): Selected VPN IDs
    """

    lan_to_wan: bool | Unset = UNSET
    lan_to_lan: bool | Unset = UNSET
    wan_in_ids: list[str] | Unset = UNSET
    vpn_in_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lan_to_wan = self.lan_to_wan

        lan_to_lan = self.lan_to_lan

        wan_in_ids: list[str] | Unset = UNSET
        if not isinstance(self.wan_in_ids, Unset):
            wan_in_ids = self.wan_in_ids

        vpn_in_ids: list[str] | Unset = UNSET
        if not isinstance(self.vpn_in_ids, Unset):
            vpn_in_ids = self.vpn_in_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lan_to_wan is not UNSET:
            field_dict["lanToWan"] = lan_to_wan
        if lan_to_lan is not UNSET:
            field_dict["lanToLan"] = lan_to_lan
        if wan_in_ids is not UNSET:
            field_dict["wanInIds"] = wan_in_ids
        if vpn_in_ids is not UNSET:
            field_dict["vpnInIds"] = vpn_in_ids

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        lan_to_wan = d.pop("lanToWan", UNSET)

        lan_to_lan = d.pop("lanToLan", UNSET)

        wan_in_ids = cast(list[str], d.pop("wanInIds", UNSET))

        vpn_in_ids = cast(list[str], d.pop("vpnInIds", UNSET))

        gateway_direction_entity = cls(
            lan_to_wan=lan_to_wan,
            lan_to_lan=lan_to_lan,
            wan_in_ids=wan_in_ids,
            vpn_in_ids=vpn_in_ids,
        )

        gateway_direction_entity.additional_properties = d
        return gateway_direction_entity

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
