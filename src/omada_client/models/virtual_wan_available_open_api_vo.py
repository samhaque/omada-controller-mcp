from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="VirtualWanAvailableOpenApiVO")


@_attrs_define
class VirtualWanAvailableOpenApiVO:
    """VirtualWanAvailableInfo

    Attributes:
        virtual_entry_id (int | Unset): Virtual WAN Entry ID.
        virtual_wan_id (str | Unset): Virtual WAN ID.
        physical_wan_id (str | Unset): Physical WAN ID.
        name (str | Unset): Virtual WAN name.
        ipv_4_proto (str | Unset): Virtual WAN IPv4 proto.
        type_ (int | Unset): Physical WAN port type, 0: WAN; 1:WAN/LAN; 2:LAN; 3:SFP WAN; 4:USB LTE WAN; 5: LTE WAN;
            6:DSL WAN;
        max_bandwidth (int | Unset): Port max bandwidth.
        weight (int | Unset): Virtual WAN weight.
        online_detection (int | Unset): Port Online Detection.
    """

    virtual_entry_id: int | Unset = UNSET
    virtual_wan_id: str | Unset = UNSET
    physical_wan_id: str | Unset = UNSET
    name: str | Unset = UNSET
    ipv_4_proto: str | Unset = UNSET
    type_: int | Unset = UNSET
    max_bandwidth: int | Unset = UNSET
    weight: int | Unset = UNSET
    online_detection: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        virtual_entry_id = self.virtual_entry_id

        virtual_wan_id = self.virtual_wan_id

        physical_wan_id = self.physical_wan_id

        name = self.name

        ipv_4_proto = self.ipv_4_proto

        type_ = self.type_

        max_bandwidth = self.max_bandwidth

        weight = self.weight

        online_detection = self.online_detection

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if virtual_entry_id is not UNSET:
            field_dict["virtualEntryId"] = virtual_entry_id
        if virtual_wan_id is not UNSET:
            field_dict["virtualWanId"] = virtual_wan_id
        if physical_wan_id is not UNSET:
            field_dict["physicalWanId"] = physical_wan_id
        if name is not UNSET:
            field_dict["name"] = name
        if ipv_4_proto is not UNSET:
            field_dict["ipv4Proto"] = ipv_4_proto
        if type_ is not UNSET:
            field_dict["type"] = type_
        if max_bandwidth is not UNSET:
            field_dict["maxBandwidth"] = max_bandwidth
        if weight is not UNSET:
            field_dict["weight"] = weight
        if online_detection is not UNSET:
            field_dict["onlineDetection"] = online_detection

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        virtual_entry_id = d.pop("virtualEntryId", UNSET)

        virtual_wan_id = d.pop("virtualWanId", UNSET)

        physical_wan_id = d.pop("physicalWanId", UNSET)

        name = d.pop("name", UNSET)

        ipv_4_proto = d.pop("ipv4Proto", UNSET)

        type_ = d.pop("type", UNSET)

        max_bandwidth = d.pop("maxBandwidth", UNSET)

        weight = d.pop("weight", UNSET)

        online_detection = d.pop("onlineDetection", UNSET)

        virtual_wan_available_open_api_vo = cls(
            virtual_entry_id=virtual_entry_id,
            virtual_wan_id=virtual_wan_id,
            physical_wan_id=physical_wan_id,
            name=name,
            ipv_4_proto=ipv_4_proto,
            type_=type_,
            max_bandwidth=max_bandwidth,
            weight=weight,
            online_detection=online_detection,
        )

        virtual_wan_available_open_api_vo.additional_properties = d
        return virtual_wan_available_open_api_vo

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
