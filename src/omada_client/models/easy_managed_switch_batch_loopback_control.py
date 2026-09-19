from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="EasyManagedSwitchBatchLoopbackControl")


@_attrs_define
class EasyManagedSwitchBatchLoopbackControl:
    """
    Attributes:
        switch_mac_list (list[str]): Parameter [switchMacList] should contain at least one switch MAC
        loopback_detect_enable (bool | Unset): LoopbackDetectEnable
        stp (int | Unset): STP should be a value as follows: 0: OFF 1: STP 2: RSTP 3: MSTP
        priority (int | Unset): priority
    """

    switch_mac_list: list[str]
    loopback_detect_enable: bool | Unset = UNSET
    stp: int | Unset = UNSET
    priority: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        switch_mac_list = self.switch_mac_list

        loopback_detect_enable = self.loopback_detect_enable

        stp = self.stp

        priority = self.priority

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "switchMacList": switch_mac_list,
            }
        )
        if loopback_detect_enable is not UNSET:
            field_dict["loopbackDetectEnable"] = loopback_detect_enable
        if stp is not UNSET:
            field_dict["stp"] = stp
        if priority is not UNSET:
            field_dict["priority"] = priority

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        switch_mac_list = cast(list[str], d.pop("switchMacList"))

        loopback_detect_enable = d.pop("loopbackDetectEnable", UNSET)

        stp = d.pop("stp", UNSET)

        priority = d.pop("priority", UNSET)

        easy_managed_switch_batch_loopback_control = cls(
            switch_mac_list=switch_mac_list,
            loopback_detect_enable=loopback_detect_enable,
            stp=stp,
            priority=priority,
        )

        easy_managed_switch_batch_loopback_control.additional_properties = d
        return easy_managed_switch_batch_loopback_control

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
