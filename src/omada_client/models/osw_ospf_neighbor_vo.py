from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OswOspfNeighborVO")


@_attrs_define
class OswOspfNeighborVO:
    """
    Attributes:
        dead (str | Unset): Dead Time
        neighbor_interface (str | Unset): Neighbor Interface
        neighbor_ip (str | Unset): Neighbor Ip
        router_id (str | Unset): Router ID
        priority (int | Unset): Priority
        state (str | Unset): State
        process_id (str | Unset): Ospf Process ID
    """

    dead: str | Unset = UNSET
    neighbor_interface: str | Unset = UNSET
    neighbor_ip: str | Unset = UNSET
    router_id: str | Unset = UNSET
    priority: int | Unset = UNSET
    state: str | Unset = UNSET
    process_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dead = self.dead

        neighbor_interface = self.neighbor_interface

        neighbor_ip = self.neighbor_ip

        router_id = self.router_id

        priority = self.priority

        state = self.state

        process_id = self.process_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dead is not UNSET:
            field_dict["dead"] = dead
        if neighbor_interface is not UNSET:
            field_dict["neighborInterface"] = neighbor_interface
        if neighbor_ip is not UNSET:
            field_dict["neighborIp"] = neighbor_ip
        if router_id is not UNSET:
            field_dict["routerId"] = router_id
        if priority is not UNSET:
            field_dict["priority"] = priority
        if state is not UNSET:
            field_dict["state"] = state
        if process_id is not UNSET:
            field_dict["processId"] = process_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        dead = d.pop("dead", UNSET)

        neighbor_interface = d.pop("neighborInterface", UNSET)

        neighbor_ip = d.pop("neighborIp", UNSET)

        router_id = d.pop("routerId", UNSET)

        priority = d.pop("priority", UNSET)

        state = d.pop("state", UNSET)

        process_id = d.pop("processId", UNSET)

        osw_ospf_neighbor_vo = cls(
            dead=dead,
            neighbor_interface=neighbor_interface,
            neighbor_ip=neighbor_ip,
            router_id=router_id,
            priority=priority,
            state=state,
            process_id=process_id,
        )

        osw_ospf_neighbor_vo.additional_properties = d
        return osw_ospf_neighbor_vo

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
