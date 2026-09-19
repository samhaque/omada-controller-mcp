from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="BaseScheduleTimeOpenApiVO")


@_attrs_define
class BaseScheduleTimeOpenApiVO:
    """Execution occurrence setting. Required when type is 1.

    Attributes:
        timing_type (int): Time type should be a value as follows: 1:Daily; 2:Weekly; 3:Monthly
        hour (int): It should be within the range of 0~23
        minute (int): It should be within the range of 0~59
        day_of_week (int | Unset): It should be within the range of 0(Sunday)~6(Saturday). Required when parameter
            [timingType] is 2.
        day_of_month (int | Unset): It should be within the range of 1~31. Required when parameter [timingType] is 3.
        month_of_year (int | Unset): It should be within the range of 1~12. Required when parameter [timingType] is 4.
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

        base_schedule_time_open_api_vo = cls(
            timing_type=timing_type,
            hour=hour,
            minute=minute,
            day_of_week=day_of_week,
            day_of_month=day_of_month,
            month_of_year=month_of_year,
        )

        base_schedule_time_open_api_vo.additional_properties = d
        return base_schedule_time_open_api_vo

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
