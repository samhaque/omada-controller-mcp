from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.osw_port_stat_open_api_vo import OswPortStatOpenApiVO


T = TypeVar("T", bound="OswStatDetailOpenApiVO")


@_attrs_define
class OswStatDetailOpenApiVO:
    """Detailed traffic information of ports

    Attributes:
        time (int | Unset): sampling moment
        cpu (int | Unset): Utilization of cpu
        mem (int | Unset): Utilization of memory
        ports (list[OswPortStatOpenApiVO] | Unset): Traffic information of ports
    """

    time: int | Unset = UNSET
    cpu: int | Unset = UNSET
    mem: int | Unset = UNSET
    ports: list[OswPortStatOpenApiVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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
        from ..models.osw_port_stat_open_api_vo import (
            OswPortStatOpenApiVO,
        )

        d = dict(src_dict)
        time = d.pop("time", UNSET)

        cpu = d.pop("cpu", UNSET)

        mem = d.pop("mem", UNSET)

        _ports = d.pop("ports", UNSET)
        ports: list[OswPortStatOpenApiVO] | Unset = UNSET
        if _ports is not UNSET:
            ports = []
            for ports_item_data in _ports:
                ports_item = OswPortStatOpenApiVO.from_dict(ports_item_data)

                ports.append(ports_item)

        osw_stat_detail_open_api_vo = cls(
            time=time,
            cpu=cpu,
            mem=mem,
            ports=ports,
        )

        osw_stat_detail_open_api_vo.additional_properties = d
        return osw_stat_detail_open_api_vo

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
