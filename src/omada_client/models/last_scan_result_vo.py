from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="LastScanResultVO")


@_attrs_define
class LastScanResultVO:
    """The results of the last scan.

    Attributes:
        time (int | Unset): Timestamp corresponding to the start of optimization.
        before_index (int | Unset): Index before WLAN Optimization, between 0 and 100.
        after_index (int | Unset): Index after WLAN Optimization, between 0 and 100.
        is_applied_success (bool | Unset): Parameter [isAppliedSuccess] means whether WLAN Optimization executes
            successfully.
        ap_num (int | Unset): The number of EAPs.
        length (int | Unset): Parameter [length] means the duration of the WLAN Optimization in seconds.
        mode (int | Unset): 0: by WLAN Optimization schedule. 1: by one-click WLAN Optimization.
    """

    time: int | Unset = UNSET
    before_index: int | Unset = UNSET
    after_index: int | Unset = UNSET
    is_applied_success: bool | Unset = UNSET
    ap_num: int | Unset = UNSET
    length: int | Unset = UNSET
    mode: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time = self.time

        before_index = self.before_index

        after_index = self.after_index

        is_applied_success = self.is_applied_success

        ap_num = self.ap_num

        length = self.length

        mode = self.mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if time is not UNSET:
            field_dict["time"] = time
        if before_index is not UNSET:
            field_dict["beforeIndex"] = before_index
        if after_index is not UNSET:
            field_dict["afterIndex"] = after_index
        if is_applied_success is not UNSET:
            field_dict["isAppliedSuccess"] = is_applied_success
        if ap_num is not UNSET:
            field_dict["apNum"] = ap_num
        if length is not UNSET:
            field_dict["length"] = length
        if mode is not UNSET:
            field_dict["mode"] = mode

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        time = d.pop("time", UNSET)

        before_index = d.pop("beforeIndex", UNSET)

        after_index = d.pop("afterIndex", UNSET)

        is_applied_success = d.pop("isAppliedSuccess", UNSET)

        ap_num = d.pop("apNum", UNSET)

        length = d.pop("length", UNSET)

        mode = d.pop("mode", UNSET)

        last_scan_result_vo = cls(
            time=time,
            before_index=before_index,
            after_index=after_index,
            is_applied_success=is_applied_success,
            ap_num=ap_num,
            length=length,
            mode=mode,
        )

        last_scan_result_vo.additional_properties = d
        return last_scan_result_vo

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
