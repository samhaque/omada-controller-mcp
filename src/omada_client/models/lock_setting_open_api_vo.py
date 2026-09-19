from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="LockSettingOpenApiVO")


@_attrs_define
class LockSettingOpenApiVO:
    """IP lock config. It is required when parameter [status] is true.

    Attributes:
        status (bool): Status of the SSL VPN server name lock or IP lock.
        times (int | Unset): The number of login failures that trigger the lock. It is required when parameter [status]
            is true, and it should be within the range of 1–10
        duration (int | Unset): Lock duration should be within the range of 1–1080(min).
    """

    status: bool
    times: int | Unset = UNSET
    duration: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        times = self.times

        duration = self.duration

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if times is not UNSET:
            field_dict["times"] = times
        if duration is not UNSET:
            field_dict["duration"] = duration

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        status = d.pop("status")

        times = d.pop("times", UNSET)

        duration = d.pop("duration", UNSET)

        lock_setting_open_api_vo = cls(
            status=status,
            times=times,
            duration=duration,
        )

        lock_setting_open_api_vo.additional_properties = d
        return lock_setting_open_api_vo

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
