from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.top_model_base_vo import TopModelBaseVO


T = TypeVar("T", bound="ApUtilizationVO")


@_attrs_define
class ApUtilizationVO:
    """
    Attributes:
        top_ap_by_cpu_utility (list[TopModelBaseVO] | Unset):
        top_ap_by_memory_utility (list[TopModelBaseVO] | Unset):
    """

    top_ap_by_cpu_utility: list[TopModelBaseVO] | Unset = UNSET
    top_ap_by_memory_utility: list[TopModelBaseVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        top_ap_by_cpu_utility: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.top_ap_by_cpu_utility, Unset):
            top_ap_by_cpu_utility = []
            for top_ap_by_cpu_utility_item_data in self.top_ap_by_cpu_utility:
                top_ap_by_cpu_utility_item = top_ap_by_cpu_utility_item_data.to_dict()
                top_ap_by_cpu_utility.append(top_ap_by_cpu_utility_item)

        top_ap_by_memory_utility: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.top_ap_by_memory_utility, Unset):
            top_ap_by_memory_utility = []
            for top_ap_by_memory_utility_item_data in self.top_ap_by_memory_utility:
                top_ap_by_memory_utility_item = (
                    top_ap_by_memory_utility_item_data.to_dict()
                )
                top_ap_by_memory_utility.append(top_ap_by_memory_utility_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if top_ap_by_cpu_utility is not UNSET:
            field_dict["topApByCpuUtility"] = top_ap_by_cpu_utility
        if top_ap_by_memory_utility is not UNSET:
            field_dict["topApByMemoryUtility"] = top_ap_by_memory_utility

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.top_model_base_vo import TopModelBaseVO

        d = dict(src_dict)
        _top_ap_by_cpu_utility = d.pop("topApByCpuUtility", UNSET)
        top_ap_by_cpu_utility: list[TopModelBaseVO] | Unset = UNSET
        if _top_ap_by_cpu_utility is not UNSET:
            top_ap_by_cpu_utility = []
            for top_ap_by_cpu_utility_item_data in _top_ap_by_cpu_utility:
                top_ap_by_cpu_utility_item = TopModelBaseVO.from_dict(
                    top_ap_by_cpu_utility_item_data
                )

                top_ap_by_cpu_utility.append(top_ap_by_cpu_utility_item)

        _top_ap_by_memory_utility = d.pop("topApByMemoryUtility", UNSET)
        top_ap_by_memory_utility: list[TopModelBaseVO] | Unset = UNSET
        if _top_ap_by_memory_utility is not UNSET:
            top_ap_by_memory_utility = []
            for top_ap_by_memory_utility_item_data in _top_ap_by_memory_utility:
                top_ap_by_memory_utility_item = TopModelBaseVO.from_dict(
                    top_ap_by_memory_utility_item_data
                )

                top_ap_by_memory_utility.append(top_ap_by_memory_utility_item)

        ap_utilization_vo = cls(
            top_ap_by_cpu_utility=top_ap_by_cpu_utility,
            top_ap_by_memory_utility=top_ap_by_memory_utility,
        )

        ap_utilization_vo.additional_properties = d
        return ap_utilization_vo

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
