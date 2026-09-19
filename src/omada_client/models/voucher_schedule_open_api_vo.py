from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="VoucherScheduleOpenApiVO")


@_attrs_define
class VoucherScheduleOpenApiVO:
    """Specified time period that voucher can be used. When parameter [validityType] is 2, parameter [schedule] is required

    Attributes:
        type_ (int): The type of schedule. It should be a value as follows: 0: Limit time by daily, 1: Limit time by
            weekly
        daily_start_hour (int | Unset): The hour of start time, should be within the range of 0-23. When parameter
            [type] is 0, parameter [dailyStartHour] is required
        daily_start_min (int | Unset): The minute of start time, should be within the range of 0-59 When parameter
            [type] is 0, parameter [dailyStartMin] is required
        daily_end_hour (int | Unset): The hour of end time, should be within the range of 0-23 When parameter [type] is
            0, parameter [dailyEndHour] is required
        daily_end_min (int | Unset): The minute of end time, should be within the range of 0-59 When parameter [type] is
            0, parameter [dailyEndMin] is required
        weekly_enable_days (list[int] | Unset): The effective days of week, array number should be within the range of
            1-7, 1 represents Monday, 2 represents Tuesday... 7 represents Sunday. When parameter [type] is 1, parameter
            [weeklyEnableDays] is required
    """

    type_: int
    daily_start_hour: int | Unset = UNSET
    daily_start_min: int | Unset = UNSET
    daily_end_hour: int | Unset = UNSET
    daily_end_min: int | Unset = UNSET
    weekly_enable_days: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        daily_start_hour = self.daily_start_hour

        daily_start_min = self.daily_start_min

        daily_end_hour = self.daily_end_hour

        daily_end_min = self.daily_end_min

        weekly_enable_days: list[int] | Unset = UNSET
        if not isinstance(self.weekly_enable_days, Unset):
            weekly_enable_days = self.weekly_enable_days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if daily_start_hour is not UNSET:
            field_dict["dailyStartHour"] = daily_start_hour
        if daily_start_min is not UNSET:
            field_dict["dailyStartMin"] = daily_start_min
        if daily_end_hour is not UNSET:
            field_dict["dailyEndHour"] = daily_end_hour
        if daily_end_min is not UNSET:
            field_dict["dailyEndMin"] = daily_end_min
        if weekly_enable_days is not UNSET:
            field_dict["weeklyEnableDays"] = weekly_enable_days

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        type_ = d.pop("type")

        daily_start_hour = d.pop("dailyStartHour", UNSET)

        daily_start_min = d.pop("dailyStartMin", UNSET)

        daily_end_hour = d.pop("dailyEndHour", UNSET)

        daily_end_min = d.pop("dailyEndMin", UNSET)

        weekly_enable_days = cast(list[int], d.pop("weeklyEnableDays", UNSET))

        voucher_schedule_open_api_vo = cls(
            type_=type_,
            daily_start_hour=daily_start_hour,
            daily_start_min=daily_start_min,
            daily_end_hour=daily_end_hour,
            daily_end_min=daily_end_min,
            weekly_enable_days=weekly_enable_days,
        )

        voucher_schedule_open_api_vo.additional_properties = d
        return voucher_schedule_open_api_vo

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
