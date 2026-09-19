from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="BaseDeviceStatDTO")


@_attrs_define
class BaseDeviceStatDTO:
    """
    Attributes:
        time (int | Unset): sampling moment
        cpu (int | Unset): Utilization of cpu
        mem (int | Unset): Utilization of memory
        reboot_times (int | Unset): reboot times
        mac (str | Unset): the mac of the device
    """

    time: int | Unset = UNSET
    cpu: int | Unset = UNSET
    mem: int | Unset = UNSET
    reboot_times: int | Unset = UNSET
    mac: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time = self.time

        cpu = self.cpu

        mem = self.mem

        reboot_times = self.reboot_times

        mac = self.mac

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

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        time = d.pop("time", UNSET)

        cpu = d.pop("cpu", UNSET)

        mem = d.pop("mem", UNSET)

        reboot_times = d.pop("rebootTimes", UNSET)

        mac = d.pop("mac", UNSET)

        base_device_stat_dto = cls(
            time=time,
            cpu=cpu,
            mem=mem,
            reboot_times=reboot_times,
            mac=mac,
        )

        base_device_stat_dto.additional_properties = d
        return base_device_stat_dto

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
