from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="StaticRoutingInterfaceInfo")


@_attrs_define
class StaticRoutingInterfaceInfo:
    """Interface information list.

    Attributes:
        interface_type (int | Unset): Enter a value as follows: 0: WAN; 1: LAN; 2: L2TP, 3: PPTP, 5: Virtual WAN
        name (str | Unset): Interface name.
        id (str | Unset): Interface ID.
        need_next_hop (bool | Unset): Parameter [needNextHop] will be true when [interfaceType] is WAN or virtual WAN,
            and proto is DHCP or static.
    """

    interface_type: int | Unset = UNSET
    name: str | Unset = UNSET
    id: str | Unset = UNSET
    need_next_hop: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interface_type = self.interface_type

        name = self.name

        id = self.id

        need_next_hop = self.need_next_hop

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if interface_type is not UNSET:
            field_dict["interfaceType"] = interface_type
        if name is not UNSET:
            field_dict["name"] = name
        if id is not UNSET:
            field_dict["id"] = id
        if need_next_hop is not UNSET:
            field_dict["needNextHop"] = need_next_hop

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        interface_type = d.pop("interfaceType", UNSET)

        name = d.pop("name", UNSET)

        id = d.pop("id", UNSET)

        need_next_hop = d.pop("needNextHop", UNSET)

        static_routing_interface_info = cls(
            interface_type=interface_type,
            name=name,
            id=id,
            need_next_hop=need_next_hop,
        )

        static_routing_interface_info.additional_properties = d
        return static_routing_interface_info

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
