from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PoePowerTrendVO")


@_attrs_define
class PoePowerTrendVO:
    """
    Attributes:
        time (int | Unset): Timestamp
        poe_power_total (int | Unset): Total power of POE
    """

    time: int | Unset = UNSET
    poe_power_total: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time = self.time

        poe_power_total = self.poe_power_total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if time is not UNSET:
            field_dict["time"] = time
        if poe_power_total is not UNSET:
            field_dict["poePowerTotal"] = poe_power_total

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        time = d.pop("time", UNSET)

        poe_power_total = d.pop("poePowerTotal", UNSET)

        poe_power_trend_vo = cls(
            time=time,
            poe_power_total=poe_power_total,
        )

        poe_power_trend_vo.additional_properties = d
        return poe_power_trend_vo

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
