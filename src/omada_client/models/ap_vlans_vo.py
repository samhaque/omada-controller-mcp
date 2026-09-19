from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApVlansVO")


@_attrs_define
class ApVlansVO:
    """
    Attributes:
        local_vlan_id (int | Unset): Vlan ID
        local_vlan_network_id (str | Unset): Network ID
        name (str | Unset): Network Name
        ipaddr (str | Unset): IP address.
        native_port (list[str] | Unset): Native Port List
        tag_port (list[str] | Unset): Tag Port List
        untag_port (list[str] | Unset): Untag Port List
    """

    local_vlan_id: int | Unset = UNSET
    local_vlan_network_id: str | Unset = UNSET
    name: str | Unset = UNSET
    ipaddr: str | Unset = UNSET
    native_port: list[str] | Unset = UNSET
    tag_port: list[str] | Unset = UNSET
    untag_port: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        local_vlan_id = self.local_vlan_id

        local_vlan_network_id = self.local_vlan_network_id

        name = self.name

        ipaddr = self.ipaddr

        native_port: list[str] | Unset = UNSET
        if not isinstance(self.native_port, Unset):
            native_port = self.native_port

        tag_port: list[str] | Unset = UNSET
        if not isinstance(self.tag_port, Unset):
            tag_port = self.tag_port

        untag_port: list[str] | Unset = UNSET
        if not isinstance(self.untag_port, Unset):
            untag_port = self.untag_port

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if local_vlan_id is not UNSET:
            field_dict["localVlanId"] = local_vlan_id
        if local_vlan_network_id is not UNSET:
            field_dict["localVlanNetworkId"] = local_vlan_network_id
        if name is not UNSET:
            field_dict["name"] = name
        if ipaddr is not UNSET:
            field_dict["ipaddr"] = ipaddr
        if native_port is not UNSET:
            field_dict["nativePort"] = native_port
        if tag_port is not UNSET:
            field_dict["tagPort"] = tag_port
        if untag_port is not UNSET:
            field_dict["untagPort"] = untag_port

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        local_vlan_id = d.pop("localVlanId", UNSET)

        local_vlan_network_id = d.pop("localVlanNetworkId", UNSET)

        name = d.pop("name", UNSET)

        ipaddr = d.pop("ipaddr", UNSET)

        native_port = cast(list[str], d.pop("nativePort", UNSET))

        tag_port = cast(list[str], d.pop("tagPort", UNSET))

        untag_port = cast(list[str], d.pop("untagPort", UNSET))

        ap_vlans_vo = cls(
            local_vlan_id=local_vlan_id,
            local_vlan_network_id=local_vlan_network_id,
            name=name,
            ipaddr=ipaddr,
            native_port=native_port,
            tag_port=tag_port,
            untag_port=untag_port,
        )

        ap_vlans_vo.additional_properties = d
        return ap_vlans_vo

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
