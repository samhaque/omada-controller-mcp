from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="EasyManagedSwitchLoopbackControl")


@_attrs_define
class EasyManagedSwitchLoopbackControl:
    """
    Attributes:
        loopback_detect_enable (bool | Unset): LoopbackDetectEnable
        stp (int | Unset): STP should be a value as follows: 0: OFF 1: STP 2: RSTP
        priority (int | Unset): priority
        max_age (int | Unset): maxAge should be between 6 and 40.
        forward_delay (int | Unset): forwardDelay should be between 4 and 30.
        tx_hold_count (int | Unset): txHoldCount should be between 1 and 10.
    """

    loopback_detect_enable: bool | Unset = UNSET
    stp: int | Unset = UNSET
    priority: int | Unset = UNSET
    max_age: int | Unset = UNSET
    forward_delay: int | Unset = UNSET
    tx_hold_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        loopback_detect_enable = self.loopback_detect_enable

        stp = self.stp

        priority = self.priority

        max_age = self.max_age

        forward_delay = self.forward_delay

        tx_hold_count = self.tx_hold_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if loopback_detect_enable is not UNSET:
            field_dict["loopbackDetectEnable"] = loopback_detect_enable
        if stp is not UNSET:
            field_dict["stp"] = stp
        if priority is not UNSET:
            field_dict["priority"] = priority
        if max_age is not UNSET:
            field_dict["maxAge"] = max_age
        if forward_delay is not UNSET:
            field_dict["forwardDelay"] = forward_delay
        if tx_hold_count is not UNSET:
            field_dict["txHoldCount"] = tx_hold_count

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        loopback_detect_enable = d.pop("loopbackDetectEnable", UNSET)

        stp = d.pop("stp", UNSET)

        priority = d.pop("priority", UNSET)

        max_age = d.pop("maxAge", UNSET)

        forward_delay = d.pop("forwardDelay", UNSET)

        tx_hold_count = d.pop("txHoldCount", UNSET)

        easy_managed_switch_loopback_control = cls(
            loopback_detect_enable=loopback_detect_enable,
            stp=stp,
            priority=priority,
            max_age=max_age,
            forward_delay=forward_delay,
            tx_hold_count=tx_hold_count,
        )

        easy_managed_switch_loopback_control.additional_properties = d
        return easy_managed_switch_loopback_control

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
