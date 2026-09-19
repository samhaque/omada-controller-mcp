from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="CustomDayModeOpenApiVO")


@_attrs_define
class CustomDayModeOpenApiVO:
    """Time range profile custom day mode, this field is required when parameter [dayMode] is 3.

    Attributes:
        day_mon (bool): Whether to enable Monday of time range profile.
        day_tue (bool): Whether to enable Tuesday of time range profile.
        day_wed (bool): Whether to enable Wednesday of time range profile.
        day_thu (bool): Whether to enable Thursday of time range profile.
        day_fri (bool): Whether to enable Friday of time range profile.
        day_sat (bool): Whether to enable Saturday of time range profile.
        day_sun (bool): Whether to enable Sunday of time range profile.
    """

    day_mon: bool
    day_tue: bool
    day_wed: bool
    day_thu: bool
    day_fri: bool
    day_sat: bool
    day_sun: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        day_mon = self.day_mon

        day_tue = self.day_tue

        day_wed = self.day_wed

        day_thu = self.day_thu

        day_fri = self.day_fri

        day_sat = self.day_sat

        day_sun = self.day_sun

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dayMon": day_mon,
                "dayTue": day_tue,
                "dayWed": day_wed,
                "dayThu": day_thu,
                "dayFri": day_fri,
                "daySat": day_sat,
                "daySun": day_sun,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        day_mon = d.pop("dayMon")

        day_tue = d.pop("dayTue")

        day_wed = d.pop("dayWed")

        day_thu = d.pop("dayThu")

        day_fri = d.pop("dayFri")

        day_sat = d.pop("daySat")

        day_sun = d.pop("daySun")

        custom_day_mode_open_api_vo = cls(
            day_mon=day_mon,
            day_tue=day_tue,
            day_wed=day_wed,
            day_thu=day_thu,
            day_fri=day_fri,
            day_sat=day_sat,
            day_sun=day_sun,
        )

        custom_day_mode_open_api_vo.additional_properties = d
        return custom_day_mode_open_api_vo

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
