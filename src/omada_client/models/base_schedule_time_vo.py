from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="BaseScheduleTimeVO")


@_attrs_define
class BaseScheduleTimeVO:
    """Backup schedule time occurrence

    Attributes:
        timing_type (int): Time type for schedule task, values are as follows:  Daily(1), Weekly(2), Monthly(3),
            Yearly(4)
        hour (int): Hour when schedule execute, value is between 0 to 23
        minute (int): Minute when schedule execute, value is between 0 to 59
        day_of_week (int | Unset): Day of week when schedule execute, only for timingType: Weekly(2), value is between 0
            to 6
        day_of_month (int | Unset): Day of month when schedule execute, only for timingType: Monthly(3), value is
            between 1 to 31
        month_of_year (int | Unset): Month of year when schedule execute, only for timingType: Yearly(4), value is
            between 1 to 12
    """

    timing_type: int
    hour: int
    minute: int
    day_of_week: int | Unset = UNSET
    day_of_month: int | Unset = UNSET
    month_of_year: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timing_type = self.timing_type

        hour = self.hour

        minute = self.minute

        day_of_week = self.day_of_week

        day_of_month = self.day_of_month

        month_of_year = self.month_of_year

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timingType": timing_type,
                "hour": hour,
                "minute": minute,
            }
        )
        if day_of_week is not UNSET:
            field_dict["dayOfWeek"] = day_of_week
        if day_of_month is not UNSET:
            field_dict["dayOfMonth"] = day_of_month
        if month_of_year is not UNSET:
            field_dict["monthOfYear"] = month_of_year

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        timing_type = d.pop("timingType")

        hour = d.pop("hour")

        minute = d.pop("minute")

        day_of_week = d.pop("dayOfWeek", UNSET)

        day_of_month = d.pop("dayOfMonth", UNSET)

        month_of_year = d.pop("monthOfYear", UNSET)

        base_schedule_time_vo = cls(
            timing_type=timing_type,
            hour=hour,
            minute=minute,
            day_of_week=day_of_week,
            day_of_month=day_of_month,
            month_of_year=month_of_year,
        )

        base_schedule_time_vo.additional_properties = d
        return base_schedule_time_vo

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
