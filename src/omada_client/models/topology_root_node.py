from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="TopologyRootNode")


@_attrs_define
class TopologyRootNode:
    """Root Node Mac In Topology.

    Attributes:
        type_ (str | Unset): Root Node Type, which can only be one of the following three types: switch, olt and other.
        mac (str | Unset): Root Node MAC address, like AA-BB-CC-DD-EE-FF.
        specific_type (int | Unset): MultiSwitch Node SpecificType, which can only be one of the following two types:
            0:Mlag and 1:Vrrp.
        mac_list (list[str] | Unset): MultiSwitch Node MAC list.
        discovery_mode (int | Unset): Discovery Mode, which can only be one of the following two types: 0:Manual and
            1:Auto.
    """

    type_: str | Unset = UNSET
    mac: str | Unset = UNSET
    specific_type: int | Unset = UNSET
    mac_list: list[str] | Unset = UNSET
    discovery_mode: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        mac = self.mac

        specific_type = self.specific_type

        mac_list: list[str] | Unset = UNSET
        if not isinstance(self.mac_list, Unset):
            mac_list = self.mac_list

        discovery_mode = self.discovery_mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if mac is not UNSET:
            field_dict["mac"] = mac
        if specific_type is not UNSET:
            field_dict["specificType"] = specific_type
        if mac_list is not UNSET:
            field_dict["macList"] = mac_list
        if discovery_mode is not UNSET:
            field_dict["discoveryMode"] = discovery_mode

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        mac = d.pop("mac", UNSET)

        specific_type = d.pop("specificType", UNSET)

        mac_list = cast(list[str], d.pop("macList", UNSET))

        discovery_mode = d.pop("discoveryMode", UNSET)

        topology_root_node = cls(
            type_=type_,
            mac=mac,
            specific_type=specific_type,
            mac_list=mac_list,
            discovery_mode=discovery_mode,
        )

        topology_root_node.additional_properties = d
        return topology_root_node

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
