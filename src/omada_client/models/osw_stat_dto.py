from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.osw_port_stat_dto import OswPortStatDTO


T = TypeVar("T", bound="OswStatDTO")


@_attrs_define
class OswStatDTO:
    """Detailed traffic information of ports

    Attributes:
        time (int | Unset): sampling moment
        cpu (int | Unset): Utilization of cpu
        mem (int | Unset): Utilization of memory
        reboot_times (int | Unset): reboot times
        mac (str | Unset): the mac of the device
        ports (list[OswPortStatDTO] | Unset):
        poe_util (int | Unset):
        poe_power (int | Unset):
    """

    time: int | Unset = UNSET
    cpu: int | Unset = UNSET
    mem: int | Unset = UNSET
    reboot_times: int | Unset = UNSET
    mac: str | Unset = UNSET
    ports: list[OswPortStatDTO] | Unset = UNSET
    poe_util: int | Unset = UNSET
    poe_power: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time = self.time

        cpu = self.cpu

        mem = self.mem

        reboot_times = self.reboot_times

        mac = self.mac

        ports: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ports, Unset):
            ports = []
            for ports_item_data in self.ports:
                ports_item = ports_item_data.to_dict()
                ports.append(ports_item)

        poe_util = self.poe_util

        poe_power = self.poe_power

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if time is not UNSET:
            field_dict["time"] = time
        if cpu is not UNSET:
            field_dict["cpu"] = cpu
        if mem is not UNSET:
            field_dict["mem"] = mem
        if reboot_times is not UNSET:
            field_dict["rebootTimes"] = reboot_times
        if mac is not UNSET:
            field_dict["mac"] = mac
        if ports is not UNSET:
            field_dict["ports"] = ports
        if poe_util is not UNSET:
            field_dict["poeUtil"] = poe_util
        if poe_power is not UNSET:
            field_dict["poePower"] = poe_power

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.osw_port_stat_dto import OswPortStatDTO

        d = dict(src_dict)
        time = d.pop("time", UNSET)

        cpu = d.pop("cpu", UNSET)

        mem = d.pop("mem", UNSET)

        reboot_times = d.pop("rebootTimes", UNSET)

        mac = d.pop("mac", UNSET)

        _ports = d.pop("ports", UNSET)
        ports: list[OswPortStatDTO] | Unset = UNSET
        if _ports is not UNSET:
            ports = []
            for ports_item_data in _ports:
                ports_item = OswPortStatDTO.from_dict(ports_item_data)

                ports.append(ports_item)

        poe_util = d.pop("poeUtil", UNSET)

        poe_power = d.pop("poePower", UNSET)

        osw_stat_dto = cls(
            time=time,
            cpu=cpu,
            mem=mem,
            reboot_times=reboot_times,
            mac=mac,
            ports=ports,
            poe_util=poe_util,
            poe_power=poe_power,
        )

        osw_stat_dto.additional_properties = d
        return osw_stat_dto

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
