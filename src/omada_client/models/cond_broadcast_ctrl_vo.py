from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="CondBroadcastCtrlVO")


@_attrs_define
class CondBroadcastCtrlVO:
    """Condition Broadcast Control config.

    Attributes:
        enable (bool | Unset): enable
        condition (int | Unset): 0: uplink down, 1: Internet down.
        up_time (int | Unset): SSID Uplink Time
        down_time (int | Unset): SSID Downlink Time
    """

    enable: bool | Unset = UNSET
    condition: int | Unset = UNSET
    up_time: int | Unset = UNSET
    down_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        condition = self.condition

        up_time = self.up_time

        down_time = self.down_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable is not UNSET:
            field_dict["enable"] = enable
        if condition is not UNSET:
            field_dict["condition"] = condition
        if up_time is not UNSET:
            field_dict["upTime"] = up_time
        if down_time is not UNSET:
            field_dict["downTime"] = down_time

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        enable = d.pop("enable", UNSET)

        condition = d.pop("condition", UNSET)

        up_time = d.pop("upTime", UNSET)

        down_time = d.pop("downTime", UNSET)

        cond_broadcast_ctrl_vo = cls(
            enable=enable,
            condition=condition,
            up_time=up_time,
            down_time=down_time,
        )

        cond_broadcast_ctrl_vo.additional_properties = d
        return cond_broadcast_ctrl_vo

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
