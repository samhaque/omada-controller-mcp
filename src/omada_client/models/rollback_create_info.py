from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="RollbackCreateInfo")


@_attrs_define
class RollbackCreateInfo:
    """
    Attributes:
        schedule_type (int): The type of execution time for the upgrade, where 0 represents now and 1 represents the
            specified time
        target_version (str): User selected rollback version, It should not be null
        year (int | Unset): User selected year
        month_of_year (int | Unset): The month of the year selected by the user, It should be within the range of 1-12
        day_of_month (int | Unset): The day of the month selected by the user, It should be within the range of 1-31
        hour (int | Unset): The hour selected by the user, It should be within the range of 0-23
        minute (int | Unset): The minute selected by the user, It should be within the range of 0-59
    """

    schedule_type: int
    target_version: str
    year: int | Unset = UNSET
    month_of_year: int | Unset = UNSET
    day_of_month: int | Unset = UNSET
    hour: int | Unset = UNSET
    minute: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        schedule_type = self.schedule_type

        target_version = self.target_version

        year = self.year

        month_of_year = self.month_of_year

        day_of_month = self.day_of_month

        hour = self.hour

        minute = self.minute

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "scheduleType": schedule_type,
                "targetVersion": target_version,
            }
        )
        if year is not UNSET:
            field_dict["year"] = year
        if month_of_year is not UNSET:
            field_dict["monthOfYear"] = month_of_year
        if day_of_month is not UNSET:
            field_dict["dayOfMonth"] = day_of_month
        if hour is not UNSET:
            field_dict["hour"] = hour
        if minute is not UNSET:
            field_dict["minute"] = minute

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        schedule_type = d.pop("scheduleType")

        target_version = d.pop("targetVersion")

        year = d.pop("year", UNSET)

        month_of_year = d.pop("monthOfYear", UNSET)

        day_of_month = d.pop("dayOfMonth", UNSET)

        hour = d.pop("hour", UNSET)

        minute = d.pop("minute", UNSET)

        rollback_create_info = cls(
            schedule_type=schedule_type,
            target_version=target_version,
            year=year,
            month_of_year=month_of_year,
            day_of_month=day_of_month,
            hour=hour,
            minute=minute,
        )

        rollback_create_info.additional_properties = d
        return rollback_create_info

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
