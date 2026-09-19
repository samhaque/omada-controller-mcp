from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="InstancesVO")


@_attrs_define
class InstancesVO:
    """Instances

    Attributes:
        stp (int | Unset): stp, 0: MSTP / 1: RPVST
        id (int | Unset): mstp instanceId
        vlan (str | Unset): rpvst vlanId
        priority (int | Unset): priority
        cost_mode (int | Unset): costMode, 0: auto / 1: custom
        cost (int | Unset): cost
    """

    stp: int | Unset = UNSET
    id: int | Unset = UNSET
    vlan: str | Unset = UNSET
    priority: int | Unset = UNSET
    cost_mode: int | Unset = UNSET
    cost: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stp = self.stp

        id = self.id

        vlan = self.vlan

        priority = self.priority

        cost_mode = self.cost_mode

        cost = self.cost

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stp is not UNSET:
            field_dict["stp"] = stp
        if id is not UNSET:
            field_dict["id"] = id
        if vlan is not UNSET:
            field_dict["vlan"] = vlan
        if priority is not UNSET:
            field_dict["priority"] = priority
        if cost_mode is not UNSET:
            field_dict["costMode"] = cost_mode
        if cost is not UNSET:
            field_dict["cost"] = cost

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        stp = d.pop("stp", UNSET)

        id = d.pop("id", UNSET)

        vlan = d.pop("vlan", UNSET)

        priority = d.pop("priority", UNSET)

        cost_mode = d.pop("costMode", UNSET)

        cost = d.pop("cost", UNSET)

        instances_vo = cls(
            stp=stp,
            id=id,
            vlan=vlan,
            priority=priority,
            cost_mode=cost_mode,
            cost=cost,
        )

        instances_vo.additional_properties = d
        return instances_vo

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
