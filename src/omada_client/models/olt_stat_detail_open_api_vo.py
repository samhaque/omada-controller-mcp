from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.olt_port_stat_open_api_vo import OltPortStatOpenApiVO


T = TypeVar("T", bound="OltStatDetailOpenApiVO")


@_attrs_define
class OltStatDetailOpenApiVO:
    """Detailed traffic information of ports

    Attributes:
        onu_count (int | Unset): Number of ONU
        up (int | Unset): Uplink traffic
        down (int | Unset): Downlink traffic
        time (int | Unset): sampling moment
        cpu (int | Unset): Utilization of cpu
        mem (int | Unset): Utilization of memory
        ports (list[OltPortStatOpenApiVO] | Unset): Traffic information of ports
    """

    onu_count: int | Unset = UNSET
    up: int | Unset = UNSET
    down: int | Unset = UNSET
    time: int | Unset = UNSET
    cpu: int | Unset = UNSET
    mem: int | Unset = UNSET
    ports: list[OltPortStatOpenApiVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        onu_count = self.onu_count

        up = self.up

        down = self.down

        time = self.time

        cpu = self.cpu

        mem = self.mem

        ports: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ports, Unset):
            ports = []
            for ports_item_data in self.ports:
                ports_item = ports_item_data.to_dict()
                ports.append(ports_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if onu_count is not UNSET:
            field_dict["onuCount"] = onu_count
        if up is not UNSET:
            field_dict["up"] = up
        if down is not UNSET:
            field_dict["down"] = down
        if time is not UNSET:
            field_dict["time"] = time
        if cpu is not UNSET:
            field_dict["cpu"] = cpu
        if mem is not UNSET:
            field_dict["mem"] = mem
        if ports is not UNSET:
            field_dict["ports"] = ports

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.olt_port_stat_open_api_vo import (
            OltPortStatOpenApiVO,
        )

        d = dict(src_dict)
        onu_count = d.pop("onuCount", UNSET)

        up = d.pop("up", UNSET)

        down = d.pop("down", UNSET)

        time = d.pop("time", UNSET)

        cpu = d.pop("cpu", UNSET)

        mem = d.pop("mem", UNSET)

        _ports = d.pop("ports", UNSET)
        ports: list[OltPortStatOpenApiVO] | Unset = UNSET
        if _ports is not UNSET:
            ports = []
            for ports_item_data in _ports:
                ports_item = OltPortStatOpenApiVO.from_dict(ports_item_data)

                ports.append(ports_item)

        olt_stat_detail_open_api_vo = cls(
            onu_count=onu_count,
            up=up,
            down=down,
            time=time,
            cpu=cpu,
            mem=mem,
            ports=ports,
        )

        olt_stat_detail_open_api_vo.additional_properties = d
        return olt_stat_detail_open_api_vo

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
