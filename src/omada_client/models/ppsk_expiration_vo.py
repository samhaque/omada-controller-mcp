from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PPSKExpirationVO")


@_attrs_define
class PPSKExpirationVO:
    """PPSK Profile expiration time config.

    Attributes:
        type_ (int | Unset): Expiration type, should be a value as follows: 0: Never expire. 1: PPSK can be used between
            the effective time and expiration time. 2: PPSK can be used after a period of time of creation. 3: PPSK can be
            used during designated time periods every day
        effective_time (int | Unset): The timestamp when the PPSK takes effect, unit: millisecond. When parameter [type]
            is 1, parameter [effectiveTime] is required
        expiration_time (int | Unset): The timestamp of the expiration of PPSK, unit: millisecond. When parameter [type]
            is 1, parameter [expirationTime] is required
        duration (int | Unset): Duration of one use. When parameter [type] is 2, parameter [duration] is required
        duration_unit (int | Unset): Unit of  parameter [duration], should be a value as follows: 0: hour, 1: day, 2:
            week. When parameter [type] is 2, parameter [duration] is required
        day_start_hour (int | Unset): The hour of start time, should be within the range of 0-23. When parameter [type]
            is 3, parameter [dayStartHour] is required
        day_start_min (int | Unset): The minute of start time, should be within the range of 0-59 When parameter [type]
            is 3, parameter [dayStartMin] is required
        day_end_hour (int | Unset): The hour of end time, should be within the range of 0-23 When parameter [type] is 3,
            parameter [dayEndHour] is required
        day_end_min (int | Unset): The minute of end time, should be within the range of 0-59 When parameter [type] is
            3, parameter [dayEndMin] is required
    """

    type_: int | Unset = UNSET
    effective_time: int | Unset = UNSET
    expiration_time: int | Unset = UNSET
    duration: int | Unset = UNSET
    duration_unit: int | Unset = UNSET
    day_start_hour: int | Unset = UNSET
    day_start_min: int | Unset = UNSET
    day_end_hour: int | Unset = UNSET
    day_end_min: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        effective_time = self.effective_time

        expiration_time = self.expiration_time

        duration = self.duration

        duration_unit = self.duration_unit

        day_start_hour = self.day_start_hour

        day_start_min = self.day_start_min

        day_end_hour = self.day_end_hour

        day_end_min = self.day_end_min

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if effective_time is not UNSET:
            field_dict["effectiveTime"] = effective_time
        if expiration_time is not UNSET:
            field_dict["expirationTime"] = expiration_time
        if duration is not UNSET:
            field_dict["duration"] = duration
        if duration_unit is not UNSET:
            field_dict["durationUnit"] = duration_unit
        if day_start_hour is not UNSET:
            field_dict["dayStartHour"] = day_start_hour
        if day_start_min is not UNSET:
            field_dict["dayStartMin"] = day_start_min
        if day_end_hour is not UNSET:
            field_dict["dayEndHour"] = day_end_hour
        if day_end_min is not UNSET:
            field_dict["dayEndMin"] = day_end_min

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        effective_time = d.pop("effectiveTime", UNSET)

        expiration_time = d.pop("expirationTime", UNSET)

        duration = d.pop("duration", UNSET)

        duration_unit = d.pop("durationUnit", UNSET)

        day_start_hour = d.pop("dayStartHour", UNSET)

        day_start_min = d.pop("dayStartMin", UNSET)

        day_end_hour = d.pop("dayEndHour", UNSET)

        day_end_min = d.pop("dayEndMin", UNSET)

        ppsk_expiration_vo = cls(
            type_=type_,
            effective_time=effective_time,
            expiration_time=expiration_time,
            duration=duration,
            duration_unit=duration_unit,
            day_start_hour=day_start_hour,
            day_start_min=day_start_min,
            day_end_hour=day_end_hour,
            day_end_min=day_end_min,
        )

        ppsk_expiration_vo.additional_properties = d
        return ppsk_expiration_vo

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
