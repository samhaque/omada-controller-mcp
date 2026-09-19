from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PowerRangeVO")


@_attrs_define
class PowerRangeVO:
    """Power range. Parameter [powerRange] should not be null when parameter [powerMode] is 1.

    Attributes:
        min_power_2_g (int | Unset): Minimum power in 2.4 GHz. Parameter [minPower2g] should between 9 and 30
        max_power_2_g (int | Unset): Maximum power in 2.4 GHz. Parameter [maxPower2g] should between 9 and 30
        min_power_5_g (int | Unset): Minimum power in 5 GHz. Parameter [minPower5g] should between 9 and 30
        max_power_5_g (int | Unset): Maximum power in 5 GHz. Parameter [maxPower5g] should between 9 and 30
        min_power_6_g (int | Unset): Minimum power in 6 GHz. Parameter [minPower6g] should between 9 and 30
        max_power_6_g (int | Unset): Maximum power in 6 GHz. Parameter [maxPower6g] should between 9 and 30
    """

    min_power_2_g: int | Unset = UNSET
    max_power_2_g: int | Unset = UNSET
    min_power_5_g: int | Unset = UNSET
    max_power_5_g: int | Unset = UNSET
    min_power_6_g: int | Unset = UNSET
    max_power_6_g: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        min_power_2_g = self.min_power_2_g

        max_power_2_g = self.max_power_2_g

        min_power_5_g = self.min_power_5_g

        max_power_5_g = self.max_power_5_g

        min_power_6_g = self.min_power_6_g

        max_power_6_g = self.max_power_6_g

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if min_power_2_g is not UNSET:
            field_dict["minPower2g"] = min_power_2_g
        if max_power_2_g is not UNSET:
            field_dict["maxPower2g"] = max_power_2_g
        if min_power_5_g is not UNSET:
            field_dict["minPower5g"] = min_power_5_g
        if max_power_5_g is not UNSET:
            field_dict["maxPower5g"] = max_power_5_g
        if min_power_6_g is not UNSET:
            field_dict["minPower6g"] = min_power_6_g
        if max_power_6_g is not UNSET:
            field_dict["maxPower6g"] = max_power_6_g

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        min_power_2_g = d.pop("minPower2g", UNSET)

        max_power_2_g = d.pop("maxPower2g", UNSET)

        min_power_5_g = d.pop("minPower5g", UNSET)

        max_power_5_g = d.pop("maxPower5g", UNSET)

        min_power_6_g = d.pop("minPower6g", UNSET)

        max_power_6_g = d.pop("maxPower6g", UNSET)

        power_range_vo = cls(
            min_power_2_g=min_power_2_g,
            max_power_2_g=max_power_2_g,
            min_power_5_g=min_power_5_g,
            max_power_5_g=max_power_5_g,
            min_power_6_g=min_power_6_g,
            max_power_6_g=max_power_6_g,
        )

        power_range_vo.additional_properties = d
        return power_range_vo

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
