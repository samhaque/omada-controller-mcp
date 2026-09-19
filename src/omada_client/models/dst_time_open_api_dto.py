from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="DstTimeOpenApiDTO")


@_attrs_define
class DstTimeOpenApiDTO:
    """DST end time config

    Attributes:
        month (int): Month of the DST config should be a value as follows: 1: January; 2: February; 3: March; 4: April;
            5: May; 6: June; 7: July; 8: August; 9: September; 10: October; 11: November; 12: December.
        serial (int): Week of the DST config should be a value as follows: 1: 1st; 2: 2nd; 3: 3rd; 4: 4th; 5: Last.
        day (int): Day of the DST config should be a value as follows: 1: Monday; 2: Tuesday; 3: Wednesday; 4: Thursday;
            5: Friday; 6: Saturday; 7: Sunday.
        hour (int): Hour of the DST config should be within the range of 0–23.
        minute (int): Minute of the DST config should be within the range of 0–59.
    """

    month: int
    serial: int
    day: int
    hour: int
    minute: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        month = self.month

        serial = self.serial

        day = self.day

        hour = self.hour

        minute = self.minute

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "month": month,
                "serial": serial,
                "day": day,
                "hour": hour,
                "minute": minute,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        month = d.pop("month")

        serial = d.pop("serial")

        day = d.pop("day")

        hour = d.pop("hour")

        minute = d.pop("minute")

        dst_time_open_api_dto = cls(
            month=month,
            serial=serial,
            day=day,
            hour=hour,
            minute=minute,
        )

        dst_time_open_api_dto.additional_properties = d
        return dst_time_open_api_dto

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
