from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="TimeValueItemVOLong")


@_attrs_define
class TimeValueItemVOLong:
    """List of common dimension value, such as rssi

    Attributes:
        time (int | Unset): Time(unit:ms)
        past_num (int | Unset): Value corresponding to time
    """

    time: int | Unset = UNSET
    past_num: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time = self.time

        past_num = self.past_num

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if time is not UNSET:
            field_dict["time"] = time
        if past_num is not UNSET:
            field_dict["pastNum"] = past_num

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        time = d.pop("time", UNSET)

        past_num = d.pop("pastNum", UNSET)

        time_value_item_vo_long = cls(
            time=time,
            past_num=past_num,
        )

        time_value_item_vo_long.additional_properties = d
        return time_value_item_vo_long

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
