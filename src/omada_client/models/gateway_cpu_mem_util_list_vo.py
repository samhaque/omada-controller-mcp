from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="GatewayCpuMemUtilListVO")


@_attrs_define
class GatewayCpuMemUtilListVO:
    """Gateway CPU and memory utilization

    Attributes:
        time (int | Unset): Timestamp, in seconds, such as 1682000000
        cpu_util (int | Unset): Device CPU utilization rate
        mem_util (int | Unset): Device memory utilization rate
    """

    time: int | Unset = UNSET
    cpu_util: int | Unset = UNSET
    mem_util: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time = self.time

        cpu_util = self.cpu_util

        mem_util = self.mem_util

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if time is not UNSET:
            field_dict["time"] = time
        if cpu_util is not UNSET:
            field_dict["cpuUtil"] = cpu_util
        if mem_util is not UNSET:
            field_dict["memUtil"] = mem_util

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        time = d.pop("time", UNSET)

        cpu_util = d.pop("cpuUtil", UNSET)

        mem_util = d.pop("memUtil", UNSET)

        gateway_cpu_mem_util_list_vo = cls(
            time=time,
            cpu_util=cpu_util,
            mem_util=mem_util,
        )

        gateway_cpu_mem_util_list_vo.additional_properties = d
        return gateway_cpu_mem_util_list_vo

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
