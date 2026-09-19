from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="ScheduleTimeOpenApiVO")


@_attrs_define
class ScheduleTimeOpenApiVO:
    """Time range profile schedule time config

    Attributes:
        day_type (int): Time range schedule time day type, 1 to 7 indicates Monday to Sunday, if parameter [dayMode] is
            0 to 2, the input value for this field should be 0.
        start_time_h (int): Time range schedule start time (unit: hour); It should be within the range of 0–24.
        start_time_m (int): Time range schedule start time (unit: minute); It should be a value as follows: [0, 15, 30,
            45].
        end_time_h (int): Time range schedule end time (unit: hour); It should be within the range of 0–24.
        end_time_m (int): Time range schedule end time (unit: minute); It should be a value as follows: [0, 15, 30, 45].
    """

    day_type: int
    start_time_h: int
    start_time_m: int
    end_time_h: int
    end_time_m: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        day_type = self.day_type

        start_time_h = self.start_time_h

        start_time_m = self.start_time_m

        end_time_h = self.end_time_h

        end_time_m = self.end_time_m

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dayType": day_type,
                "startTimeH": start_time_h,
                "startTimeM": start_time_m,
                "endTimeH": end_time_h,
                "endTimeM": end_time_m,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        day_type = d.pop("dayType")

        start_time_h = d.pop("startTimeH")

        start_time_m = d.pop("startTimeM")

        end_time_h = d.pop("endTimeH")

        end_time_m = d.pop("endTimeM")

        schedule_time_open_api_vo = cls(
            day_type=day_type,
            start_time_h=start_time_h,
            start_time_m=start_time_m,
            end_time_h=end_time_h,
            end_time_m=end_time_m,
        )

        schedule_time_open_api_vo.additional_properties = d
        return schedule_time_open_api_vo

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
