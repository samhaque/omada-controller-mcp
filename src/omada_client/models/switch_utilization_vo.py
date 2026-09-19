from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.top_model_base_vo import TopModelBaseVO


T = TypeVar("T", bound="SwitchUtilizationVO")


@_attrs_define
class SwitchUtilizationVO:
    """
    Attributes:
        top_switch_cpu (list[TopModelBaseVO] | Unset):
        top_switch_memory (list[TopModelBaseVO] | Unset):
    """

    top_switch_cpu: list[TopModelBaseVO] | Unset = UNSET
    top_switch_memory: list[TopModelBaseVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        top_switch_cpu: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.top_switch_cpu, Unset):
            top_switch_cpu = []
            for top_switch_cpu_item_data in self.top_switch_cpu:
                top_switch_cpu_item = top_switch_cpu_item_data.to_dict()
                top_switch_cpu.append(top_switch_cpu_item)

        top_switch_memory: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.top_switch_memory, Unset):
            top_switch_memory = []
            for top_switch_memory_item_data in self.top_switch_memory:
                top_switch_memory_item = top_switch_memory_item_data.to_dict()
                top_switch_memory.append(top_switch_memory_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if top_switch_cpu is not UNSET:
            field_dict["topSwitchCpu"] = top_switch_cpu
        if top_switch_memory is not UNSET:
            field_dict["topSwitchMemory"] = top_switch_memory

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.top_model_base_vo import TopModelBaseVO

        d = dict(src_dict)
        _top_switch_cpu = d.pop("topSwitchCpu", UNSET)
        top_switch_cpu: list[TopModelBaseVO] | Unset = UNSET
        if _top_switch_cpu is not UNSET:
            top_switch_cpu = []
            for top_switch_cpu_item_data in _top_switch_cpu:
                top_switch_cpu_item = TopModelBaseVO.from_dict(top_switch_cpu_item_data)

                top_switch_cpu.append(top_switch_cpu_item)

        _top_switch_memory = d.pop("topSwitchMemory", UNSET)
        top_switch_memory: list[TopModelBaseVO] | Unset = UNSET
        if _top_switch_memory is not UNSET:
            top_switch_memory = []
            for top_switch_memory_item_data in _top_switch_memory:
                top_switch_memory_item = TopModelBaseVO.from_dict(
                    top_switch_memory_item_data
                )

                top_switch_memory.append(top_switch_memory_item)

        switch_utilization_vo = cls(
            top_switch_cpu=top_switch_cpu,
            top_switch_memory=top_switch_memory,
        )

        switch_utilization_vo.additional_properties = d
        return switch_utilization_vo

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
